#!/usr/bin/env python3
"""Validate suite packaging, conservative skill metadata, JSON and source hygiene."""
import json
import os
from pathlib import Path
import re
import sys

from install import ROOT, NAME, SKIP_DIRS, available, excluded, linked

VERSION = re.compile(r'(0|[1-9]\d*)\.(0|[1-9]\d*)\.(0|[1-9]\d*)\Z')
REQUIRED = ['README.md', 'LICENSE', 'CONTRIBUTING.md', 'CODE_OF_CONDUCT.md',
            'SECURITY.md', 'CHANGELOG.md', 'ROADMAP.md', 'RELEASE_NOTES.md',
            'docs/README.it.md', 'docs/architecture.md', 'docs/installation.md',
            'docs/contributing-skills.md', 'docs/seo.md', 'docs/publication.md',
            'docs/release-readiness.md', 'docs/github-metadata.json',
            '.github/workflows/checks.yml', '.github/PULL_REQUEST_TEMPLATE.md']


def scalar(raw):
    raw = raw.strip()
    if raw.startswith('"'):
        value = json.loads(raw)
        if not isinstance(value, str):
            raise ValueError('Frontmatter scalar must be a string')
        return value
    if raw.startswith("'") and raw.endswith("'"):
        return raw[1:-1].replace("''", "'")
    if not raw or raw[0] in '|>[' or ': ' in raw or ' #' in raw:
        raise ValueError('Use a single-line quoted frontmatter scalar')
    return raw


def frontmatter(text):
    match = re.match(r'\A---\n(.*?)\n---\n', text, re.S)
    if not match:
        raise ValueError('SKILL.md needs YAML frontmatter')
    fields, in_metadata = {}, False
    for line in match[1].splitlines():
        if not line.strip():
            continue
        if line == 'metadata:':
            if 'metadata' in fields:
                raise ValueError('Duplicate metadata')
            fields['metadata'] = {}
            in_metadata = True
            continue
        nested = re.fullmatch(r'  ([a-z][a-z0-9_-]*):\s*(.+)', line)
        if nested and in_metadata:
            if nested[1] in fields['metadata']:
                raise ValueError('Duplicate metadata key')
            fields['metadata'][nested[1]] = scalar(nested[2])
            continue
        pair = re.fullmatch(r'([a-z][a-z0-9-]*):\s*(.+)', line)
        if not pair or pair[1] not in {'name', 'description', 'license', 'compatibility'} or pair[1] in fields:
            raise ValueError(f'Unsupported or duplicate frontmatter syntax: {line}')
        fields[pair[1]] = scalar(pair[2])
        in_metadata = False
    return fields


def validate(root=ROOT):
    issues = []
    for name in REQUIRED:
        if not (root / name).is_file():
            issues.append(f'Missing required suite file: {name}')
    try:
        manifest = json.loads((root / 'suite.json').read_text(encoding='utf-8'))
        modules = available(root)
        if manifest['name'] != 'skills-italia' or not VERSION.fullmatch(manifest['version']) or manifest['license'] != 'MIT':
            issues.append('Invalid suite identity, version or license')
        directories = {p.name for p in (root / 'skills').iterdir() if p.is_dir()}
        if directories != set(modules):
            issues.append('skills/ directories must match available manifest entries; no placeholders')
        for entry in manifest['skills']:
            module = modules[entry['name']]
            fm = frontmatter((module / 'SKILL.md').read_text(encoding='utf-8'))
            if fm.get('name') != module.name or module != root / 'skills' / entry['name']:
                issues.append(f'Skill name/path mismatch: {entry["name"]}')
            description = fm.get('description', '')
            if not description.strip() or len(description) > 1024:
                issues.append(f'Invalid description: {module.name}')
            if fm.get('metadata', {}).get('version') != entry['version'] or not VERSION.fullmatch(entry['version']):
                issues.append(f'Skill version mismatch: {module.name}')
            if fm.get('license') != 'MIT':
                issues.append(f'Undeclared license: {module.name}')
        for filename in ('install.py', 'install.ps1', 'install.sh'):
            if (root / 'scripts' / filename).read_bytes() != (root / 'skills/italian-pa-frontend/scripts' / filename).read_bytes():
                issues.append(f'Standalone installer diverged: {filename}')
        metadata = json.loads((root / 'docs/github-metadata.json').read_text(encoding='utf-8'))
        topics = metadata['topics']
        if len(topics) > 20 or len(set(topics)) != len(topics) or any(len(t) > 50 or not NAME.fullmatch(t) for t in topics):
            issues.append('Invalid GitHub topics')
        if metadata['homepage'] is not None:
            issues.append('Review homepage/canonical configuration before setting a real published URL')
        if not (root / metadata['social_preview']).is_file():
            issues.append('Missing social preview')
    except (OSError, ValueError, KeyError, TypeError) as exc:
        issues.append(f'Manifest/frontmatter validation: {exc}')
    for base, dirs, files in os.walk(root, followlinks=False):
        base = Path(base)
        dirs[:] = [d for d in dirs if d not in SKIP_DIRS]
        for name in dirs + files:
            if linked(base / name):
                issues.append(f'Symlink/junction in source: {(base / name).relative_to(root)}')
        for name in files:
            path = base / name
            relative = path.relative_to(root)
            if name.startswith('.env') or name in {'local.json', 'storage-state.json', 'storageState.json'} or path.suffix in {'.key', '.pem', '.tmp', '.bak'}:
                issues.append(f'Private/temporary file in source: {relative}')
            if excluded(relative):
                continue
            if path.suffix == '.json':
                try:
                    doc = json.loads(path.read_text(encoding='utf-8'))
                    if path.name == 'package.json':
                        lock = json.loads(path.with_name('package-lock.json').read_text(encoding='utf-8'))
                        package = lock['packages']['']
                        if any(package.get(key) != doc.get(key) for key in ('name', 'version', 'dependencies', 'devDependencies', 'engines')):
                            issues.append(f'Dependency lockfile mismatch: {relative}')
                except (OSError, ValueError) as exc:
                    issues.append(f'Invalid JSON {relative}: {exc}')
                except (KeyError, TypeError) as exc:
                    issues.append(f'Invalid dependency lockfile for {relative}: {exc}')
            if path.suffix.lower() in {'.png', '.jpg', '.gif', '.zip'}:
                continue
            try:
                text = path.read_text(encoding='utf-8')
            except UnicodeError:
                issues.append(f'Unexpected binary/non-UTF8 source file: {relative}')
                continue
            # Narrow high-confidence patterns only. Never print a matched credential.
            signatures = [r'-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----',
                          r'\bgh[pousr]_[A-Za-z0-9]{30,}\b', r'\bAKIA[A-Z0-9]{16}\b',
                          r'\bsk-[A-Za-z0-9_-]{40,}\b']
            if any(re.search(pattern, text) for pattern in signatures):
                issues.append(f'Possible credential pattern (value redacted): {relative}')
    return issues


if __name__ == '__main__':
    issues = validate()
    for issue in issues:
        print('ERROR:', issue)
    if not issues:
        print('OK: suite identity, available skills, versions, JSON and narrow hygiene checks.')
    raise SystemExit(1 if issues else 0)
