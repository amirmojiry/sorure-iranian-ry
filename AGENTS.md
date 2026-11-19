# Agent instructions — Sorure Iranian ry

This is the public, multilingual Hugo/Blowfish website for **Sorure Iranian ry**, Vaasa, Finland. It is also used alongside a private Google Sheets event register and third-party event calendars.

## Mandatory event workflow

Whenever a request says **add, announce, publish, update, document or recap an association event**, read [docs/EVENT_WORKFLOW.md](docs/EVENT_WORKFLOW.md) before acting. Follow its two distinct paths:

- **Upcoming event:** look up or create the existing event record in Google Sheets; create or update appropriately labelled announcements on the website in English, Finnish and Persian; prepare the Vaasa Events and Lähellä.fi forms, a concise trilingual Facebook post, and copy-ready Persian WhatsApp/Telegram notices; provide suitable real or generated *promotional* artwork when needed. Publish to external services only with actual authorised access and verify the outcome.
- **Completed event:** obtain the factual report and usable event photos; update the *same* Google Sheets record with actual attendance and outcomes; create or convert the corresponding three-language website event page to an accurate recap with the authorised photos. Prepare a short Facebook recap as appropriate; do not create fresh past-event announcements in the future-event calendars.

## Source of truth and safety

1. **Do not duplicate events.** Search the spreadsheet and `content/events/` first. Identify a record by event date, venue, name and stable website slug. Update existing records/pages when the event already exists.
2. **Read live Sheet headers.** The current workbook is linked in the workflow guide. Column positions, sorting and types may change. In particular, `Date` is an eight-digit *numeric* `YYYYMMDD` sort key, not a string or Google date serial.
3. **Never fabricate facts or links.** Distinguish confirmed details, provisional details, planned activities and actual results. Use approximate dates only when clearly labelled as such.
4. **Never claim publication without verification.** For any external platform requiring an account, use an authenticated supported tool if available; otherwise return ready-to-paste fields and report `prepared — not submitted`. Never mistake `saved` for `published` or `submitted` for `approved/live`.
5. **The GitHub repository is public.** Keep participant names/contact details, private correspondence, financial data, raw attendance spreadsheets, internal planning notes and identifiable children's photos out of public commits. Public summaries may contain only approved, non-sensitive facts. Preserve privacy and image permissions.
6. **Use trilingual, consistent website content** (`en`, `fi`, `fa`); exact existing taxonomy IDs from `data/content_taxonomy.yaml`; real event-specific links only; and `{{< event-meta >}}` on event pages.
7. **Differentiate announcements and reports.** Future activities must be described in the future tense and must not be presented as completed; past activities must be based on actual evidence, not earlier publicity promises. Keep the original slug when converting an announcement into a recap.
8. **Respect the user's editorial preference:** friendly, concise, inclusive language without unnecessary formalism. Default to no emojis in WhatsApp/Telegram/Facebook event copy unless asked. Facebook multilingual blocks use `===` as separators and must be short enough not to truncate.
9. **Check the build and delivery.** Run `python3 scripts/validate_content.py`, `hugo --gc --minify --cleanDestinationDir` and `python3 scripts/verify_generated_site.py` where supported, and check GitHub Actions deployment and published pages. Do not report a live URL as verified until it loads.

## Where things live

- Website: https://amirmojiry.github.io/sorure-iranian-ry/
- Event sources: `content/events/<slug>.en.md`, `<slug>.fi.md`, `<slug>.fa.md`
- Event images: `static/img/events/`
- Categories/tags: `data/content_taxonomy.yaml`
- Site build: `.github/workflows/deploy.yml`
- Detailed operations, platform classifications, field formats, templates, completion checklist: **[docs/EVENT_WORKFLOW.md](docs/EVENT_WORKFLOW.md)**

Follow the user's instructions when they specify a narrower scope (for example, "draft only" or "do not publish"). Do not perform unrelated edits.
