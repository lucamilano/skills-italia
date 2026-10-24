import {test} from 'node:test';
import {strict as assert} from 'node:assert';
import {validateConfig} from '../lib/settings.mjs';
const valid={baseURL:'http://127.0.0.1:5000',pages:['/']};
test('accepts local project settings',()=>assert.equal(validateConfig(valid),valid));
test('refuses remote target by default',()=>assert.throws(()=>validateConfig({...valid,baseURL:'https://example.org'}),/localhost/));
test('rejects external path',()=>assert.throws(()=>validateConfig({...valid,pages:['//evil.org']}),/root-relative/));
test('rejects incomplete component spec',()=>assert.throws(()=>validateConfig({...valid,components:{modal:{path:'/'}}}),/Missing/));
test('rejects embedded credentials',()=>assert.throws(()=>validateConfig({...valid,baseURL:'http://user:pass@localhost:5000'}),/Credentials/));
test('rejects external and invalid component paths',()=>{
  for (const path of ['//example.org', '/\\example.org', 42]) {
    assert.throws(()=>validateConfig({...valid,components:{modal:{path,trigger:'#open',dialog:'#dialog',close:'#close'}}}),/Invalid component path/);
  }
});
