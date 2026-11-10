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

Keep the same slug and core facts. Required metadata: `title`, `description`, `date` (sorting anchor), `publishDate` (actual web publication date), `event_date` (exact dates only), `event_date_label`, `date_precision` (`exact`, `season`, `year`), `event_year`, `event_type`, `symbol`, exactly one `eventcategories` term and one or more `eventtags`. Optional public links: `facebook`, `vaasa`, `lahella`, `osterbotten`. Include the `{{< event-meta >}}` shortcode at the beginning of each event story.

When an exact event date is unknown, use a representative date only for sorting, mark `date_precision` as approximate and show a clearly approximate `event_date_label`. Approximate dates are not exposed as exact Event dates in structured data.

## Public-content and privacy rules

**The repository is public.** Never commit budgets, bank details, attendance numbers, internal WhatsApp exports, board-only notes, participant names, private images, internal assessments of turnout or unpublished event plans. Event descriptions should only cover suitable public information.

Links should refer to the real public Facebook post or Vaasa/Lähellä/Ostrobothnia listing for the event. If an event has no Facebook post-specific source, omit the Facebook link from its event metadata. The association's general Facebook page is linked from the site's navigation/contact sections, not each event.

There are no trackers, cookies, login systems or contact forms. The public email is `sorureiranianry@gmail.com` (also listed by the City of Vaasa), and the Facebook profile is https://www.facebook.com/profile.php?id=100090246127295.

## SEO and maintenance

Hugo/Blowfish handles sitemaps, robots.txt, canonical and alternate-language (hreflang) links, Open Graph metadata and RSS. The site includes a decorative public SVG sharing image and its own privacy-conscious structured data. Event articles are published as stories about past events, not misleading announcements for future events.

Blowfish remains a separate, MIT-licensed theme; rights to third-party photographs, links and original cultural works remain with their creators.

## Persian typography

Persian-language pages (`/fa/`) use **Vazirmatn Variable** v33.003 (100–900). Hugo downloads the pinned WOFF2 asset at build time and serves it locally alongside the generated site, avoiding third-party font requests in visitors' browsers. English and Finnish typography is unchanged. The font is copyright the Vazirmatn Project Authors and licensed under SIL OFL 1.1; see `static/licenses/Vazirmatn-OFL.txt`.

## Activity classification and annual reporting

Event archive pages use **their own taxonomies**:

- `eventcategories`: exactly one **primary activity category** per event. This is the category used to count events on the About timeline, without counting any event twice.
- `eventtags`: zero or more **cross-cutting themes** describing purpose or audiences, such as community building, language learning, intercultural exchange, volunteering and wellbeing.
- Canonical slugs, display order and English/Finnish/Persian labels are in `data/content_taxonomy.yaml`. Keep slugs stable across all three translations of an event.
- Example: `eventcategories: ["sports-wellbeing"]` and `eventtags: ["physical-activity", "wellbeing", "community-building"]`.

The About page dynamically counts unique *published event entries* grouped by `event_year` and primary category within the current language. It does **not** count separate sessions within a recurring programme, attendees, volunteer hours, activities not yet on the website, impact or grant achievements. The history cards use language-neutral `year_key` for accurate counts even when the year is displayed using Persian numerals.

Blogs use **separate** `blogcategories` (one primary editorial category) and `blogtags`. Never use a shared `tags` or `categories` field across events and blog posts; they must remain independent collections and URL taxonomies. Example: `blogcategories: ["culture-literature"]` with `blogtags: ["persian-literature", "hafez"]`.

For future reports and Finnish grant applications, keep **internal, privacy-safe** evidence of the number of sessions, participants (aggregate only), volunteer hours, partners, target groups, expenditure and outcomes where appropriate. Do not equate website event counts with performance indicators or add participants' personal details to this public repository.

Run `python3 scripts/validate_content.py` when editing or adding event/blog content; the deploy workflow runs the same check before the Hugo build.

## Registered association information

Official association details shown on the About page in all three languages are maintained in `data/association.yaml`: Y-tunnus, registered language, legal form, start of activities and founding year. Unlike a relative statement such as "three years ago," founding years do not go stale as time passes.
