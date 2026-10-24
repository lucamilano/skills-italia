#!/usr/bin/env python3
"""Repeatable suite release gate. Application browser E2E remains separate."""
import json
import os
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]


def main():
    commands = [
        ('suite structure and hygiene', [sys.executable, 'scripts/validate_suite.py'], ROOT),
        ('local documentation links', [sys.executable, 'scripts/check_links.py'], ROOT),
        ('suite Python regression tests', [sys.executable, '-m', 'unittest', 'discover', '-s', 'tests', '-v'], ROOT),
        ('native installation wrappers', [sys.executable, 'scripts/test_install_wrappers.py'], ROOT),
    ]
    manifest = json.loads((ROOT / 'suite.json').read_text(encoding='utf-8'))
    for entry in manifest['skills']:
        module = ROOT / entry['path']
        commands.append((entry['name'] + ' release checks', [sys.executable, 'scripts/release_check.py'], module))
    env = {**os.environ, 'PYTHONDONTWRITEBYTECODE': '1'}
    for label, command, directory in commands:
        print(f'\nChecking {label}', flush=True)
        try:
            result = subprocess.run(command, cwd=directory, env=env, check=False)
        except OSError as exc:
            print(f'FAIL: {label}: {exc}', file=sys.stderr)
            return 1
        if result.returncode:
            print(f'FAIL: {label} (exit {result.returncode})', file=sys.stderr)
            return result.returncode
    print('\nPASS: suite, documentation, unit, installation and packaging checks.')
    print('NOT RUN by this command: external links, dependency registry audit, interactive agents, application browser E2E and manual accessibility.')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
