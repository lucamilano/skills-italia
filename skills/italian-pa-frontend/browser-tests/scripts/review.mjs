#!/usr/bin/env node
import fs from 'node:fs';
import path from 'node:path';
import { spawnSync } from 'node:child_process';
import { fileURLToPath } from 'node:url';
import { formatReport, saveReport } from '../lib/visual-review.mjs';
const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const argv = process.argv.slice(2);
function arg(name, fallback) {
  const i = argv.indexOf(name);
  return i >= 0 ? argv[i+1] : fallback;
}
const iteration = Number(arg('--iteration','1'));
if (!Number.isSafeInteger(iteration) || iteration < 1 || iteration > 10) { console.error('Iteration must be 1..10'); process.exit(2); }
const config = path.resolve(arg('--config', path.join(root,'config','local.json')));
if (!fs.existsSync(config)) { console.error(`Missing config: ${config}`); process.exit(2); }
const output = path.resolve(arg('--output', path.join(root,'reports',`review-${iteration}.md`)));
const resultsPath = path.resolve(root,'reports',`review-${iteration}.json`);
fs.mkdirSync(path.dirname(resultsPath), {recursive:true});
const localCli = path.join(root, 'node_modules', '@playwright', 'test', 'cli.js');
if (!fs.existsSync(localCli)) { console.error('Install dependencies first: npm ci && npx playwright install chromium'); process.exit(2); }
const env = {...process.env, PA_TEST_CONFIG:config, PA_REVIEW_JSON:resultsPath, PA_REVIEW_ITERATION:String(iteration)};
const run = spawnSync(process.execPath, [localCli, 'test', '--project=desktop-chromium', '--project=mobile-chromium'], {cwd:root, env, stdio:'inherit', shell:false});
if (run.error) { console.error(`Unable to launch Playwright: ${run.error.message}`); process.exit(1); }
let data;
try { data = JSON.parse(fs.readFileSync(resultsPath,'utf8')); }
catch { console.error('Playwright did not write parseable JSON; inspect runtime errors.'); process.exit(run.status || 1); }
const markdown = formatReport({iteration,data,configPath:config,reportPath:resultsPath});
saveReport(output, markdown);
console.log(`Review report: ${output}`);
process.exit(run.status === null ? 1 : run.status);
