import unittest, json, sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'scripts'))
from validate_administrative_flow import validate

class AdministrativeFlowTests(unittest.TestCase):
    def setUp(self):self.sample=json.loads((ROOT/'templates/administrative-flow.example.json').read_text(encoding='utf-8'))
    def test_valid_sample(self):
        errors,warnings=validate(self.sample)
        self.assertEqual(errors,[]); self.assertTrue(any('submit' in w for w in warnings))
    def test_duplicate_step_id(self):
        self.sample['steps'].append(dict(self.sample['steps'][0]))
        self.assertTrue(any('duplicate' in e for e in validate(self.sample)[0]))
    def test_duplicate_field_id(self):
        self.sample['steps'][1]['fields']=[dict(self.sample['steps'][0]['fields'][0])]
        self.assertTrue(any('duplicate' in e for e in validate(self.sample)[0]))
    def test_missing_required_flag(self):
        self.sample['steps'][0]['fields'][0].pop('required')
        self.assertTrue(any('boolean' in e for e in validate(self.sample)[0]))
    def test_draft_warning(self):
        self.sample['features']['draft']=True
        self.assertTrue(any('draft' in w for w in validate(self.sample)[1]))
    def test_attachments_warning(self):
        self.sample['features']['attachments']=True
        self.assertTrue(any('attachments' in w for w in validate(self.sample)[1]))
    def test_invalid_workflow(self):
        self.sample['workflow']='other'
        self.assertTrue(validate(self.sample)[0])
    def test_catalog_references_exist(self):
        catalog=json.loads((ROOT/'catalog/administrative-workflows.json').read_text(encoding='utf-8'))
        for flow in catalog['workflows']:
            for ref in flow['references']:self.assertTrue((ROOT/ref).is_file())
if __name__=='__main__':unittest.main()
