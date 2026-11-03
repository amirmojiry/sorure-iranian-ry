# Sorure Iranian ry — Public website

The public, three-language site of Sorure Iranian ry in Vaasa, Finland.

**Stack:** [Hugo](https://gohugo.io/) + [Blowfish](https://blowfish.page/) v3.9.0 (Hugo Modules), built as a static site and deployed on GitHub Pages. All event content is available in English (`en`), Finnish (`fi`) and Persian (`fa`, RTL).

## Local development

Install Hugo Extended and Go, then:

```bash
hugo mod download
hugo server --disableFastRender
```

To build:

```bash
hugo --gc --minify
```

The deployment workflow is in `.github/workflows/deploy.yml`. In **Settings → Pages**, choose **Build and deployment → Source: GitHub Actions**. The expected website URL is https://amirmojiry.github.io/sorure-iranian-ry/ (only after deployment has succeeded).

## Edit or add an event

Create **three matching Markdown files**:

- `content/events/your-event.en.md`
- `content/events/your-event.fi.md`
- `content/events/your-event.fa.md`

Use the same base filename and `slug` in all three languages. Required content fields: `title`, `description`, `date` (sorting reference only), `publishDate` (actual publication date), `event_date` (only an exact date if verified), `event_date_label`, `date_precision` (`exact`, `month`, `season`, `year`), `event_year`, `event_type`, `symbol`; optional: `venue`, `facebook`, `vaasa`, `lahella`, `osterbotten`. Begin the body with `{{< event-meta >}}` to show an honest date label and available public source links.

When only the season or year is known, use an approximate sort anchor (`date`), set `date_precision` to `season` or `year`, and describe it as approximate in `event_date_label`. Approximate dates are **never published as exact structured Event dates**.

## Privacy and publication policy

This is a **public GitHub repository**. Do not commit attendance counts, internal meeting notes, bank statements, budgets, volunteer contact details, private photos, unpublished evaluations, private WhatsApp material, or financial grant applications. Public event articles should describe the activity itself, not internal performance or financial details. Use only event photos with consent and appropriate usage rights.

The association's public contact email is `sorureiranianry@gmail.com`. The Facebook page is https://www.facebook.com/profile.php?id=100090246127295. External event links are optional and should refer to actual public pages.

The site does not use trackers, cookies or a contact form. Messages go through the visitor's email client.

## Design, localization and SEO

- Blowfish layout plus public-facing customized home, about and event link components
- Hugo multilingual site with Persian RTL and translated navigation
- XML sitemap, robots.txt, canonical and hreflang via Hugo/Blowfish
- RSS, Open Graph, and privacy-aware JSON-LD BlogPosting metadata
- Decorative SVG OG image: not a photograph of any real event

Website code © contributors. Blowfish is a separate, MIT-licensed theme. Event descriptions and third-party assets retain their respective rights.
