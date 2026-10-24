import hashlib
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
import zipfile

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'scripts'))
import install
import package_release
import check_links
from validate_suite import frontmatter


class ReleaseTests(unittest.TestCase):
    def test_reproducible_archives_inventory_checksums_and_standalone_install(self):
        with tempfile.TemporaryDirectory(prefix='skills italia release ') as temp:
            temp = Path(temp)
            outputs = package_release.build(ROOT, temp / 'first')
            again = package_release.build(ROOT, temp / 'second')
            self.assertEqual([p.name for p in outputs], [p.name for p in again])
            self.assertEqual([p.read_bytes() for p in outputs], [p.read_bytes() for p in again])
            inventory = json.loads((temp / 'first/release-inventory.json').read_text())
            for item in inventory['archives']:
                with zipfile.ZipFile(temp / 'first' / item['archive']) as archive:
                    names = archive.namelist()
                    self.assertEqual(len(names), len(set(names)))
                    self.assertTrue(any(name.endswith('/LICENSE') for name in names))
                    self.assertFalse(any(install.excluded(Path(name)) for name in names))
                    for name in names:
                        relative = name.split('/', 1)[1]
                        self.assertEqual(hashlib.sha256(archive.read(name)).hexdigest(), item['files'][relative])
            for line in (temp / 'first/SHA256SUMS').read_text().splitlines():
                digest, name = line.split('  ')
                self.assertEqual(hashlib.sha256((temp / 'first' / name).read_bytes()).hexdigest(), digest)
            standalone = temp / 'extracted'
            with zipfile.ZipFile(temp / 'first/italian-pa-frontend-1.0.0.zip') as archive:
                archive.extractall(standalone)
            module = standalone / 'italian-pa-frontend'
            target = temp / 'independent target'
            target.mkdir()
            result = subprocess.run([sys.executable, str(module / 'scripts/install.py'), '--all',
                                     '--agent', 'both', '--project-path', str(target)],
                                    cwd=temp, capture_output=True, text=True)
            self.assertEqual(result.returncode, 0, result.stderr)
            result = subprocess.run([sys.executable, 'scripts/validate_skill.py'], cwd=module, capture_output=True, text=True)
            self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
            result = subprocess.run([sys.executable, str(target / '.agents/skills/italian-pa-frontend/scripts/component_lookup.py'), 'show', 'forms'], cwd=temp, capture_output=True, text=True)
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertEqual(json.loads(result.stdout)['id'], 'forms')

    def test_release_rejects_output_in_source_subdirectories(self):
        with self.assertRaises(ValueError):
            package_release.build(ROOT, ROOT / 'docs/generated')

    def test_link_checker_reports_broken_targets_and_anchors(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            (root / 'README.md').write_text('# Heading\n\n[good](#heading) [bad](missing.md) [anchor](#missing)\n')
            errors, external = check_links.check_local(root)
            self.assertEqual(len(errors), 2)
            self.assertEqual(external, set())

    def test_frontmatter_rejects_duplicates_and_unsupported_syntax(self):
        for contents in ('name: one\nname: two', 'name: one\ndescription: >\n  hidden', 'name: one\nallowed-tools: shell'):
            with self.subTest(contents=contents), self.assertRaises(ValueError):
                frontmatter('---\n' + contents + '\n---\n')


if __name__ == '__main__':
    unittest.main()
