# Contributing a new independent skill

[Contribution policy](../CONTRIBUTING.md) · [Roadmap](../ROADMAP.md) · [Architecture](architecture.md)

## 1. Propose before expanding the suite

Open a skill proposal Issue after publication, or discuss scope in Discussions if enabled. Describe the user problem, concrete requests the skill should handle, boundaries with available modules, official sources, verification strategy, maintenance ownership and license. A roadmap label alone does not authorize placeholder directories or mark a feature available.

## 2. Minimum package

A real module needs `skills/<name>/SKILL.md` and a license; add only resources its workflow uses. A non-trivial module should include focused references, realistic examples, independent version metadata and changelog, meaningful tests and documented environment requirements. Scripts, templates and browser tooling are optional. Each package must remain useful after extraction from this repository.

```text
skills/<name>/
├── SKILL.md
├── LICENSE
├── CHANGELOG.md          # module release history
├── references/          # only if needed
├── scripts/             # only if needed
└── tests/               # meaningful verification for provided tools
```

This is a template description, not a planned module implementation.

## 3. SKILL.md conventions

Follow the [Agent Skills specification](https://agentskills.io/specification): YAML frontmatter, required `name` matching the directory and a concise `description` saying what the skill does and when it applies. Use lowercase ASCII letters, digits and single hyphens, up to 64 characters. Keep descriptions under 1024 characters. Store `metadata.version` as a quoted semantic version string. Include the license and compatibility requirements where useful.

The suite's validator accepts the deliberately small metadata subset used here: single-line scalar `name`, `description`, `license`, `compatibility` and indented string metadata. It rejects unsupported forms instead of pretending to parse all YAML. Propose broader syntax with a real parser and tests if needed. Agent-specific fields need separately verified support and must not silently grant permissions.

Keep shared workflow and decision rules in `SKILL.md`, and route to detailed references only when relevant. Avoid a copy of the entire official manual. Preserve user intent, technology choice and normal approval boundaries. State exclusions where they prevent incorrect routing. Resolve helper paths from the installed skill root, never assume the application has the same `scripts/` directory.

## 4. References and sources

Organize references by actual task or domain. Link them from the entry point or another relevant reference. Prefer official, version-specific documentation; record source URL, purpose, checked date and uncertainty. Separate normative requirements, official technical documentation, official libraries and independent technical recommendations. Check applicability instead of inventing legal obligations. Do not imply official affiliation or copy copyrighted manuals into the package.

## 5. Scripts and dependencies

Use deterministic helpers only where they add reliability. Document arguments, output, side effects, exit codes, prerequisites and failure conditions. Prefer standard-library code and read-only defaults. Avoid uncontrolled remote execution, embedded secrets and production mutation. Optional dependencies belong to the module with a lockfile where supported. Exclude generated data from both installation and releases. Shared utilities must be packaged so extraction remains independent.

## 6. Verification

Test observable behavior and useful failure boundaries. Validate examples, JSON catalogs, source references and module-relative paths. Test installation, update, extraction and operation from a different working directory. For agent-specific features, record product/version and actual invocation results when tested; format compliance is not a substitute for runtime evidence.

Clearly separate structural/unit checks from application E2E, manual accessibility, security and legal assessment. Synthetic fixtures are useful but do not prove a real PA portal works. List checks not run and why. Never present automatic reports as conformity certificates.

## 7. Versioning

Each accepted module gets its own semantic version and changelog, independent of `suite.json`'s suite version. Keep `metadata.version` and the module's manifest entry consistent. Never repurpose an existing name for different behavior or rewrite published tags. See the [version policy](architecture.md).

## 8. Pull request and acceptance

Submit a focused PR linking the proposal. Include scope and examples, evidence for sources, test commands/results, compatibility limits, license/attribution, maintenance plan and updates to both README languages and roadmap status.

Acceptance requires:

- A useful implemented workflow with clear responsibility and no simulated integrations.
- Accurate discovery metadata and self-contained resources with working local links.
- Official references checked for relevance and a plan to recheck changing specifications.
- Safe, documented and reproducible scripts with meaningful checks where applicable.
- Independent installation and versioning, no secrets or generated reports in archives.
- Clear distinction between implemented, untested, planned and specialist-review work.
- Passing suite checks and maintainer review, including whether it overlaps an existing module.

Only then add the available module to `suite.json`, the installer inventory and both README tables. No hard dependency on an unreleased skill is allowed.
