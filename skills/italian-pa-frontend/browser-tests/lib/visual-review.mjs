import fs from 'node:fs';
import path from 'node:path';

export function slugForPath(value) {
  const clean = value.split('?')[0].split('#')[0].replace(/[^a-zA-Z0-9_-]+/g, '-').replace(/^-|-$/g, '').slice(0, 70);
  return clean || 'home';
}

export function summarizeResults(data) {
  const totals = { passed: 0, failed: 0, skipped: 0, timedOut: 0, interrupted: 0 };
  const failures = [];
  function visit(suites) {
    for (const suite of suites || []) {
      for (const spec of suite.specs || []) {
        for (const entry of spec.tests || []) {
          const result = (entry.results || []).at(-1);
          const outcome = entry.status === 'expected' ? 'passed' : entry.status === 'skipped' ? 'skipped' : entry.status === 'unexpected' ? (result?.status || 'failed') : entry.status === 'flaky' ? 'passed' : (result?.status || entry.status || 'skipped');
          if (Object.hasOwn(totals, outcome)) totals[outcome]++;
          else totals.skipped++;
          if (outcome !== 'passed') {
            const errors = (entry.results || []).flatMap(r => (r.errors || []).map(e => e.message || String(e))).slice(0, 3);
            if (outcome !== 'skipped') failures.push({ title: spec.title, project: entry.projectName, status: outcome, errors });
          }
        }
      }
      visit(suite.suites);
    }
  }
  visit(data.suites);
  return { totals, failures };
}

export function formatReport({ iteration, data, configPath, reportPath }) {
  const {totals, failures} = summarizeResults(data);
  const lines = [
    `# UI review — iteration ${iteration}`,
    '',
    `- Test config: \`${configPath}\``,
    `- Playwright JSON: \`${reportPath}\``,
    `- Outcomes: passed ${totals.passed}, failed ${totals.failed}, skipped ${totals.skipped}, timed out ${totals.timedOut}, interrupted ${totals.interrupted}`,
    '- Screenshot evidence: open the Playwright HTML report and inspect attachments for each desktop/mobile test.',
    '- Visual evaluation: **NOT AUTOMATED**; screenshots must be inspected by an agent with image capabilities or a human.',
    '- Accessibility: automated axe findings are partial; manual assistive-technology checks are required.',
    '', '## Test failures'
  ];
  if (!failures.length) lines.push('No failing test reported; this is not a visual quality pass.');
  for (const f of failures) lines.push(`- **${f.project || 'unknown'} / ${f.title}** (${f.status}): ${(f.errors.join(' ').slice(0,500) || 'See Playwright report').replace(/\s+/g,' ')}`);
  lines.push('', '## Manual visual inspection', '- [ ] Desktop screenshots checked for layout, density, hierarchy, focus and missing content.', '- [ ] Mobile screenshots checked for clipping, wrapping, tap targets and scroll.', '- [ ] Screenshots with dynamic content reviewed with appropriate masks/fixtures.', '', '## Change proposal and next iteration', '- File(s):', '- Problem / evidence:', '- Minimal proposed fix:', '- Regression risk:', '- Result after rerun:', '', '## Stop condition', 'Stop when all configured tests pass and the review is accepted, or when the iteration/effort budget is reached. Escalate unresolved regressions; never silently claim success.', '');
  return lines.join('\n');
}

export function saveReport(output, markdown) {
  fs.mkdirSync(path.dirname(output), {recursive: true});
  fs.writeFileSync(output, markdown, 'utf8');
}
