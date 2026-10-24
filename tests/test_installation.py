import contextlib
import io
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'scripts'))
import install


class InstallationTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix='skills italia ')
        self.addCleanup(self.temp.cleanup)
        self.base = Path(self.temp.name)
        self.project = self.base / 'project with spaces'
        self.project.mkdir()

    def perform(self, source=ROOT, agent='both', scope='project', selections=None, force=False, dry=False):
        plan = install.plan_install(source, agent, scope, self.project, selections, force)
        with contextlib.redirect_stdout(io.StringIO()):
            install.install(plan, dry)
        return plan

    def test_both_agents_project_complete_payload(self):
        self.perform(selections=['italian-pa-frontend'])
        expected = install.payload(ROOT / 'skills/italian-pa-frontend')
        for folder in ('.agents', '.claude'):
            target = self.project / folder / 'skills/italian-pa-frontend'
            self.assertEqual(install.payload(target), expected)
            self.assertTrue((target / 'LICENSE').is_file())
            self.assertFalse((target / 'suite.json').exists())

    def test_all_available_user_scope(self):
        with patch.object(Path, 'home', return_value=self.project):
            self.perform(scope='user')
        self.assertTrue((self.project / '.agents/skills/italian-pa-frontend/SKILL.md').is_file())
        self.assertTrue((self.project / '.claude/skills/italian-pa-frontend/SKILL.md').is_file())

    def test_dry_run_does_not_write(self):
        self.perform(dry=True)
        self.assertEqual(list(self.project.iterdir()), [])

    def test_repeat_preserves_files(self):
        self.perform(agent='codex')
        target = self.project / '.agents/skills/italian-pa-frontend/SKILL.md'
        os.utime(target, (1000000, 1000000))
        plan = self.perform(agent='codex')
        self.assertTrue(plan[0][2])
        self.assertEqual(target.stat().st_mtime, 1000000)

    def test_preflight_refuses_all_before_any_destination_is_changed(self):
        target = self.project / '.claude/skills/italian-pa-frontend'
        target.mkdir(parents=True)
        (target / 'custom.txt').write_text('do not destroy')
        with self.assertRaises(ValueError):
            self.perform()
        self.assertFalse((self.project / '.agents').exists())
        self.assertEqual((target / 'custom.txt').read_text(), 'do not destroy')

    def test_force_replaces_selected_skill_without_touching_others(self):
        self.perform(agent='codex')
        target = self.project / '.agents/skills/italian-pa-frontend'
        (target / 'obsolete.txt').write_text('old')
        other = target.parent / 'another-skill'
        other.mkdir()
        (other / 'keep.txt').write_text('keep')
        self.perform(agent='codex', force=True)
        self.assertFalse((target / 'obsolete.txt').exists())
        self.assertEqual((other / 'keep.txt').read_text(), 'keep')
        self.assertFalse(list(target.parent.glob('.skills-italia-stage-*')))

    def test_rollback_on_failed_destination_rename(self):
        self.perform(agent='codex')
        target = self.project / '.agents/skills/italian-pa-frontend'
        (target / 'custom.txt').write_text('restore me')
        original = Path.rename

        def fail_incoming(path, destination):
            if path.name == 'incoming':
                raise OSError('simulated rename failure')
            return original(path, destination)

        with patch.object(Path, 'rename', fail_incoming):
            with self.assertRaises(OSError):
                self.perform(agent='codex', force=True)
        self.assertEqual((target / 'custom.txt').read_text(), 'restore me')

    def test_unknown_duplicate_and_traversal_names_do_not_write(self):
        for selection in (['italian-pa-security'], ['../escape'], ['italian-pa-frontend'] * 2):
            with self.subTest(selection=selection), self.assertRaises(ValueError):
                self.perform(selections=selection)
        self.assertEqual(list(self.project.iterdir()), [])

    def test_source_destination_overlap_is_rejected(self):
        module = ROOT / 'skills/italian-pa-frontend'
        with self.assertRaises(ValueError):
            install.plan_install(module, 'codex', 'project', module, force=True)

    def test_manifest_escape_is_rejected(self):
        source = self.base / 'bad-suite'
        source.mkdir()
        manifest = {'skills': [{'name': 'escape', 'status': 'available', 'path': '../outside'}]}
        (source / 'suite.json').write_text(json.dumps(manifest))
        with self.assertRaises(ValueError):
            install.available(source)

    def test_symlinked_destination_is_rejected(self):
        outside = self.base / 'outside'
        outside.mkdir()
        try:
            (self.project / '.agents').symlink_to(outside, target_is_directory=True)
        except OSError:
            self.skipTest('symlink creation not supported by current account')
        with self.assertRaises(ValueError):
            self.perform(agent='codex', force=True)
        self.assertEqual(list(outside.iterdir()), [])

    def test_generated_and_private_files_are_excluded(self):
        source = self.base / 'standalone'
        source.mkdir()
        (source / 'SKILL.md').write_text('---\nname: example-skill\ndescription: example\n---\n')
        (source / 'LICENSE').write_text('MIT')
        for name in ('.env', 'local.json', 'storageState.json', 'private.key'):
            (source / name).write_text('private test fixture')
        (source / 'node_modules').mkdir()
        (source / 'node_modules/dependency.js').write_text('generated')
        self.perform(source=source, agent='claude')
        dest = self.project / '.claude/skills/example-skill'
        self.assertEqual(set(install.payload(dest)), {'SKILL.md', 'LICENSE'})

    @unittest.skipUnless(os.name == 'nt', 'Windows junction behavior')
    def test_windows_junction_destination_is_rejected(self):
        import _winapi
        outside = self.base / 'junction target'
        outside.mkdir()
        _winapi.CreateJunction(str(outside), str(self.project / '.agents'))
        with self.assertRaises(ValueError):
            self.perform(agent='codex', force=True)
        self.assertEqual(list(outside.iterdir()), [])

    def test_cli_outside_source_cwd_and_nonexistent_project(self):
        command = [sys.executable, str(ROOT / 'scripts/install.py'), '--agent', 'codex',
                   '--skill', 'italian-pa-frontend', '--project-path', str(self.project)]
        result = subprocess.run(command, cwd=self.base, capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, result.stderr)
        result = subprocess.run(command[:-1] + [str(self.base / 'missing')], cwd=self.base, capture_output=True)
        self.assertNotEqual(result.returncode, 0)


if __name__ == '__main__':
    unittest.main()
