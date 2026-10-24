import json
import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CATALOG = ROOT / 'catalog/components.json'

class ComponentCatalogTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data = json.loads(CATALOG.read_text(encoding='utf-8'))
        cls.items = cls.data['components']

    def test_unique_six_components(self):
        ids = [c['id'] for c in self.items]
        self.assertEqual(len(ids), len(set(ids)))
        self.assertEqual(set(ids), {'header','navigation','forms','tables','modals','steppers'})

    def test_sources_and_paths(self):
        for item in self.items:
            with self.subTest(item=item['id']):
                self.assertTrue(item['documentation_url'].startswith('https://italia.github.io/bootstrap-italia/docs/'))
                self.assertTrue((ROOT / item['doc']).is_file())
                self.assertTrue((ROOT / item['example']).is_file())
                self.assertEqual(item['status'], 'documented-not-runtime-verified')
                self.assertTrue(item['checks'])

    def test_lookup_list_and_show(self):
        cmd = [sys.executable,str(ROOT/'scripts/component_lookup.py')]
        out = subprocess.run(cmd+['list'], capture_output=True,text=True,check=True)
        self.assertIn('steppers:',out.stdout)
        out = subprocess.run(cmd+['show','forms'],capture_output=True,text=True,check=True)
        self.assertEqual(json.loads(out.stdout)['id'],'forms')

    def test_lookup_rejects_unknown(self):
        cmd = [sys.executable,str(ROOT/'scripts/component_lookup.py'),'show','not-real']
        out = subprocess.run(cmd,capture_output=True,text=True)
        self.assertEqual(out.returncode,2)

    def test_examples_no_external_cdn(self):
        for ex in (ROOT/'examples/components').glob('*.html'):
            content = ex.read_text(encoding='utf-8')
            self.assertNotIn('https://cdn.',content)
            self.assertNotIn('onclick=',content)

if __name__=='__main__':
    unittest.main()
