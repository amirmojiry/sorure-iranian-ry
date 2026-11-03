# Sorure Iranian ry — Public website

A public, multilingual Hugo / Blowfish website for Sorure Iranian ry in Vaasa, Finland.

**Languages:** English (`/en/`), Finnish (`/fi/`), Persian (`/fa/` with RTL).

**Public URL (after Pages is enabled):** https://amirmojiry.github.io/sorure-iranian-ry/

## Development

Install Hugo Extended 0.162+ and Go 1.24+, then:

```sh
hugo mod get github.com/nunocoracao/blowfish/v3@v3.9.0
hugo server
```

The theme is pinned to v3.9.0 via Hugo Modules in `go.mod` and `hugo.toml`. Deployments run with `.github/workflows/deploy.yml`.

To enable: GitHub repo **Settings → Pages → Build and deployment → GitHub Actions**. Check **Actions** for the result. The expected public URL is not confirmed until a deployment finishes successfully.

## Add an archived event

Each archived event has three corresponding files:

- `content/events/<slug>.en.md`
- `content/events/<slug>.fi.md`
- `content/events/<slug>.fa.md`

Keep the same slug and core facts. Required metadata: `title`, `description`, `date` (sorting anchor), `publishDate` (actual web publication date), `event_date` (exact dates only), `event_date_label`, `date_precision` (`exact`, `season`, `year`), `event_year`, `event_type` and `symbol`. Optional public links: `facebook`, `vaasa`, `lahella`, `osterbotten`. Include the `{{< event-meta >}}` shortcode at the beginning of each event story.

When an exact event date is unknown, use a representative date only for sorting, mark `date_precision` as approximate and show a clearly approximate `event_date_label`. Approximate dates are not exposed as exact Event dates in structured data.

## Public-content and privacy rules

**The repository is public.** Never commit budgets, bank details, attendance numbers, internal WhatsApp exports, board-only notes, participant names, private images, internal assessments of turnout or unpublished event plans. Event descriptions should only cover suitable public information.

Links should refer to the real public Facebook post or Vaasa/Lähellä/Ostrobothnia listing for the event. An event with no post-specific source can link to the association's public Facebook page instead; do not present the Facebook profile as an event proof.

There are no trackers, cookies, login systems or contact forms. The public email is `sorureiranianry@gmail.com` (also listed by the City of Vaasa), and the Facebook profile is https://www.facebook.com/profile.php?id=100090246127295.

## SEO and maintenance

Hugo/Blowfish handles sitemaps, robots.txt, canonical and alternate-language (hreflang) links, Open Graph metadata and RSS. The site includes a decorative public SVG sharing image and its own privacy-conscious structured data. Event articles are published as stories about past events, not misleading announcements for future events.

Blowfish remains a separate, MIT-licensed theme; rights to third-party photographs, links and original cultural works remain with their creators.
