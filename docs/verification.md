# Verification guide and evidence boundaries

[Local release report](release-readiness.md) · [Release notes](../RELEASE_NOTES.md)

## Required local checks

With Python 3.10+ and Node.js 22.12+, from the suite root:

```console
python scripts/release_check.py
```

This runs suite structure, metadata/version and repository hygiene validation, Markdown links and anchors, JSON parsing, suite Python regression tests and each skill's preserved release checks. Tests use temporary destinations, including paths with spaces; they do not install skills into your actual home directory. Dependency registry audits are a separate online check.

Suite regression tests cover installation selection, both agents, user/project scope, repeat installation, changed-content refusal and replacement, unsafe names, path overlap and symlinks where supported. They also inspect release inventories, deterministic archives and standalone extraction. Individual modules keep their own domain test suites. Missing required executables are a failure, not a pass.

The PowerShell and Bash wrappers can be tested through `python scripts/test_install_wrappers.py`. A missing shell is reported as **NOT RUN**; CI runs PowerShell on Windows and Bash on Linux/macOS. CI configuration is prepared locally; remote CI results cannot be claimed before publication.

## External links and dependency audit

```console
python scripts/check_links.py --external
```

External link checks use bounded timeouts, show final URLs and fail on inaccessible URLs; local checks do not require network. Distinguish a transient upstream outage from an obsolete link through content review, rather than rewriting official links to unofficial mirrors. External checks are a manual workflow in CI so network availability does not make every contribution fail.

From the frontend `browser-tests/` directory:

```console
npm ci
npm run validate
npm audit --audit-level=high
```

The lockfile makes npm installation repeatable. Audit needs current registry data; a clean result covers only vulnerabilities known to that registry at that time. Dependabot is configured for npm and GitHub Actions. Dependency installation and audit do not run a browser.

## Application browser checks (separate)

To exercise all existing browser contracts against the repository's synthetic fixture, first install the locked browser dependencies and Chromium, then run `python scripts/browser_smoke.py` from the suite root. This starts a temporary localhost HTTP server and invokes the real review runner on desktop/mobile. It creates ignored reports under the frontend browser module. The fixture is a harness regression check, not a PA portal or proof that every catalog component works with a real design-system library.

The frontend Playwright suite needs an actual running application and a configuration with real selectors and synthetic data. Read the [browser guide](../skills/italian-pa-frontend/browser-tests/README.md) and run `npm test` or `npm run review` only against an authorized target. The example configuration is not a test-ready universal application. Test collection is useful but is not an E2E pass.

Record target, date, browser, viewport, configured contracts, screenshots and results. Do not commit real session state or private reports. The runner does not interpret screenshots or implement fixes. Keyboard, focus, zoom/reflow, contrast, content and screen reader checks require actual review; an agent must open screenshots before claiming visual analysis.

## What passing the release gate means

It means the package and developer tools passed the specified checks in the reported environment. It does not prove interactive agent behavior, correctness on every stack, real API integration, full accessibility, security certification or regulatory conformity. JSON brief validators check structure; the HTML scanner is heuristic; the component/version catalogs are partial and not fully browser-verified. Checks not performed must stay explicit in release notes and delivery reports.
