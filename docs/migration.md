# Initial suite migration inventory

[Architecture](architecture.md) · [Verification report](release-readiness.md) · [Machine-readable file inventory](migration-inventory.json)

The input contained **97 files**, excluding generated Python caches. All 97 have a destination in the new suite: **83 retain their exact original SHA-256**, while **14 are adapted** for the suite, installation or verified fixes. The JSON inventory records original/destination paths and before/after hashes at migration time. It is a dated migration snapshot, not a claim that files will never evolve.

No Git history was present in the input directory. Earlier frontend releases are preserved in the module's original `CHANGELOG.md`, `ROADMAP.md` and `RELEASE_NOTES.md`, byte-for-byte. Module catalogs, examples, templates, original Python tests and domain helper logic are also preserved byte-for-byte. The original license attribution is retained; the skill's standalone license is a copy of the original.

## Adapted original files

| File | Reason |
| --- | --- |
| Root `.gitignore` | Exclude release outputs, environments, local configuration and private session files. |
| Root `LICENSE` | Retain original attribution and add Skills Italia contributors. |
| `.github/workflows/checks.yml` | Suite checks, three OS targets, reviewed commit pins, dependency audit and a synthetic browser fixture. |
| Frontend `README.md` | Module-root commands, suite identity, installation behavior and local invocation guidance. |
| Frontend `SKILL.md` | Version/license metadata, installed-root path resolution, environment requirements and current-source verification instead of a fixed default library version. |
| Frontend `references/official-sources.md` | Add Dev Kit Italia and record the current link/content verification boundaries while retaining the historic snapshot. |
| Frontend `scripts/install.ps1` and `scripts/install.sh` | Preserve entry points; delegate to the self-contained local Python installer. |
| Frontend `scripts/validate_skill.py` | Require packaged license and exclude third-party/generated Markdown after dependency installation. |
| Frontend `browser-tests/package.json` | Declare the Node version required by the locked dependencies; preserve harness version 0.6.0. |
| Frontend `browser-tests/README.md` | Document repeatable `npm ci`. |
| Frontend `browser-tests/lib/settings.mjs` | Reject protocol-relative, backslash and non-string component paths. |
| Frontend `browser-tests/scripts/config.test.mjs` | Regression checks for rejected unsafe component paths. |
| Frontend `browser-tests/scripts/review.mjs` | Launch Playwright's local JavaScript CLI through Node on all OSes and report launch errors; avoid executing a Windows `.cmd` with `shell:false`. |

## New files

Suite files include the English README, complete Italian overview, manifest, suite changelog/roadmap/release notes, contribution/code-of-conduct/security policies, editor settings and the `docs/` guides. A vector source and 1280 × 640 PNG provide an independent social preview. GitHub gains issue/PR templates, a manual external-link workflow and dependency update configuration.

Root `scripts/` contains installation entry points, link and structure validation, the release gate, deterministic archive generation, wrapper tests and the synthetic browser runner. Root `tests/` contains installation and release regressions and the synthetic HTML fixture. The frontend gains its bundled license, Python installer, locked browser dependency tree and packaging regression tests. No future module directories were added.

For an exact current file list use `git status --short --untracked-files=all` before the initial commit; after committing, `git ls-files`. Generated `dist/`, dependencies, caches and private reports are excluded from both source publication and release payloads.
