import { test, expect } from '@playwright/test';
import AxeBuilder from '@axe-core/playwright';
import { loadSettings } from '../lib/settings.mjs';
const settings = loadSettings();
for (const target of settings.pages) {
  test(`Page smoke and axe: ${target}`, async ({ page }, testInfo) => {
    const errors = [];
    page.on('pageerror', (e) => errors.push(e.message));
    const response = await page.goto(target);
    expect(response, 'App should return a navigation response').toBeTruthy();
    expect(response.status(), 'Page must be served').toBeLessThan(400);
    await expect(page.locator('body')).toBeVisible();
    expect(errors, 'Page JavaScript errors').toEqual([]);
    const results = await new AxeBuilder({page}).withTags(['wcag2a','wcag2aa','wcag21a','wcag21aa','wcag22aa']).analyze();
    await testInfo.attach('axe-violations.json', {body: Buffer.from(JSON.stringify(results.violations,null,2)), contentType:'application/json'});
    expect(results.violations, 'Automated axe checks; manual checks still required').toEqual([]);
  });
}
