# Official sources and verification register

[Overview](../README.md) · [Module source policy](../skills/italian-pa-frontend/references/official-sources.md)

Checked during local preparation on **2026-10-24**. Links are entry points, not synchronized copies. Availability does not establish that every statement in every historical module reference has been revalidated. Verify the installed version and current official source again when implementing.

| Resource | Type and relevance | Observed result |
| --- | --- | --- |
| [Designers Italia](https://designers.italia.it/) | Official design documentation and service design resources | Opened; relevant to Italian PA service design. |
| [Design system .italia](https://designers.italia.it/design-system/) | Official foundations and components | Opened; relevant to the frontend workflow. |
| [Bootstrap Italia](https://github.com/italia/bootstrap-italia) | Official library source and version history | Opened; choose examples matching the project's actual version. |
| [Dev Kit Italia](https://github.com/italia/dev-kit-italia) | Official toolkit implementing design system .italia | Opened; inspect maturity, APIs and version before adoption. |
| [Design React Kit](https://github.com/italia/design-react-kit) | Official React library | Opened; use only when compatible with the selected React project. |
| [Codex skills](https://developers.openai.com/codex/skills/) | Official local skill discovery documentation | Opened; redirects to ChatGPT Learn; project/user `.agents/skills` paths confirmed. |
| [Claude Code skills](https://code.claude.com/docs/en/skills) | Official local skill format, discovery and invocation | Opened; project/user `.claude/skills` paths confirmed. |
| [Agent Skills specification](https://agentskills.io/specification) | Open package format | Opened; name/description frontmatter and self-contained resources. |
| [WCAG 2.2](https://www.w3.org/TR/WCAG22/) | W3C technical recommendation | Opened; not treated as proof of all Italian legal requirements. |
| [AgID accessibility entry point](https://www.agid.gov.it/it/design-servizi/accessibilita) | Official authority entry point for applicable publications | Redirected to an AgID maintenance page during browsing; normative contents were not verified. |
| [GitHub topics](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/classifying-your-repository-with-topics) | Repository discoverability documentation | Opened; metadata remains prepared locally. |
| [GitHub social preview](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/customizing-your-repositorys-social-media-preview) | Repository preview configuration | Opened; PNG prepared for manual upload. |

## Evidence and precedence

Official documentation explains a technology; official libraries implement it. Neither is a compliance certificate for the service using it. The independent Skills Italia procedures translate source material into technical work and must identify recommendations as such. Normative claims require the applicable current primary legal/authority publication and an assessment of scope, not an inferred requirement from a component catalog.

The module retains its dated 2026-10-22 source snapshot and version matrix as historical information. This preparation does not assert those listed versions are the current latest releases. The skill now requires checking actual versions before new adoption. Planned SPID, CIE and PDND modules must establish their own verified official source inventory before implementation.

Run `python scripts/check_links.py --external` to produce a repeatable network availability report. HTTP success alone cannot detect a maintenance page, obsolete legal text or incorrect semantic interpretation; review content as well as status. See the actual local results in [release readiness](release-readiness.md).
