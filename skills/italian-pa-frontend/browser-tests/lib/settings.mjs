import fs from 'node:fs';
import path from 'node:path';
const supported = ['menu', 'modal', 'form', 'table', 'wizard'];
export function validateConfig(data) {
  if (!data || typeof data !== 'object' || Array.isArray(data)) throw Error('config must be an object');
  const url = new URL(data.baseURL);
  if (!['http:', 'https:'].includes(url.protocol)) throw Error('baseURL must use HTTP(S)');
  if (url.username || url.password) throw Error('Credentials must not be embedded in baseURL');
  const local = ['localhost', '127.0.0.1', '[::1]', '::1'].includes(url.hostname);
  if (!local && process.env.PA_ALLOW_REMOTE !== '1') throw Error('Only localhost is allowed by default; set PA_ALLOW_REMOTE=1 to opt in to remote targets');
  if (!Array.isArray(data.pages) || !data.pages.length) throw Error('pages must be a nonempty array');
  for (const page of data.pages) {
    if (typeof page !== 'string' || !page.startsWith('/') || page.startsWith('//') || page.includes('\\')) throw Error('Every page must be a root-relative path');
  }
  if (data.components && (typeof data.components !== 'object' || Array.isArray(data.components))) throw Error('components must be an object');
  for (const [name, item] of Object.entries(data.components || {})) {
    if (!supported.includes(name)) throw Error(`Unknown component contract: ${name}`);
    if (!item || typeof item !== 'object' || typeof item.path !== 'string' || !item.path.startsWith('/') || item.path.startsWith('//') || item.path.includes('\\')) throw Error(`Invalid component path for ${name}`);
    const required = {menu:['trigger','panel','close'],modal:['trigger','dialog','close'],form:['submit','error'],table:['table','header','row'],wizard:['next','previous','step']}[name];
    for(const key of required) if(typeof item[key] !== 'string' || !item[key].trim()) throw Error(`Missing ${name}.${key}`);
  }
  return data;
}
export function loadSettings() {
  const file = path.resolve(process.env.PA_TEST_CONFIG || path.join(process.cwd(),'config','example.json'));
  const data = validateConfig(JSON.parse(fs.readFileSync(file,'utf8')));
  return { ...data, file };
}
