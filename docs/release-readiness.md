# Local release readiness report

Preparation date: **2026-10-24**. Target directory: `skills-italia`. Suite **0.1.0**, frontend skill **1.0.0**. This is the historical local preparation snapshot, before the separately authorized GitHub publication. See [publication status](publication-status.md) for the subsequent remote state.

See [verification procedures](verification.md), [release notes](../RELEASE_NOTES.md) and [publication steps](publication.md). No pending check should be inferred as passed.

## Initial repository analysis

The source directory contained one complete standalone skill: instructions, references, partial component/version catalogs, templates, examples, Python helpers and tests, an optional Playwright/axe module and a small Linux CI workflow. Initial checks passed: **41 Python tests and 7 Node tests**. The supplied directory had no Git metadata, branch, remote or tags. A new local repository was initialized on `main` in the sibling `skills-italia` deliverable; the source directory remains available.

The migration retains the domain logic, catalogs, examples, templates and historic 1.0.0 documents. Necessary packaging adaptations add module metadata, installed-path guidance, local installers and a lockfile. Browser config validation and Windows runner invocation receive targeted fixes verified separately. The historical module release notes describe earlier evidence, not the current migration checks.

## Final checks

Environment: Windows, Python **3.13.15**, Node.js **22.23.0**, npm **12.0.2**; native Windows PowerShell and Git Bash. Browser tooling was installed with the committed lockfile: Playwright **1.64.1**, axe-core integration **4.14.0**, Chromium **156.0.8078.4**. Optional validation used PyYAML **6.0.3** in a temporary environment outside the repository; it is not a runtime dependency.

| Check | Actual result |
| --- | --- |
| `python scripts/release_check.py` | **PASS** after targeted fixes; includes all rows below identified as local release checks. |
| Suite identity, manifest, versions, JSON and dependency lock consistency | **PASS**; one available skill, no future-module placeholders. |
| Local Markdown links, anchors and original module-relative references | **PASS**, zero broken targets. |
| Suite Python regressions | **18 discovered: 17 passed, 1 skipped**. Symlink creation is unavailable for this Windows account; the separate real Windows junction rejection test passed. |
| Frontend Python tests | **44 passed**: all original 41 plus three meaningful packaging regressions. |
| Frontend Node unit tests | **8 passed**: all original seven plus unsafe component-path regression coverage. |
| Native PowerShell and Git Bash installers | **PASS**: preview, project/user scope, both agents, repeat installs, changed-install refusal and forced replacement. Tests used temporary homes/projects. |
| Standalone archive extraction and installation | **PASS**; extracted module validates independently and its component lookup runs from an unrelated working directory. |
| Reproducible archives, exact inventories and SHA-256 checksums | **PASS**, tested by two independent local builds from unchanged inputs. |
| `npm ci --ignore-scripts` and `npm audit --audit-level=high` | **PASS**, registry reported **0 vulnerabilities** at preparation time. |
| `python scripts/browser_smoke.py` | **14 passed**, desktop and mobile Chromium: page smoke/axe, screenshots, menu, dialog, form error, table and wizard contracts on a synthetic localhost fixture. |
| Screenshot inspection | Desktop/mobile fixture screenshots and the social preview were actually opened; fixture content remains visible without captured horizontal clipping. This is not a visual review of a PA service. |
| External documentation URLs | **40 checked, HTTP success**, including redirects. AgID home/accessibility URLs redirected to maintenance, so their normative content remains unverified. |
| Bundled skill-creator `quick_validate.py` | **PASS** with the conservative frontend frontmatter. Environment requirements are in the body for compatibility with that validator. |
| GitHub YAML syntax | **7 files parsed successfully** with PyYAML. Full GitHub workflow execution remains pending. |
| Narrow source secret-pattern/private-file checks | **PASS**, no matching credentials/private configuration found in the publication payload. This is not a comprehensive secret or security audit. |
| Original file integrity | All **97** input files retained; **83 byte-identical**, **14 adaptations documented** in the [migration inventory](migration.md). |

The browser smoke runner executes the actual review command and captures evidence. It does not load Bootstrap Italia or simulate SPID, CIE, PDND or a real PA backend. Thus its success is evidence for the harness, not runtime validation of the full catalog or a production service.

## Documentation, discoverability and artifacts

The English README and complete Italian translation cover the same available/planned scope, installation paths, usage and limitations. Architecture, contribution, security, license, roadmap, source and release documents are linked. The suite has its own 0.1.0 changelog and release notes; original module history remains unchanged.

Repository description, ten valid topics, an original **1280 × 640** PNG social preview and GitHub CLI instructions are prepared locally. Homepage is unset. GitHub Pages is deliberately deferred; canonical URLs, sitemap, Open Graph and hreflang are documented as future site acceptance criteria, not claimed as deployed metadata.

Local release generation produces `dist/skills-italia-0.1.0.zip`, `dist/italian-pa-frontend-1.0.0.zip`, `dist/release-inventory.json` and `dist/SHA256SUMS`. These generated outputs are ignored. Dependencies, local reports, caches, `.git` and private configuration are excluded from archive contents.

## Checks not completed

- Actual Linux/macOS execution and remote GitHub Actions: the three-platform workflow is prepared but has not run on GitHub. Git Bash on Windows is not evidence of Linux/macOS execution.
- Interactive Codex and Claude Code sessions, other Agent Skills clients, and cloud/managed deployment variants.
- Browser E2E against a real PA application, integration/authorization tests against actual backends and runtime verification of all catalog/library versions.
- Screen reader, manual keyboard/zoom/contrast assessment of a real service, complete security/threat review, legal applicability and accessibility-statement assessment.
- Content verification of the AgID publications currently replaced by maintenance redirects.
- GitHub repository settings, public security reporting, branch protection and social-preview upload: no remote is configured and GitHub CLI is unavailable.

## Publication decisions at the end of local preparation

At the end of local preparation, owner/remote, reporting channels, public release date and explicit publication authorization were outstanding. These are historical observations; subsequent changes are tracked in [publication status](publication-status.md). No homepage or Pages origin is configured. Interactive agent testing, real PA application E2E and specialist/manual assessments remain separate from package verification.

Git state at that preparation checkpoint: branch `main`, **0 commits**, **no remotes**, **no tags**; prepared source files were untracked and uncommitted. Nothing had been pushed, published or uploaded at that checkpoint. The later authorized publication follows the [publication checklist](publication.md).
