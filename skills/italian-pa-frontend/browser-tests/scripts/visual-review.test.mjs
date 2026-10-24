import test from 'node:test';
import assert from 'node:assert/strict';
import { slugForPath, summarizeResults, formatReport } from '../lib/visual-review.mjs';
test('path slugs are safe and deterministic', () => {
 assert.equal(slugForPath('/'), 'home');
 assert.equal(slugForPath('/pratiche/lista?x=1'), 'pratiche-lista');
});
test('nested suites are summarized', () => {
 const obj = { suites: [{ specs: [{ title: 'smoke', tests: [
  { status: 'expected', projectName: 'desktop', results: [{ status: 'passed' }] },
  { status: 'unexpected', projectName: 'mobile', results: [{ status: 'failed', errors: [{ message: 'horizontal scroll' }] }] }
 ] }] }] };
 const summary = summarizeResults(obj);
 assert.equal(summary.totals.passed,1);assert.equal(summary.totals.failed,1);
 assert.equal(summary.failures[0].errors[0], 'horizontal scroll');
 const report=formatReport({iteration:2,data:obj,configPath:'local.json',reportPath:'out.json'});
 assert.match(report,/NOT AUTOMATED/);assert.match(report,/horizontal scroll/);
});
