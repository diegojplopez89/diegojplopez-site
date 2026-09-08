# DiegoJPLopez.com — Search, Press, and Identity Architecture

Working branch: `seo-press-architecture`

## Objective

Build `diegojplopez.com` into the authoritative public home for Diego Javier Piña Lopez's professional identity while preserving source integrity and avoiding thin, duplicate, or copied content.

The site should help visitors and search engines understand the same entity consistently:

- Diego Javier Piña Lopez
- Diego Piña Lopez
- Diego Pina Lopez
- Humanitarian leadership
- Migration and asylum response
- Public health and research
- Nonprofit operations and systems
- Speaking, teaching, and public service

## Information architecture

### Tier 1 — identity hubs

- `/` — authoritative homepage and entity overview
- `/about.html` — full professional biography; primary `ProfilePage`
- `/press/` — independent press and media archive
- `/research/` — publications, academic work, and research records
- `/speaking/` — talks, training, panels, and presentations
- `/projects.html` — selected projects and systems
- `/contact.html` — contact and professional profiles

### Tier 2 — evidence pages

Each meaningful press appearance gets a distinct page under `/press/<slug>/`.

Every press evidence page should contain:
1. Publisher
2. Publication date
3. Accurate original headline or a clearly labeled summary title
4. 150–350 words of original summary/context
5. What Diego's role was at the time
6. Direct link to the original publisher
7. Topics/tags
8. Canonical URL
9. Internal links back to `/press/` and relevant research/project pages

Do not copy entire articles. Do not reuse publisher photography unless licensing or permission allows it.

### Tier 3 — authoritative external sources

Prefer links to:
- original news publishers
- universities
- peer-reviewed journals and DOI records
- government or event-organizer pages
- recognized nonprofit/board profiles
- verified professional profiles

The website should summarize and organize the public record rather than pretend to replace it.

## Technical SEO baseline

Every indexable page should have:
- unique `<title>`
- unique meta description
- self-referencing canonical URL
- one clear H1
- sensible heading hierarchy
- crawlable internal links
- descriptive image alt text
- mobile-responsive layout
- Open Graph metadata on high-priority pages

Site-wide:
- `robots.txt`
- `sitemap.xml`
- HTTPS
- one preferred hostname/domain
- no accidental staging pages indexed
- no duplicate versions of the same summary

## Structured data

### Homepage
Use `WebSite` + `Person` JSON-LD.

### About page
Use `ProfilePage` with `mainEntity: Person`.

The Person entity should use stable identity fields:
- canonical name: Diego Javier Piña Lopez
- relevant alternate spelling without diacritics
- official website
- accurate image
- `sameAs` links only to real profiles or authoritative identity pages

Do not add unsupported awards, employers, affiliations, or credentials merely to increase schema density.

### Press archive
Use `CollectionPage`.

Individual press-summary pages can remain ordinary `WebPage` content. Only use `Article` markup if the page is genuinely an original article authored and published on this site.

## Editorial standard for press summaries

The goal is credibility, not keyword volume.

Each entry should:
- distinguish facts reported by the publisher from Diego's own interpretation
- use original language
- link to the source
- note the historic role/title when relevant
- avoid exaggeration
- avoid presenting an external article as if Diego or this site authored it

Short quotations may be used when genuinely useful, but summaries should be predominantly original paraphrase.

## Publishing workflow

1. Find a relevant independent or authoritative source.
2. Verify that it actually refers to Diego.
3. Record publisher, author, original URL, publication date, and role/title used in the source.
4. Write a distinct summary page.
5. Link the page from `/press/`.
6. Add it to `sitemap.xml`.
7. Link it to one or two relevant internal pages.
8. Validate structured data where present.
9. After deployment, inspect the URL in Google Search Console and request indexing when appropriate.
10. Track impressions/queries and improve pages based on useful search demand, not keyword stuffing.

## Search-intent clusters

Primary identity:
- Diego Javier Piña Lopez
- Diego Piña Lopez
- Diego Pina Lopez

Professional:
- Diego Piña Lopez Casa Alitas
- Diego Piña Lopez migration
- Diego Piña Lopez humanitarian
- Diego Piña Lopez public health
- Diego Piña Lopez research
- Diego Piña Lopez asylum seekers

Evidence:
- Diego Piña Lopez NPR
- Diego Piña Lopez KJZZ
- Diego Piña Lopez AZPM
- Diego Piña Lopez Cronkite News
- Diego Pina Lopez publication

These are editorial planning concepts, not phrases to repeat unnaturally on every page.

## Content roadmap

### Phase 1 — foundation
- rebuild homepage metadata and navigation
- create Press, Research, and Speaking hubs
- create first set of source-backed press summaries
- add sitemap and robots file
- document architecture

### Phase 2 — identity consolidation
- rebuild About page as the canonical `ProfilePage`
- verify all current credentials, board roles, education, and professional history
- add authoritative `sameAs` links
- add a professional timeline

### Phase 3 — evidence expansion
- locate additional reputable press, interviews, video, podcasts, organizational profiles, awards, and event records
- create only pages with enough distinct source material to be genuinely useful
- cross-link related press, research, and project pages

### Phase 4 — measurement
- connect/verify Google Search Console
- submit sitemap
- monitor branded queries
- improve titles/descriptions based on real impressions
- fix coverage, canonical, and Core Web Vitals issues

## Guardrails

Avoid:
- copying full news stories
- mass-producing near-identical pages
- fake publication dates
- unattributed publisher text or images
- keyword stuffing
- fabricated awards, credentials, affiliations, or quotes
- doorway pages created solely to occupy search results

The long-term strategy is to make the official site the most organized, accurate, and well-sourced version of Diego's legitimate professional public record.
