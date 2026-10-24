# Skills Italia release and GitHub publication guide

[Publication status](publication-status.md) · [Release notes](../RELEASE_NOTES.md) · [Verification](verification.md) · [SEO and Pages](seo.md)

## Prepared locally

The supplied folder was not a Git repository. There were no local branches, commits, remotes or tags to inspect or migrate. Initial local preparation created a fresh `main` branch without publishing. The owner subsequently authorized publication to [lucamilano/skills-italia](https://github.com/lucamilano/skills-italia); see [publication status](publication-status.md) for verified remote results. The standalone frontend history is retained as documentation. Do not rewrite published history if earlier standalone history is discovered later.

The original folder remains unchanged as a source copy because Windows prevented renaming an in-use directory. The deliverable is the sibling `skills-italia` directory. Do not publish the source copy as a second competing repository.

## Recheck and build

```console
git status --short
git branch --show-current
git remote -v
git tag --list
python scripts/release_check.py
python scripts/check_links.py --external
python scripts/package_release.py
```

`dist/` receives a suite ZIP, an independently installable frontend ZIP, `release-inventory.json` and `SHA256SUMS`. Those files are generated and ignored. Inspect the archive inventory and checksums before uploading; checksums do not authenticate the publisher. Link checks requiring network can fail because an upstream site is unavailable; inspect the actual URL and result, and never describe an inaccessible normative source as verified content.

Review the final diff and untracked files before staging. The initial publication uses the verified owner's GitHub `noreply` commit address. Future commits and publication require the maintainer's authorization. If a remote already contains history or tags, inspect and reconcile it first; do not force push or recreate published tags.

## Checklist for subsequent releases

- Verify that the intended repository is `lucamilano/skills-italia` and inspect its branch/tag history before updating it.
- Check private vulnerability reporting and the GitHub-only conduct reporting channels selected by the owner. Do not publish personal contact details without explicit consent.
- Inspect repository files and artifacts for private information. The local narrow secret-pattern scan does not replace owner review or a dedicated scanner.
- Review checks executed locally and checks pending on Linux/macOS CI and in interactive agent sessions. Real PA application E2E and manual accessibility testing remain project-specific.
- Set the release date when publication occurs. Keep suite 0.1.0 distinct from the included frontend skill 1.0.0 and its historical notes.

## GitHub metadata commands (alternative maintenance method)

The initial repository settings were configured through GitHub's REST API using the owner's existing Git authentication. GitHub CLI was not installed. These equivalent CLI commands are documented for later authorized maintenance; they were not used during the initial setup:

```console
gh repo edit lucamilano/skills-italia --description "Skill open source per agenti AI dedicate allo sviluppo di software e servizi digitali della Pubblica Amministrazione italiana. Primo modulo disponibile: frontend accessibili con il design system .italia."
gh repo edit lucamilano/skills-italia --add-topic agent-skills,claude-code,openai-codex,public-administration,italian-public-administration,design-italia,bootstrap-italia,designers-italia,accessibility,open-source
gh repo edit lucamilano/skills-italia --enable-issues --enable-discussions
```

See [GitHub CLI repository editing](https://cli.github.com/manual/gh_repo_edit) and [GitHub topics](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/classifying-your-repository-with-topics). Keep the About description in Italian and aligned with the available modules; future security/interoperability modules remain explicitly planned in the roadmap. Leave homepage unset until there is a real reachable documentation website. Upload `docs/assets/social-preview.png` through repository Settings → Social preview; standard `gh repo edit` does not set that image.

Enable secret scanning/push protection and dependency alerts where available; confirm Actions permissions and branch protection for `main`. Require the suite CI checks after their first successful remote run. Enable private vulnerability reporting through repository Security settings. Optionally enable Discussions for module proposals; Issues work without it.

## Publish an authorized release

Only after the reviewed commit is pushed and CI succeeds, create an unused suite tag `v0.1.0` on that exact commit through the owner's approved workflow. Do not retag any published frontend version. To prepare a **draft** release against an already pushed tag:

```console
gh release create v0.1.0 dist/skills-italia-0.1.0.zip dist/italian-pa-frontend-1.0.0.zip dist/release-inventory.json dist/SHA256SUMS --repo lucamilano/skills-italia --verify-tag --draft --title "Skills Italia — Initial Public Release" --notes-file RELEASE_NOTES.md
```

The command above is an alternative CLI procedure, not an automatically executed step. Review the draft, asset contents, reporting channels and CI results before publishing. The initial publication uses the REST API and is recorded in [publication status](publication-status.md). Publish a separate module release only when its independent lifecycle needs one.

## Optional future documentation site

Pages is deferred, with no hosted URL or deployment workflow. Follow [SEO acceptance criteria](seo.md) if later enabling it. Configure the actual owner, Pages source/origin, canonical URL and sitemap before setting a homepage or claiming web metadata is deployed.
