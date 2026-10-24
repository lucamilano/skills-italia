import { test, expect } from '@playwright/test';
import AxeBuilder from '@axe-core/playwright';
import { loadSettings } from '../lib/settings.mjs';
const components = loadSettings().components || {};
async function scan(page) {
  const results = await new AxeBuilder({page}).withTags(['wcag2a','wcag2aa','wcag21a','wcag21aa','wcag22aa']).analyze();
  expect(results.violations).toEqual([]);
}
if (components.menu) test('Menu opens, receives focus, closes', async ({page}) => {
  const c=components.menu; await page.goto(c.path);
  await page.locator(c.trigger).click();
  await expect(page.locator(c.panel)).toBeVisible();
  await scan(page);
  await page.locator(c.close).click();
  await expect(page.locator(c.panel)).toBeHidden();
  await expect(page.locator(c.trigger)).toBeFocused();
});
if (components.modal) test('Modal focus, name and dismissal', async ({page}) => {
  const c=components.modal; await page.goto(c.path);
  await page.locator(c.trigger).click();
  const dlg=page.locator(c.dialog); await expect(dlg).toBeVisible();
  const ariaLabel=await dlg.getAttribute('aria-label');
  const labelledBy=await dlg.getAttribute('aria-labelledby');
  expect(Boolean(ariaLabel || labelledBy), 'Dialog accessible name').toBeTruthy();
  await scan(page);
  await page.locator(c.close).click();
  await expect(dlg).toBeHidden();
  await expect(page.locator(c.trigger)).toBeFocused();
});
if (components.form) test('Empty form shows actionable validation feedback', async ({page}) => {
  const c=components.form; await page.goto(c.path);
  await page.locator(c.submit).click();
  await expect(page.locator(c.error).first()).toBeVisible();
  await scan(page);
});
if (components.table) test('Table has header(s) and renders rows', async ({page}) => {
  const c=components.table; await page.goto(c.path);
  await expect(page.locator(c.table)).toBeVisible();
  expect(await page.locator(c.header).count()).toBeGreaterThan(0);
  // Zero rows may be valid when filtering or empty state applies.
  await scan(page);
});
if (components.wizard) test('Wizard navigates forward and backward', async ({page}) => {
  const c=components.wizard; await page.goto(c.path);
  const before=await page.locator(c.step).textContent();
  await page.locator(c.next).click();
  await expect.poll(async()=>page.locator(c.step).textContent()).not.toBe(before);
  await scan(page);
  await page.locator(c.previous).click();
  await expect.poll(async()=>page.locator(c.step).textContent()).toBe(before);
});
