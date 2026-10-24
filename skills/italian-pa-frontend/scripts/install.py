#!/usr/bin/env python3
"""Install reviewed local Agent Skills; no network, dependency installs or agent APIs."""
import argparse
import hashlib
import json
import os
from pathlib import Path
import re
import shutil
import stat
import sys
import tempfile

ROOT = Path(__file__).resolve().parents[1]
SKIP_DIRS = {'.git', '.agents', '.claude', '__pycache__', '.pytest_cache',
             'node_modules', 'reports', 'playwright-report', 'test-results',
             '.venv', 'venv', 'dist', '.cache'}
SKIP_NAMES = {'.DS_Store', 'Thumbs.db', 'local.json', 'storage-state.json',
              'storageState.json', '.skills-italia-install.json'}
NAME = re.compile(r'[a-z0-9]+(?:-[a-z0-9]+)*\Z')


def excluded(path):
    """Exclude generated outputs and private configuration from distributions."""
    path = Path(path)
    return (bool(set(path.parts) & SKIP_DIRS) or path.name in SKIP_NAMES
            or path.name.startswith('.env') or path.suffix in {'.pyc', '.pyo', '.pem', '.key', '.log', '.tmp', '.bak'}
            or path.name.endswith('~'))


def linked(path):
    if path.is_symlink() or (hasattr(path, 'is_junction') and path.is_junction()):
        return True
    try:
        attributes = getattr(path.lstat(), 'st_file_attributes', 0)
    except FileNotFoundError:
        return False
    return bool(attributes & getattr(stat, 'FILE_ATTRIBUTE_REPARSE_POINT', 0x400))


def plain_path(path):
    """Reject application links; canonicalize only known macOS system aliases."""
    path = Path(os.path.abspath(path))
    system_aliases = {'/var': '/private/var', '/tmp': '/private/tmp', '/etc': '/private/etc'}
    for item in (path, *path.parents):
        if linked(item):
            expected = system_aliases.get(item.as_posix()) if sys.platform == 'darwin' else None
            if expected and item.resolve(strict=True) == Path(expected):
                continue
            raise ValueError(f'Symlink/junction paths are not supported: {item}')
    return path.resolve()


def payload(root):
    root = plain_path(root)
    result = {}
    for base, dirs, files in os.walk(root, followlinks=False):
        base = Path(base)
        # Reject even ignored links; a reviewed package must have a plain tree.
        for name in dirs + files:
            if linked(base / name):
                raise ValueError(f'Symlink/junction in package: {base / name}')
        dirs[:] = sorted(d for d in dirs if not excluded((base / d).relative_to(root)))
        for name in sorted(files):
            path = base / name
            relative = path.relative_to(root)
            if not excluded(relative):
                result[relative.as_posix()] = hashlib.sha256(path.read_bytes()).hexdigest()
    return result


def available(root):
    root = plain_path(root)
    if (root / 'suite.json').is_file():
        entries = json.loads((root / 'suite.json').read_text(encoding='utf-8'))['skills']
    else:
        text = (root / 'SKILL.md').read_text(encoding='utf-8')
        name = re.search(r'^name:\s*([a-z0-9-]+)\s*$', text, re.M)
        if not name:
            raise ValueError('Missing standalone skill name')
        entries = [{'name': name[1], 'path': '.', 'status': 'available'}]
    modules = {}
    for entry in entries:
        name = entry['name']
        if not isinstance(name, str) or len(name) > 64 or not NAME.fullmatch(name):
            raise ValueError('Invalid skill name in local inventory')
        if entry['status'] != 'available' or name in modules:
            raise ValueError('Inventory must contain unique available skills only')
        module = plain_path(root / entry['path'])
        if not module.is_relative_to(root) or not (module / 'SKILL.md').is_file() or not (module / 'LICENSE').is_file():
            raise ValueError(f'Invalid/self-contained skill path: {name}')
        modules[name] = module
    if not modules:
        raise ValueError('No available skills')
    return modules


def plan_install(root, agent, scope, project_path, selections=None, force=False):
    modules = available(root)
    names = selections or sorted(modules)
    if len(set(names)) != len(names) or any(name not in modules for name in names):
        raise ValueError('Select unique available skill names from the local inventory')
    base = plain_path(Path.home() if scope == 'user' else project_path)
    if not base.is_dir():
        raise ValueError(f'Target directory does not exist: {base}')
    agents = ['codex', 'claude'] if agent == 'both' else [agent]
    plan = []
    for name in names:
        source = modules[name]
        source_files = payload(source)
        for target_agent in agents:
            folder = '.agents' if target_agent == 'codex' else '.claude'
            parent = plain_path(base / folder / 'skills')
            target = plain_path(parent / name)
            if not target.is_relative_to(base) or target.parent != parent:
                raise ValueError('Destination escaped the selected installation directory')
            if target == source or target.is_relative_to(source) or source.is_relative_to(target):
                raise ValueError('Source and destination overlap')
            if target.exists() and not target.is_dir():
                raise ValueError(f'Destination is not a directory: {target}')
            same = target.is_dir() and payload(target) == source_files
            if target.exists() and not same and not force:
                raise ValueError(f'Changed installation exists: {target}; back it up, then use --force')
            plan.append((source, target, same))
    return plan


def copy_payload(source, target):
    for relative in payload(source):
        dest = target / relative
        dest.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source / relative, dest)


def install(plan, dry_run=False):
    for source, target, same in plan:
        action = 'unchanged' if same else ('replace' if target.exists() else 'install')
        print(f'{"DRY RUN " if dry_run else ""}{action}: {target}')
        if dry_run or same:
            continue
        parent = plain_path(target.parent)
        parent.mkdir(parents=True, exist_ok=True)
        # All destructive cleanup is limited to this generated staging directory.
        with tempfile.TemporaryDirectory(prefix='.skills-italia-stage-', dir=parent) as temp:
            stage = Path(temp)
            incoming = stage / 'incoming'
            incoming.mkdir()
            copy_payload(source, incoming)
            backup = stage / 'previous'
            if target.exists():
                target.rename(backup)
            try:
                incoming.rename(target)
            except OSError:
                if backup.exists():
                    backup.rename(target)
                raise


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--agent', choices=['both', 'codex', 'claude'], default='both')
    parser.add_argument('--scope', choices=['project', 'user'], default='project')
    parser.add_argument('--project-path', type=Path, default=Path.cwd())
    selector = parser.add_mutually_exclusive_group()
    selector.add_argument('--skill', action='append', help='select an available skill; repeat for multiple')
    selector.add_argument('--all', action='store_true', help='select all available skills (also the default)')
    parser.add_argument('--force', action='store_true', help='replace a changed install; back it up first')
    parser.add_argument('--dry-run', action='store_true', help='validate and display plan without copying')
    args = parser.parse_args(argv)
    try:
        plan = plan_install(ROOT, args.agent, args.scope, args.project_path, args.skill, args.force)
        install(plan, args.dry_run)
    except (OSError, ValueError, KeyError, TypeError) as exc:
        print(f'ERROR: {exc}', file=sys.stderr)
        return 1
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
