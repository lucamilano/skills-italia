# Skills Italia roadmap

[Panoramica italiana](README.md) · [English overview](docs/README.en.md) · [Propose a skill](docs/contributing-skills.md)

Skills Italia supports the lifecycle of Italian public sector software, from interfaces to modernization and trustworthy integrations. This is a sequence of areas to develop, not a dated delivery commitment. Community needs, official specifications, maintainers and verification capacity determine priorities.

**Available** means implemented and installable, with documented limits. **Planned** means a defined direction without an implementation. **Under consideration** means a proposal whose scope and value still need evaluation. Only available modules belong in `suite.json` and installation packages.

| Phase | Module | Status | Prerequisites and relationship |
| --- | --- | --- | --- |
| 1 | [Italian PA Frontend](skills/italian-pa-frontend/SKILL.md) | **Available**, 1.0.0 | Existing or explicitly selected stack; optional browser tooling. |
| 2 | Italian PA Accessibility | **Planned** | Current official requirements, manual testing expertise and a reproducible audit corpus; complements Frontend. |
| 3 | Italian PA Identity | **Planned** | Protocol expertise, official versioned specifications and authorized identity test environments; security review required. |
| 4 | Italian PA Interoperability | **Planned** | Real API contracts and authorized PDND sandbox access where required; may use identity and security expertise. |
| 5 | Italian PA Security | **Planned** | Threat models, evidence-based rules and safe test fixtures; cross-cutting review for Identity and Interoperability. |
| 6 | Italian PA Architecture | **Planned** | Repository analysis and regression baselines; coordinates applicable frontend, security and API work. |
| 7 | Italian PA Quality | **Under consideration** | Define added value beyond existing project tests and the frontend browser module. |
| 8 | Italian PA Documentation | **Under consideration** | Establish source ownership, traceability and maintainable document workflows. |
| 9 | Italian PA Privacy | **Under consideration** | Specialist privacy review, data inventories and clearly bounded technical assistance. |

These are knowledge and validation prerequisites, not mandatory dependencies on unreleased modules. Every future skill must remain independently installable. Where collaboration is useful, reference shared evidence or documented interfaces; never assume another skill is installed.

## Phase 1 — Design and interfaces / Design e interfacce

**Italian PA Frontend — Available.** Generate, audit and improve frontend interfaces using design system .italia, official kit references, accessible component contracts, administrative forms and wizards, dashboards and responsive tables. Preserve the user's technology choice, reuse project components and distinguish backend capabilities from UI behavior. Static validators and optional browser checks have different evidence levels. The [module roadmap](skills/italian-pa-frontend/ROADMAP.md) preserves its earlier milestones and outstanding runtime work.

## Phase 2 — Accessibility and inclusion / Accessibilità e inclusione

**Italian PA Accessibility — Planned.** WCAG 2.2 and requirements applicable to the actual service; interface accessibility, keyboard navigation, focus, screen readers and accessible forms. Review accessibility statements, combine automatic and manual checks, and produce scoped audit reports with evidence and unresolved findings. Verify normative sources when used. No automatic conformity certification. First acceptance gate: reproducible audits, reviewed manual procedures and clear coverage limits.

## Phase 3 — Digital identity / Identità digitale

**Italian PA Identity — Planned.** Future support for integrazione SPID CIE, OpenID Connect and SAML where pertinent, sessions, authentication and authorization, secure tokens, expiry and logout. Implementations must use the official specifications and versions actually deployed. Prerequisites include authorized test providers, synthetic identities and security review; no fabricated production integrations or bundled credentials.

## Phase 4 — Interoperability and APIs / Interoperabilità e API

**Italian PA Interoperability — Planned.** REST, OpenAPI, interoperabilità PDND and e-services, error handling, transport security, API versioning, contract validation, integration, traceability and observability. Public sector interoperability needs real contracts and documented authorization boundaries. First validate against local contract fixtures; test platform integration only in authorized environments with relevant official specifications.

## Phase 5 — Application security / Sicurezza applicativa

**Italian PA Security — Planned.** Secure coding, OWASP references, secret handling, data protection, input validation, permissions, safe logging, dependency vulnerabilities, security reviews and threat modeling. Findings must separate confirmed issues from hypotheses, with reproducible safe checks. No unverified regulatory compliance claims. This area may be developed alongside Identity and Interoperability despite its phase number.

## Phase 6 — Architecture and modernization / Architetture e modernizzazione

**Italian PA Architecture — Planned.** Legacy analysis, reverse engineering, modular architectures, refactoring, technology migrations, regression testing, architecture documentation, ADRs and gradual migration strategies. Agent skills for government software must first map existing behavior and operational constraints before guiding modernization. Acceptance requires a migration example with preserved contracts and a rollback strategy.

## Phase 7 — Quality and testing / Qualità e testing

**Italian PA Quality — Under consideration.** Unit, integration, end-to-end, contract and performance tests; static analysis, CI/CD, quality gates and regression checks. Evaluate whether a standalone skill adds reusable decision support beyond framework tooling and the available frontend browser tests.

## Phase 8 — Documentation and processes / Documentazione e processi

**Italian PA Documentation — Under consideration.** Technical and functional specifications, OpenAPI documentation, operational manuals, architecture diagrams, requirement traceability, decision templates and migration documentation. Evaluate source synchronization and review ownership before adding generators.

## Phase 9 — Data protection and privacy / Protezione dati e privacy

**Italian PA Privacy — Under consideration.** Privacy by design, minimization, retention, pseudonymization, personal data handling and technical support for privacy assessment documentation. This module must not replace legal professionals, DPOs or controllers/processors responsible for their decisions. Scope and acceptance require specialist review; no automatic legal conclusions.

## How a planned module becomes available

Propose a focused use case in a GitHub Issue using the skill proposal template. Discussions may be enabled by maintainers after publication. Agree on scope and official sources, implement a self-contained package, supply meaningful tests and limitations, document licensing and independent versioning, and pass maintainer review. See the [acceptance criteria](docs/contributing-skills.md). Future names are descriptive proposals until implementation is accepted; no empty skill directories are created.
