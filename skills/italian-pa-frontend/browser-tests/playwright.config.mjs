import { defineConfig, devices } from '@playwright/test';
import { loadSettings } from './lib/settings.mjs';
const config = loadSettings();
export default defineConfig({
  testDir: './tests',
  timeout: 30000,
  expect: { timeout: 5000 },
  retries: process.env.CI ? 1 : 0,
  reporter: [['list'], ['html', { open: 'never', outputFolder: 'reports/html' }], ['json', { outputFile: process.env.PA_REVIEW_JSON || 'reports/results.json' }]],
  outputDir: 'reports/artifacts',
  use: { baseURL: config.baseURL, trace: 'retain-on-failure', screenshot: 'only-on-failure' },
  projects: [{name:'desktop-chromium',use:{...devices['Desktop Chrome']}}, {name:'mobile-chromium',use:{...devices['Pixel 7']}}]
});
