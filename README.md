# Thyraen Robotics Website

Zola-based site for the Thyraen Robotics public landing page.

Fully custom templates and stylesheet — no theme, no CSS framework, no external
CDNs. Fonts (IBM Plex Sans/Mono) are self-hosted under `static/fonts/`.

## Layout

- `templates/base.html` — head/meta (incl. OpenGraph), nav, footer, inline nav JS
- `templates/index.html` — homepage: hero, capabilities, ecosystem diagram,
  tiered product grid, engagement section
- `templates/page.html` — product pages: compact hero, prose, related products,
  prev/next navigation
- `templates/section.html` — product listing at `/products/`
- `static/css/site.css` — the single stylesheet
- `navigation.toml` / `contact.toml` — nav items and contact data
- `tools/` — deterministic generators for the hero backgrounds and OG share
  card (see `tools/README.md`)

## Product content sync

Product pages in `content/products/` are synced from `Thyraen-Robotics/.github`
(`docs/products/*.md`) by `.github/workflows/sync-org-product-docs.yml`. The
workflow owns the product roster and per-product metadata (group, hero subtitle,
card text, epigraph, related products, ordering weight) and strips each doc's
leading H1 (the page template renders its own hero title). To add or change a
product: edit the doc in the org repo **and** the roster in that workflow.
