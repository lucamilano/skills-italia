# Suite architecture and independent skill lifecycle

[Overview](../README.md) · [Installation](installation.md) · [Contributing skills](contributing-skills.md)

## Boundaries

The root owns the public identity, suite manifest, governance, installer, repository checks and release packaging. `skills/<name>/` owns domain instructions, references, catalogs, examples, templates, helper scripts and domain tests. A skill must work after being copied out of the suite: do not require relative paths into root docs or another module.

`suite.json` lists **only available** skills, their path and their independent version. Planned modules belong in [ROADMAP.md](../ROADMAP.md). They have no empty directories or installable stubs. The manifest is also the installation allowlist and release inventory.

The first module retains `italian-pa-frontend` as its Agent Skills identifier and 1.0.0 as its version. It offers Generate, Audit and Refactor workflows; specialist rules remain in its `SKILL.md` and progressively loaded references. Root policy does not add framework requirements or replace module workflows.

## Versioning

The initial **suite 0.1.0** is distinct from **frontend skill 1.0.0** and its **browser harness 0.6.0**. The latter is an internal optional tool package version. Record skill versions in `SKILL.md` metadata and `suite.json`; validators check agreement. Add future skills with their own version and changelog when accepted.

Use semantic versioning: breaking installation/contract changes require an appropriate major release once stable; compatible capabilities a minor release; compatible fixes a patch release. During suite 0.x, document breaking changes explicitly in release notes. Update only the module versions actually changed after release, and update the suite manifest when distributing them. This migration preserves frontend 1.0.0 as requested; packaging adaptations are recorded in the suite changelog, with the original module changelog preserved.

Never rewrite published tags. Suggested future tag conventions: `v0.1.0` for the suite and `<skill-name>-v<version>` for independent module releases. Existing standalone tags, if later imported, retain their original identifiers. No history or tags were present in the supplied directory; it was not a Git checkout.

## Installation and distribution

An installer copies the complete selected skill folder, including its MIT license. It excludes caches, installed dependencies, generated reports, local configs and secret/session files. The suite implementation of `scripts/install.py` is mirrored byte-for-byte inside the frontend module so the historical standalone entry points keep working after extraction. A repository check prevents divergence; update the root implementation then synchronize the module copy.

Install plans are validated before copying. Copies are staged beside destinations and renamed into place. Changed existing installs require `--force`; an internal backup supports rollback if the rename fails, but is removed after success. Users must separately back up customizations they wish to keep. This is a per-destination replacement, not a multi-agent filesystem transaction.

`scripts/package_release.py` creates a deterministic suite ZIP, a ZIP for each available skill, an inventory and SHA-256 checksums. Root archives use the `skills-italia/` prefix; standalone archives use the skill name as prefix. The exact generated allowlist is validated and secrets/local outputs are excluded. Checksums detect corruption; they are not cryptographic signatures or evidence of publisher identity.

## Quality layers

Root checks validate manifest consistency, local Markdown links, JSON, required distribution files and repository hygiene. Suite regression tests exercise installation, unsafe paths, replacement and packaging. Each module keeps its existing Python and Node tests, run from that module's root. E2E checks require a running application and remain explicitly separate.

## Public documentation decision

For this release, GitHub-rendered Markdown is the maintained public documentation. A separate Pages site would duplicate navigation and add a generator dependency before there is a real origin URL. [SEO and Pages guidance](seo.md) defines the future bilingual information architecture and canonical/sitemap requirements without inventing a domain or generating empty pages.
