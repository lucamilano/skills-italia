import copy
import importlib.util
import json
import tempfile
import unittest
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
def load(name,path):
    spec=importlib.util.spec_from_file_location(name,ROOT/path)
    module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module);return module
validator=load('data_validator','scripts/validate_data_view.py')
scanner=load('pattern_scanner','scripts/discover_ui_patterns.py')
example=json.loads((ROOT/'templates/data-view.example.json').read_text(encoding='utf8'))

class DataViewTests(unittest.TestCase):
    def test_example_valid_with_honest_warnings(self):
        errors,warnings=validator.validate(example)
        self.assertEqual(errors,[])
        self.assertTrue(any('not verified' in msg for msg in warnings))
        self.assertTrue(any('server permission' in msg for msg in warnings))
    def test_rejects_unsupported_sort(self):
        data=copy.deepcopy(example);data['sorting']['allowed_fields']=['status']
        self.assertTrue(validator.validate(data)[0])
    def test_rejects_bad_pagination(self):
        data=copy.deepcopy(example);data['pagination']['page_size']=True
        self.assertTrue(validator.validate(data)[0])
    def test_export_warning(self):
        data=copy.deepcopy(example);data['export']={'enabled':True,'scope':'filtered_all','authorized_backend':False}
        self.assertTrue(any('export' in s for s in validator.validate(data)[1]))
    def test_source_confirmed_requires_endpoint(self):
        data=copy.deepcopy(example);data['data_source']['status']='confirmed'
        self.assertTrue(validator.validate(data)[0])
    def test_scanner_respects_ignored_dirs(self):
        with tempfile.TemporaryDirectory() as tmp:
            p=Path(tmp);(p/'components').mkdir();(p/'components'/'DataTable.tsx').write_text('// example')
            (p/'node_modules').mkdir();(p/'node_modules'/'HugeTable.tsx').write_text('no')
            report=scanner.discover(p)
            self.assertEqual(report['hints']['tables'],['components/DataTable.tsx'])
    def test_scanner_truncates(self):
        with tempfile.TemporaryDirectory() as tmp:
            p=Path(tmp)
            for n in range(3):(p/f'Form{n}.tsx').write_text('x')
            self.assertTrue(scanner.discover(p,limit=1)['truncated'])

if __name__=='__main__':unittest.main()
