# Security policy

Skills Italia contains instructions and developer tools, not a hosted public service. Security issues can still affect installers, parsers, example code, dependency handling or agent instructions. Skills are trusted executable guidance: review them before installation and keep normal agent approval controls in place.

## Supported versions

Maintainers aim to review reports against the latest suite release and the latest distributed version of each available skill. The initial suite version is 0.1.0 and its available skill is Italian PA Frontend 1.0.0. There is no promised response-time SLA or automatic support for future roadmap modules.

## Report privately

Use [**Security → Report a vulnerability**](https://github.com/lucamilano/skills-italia/security/advisories/new) to report privately to the repository owner. Private vulnerability reporting is enabled on [lucamilano/skills-italia](https://github.com/lucamilano/skills-italia). Do not put exploit details, tokens, personal data or production session files in public Issues. If the repository's private reporting feature is unavailable, wait until it is restored rather than publishing sensitive details.

The owner has chosen GitHub-only reporting channels; no personal email address is published. Conduct and platform-abuse reports follow the separate [Code of Conduct](CODE_OF_CONDUCT.md), not Security Advisories.

Provide the affected module/version, environment, impact, minimal synthetic reproduction and any suggested mitigation. Do not test third-party or production systems without authorization. Maintainers should coordinate disclosure and fixes with the reporter; no arbitrary response or fix deadline is promised.

## Operational boundaries

- Install only from a reviewed local checkout or verified release archive. Installers copy local files, refuse unsafe path overlap and do not download dependencies or execute remote scripts.
- Identical installations are a no-op. `--force` replaces a changed selected skill; back up local customizations first. Application symlink/junction sources or destinations are rejected. Standard macOS `/var`, `/tmp` and `/etc` aliases are canonicalized only when they resolve to their expected `/private/` locations.
- Browser tooling is optional and separate from application dependencies. Localhost is the default target. A remote staging target requires explicit authorization and `PA_ALLOW_REMOTE=1`; that variable is not proof of permission.
- Keep browser storage state, credentials, personal data, screenshots of real users and production reports out of the repository and release archives. Ignore rules are not a complete secret scanner.
- Preserve authorization, CSRF controls, input validation and output encoding during frontend work. A hidden button does not enforce server permissions.
- Run dependency audits when dependencies change. Automated audits and the repository's narrow credential-pattern checks are incomplete and do not constitute a security assessment.

No generated report, skill or CI result is an assertion of regulatory compliance. See [verification limits](docs/verification.md).
