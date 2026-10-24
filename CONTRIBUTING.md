# Contributing to Skills Italia

Contributions in English or Italian are welcome. Start with a concrete user problem, preserve existing project behavior and support technical claims with official, version-specific sources. This is an independent project; do not imply institutional endorsement.

## Propose or report

Use repository Issues after publication: bug report, improvement or new skill proposal. For a new module, read the [skill contribution guide](docs/contributing-skills.md) before implementation. Discussions are an optional community channel to enable after publication. A roadmap entry is not an accepted implementation commitment.

For vulnerabilities, follow [SECURITY.md](SECURITY.md) rather than posting exploit details publicly. Our [Code of Conduct](CODE_OF_CONDUCT.md) applies to project spaces.

## Development workflow

1. Work on a focused branch. Identify whether the change belongs to suite infrastructure or a specific skill.
2. Preserve the user's stack and working features. Keep specialist instructions and dependencies inside the relevant module.
3. Update affected documentation, examples and the appropriate changelog. Italian is the primary language of the [root README](README.md) and GitHub description. Keep the complete [English overview](docs/README.en.md) and the retained [Italian documentation entry point](docs/README.it.md) aligned with the root README when user-visible behavior changes.
4. Run `python scripts/release_check.py` with Python 3.10+ and Node.js 22.12+. This includes installation and packaging tests in temporary directories. No application or remote credentials are required.
5. For browser-harness changes, install locked browser dependencies and run its Node validation. Application E2E tests require a configured authorized target; document target, viewport and actual results. See [verification](docs/verification.md).
6. Submit a pull request using the template. Explain the problem, resulting behavior, sources/versions, meaningful checks run, and any checks not performed.

The core uses Python's standard library. Avoid adding dependencies unless they solve a demonstrated problem. Do not run remote shell installers. Do not commit reports, local browser configuration, sessions, secrets, personal data or generated caches.

## Review criteria

Reviewers assess usefulness, focused scope, correct sources, technology neutrality, safe behavior, independent installation, backward compatibility and reproducible evidence. Tests should exercise behavior and failure boundaries rather than merely repeat wording. Missing browser/manual checks must be disclosed; passing structural checks alone is not proof of service quality or legal compliance.

## Versions and licensing

Suite version is in `suite.json`; skill versions are independent. Preserve the frontend 1.0.0 history and all existing published tags. Use semantic versions for changes after release, with module changes documented in the module changelog. See [architecture](docs/architecture.md).

By submitting a contribution, you agree to license it under the repository's MIT license unless a separately identified compatible license is agreed during review. Preserve existing copyright notices; cite external material instead of copying manuals. Maintainers approve release tags and publication separately.
