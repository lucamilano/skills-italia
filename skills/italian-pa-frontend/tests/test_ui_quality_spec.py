import importlib.util
import json
import unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location('ui_quality',ROOT/'scripts/validate_ui_spec.py')
mod=importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)
class UIQualityTests(unittest.TestCase):
    def setUp(self): self.data=json.loads((ROOT/'templates/ui-quality-spec.example.json').read_text())
    def test_example(self): self.assertEqual(mod.check(self.data),[])
    def test_missing_content_order(self):
        self.data['layout'].pop('content_order')
        self.assertTrue(any('content_order' in x for x in mod.check(self.data)))
    def test_states(self):
        self.data['states']=['success']
        self.assertTrue(any('states' in x for x in mod.check(self.data)))
    def test_validation_flags(self):
        self.data['validation']['keyboard']='done'
        self.assertTrue(any('booleans' in x for x in mod.check(self.data)))
if __name__=='__main__': unittest.main()
