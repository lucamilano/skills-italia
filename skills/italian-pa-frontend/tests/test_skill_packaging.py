import importlib.util
from pathlib import Path
import shutil
import tempfile
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('skill_packaging_validator', ROOT / 'scripts/validate_skill.py')
validator = importlib.util.module_from_spec(spec)
spec.loader.exec_module(validator)


class SkillPackagingTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        for name in ['SKILL.md', *validator.REQUIRED]:
            target = self.root / name
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(ROOT / name, target)
        # A minimal entry point avoids unrelated reference requirements in this fixture.
        (self.root / 'SKILL.md').write_text('---\nname: italian-pa-frontend\ndescription: Test packaging\n---\n', encoding='utf-8')
        for name in validator.REQUIRED:
            if name.endswith('.md'):
                (self.root / name).write_text('# Fixture\n', encoding='utf-8')

    def validate(self):
        with patch.object(validator, 'ROOT', self.root), patch.object(validator, 'MANIFEST', self.root / 'SKILL.md'):
            return validator.validate()

    def test_ignores_dependency_markdown(self):
        path = self.root / 'browser-tests/node_modules/example/README.md'
        path.parent.mkdir(parents=True)
        path.write_text('`references/only-in-dependency.md`', encoding='utf-8')
        self.assertEqual(self.validate(), [])

    def test_reports_missing_packaged_reference(self):
        (self.root / 'README.md').write_text('`references/missing.md`', encoding='utf-8')
        self.assertTrue(any('references/missing.md' in issue for issue in self.validate()))

    def test_requires_license(self):
        (self.root / 'LICENSE').unlink()
        self.assertTrue(any('LICENSE' in issue for issue in self.validate()))


if __name__ == '__main__':
    unittest.main()
