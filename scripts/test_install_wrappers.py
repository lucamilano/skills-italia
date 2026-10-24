#!/usr/bin/env python3
"""Exercise native installer wrappers in temporary project and user destinations."""
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile

from install import ROOT


def main():
    shells = [('PowerShell', shutil.which('pwsh') or shutil.which('powershell')),
              ('Bash', shutil.which('bash'))]
    if os.name == 'nt' and not shells[1][1]:
        candidate = Path(os.environ.get('ProgramFiles', 'C:/Program Files')) / 'Git/bin/bash.exe'
        if candidate.is_file():
            shells[1] = ('Bash', str(candidate))
    for label, shell in shells:
        if not shell:
            print(f'NOT RUN: {label} wrapper (shell unavailable)')
            continue
        with tempfile.TemporaryDirectory(prefix='skills italia wrappers ') as temp:
            target = Path(temp) / 'project with spaces'
            target.mkdir()
            user_home = Path(temp) / 'user home'
            user_home.mkdir()
            env = {**os.environ, 'HOME': str(user_home), 'USERPROFILE': str(user_home),
                   'PYTHONDONTWRITEBYTECODE': '1'}
            if label == 'PowerShell':
                base = [shell, '-NoProfile', '-File', str(ROOT / 'scripts/install.ps1')]
                project = ['-All', '-Agent', 'both', '-Scope', 'project', '-ProjectPath', str(target)]
                user = ['-Skill', 'italian-pa-frontend', '-Agent', 'both', '-Scope', 'user']
                dry = ['-DryRun']
                force = ['-Force']
            else:
                script = (ROOT / 'scripts/install.sh').as_posix()
                if os.name == 'nt':
                    script = '/' + script[0].lower() + script[2:]
                base = [shell, script]
                project = ['--all', '--agent', 'both', '--scope', 'project', '--project-path', str(target)]
                user = ['--skill', 'italian-pa-frontend', '--agent', 'both', '--scope', 'user']
                dry, force = ['--dry-run'], ['--force']
            for options in (project + dry, project, project, user):
                result = subprocess.run(base + options, cwd=ROOT, env=env, check=False, capture_output=True, text=True)
                if result.returncode:
                    print(result.stdout, result.stderr)
                    return result.returncode
            installed = target / '.agents/skills/italian-pa-frontend'
            (installed / 'customization.txt').write_text('local change', encoding='utf-8')
            rejected = subprocess.run(base + project, cwd=ROOT, env=env, capture_output=True, text=True)
            if rejected.returncode == 0:
                print(f'FAIL: {label} did not reject a changed installation')
                return 1
            subprocess.run(base + project + force, cwd=ROOT, env=env, check=True, capture_output=True)
            for dest in (target, user_home):
                for agent_dir in ('.agents', '.claude'):
                    if not (dest / agent_dir / 'skills/italian-pa-frontend/SKILL.md').is_file():
                        print(f'FAIL: {label} missing {agent_dir} installation')
                        return 1
            if (installed / 'customization.txt').exists():
                print(f'FAIL: {label} replacement retained obsolete file')
                return 1
            print(f'PASS: {label} dry run, both agents, project/user, repeat, refusal and forced update.')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
