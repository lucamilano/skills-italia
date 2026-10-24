# Discoverability, technical SEO and GitHub Pages

[Overview](../README.md) · [GitHub publication](publication.md) · [Sources](sources.md)

## Current release: repository documentation

The maintained public documentation is Markdown on GitHub. Italian is the primary language of the root README and GitHub About description, serving the developers building services for Italy's public administration. The complete English overview is maintained in `docs/README.en.md`; `docs/README.it.md` preserves the existing Italian documentation entry point. The overviews link to one another and to installation, architecture, contribution and roadmap documents. Descriptive headings, meaningful link text, explicit availability statuses and a concise repository description support discoverability without keyword repetition.

Keywords appear in relevant prose: frontend terms describe the available module; SPID/CIE, PDND, security, privacy and modernization proposals are confined to roadmap content. Do not add invisible keywords, repeated search phrases, empty module pages or claims of official affiliation. GitHub controls the HTML metadata of repository pages; raw README HTML is not a reliable way to inject canonical or Open Graph tags.

`docs/github-metadata.json` records the repository name, description, ten pertinent topics and an unset homepage. Description and topics are configured on [lucamilano/skills-italia](https://github.com/lucamilano/skills-italia). Topic limits are checked locally: at most 20, each up to 50 characters, lowercase letters, digits and hyphens. Topics describe technical scope, not institutional endorsement. No homepage, deployed site or canonical domain is invented.

The original [social preview](assets/social-preview.png) uses only the Skills Italia name, tagline and abstract shapes. Upload it manually through GitHub repository Settings → Social preview after authorization. It contains no institutional logos. GitHub recommends 1280 × 640 pixels, under 1 MB; the prepared PNG uses those dimensions. [GitHub social preview documentation](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/customizing-your-repositorys-social-media-preview).

## Pages decision

GitHub Pages is useful once there are enough modules or tutorials to justify dedicated navigation. It is deferred for the initial release: a generator would add dependencies and duplicate the current documentation before a real repository URL exists. There is no Pages deployment workflow, no generated website and no claim that web SEO tags have been deployed. A public repository can already expose and index its README and linked documents.

When a site is justified, choose a light static generator such as MkDocs and record the decision in an ADR. This proposal does not add a generator dependency. Confirm the actual GitHub Pages address or custom domain before setting a `site_url`, canonical URLs or homepage metadata. [GitHub Pages overview](https://docs.github.com/en/pages/getting-started-with-github-pages/what-is-github-pages).

## Future information architecture

Use paired `/en/` and `/it/` routes for maintained translations:

| Page | Purpose |
| --- | --- |
| Home | Project purpose, independence and immediate Available/Planned distinction. |
| Getting started | Local installation, trust, invocation and update procedures. |
| Available skills → Italian PA Frontend | The implemented module, capabilities, limits and examples. |
| Roadmap | One substantial status page for all future modules; split only when content warrants it. |
| Contributing | Proposals, acceptance, testing and versions. |
| About | License, sources, governance and non-affiliation. |

Do not create a separate empty page per proposed skill. Keep module pages derived from maintained sources, and validate links into source files after publishing.

## Required site checks before enabling indexing

- Give each page a unique meaningful title, visible heading and meta description in the page's language.
- Use readable, stable URLs. Confirm the origin and project path, then produce self-referencing canonical URLs; do not canonicalize all Italian pages to English.
- Emit a sitemap containing only real, indexable canonical pages and a `robots.txt` referencing the real sitemap. Keep previews out of indexing through deployment controls; robots rules are not authentication.
- Add reciprocal `hreflang="en"` and `hreflang="it"` only for complete equivalent translations, including self references. Use `x-default` only for a genuine language selector/default page.
- Set `lang`, accessible language navigation, descriptive link text, skip link, semantic landmarks and keyboard-visible focus. Test reflow, text zoom, contrast and navigation on narrow viewports.
- Set per-page Open Graph title, description, canonical URL and an absolute preview image URL on the actual host. Match any social-card metadata to page language.
- Run a strict site build, local links/anchors validation and actual browser checks at desktop/mobile sizes. Verify canonical, alternate-language, sitemap and redirect behavior on the deployed origin.
- Update repository homepage only after the site is reachable. Recheck source URLs, sitemap and language mappings after moves.

These are implementation acceptance criteria for a future site, not assertions about features present in the Markdown release.
