# Skills Italia

**AI Agent Skills for Italian Public Administration Development**

[Italiano — lingua principale](../README.md) · [Usage modes](#three-operating-modes-generate-audit-and-refactor) · [Installation](installation.md) · [Roadmap](../ROADMAP.md) · [Contributing](../CONTRIBUTING.md) · [MIT license](../LICENSE)

[![Suite checks](https://github.com/lucamilano/skills-italia/actions/workflows/checks.yml/badge.svg)](https://github.com/lucamilano/skills-italia/actions/workflows/checks.yml)

[GitHub repository](https://github.com/lucamilano/skills-italia) · [Report an issue](https://github.com/lucamilano/skills-italia/issues/new/choose) · [Discussions](https://github.com/lucamilano/skills-italia/discussions)

Skills Italia is an independent open-source suite of **AI agent skills** for developers building and maintaining Italian public sector software. It brings version-aware official references, implementation workflows and verification tools into an agent's development process.

Italian is the primary language of the repository overview and GitHub description. This complete English version is maintained for international contributors.

The suite starts with the **Italian public administration frontend**: accessible government websites, administrative forms, dashboards and existing applications. Its vision extends to security, identity, public sector interoperability and software modernization. Only the frontend skill is available today.

Suite **0.1.0** packages Italian PA Frontend **1.0.0**. These versions have separate lifecycles; see the [changelog](../CHANGELOG.md).

## Why Skills Italia?

Government services need usable interfaces, reliable integrations and technical decisions grounded in the actual project. Generic code generation can mix design-system versions, replace working components or invent backend capabilities. Skills Italia helps agents inspect the repository, reuse existing solutions, consult relevant sources and report what they actually verified.

These Italian public administration AI skills support implementation, analysis and maintenance. They do not certify legal compliance or replace specialist review.

## Three operating modes: Generate, Audit and Refactor

The first skill, **Italian PA Frontend**, provides three core operating modes. Name the mode in your initial prompt when starting a new PA portal or working on an existing application.

| Mode | When to use it | What it produces |
| --- | --- | --- |
| **Generate — Create** | Start from scratch or add pages, components or a new section to a project. | Interface structure, components, states and frontend code, with checks and a report. It can also produce only a UX specification when requested. |
| **Audit — Analyze** | Understand interface quality and issues before making changes. | A prioritized report with evidence, files/lines, impact and proposed fixes. It separates confirmed issues, potential issues and checks not performed; **it does not change code by default**. |
| **Refactor — Improve** | Correct or modernize the frontend while preserving service behavior. | Incremental changes and regression checks, preserving the existing stack, APIs, validation, authorization and business logic. |

**Generate can build a portal's frontend from an empty directory.** If no technology is selected and that choice is necessary to write code, the agent asks for it; for an existing project it detects the stack. The user's explicit choice always takes priority.

These modes cover the frontend available today. Backends, authentication, persistence and real integrations require verified contracts and services. Synthetic data and demonstration-only behavior in a prototype must be clearly identified.

See [examples for each mode](#usage-examples) below and the [expanded prompt collection](../skills/italian-pa-frontend/examples/prompts.md). These are modes of the same skill, not separately installed modules.

## Available Skills

| Skill | Version | Status | Scope |
| --- | --- | --- | --- |
| [Italian PA Frontend](../skills/italian-pa-frontend/SKILL.md) | 1.0.0 | **Available** | Generate, audit and refactor frontend interfaces with any selected or detected web stack. |

Italian PA Frontend includes:

- Design system .italia and Designers Italia workflows, Bootstrap Italia component references and version rules, with Dev Kit Italia and Design React Kit considered when appropriate to the actual project.
- Accessible components, administrative forms and wizards, responsive dashboards and tables.
- Stack detection, an indicative inventory of reusable patterns and a static HTML-like audit.
- JSON brief validators, implementation templates and realistic [usage examples](../skills/italian-pa-frontend/examples/prompts.md).
- Optional, separate Playwright and axe checks, screenshots and bounded iterative UI review.

The component catalog and version matrix are partial. Specification validators check structure, not a running application's behavior. See the [module documentation](../skills/italian-pa-frontend/README.md) and [verification limits](verification.md).

## Planned Skills

These are proposals for future modules, **not installable skills**. There are no placeholder implementations.

| Module | Status | Intended scope |
| --- | --- | --- |
| Italian PA Accessibility | **Planned** | WCAG 2.2, applicable requirements, keyboard, focus, screen readers and evidence-based audits. |
| Italian PA Identity | **Planned** | SPID, CIE, OpenID Connect, relevant SAML specifications and secure sessions. |
| Italian PA Interoperability | **Planned** | REST, OpenAPI, PDND, e-services, contracts and observability. |
| Italian PA Security | **Planned** | Secure coding, OWASP, secrets, authorization and threat modeling. |
| Italian PA Architecture | **Planned** | Legacy analysis, modular architecture, incremental modernization, migrations and ADRs. |
| Italian PA Quality | **Under consideration** | Unit, integration, end-to-end, contract and performance testing; CI/CD. |
| Italian PA Documentation | **Under consideration** | Technical specifications, operational guides, diagrams and requirement traceability. |
| Italian PA Privacy | **Under consideration** | Privacy by design, minimization, retention and technical support for privacy assessments. |

The [public roadmap](../ROADMAP.md) explains boundaries, prerequisites and acceptance gates. It assigns no speculative release dates. Propose modules through repository Issues or Discussions.

## AI agent compatibility

| Agent | Installation | Explicit use | Evidence |
| --- | --- | --- | --- |
| OpenAI Codex | `.agents/skills/` in a project or user home | `$italian-pa-frontend` | Format and paths checked against [official documentation](https://developers.openai.com/codex/skills/). |
| Claude Code | `.claude/skills/` in a project or user home | `/italian-pa-frontend` | Format and paths checked against [official documentation](https://code.claude.com/docs/en/skills). |
| Other Agent Skills agents | Follow the agent's documentation | Agent-specific | Not verified; check discovery, script access and permissions. |

Local installation and structural compatibility are tested separately from agent behavior. Interactive sessions with both agents have **not** been tested. This guide concerns local clients; cloud or managed environments may use different installation policies. The package follows the [Agent Skills format](https://agentskills.io/specification).

## Installation

Download or clone a reviewed copy of this repository, then run from its root with Python **3.10+**. Python helpers have no third-party dependencies. Node.js **22.12+** is needed only for Node checks and optional browser tooling. No installer downloads or executes remote scripts.

```console
git clone https://github.com/lucamilano/skills-italia.git
cd skills-italia
```

Install one skill into an existing target project:

```console
python scripts/install.py --skill italian-pa-frontend --agent codex --scope project --project-path /path/to/project
```

Install all available skills for both agents at user scope (currently the same single skill):

```console
python scripts/install.py --all --agent both --scope user
```

Use `--agent claude` for Claude Code, `--dry-run` to inspect destinations and `--force` to replace a changed installation after making a backup. Identical installs are a no-op. PowerShell and Bash entry points are provided for Windows, Linux and macOS. [Full installation, update and removal guide](installation.md).

## Quick start

1. Install the skill into your target project or user directory.
2. Start a new local agent session in the target project and verify that the skill is listed.
3. Invoke it with a bounded request and inspect its changes and reported evidence.

Codex example:

```text
Use $italian-pa-frontend in Generate mode to create a PA portal's
frontend from scratch. First clarify the purpose, pages and technology
with me; then propose the structure and implement it using design
system .italia, performing the checks available in the environment.
```

Claude Code example:

```text
/italian-pa-frontend In Audit mode, analyze the dashboard without changing files.
Check keyboard navigation, table filters and error states.
Report evidence and distinguish confirmed issues from checks not performed.
```

## Usage examples

These examples use Codex syntax, `$italian-pa-frontend`. In Claude Code, start with `/italian-pa-frontend` followed by the same request, or refer to the skill by name.

### Generate — A portal from scratch

```text
Use $italian-pa-frontend in Generate mode to create the frontend
of a municipal portal: homepage, searchable service catalog,
service details and a multi-step request form.
This is a new project: ask for my technology choice before coding.
Define pages, components, states and errors, then implement and verify.
If real APIs are missing, use clearly labeled synthetic demo data.
```

### Generate — A new section in an existing project

```text
Use $italian-pa-frontend in Generate mode to add a public-notice
management section with filters, a table and a detail page.
Detect the repository's stack and reuse available components.
Connect only confirmed APIs and document missing integrations.
Handle loading, empty results, errors and mobile layouts.
```

### Audit — Analyze a portal without changing it

```text
Use $italian-pa-frontend in Audit mode on the existing portal.
Do not change files. Review navigation, components, responsive behavior,
accessibility and consistency with the installed design-system version.
Report priorities, file/line evidence and proposed corrections.
Distinguish confirmed issues, potential issues and checks not performed.
```

### Audit — Review a form or wizard

```text
Use $italian-pa-frontend in Audit mode on the application wizard.
Check labels, errors, focus, forward/back navigation, data preservation
and the distinction between drafts, uploads and final submission.
Do not apply fixes. Report evidence, impact and missing checks;
do not infer backend capabilities from the interface alone.
```

### Refactor — Improve a form while preserving the service

```text
Use $italian-pa-frontend in Refactor mode on the application form.
Detect and retain the stack. Preserve endpoints, server validation,
authorization and CSRF protections. Reuse existing components.
Improve labels, the error summary, focus and responsive behavior.
Make incremental changes and check for regressions.
```

### Refactor — Make a table usable on mobile

```text
Use $italian-pa-frontend in Refactor mode on the case list.
The project uses Java/Thymeleaf: retain that stack and backend contracts.
Improve filters, sorting, pagination and mobile access to actions
without losing columns, functionality or authorization checks.
Test keyboard access, empty/error states and document checks not run.
```

For specifications without code, focused audits and refactoring with iterative browser review, see the skill's [additional examples](../skills/italian-pa-frontend/examples/prompts.md).

For Bootstrap Italia AI assistance, ask the agent to identify the installed library version before consulting component examples. Designers Italia Codex workflows and Bootstrap Italia Claude Code workflows use the same independent skill; neither integration is an official endorsement.

## Technology choice

The user's explicit technology choice takes priority. Otherwise the agent inspects the existing stack and preserves its framework, versions and conventions. Any plausible web stack can be specified; React, Razor and HTML examples are optional references. New projects require clarification only when choosing a technology is necessary to proceed. A UX audit or specification can proceed without a framework.

## Modular architecture

```text
skills-italia/
├── README.md, LICENSE, CONTRIBUTING.md, SECURITY.md
├── suite.json, CHANGELOG.md, ROADMAP.md, RELEASE_NOTES.md
├── docs/                 # bilingual overview, installation, governance, release guide
├── skills/
│   └── italian-pa-frontend/
│       ├── SKILL.md, LICENSE, README.md, CHANGELOG.md, ROADMAP.md
│       ├── references/, catalog/, templates/, examples/
│       ├── scripts/, tests/
│       └── browser-tests/
├── scripts/              # suite installation, validation and release packaging
├── tests/                # suite and installation regression tests
└── .github/              # CI, dependency updates and contribution templates
```

Each available skill is self-contained, independently installable and versioned. Suite governance does not replace specialist module rules. [Architecture and version policy](architecture.md).

## Accessibility and security

Automated checks find only some accessibility issues. Keyboard, focus, screen reader, zoom and visual reviews remain necessary, alongside verification of applicable requirements. A design kit, a clean axe result or a generated report does not certify WCAG or AGID compliance.

Reuse existing authorization, server validation, CSRF protections and escaping. Do not include secrets, personal data or real production sessions in examples, screenshots or reports. Browser checks require a configured, authorized target and default to localhost. [Security policy](../SECURITY.md).

## Roadmap

Skills Italia aims to support the software lifecycle beyond frontend development. See [Available, Planned and Under consideration modules](../ROADMAP.md), including the future identity, interoperability and modernization work. Contributions must demonstrate a useful workflow and credible verification before a module becomes available.

## Official sources

- [Designers Italia](https://designers.italia.it/) and the [design system .italia](https://designers.italia.it/design-system/): official design documentation.
- [Bootstrap Italia](https://github.com/italia/bootstrap-italia), [Dev Kit Italia](https://github.com/italia/dev-kit-italia) and [Design React Kit](https://github.com/italia/design-react-kit): official tools and libraries, to be checked against installed versions.
- [AgID](https://www.agid.gov.it/): verify current legal and technical requirements in the relevant official publications.
- [WCAG 2.2](https://www.w3.org/TR/WCAG22/): W3C technical recommendation; applicability to a service must be assessed separately.

Skills Italia supplies independent workflows and technical recommendations. It does not issue normative requirements. [Source verification register](sources.md).

## Contributing

Read [CONTRIBUTING.md](../CONTRIBUTING.md), the [new skill guide](contributing-skills.md) and our [Code of Conduct](../CODE_OF_CONDUCT.md). Contributions in Italian or English are welcome. Include official sources, reproducible evidence and honest test limits.

Run the repository's local release checks:

```console
python scripts/release_check.py
```

This command runs structural, documentation, Python, Node and installation checks. Browser E2E tests require an application and are separate. [Verification guide](verification.md).

## License

[MIT](../LICENSE). Existing Italian PA Frontend contributor attribution is retained. External documentation and libraries keep their own licenses and trademarks.

## Disclaimer

Skills Italia is an independent open-source project and is not officially affiliated with or endorsed by AGID, Designers Italia, or the Italian Government.

The skills support technical work and do not replace legal, security, accessibility or privacy professionals. There is no automatic compliance certification.
