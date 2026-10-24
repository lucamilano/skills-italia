# Skills Italia — Initial Public Release

Suite version: **0.1.0**. Release date: **2026-10-24**. Included skill: **Italian PA Frontend 1.0.0**. Suite tag: `v0.1.0`. The local preparation scripts never publish automatically.

Skills Italia introduces an independent, modular collection of AI agent skills for developing Italian Public Administration software. This initial release makes one skill available: Italian PA Frontend, for generating, auditing and improving accessible interfaces while preserving the project's chosen technology and existing backend contracts.

## Included

- Frontend skill with official design references, partial component and version catalogs, forms, wizards, data-view contracts, stack and reuse scanners, JSON validators and delivery templates.
- Optional Playwright and axe browser checks with screenshots and iterative review workflows.
- Bilingual English/Italian overview, installation and contribution guides, security policy and a public suite roadmap.
- Single skill and all-available installation for local Codex and Claude Code at project or user scope; Windows, Linux and macOS entry points.
- Reproducible local quality checks, CI configuration, release archives and GitHub metadata preparation.

## Availability and compatibility

Accessibility, Identity, Interoperability, Security and Architecture modules are **Planned**. Quality, Documentation and Privacy modules are **Under consideration**. They are not distributed as implementations.

Compatibility is based on the Agent Skills format and the documented local installation paths. Installation tests do not constitute interactive end-to-end testing in Codex or Claude Code. The frontend browser harness retains its own package version, 0.6.0; it is tooling inside skill 1.0.0, not the suite version.

## Migration

The former standalone package now lives in `skills/italian-pa-frontend/`. Skill-relative paths and commands remain based on that directory. Run suite commands from the repository root and module commands from the module root, or use absolute paths. Old standalone install entry points remain inside the module. Existing customized installations require a backup before replacement with `--force`.

The original frontend [changelog](skills/italian-pa-frontend/CHANGELOG.md), [roadmap](skills/italian-pa-frontend/ROADMAP.md) and [1.0.0 release notes](skills/italian-pa-frontend/RELEASE_NOTES.md) remain historical records. No existing tags or version history have been rewritten.

## Verification and limitations

Run `python scripts/release_check.py`; see the dated [local verification report](docs/release-readiness.md) for actual results and incomplete checks. The command checks structure, relative links, JSON, repository hygiene, Python/Node tests, installation and archive contents. Browser tests against real applications and manual accessibility assessments are separate.

The suite does not certify WCAG, AGID, security or legal conformity. Catalogs are partial, static audit findings are heuristic, and JSON validators only assess specification structure. Real service integrations, browser behavior, screen reader support and applicable legal requirements require project-specific verification.

## Riepilogo italiano

Prima release pubblica di **Skills Italia**, suite indipendente di skill per lo sviluppo di software della PA. Include soltanto **Italian PA Frontend 1.0.0**, preservata nella nuova struttura modulare. Sono aggiunte documentazione bilingue, installazione per singola skill o tutti i moduli disponibili, policy di contribuzione, controlli e pacchetti di rilascio. La roadmap distingue moduli pianificati e proposte da valutare. Non sono certificazioni automatiche e non sono state simulate integrazioni future.

## License and independence

MIT, retaining the original frontend contributor attribution. External tools and sources retain their own licenses.

Skills Italia is an independent open-source project and is not officially affiliated with or endorsed by AGID, Designers Italia, or the Italian Government.

Repository: [lucamilano/skills-italia](https://github.com/lucamilano/skills-italia). Release publication is an explicit maintainer operation after CI succeeds. Follow the [publication guide](docs/publication.md).
