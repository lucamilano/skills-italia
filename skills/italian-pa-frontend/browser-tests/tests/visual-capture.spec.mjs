import { test, expect } from '@playwright/test';
import { loadSettings } from '../lib/settings.mjs';
import { slugForPath } from '../lib/visual-review.mjs';
const settings = loadSettings();
for (const target of settings.pages) {
  test(`Visual evidence: ${target}`, async ({ page }, testInfo) => {
    const response = await page.goto(target, { waitUntil: 'domcontentloaded' });
    expect(response?.status()).toBeLessThan(400);
    await page.locator('body').waitFor({ state: 'visible' });
    await page.evaluate(() => document.fonts.ready);
    // Avoid networkidle: background polling in real portals may never finish.
    const name = slugForPath(target);
    const fileName = `${name}-${testInfo.project.name}.png`;
    const image = await page.screenshot({ fullPage: true, animations: 'disabled', caret: 'hide' });
    await testInfo.attach(fileName, { body: image, contentType: 'image/png' });
    const diagnostics = await page.evaluate(() => ({
      viewportWidth: window.innerWidth,
      scrollWidth: document.documentElement.scrollWidth,
      title: document.title,
      lang: document.documentElement.lang || null,
      h1Count: document.querySelectorAll('h1').length
    }));
    await testInfo.attach('layout-diagnostics.json', { body: Buffer.from(JSON.stringify(diagnostics, null, 2)), contentType: 'application/json' });
    expect(diagnostics.scrollWidth, 'Page should not overflow viewport horizontally').toBeLessThanOrEqual(diagnostics.viewportWidth + 2);
  });
}
