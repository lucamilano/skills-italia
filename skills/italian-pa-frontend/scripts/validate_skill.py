#!/usr/bin/env python3
"""Validate packaging and local markdown references; no third-party deps."""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / 'SKILL.md'
REQUIRED = ['README.md','references/official-sources.md','references/accessibility.md',
            'references/design-rules.md','references/audit.md',
            'references/technology-selection.md','ROADMAP.md','LICENSE']
IGNORE = {'node_modules', '__pycache__', 'reports', 'dist', '.git', '.venv',
          'playwright-report', 'test-results'}


def validate():
    issues = []
    contents = MANIFEST.read_text(encoding='utf-8')
    match = re.match(r'\A---\n(.*?)\n---\n', contents, flags=re.S)
    if not match:
        issues.append('SKILL.md requires YAML frontmatter at top')
    else:
        fm = match.group(1)
        for field in ('name','description'):
            if not re.search(rf'^{field}:\s*\S+', fm, re.M):
                issues.append(f'frontmatter missing: {field}')
        if not re.search(r'^name:\s*italian-pa-frontend\s*$', fm, re.M):
            issues.append('skill name must match directory')
    for path in REQUIRED:
        if not (ROOT / path).is_file():
            issues.append(f'missing required file: {path}')
    for md in ROOT.rglob('*.md'):
        if set(md.relative_to(ROOT).parts) & IGNORE:
            continue
        text = md.read_text(encoding='utf-8')
        # Only backtick-enclosed local paths in the current package.
        for name in re.findall(r'`((?:references|templates|examples|scripts)/[\w./-]+)`', text):
            if '<' not in name and not (ROOT/name).exists():
                issues.append(f'{md.relative_to(ROOT)} references missing: {name}')
    return issues


if __name__ == '__main__':
    problems = validate()
    if problems:
        print('\n'.join(f'ERROR: {p}' for p in problems))
        sys.exit(1)
    print('OK: SKILL.md, required files and local links validated.')
