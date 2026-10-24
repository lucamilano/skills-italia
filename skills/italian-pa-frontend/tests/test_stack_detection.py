import json
import tempfile
import unittest
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
from detect_stack import inspect

class StackDetectionTests(unittest.TestCase):
    def test_empty_project_does_not_guess(self):
        with tempfile.TemporaryDirectory() as d:
            result=inspect(d)
            self.assertEqual(result['signals'], [])
            self.assertEqual(result['decision'], 'ask-user-if-code-required')

    def test_multiple_frameworks_reported_not_selected(self):
        with tempfile.TemporaryDirectory() as d:
            Path(d,'package.json').write_text(json.dumps({'dependencies':{'next':'15.1.0','react':'19.0.0','bootstrap-italia':'2.18.0'}}))
            result=inspect(d)
            technologies={s['technology'] for s in result['signals']}
            self.assertTrue({'Next.js','React','Bootstrap Italia'} <= technologies)
            self.assertEqual(result['decision'], 'review-signals')

    def test_source_only_stack(self):
        with tempfile.TemporaryDirectory() as d:
            Path(d,'Page.razor').write_text('<h1>Hello</h1>')
            self.assertIn('Blazor', {s['technology'] for s in inspect(d)['signals']})

if __name__=='__main__': unittest.main()
