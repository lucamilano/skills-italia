# GitHub publication status

Repository: [lucamilano/skills-italia](https://github.com/lucamilano/skills-italia), public, default branch `main`.

The owner explicitly authorized repository creation and publication after reviewing the local preparation. GitHub authentication was verified against the `lucamilano` account. Commits use the account's GitHub `noreply` address; no personal email is published.

## Configuration verified

- The repository description is in Italian and all ten topics from `github-metadata.json` are configured. The root README uses Italian as its primary language, with a complete [English overview](README.en.md) linked for international contributors.
- Issues and Discussions are enabled; the wiki is disabled.
- Private vulnerability reporting, dependency vulnerability alerts, secret scanning and push protection are enabled.
- Private security reports use [GitHub Security Advisories](https://github.com/lucamilano/skills-italia/security/advisories/new).
- Conduct and abuse reports use the GitHub channels described in [CODE_OF_CONDUCT.md](../CODE_OF_CONDUCT.md), as selected by the owner.
- Homepage remains unset because no documentation website has been deployed.

## Publication verification

The code is uploaded to `main`. [Suite checks run 40096624618](https://github.com/lucamilano/skills-italia/actions/runs/40096624618) completed successfully for all three hosted environments:

| Environment | Result |
| --- | --- |
| Ubuntu, Python 3.10, Node.js 22 | **PASS**, including the dependency audit and 14 synthetic browser tests. |
| Windows, Python 3.13, Node.js 22 | **PASS**, including native PowerShell and Git Bash installation checks. |
| macOS, Python 3.13, Node.js 22 | **PASS**, including installation through the real macOS system temporary-directory alias. |

The initial CI run exposed an overly broad rejection of macOS `/var` aliases. Commit `e2dd37c` permits only the verified standard aliases `/var`, `/tmp` and `/etc` to their expected `/private/` targets; application symlink/junction rejection remains in place. A dedicated macOS regression test was added. Suite Python tests now discover 19 cases, with platform-specific skips; the frontend retains 44 passing Python tests and eight passing Node tests.

The 48 external URLs present at publication preparation were checked successfully, including expected login redirects for private reporting and issue creation. AgID maintenance redirects still do not verify normative content.

The initial suite release uses tag **`v0.1.0`**, with the available frontend skill remaining **1.0.0**. Published assets are listed in [GitHub Releases](https://github.com/lucamilano/skills-italia/releases). Each release archive is built from the tagged source with an inventory and SHA-256 checksums. Future changes to `main` do not rewrite that tag.

The [local preparation report](release-readiness.md) remains a historical snapshot; its earlier no-remote/no-commit observations do not describe this subsequent publication.

## Manual configuration

Upload [the prepared social preview](assets/social-preview.png) through GitHub repository Settings → Social preview. GitHub's standard repository REST API does not expose the image-upload setting. Reported-content options for repository administrators can also be reviewed in Settings; GitHub Support abuse reporting is available separately as documented in the Code of Conduct.

No Pages site, custom domain, mandatory review policy or branch protection is claimed. Interactive agent testing, E2E on real PA services and specialist accessibility/security/legal assessment remain outside the package publication checks.
