import json,unittest,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'scripts'))
from version_lookup import parse_version,applicable
class VersionRulesTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls): cls.data=json.loads((ROOT/'catalog/version-rules.json').read_text(encoding='utf8'))
    def test_parse(self):
        self.assertEqual(parse_version('2.15'),(2,15,0))
        with self.assertRaises(ValueError): parse_version('3.0.0')
    def test_boundary(self):
        self.assertNotIn('header-mobile-dialog',[r['id'] for r in applicable(self.data,'2.14.9','header')])
        self.assertIn('header-mobile-dialog',[r['id'] for r in applicable(self.data,'2.15.0','header')])
    def test_input_rules(self):
        self.assertNotIn('input-form-control',[r['id'] for r in applicable(self.data,'2.10.0','forms')])
        self.assertIn('input-form-control',[r['id'] for r in applicable(self.data,'2.11.0','forms')])
    def test_sources_and_ids(self):
        ids=[r['id'] for r in self.data['rules']]
        self.assertEqual(len(ids),len(set(ids)))
        for r in self.data['rules']:
            self.assertTrue(r['source'].startswith('https://italia.github.io/'))
            self.assertFalse(r['runtime_verified'])
    def test_global(self):
        self.assertIn('focus-mouse-attribute',[r['id'] for r in applicable(self.data,'2.15.0','tables')])
if __name__=='__main__': unittest.main()
