# Installing and updating Skills Italia

[Panoramica italiana](../README.md) · [English overview](README.en.md) · [Architecture](architecture.md)

## Requirements and trust

Use a reviewed local clone of [lucamilano/skills-italia](https://github.com/lucamilano/skills-italia), downloaded source archive or standalone skill archive. Python **3.10+** runs the installer and core helpers without external packages. On Windows, `py -3` may be used instead of `python`. Node.js 22.12+ is needed for Node checks; browser tests additionally require the locked npm dependencies and Chromium.

```console
git clone https://github.com/lucamilano/skills-italia.git
cd skills-italia
```

Inspect `SKILL.md`, scripts and references before installation. No install command fetches or executes remote scripts, changes agent settings, installs dependencies or publishes anything. The same commands work on Windows, Linux and macOS with their normal path syntax.

## Local agent paths

| Agent | Project scope | User scope |
| --- | --- | --- |
| OpenAI Codex | `<project>/.agents/skills/<skill-name>/` | `~/.agents/skills/<skill-name>/` |
| Claude Code | `<project>/.claude/skills/<skill-name>/` | `~/.claude/skills/<skill-name>/` |

Checked against [Codex local skills](https://developers.openai.com/codex/skills/) and [Claude Code skills](https://code.claude.com/docs/en/skills). Local user scope is not a cloud deployment. Managed agent policies may restrict discovery. Other agents require separate format, location and permission verification; no compatibility is assumed merely from a product name.

## One skill or all available skills

Run from the suite root. The target project must already exist; source paths are resolved from the installer location, independently of the shell's current directory.

```console
python scripts/install.py --skill italian-pa-frontend --agent codex --scope project --project-path /path/to/project --dry-run
python scripts/install.py --skill italian-pa-frontend --agent codex --scope project --project-path /path/to/project
python scripts/install.py --all --agent both --scope user
python scripts/install.py --skill italian-pa-frontend --agent claude --scope user
```

Repeat `--skill` to select multiple available modules when more exist. `--all` selects only the available manifest entries; it cannot install roadmap proposals. With neither selector, the installer selects all available skills. Defaults retain the original behavior: both agents, project scope, current directory as target project. Explicit options are recommended.

PowerShell supports the historical parameter style and adds suite selection:

```powershell
./scripts/install.ps1 -Skill italian-pa-frontend -Agent codex -Scope project -ProjectPath 'C:\work\my-project' -DryRun
./scripts/install.ps1 -All -Agent both -Scope user
```

Bash on Linux/macOS or Git Bash:

```bash
bash scripts/install.sh --skill italian-pa-frontend --agent claude --scope project --project-path '/path/with spaces/project'
```

PowerShell locates `python` (or `py -3`); Bash locates `python3` (or `python`). Both forward the exit status. Bash options are the Python options. Do not bypass an organization-wide execution policy to run the wrapper; use the reviewed Python entry point directly.

## Verify discovery and invoke

Confirm that the destination contains `SKILL.md`, `LICENSE`, references and scripts. Start a new agent session in the project and check that `italian-pa-frontend` is listed. In Codex use `$italian-pa-frontend`; in Claude Code use `/italian-pa-frontend`. A natural-language request naming the skill is also possible. If it is missing, check the actual destination, agent version, trust and managed policies; avoid duplicate user and project installations with the same name unless intentional.

The installer has no API integration with either agent. Filesystem verification is tested; interactive invocation and all cloud/managed variants have not been tested.

## Running skill helpers

Paths written inside a skill are relative to that **installed skill directory**, not the application repository. Use an absolute script path from your application directory, and pass the application path explicitly. For example, after a project Codex install:

```console
python /path/to/project/.agents/skills/italian-pa-frontend/scripts/detect_stack.py /path/to/project --json
```

When working on this suite's source, run module-local commands from `skills/italian-pa-frontend/`. Browser tests run from that module's `browser-tests/` directory. Do not copy the whole suite into an agent's single-skill folder.

## Updates and removal

An identical installation exits successfully without rewriting files. If the destination differs, installation fails before copying until you explicitly pass `--force`. First back up local customizations, then review the new version and run the same command with `--force`. Replacement removes obsolete files within the selected skill. Other installed skills are unaffected. Application symlinks/junctions in a source or target path, source/destination overlap and unknown names are rejected. Standard macOS `/var`, `/tmp` and `/etc` aliases are accepted only after verifying and resolving their expected `/private/` targets.

To remove a skill, delete only its exact directory under `.agents/skills/` or `.claude/skills/`, after checking the resolved path and backing up customizations. Restart the agent if its skill list remains cached. No settings or project source changes need to be reverted.

## Standalone distribution and manual copying

An extracted frontend archive has its own `scripts/install.py`, PowerShell and Bash wrappers, license, changelog and tests. Run the same options from its root; `--all` means that one extracted module. Alternatively copy the complete reviewed `skills/italian-pa-frontend/` folder into an agent location from the table, excluding generated dependencies, local configs and reports. Do not copy only `SKILL.md`.

## Optional browser dependencies

From `skills/italian-pa-frontend/browser-tests/`:

```console
npm ci
npx playwright install chromium
npm run validate
```

Then configure a real local target and selectors before `npm test` or `npm run review`. See the [browser guide](../skills/italian-pa-frontend/browser-tests/README.md). `npm ci` requires network or a populated cache; Chromium is a separate download. A successful dependency install is not an E2E pass.
