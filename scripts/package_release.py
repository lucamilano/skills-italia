#!/usr/bin/env python3
"""Build reproducible local archives and checksums. Never creates tags or releases."""
import argparse
import hashlib
import json
from pathlib import Path
import sys
import zipfile

from install import ROOT, available, excluded, payload, plain_path

ROOT_FILES = {'README.md', 'LICENSE', 'CONTRIBUTING.md', 'CODE_OF_CONDUCT.md',
              'SECURITY.md', 'CHANGELOG.md', 'ROADMAP.md', 'RELEASE_NOTES.md',
              'suite.json', '.gitignore', '.gitattributes', '.editorconfig'}
ROOT_DIRS = {'docs', 'skills', 'scripts', 'tests', '.github'}


def suite_payload(root):
    files = payload(root)
    return {name: digest for name, digest in files.items()
            if (len(Path(name).parts) == 1 and name in ROOT_FILES)
            or (len(Path(name).parts) > 1 and Path(name).parts[0] in ROOT_DIRS)}


def write_zip(path, root, prefix, names):
    with zipfile.ZipFile(path, 'w', compression=zipfile.ZIP_DEFLATED, compresslevel=9) as archive:
        for name in sorted(names):
            info = zipfile.ZipInfo(f'{prefix}/{name}', date_time=(2026, 1, 1, 0, 0, 0))
            info.create_system = 3
            info.external_attr = (0o100644 << 16)
            info.compress_type = zipfile.ZIP_DEFLATED
            archive.writestr(info, (root / name).read_bytes(), compresslevel=9)


def build(root, output):
    root, output = plain_path(root), plain_path(output)
    manifest = json.loads((root / 'suite.json').read_text(encoding='utf-8'))
    modules = available(root)
    if output == root or root.is_relative_to(output):
        raise ValueError('Output must not be the source or its ancestor')
    if output.is_relative_to(root) and output != root / 'dist':
        raise ValueError('Use the ignored dist/ directory or an external output directory')
    output.mkdir(parents=True, exist_ok=True)
    records = []
    files = suite_payload(root)
    archive = output / f'skills-italia-{manifest["version"]}.zip'
    write_zip(archive, root, 'skills-italia', files)
    records.append({'archive': archive.name, 'files': files})
    for entry in manifest['skills']:
        name = entry['name']
        files = payload(modules[name])
        archive = output / f'{name}-{entry["version"]}.zip'
        write_zip(archive, modules[name], name, files)
        records.append({'archive': archive.name, 'files': files})
    inventory = output / 'release-inventory.json'
    inventory.write_text(json.dumps({'suite_version': manifest['version'], 'archives': records}, indent=2) + '\n', encoding='utf-8')
    paths = [output / item['archive'] for item in records] + [inventory]
    (output / 'SHA256SUMS').write_text(''.join(f'{hashlib.sha256(p.read_bytes()).hexdigest()}  {p.name}\n' for p in paths), encoding='utf-8')
    return paths + [output / 'SHA256SUMS']


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, default=ROOT / 'dist')
    args = parser.parse_args()
    try:
        for path in build(ROOT, args.output):
            print(path)
    except (OSError, ValueError, KeyError) as exc:
        print(f'ERROR: {exc}', file=sys.stderr)
        return 1
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
