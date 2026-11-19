# Sorure event publication & reporting workflow

> For AI coding/operations agents. Read `/AGENTS.md` first.  
> Checked 2026-11-19. Live forms and Sheet headers may change.
> This is a workflow, not authentication or automatic cross-platform publication.

## A. Systems and overall rules

- Google Sheet (internal record): https://docs.google.com/spreadsheets/d/1qYdBHSv-x6_7TnlSnMh7CcI5cb6xwBgjdgWMxkobZdw/edit
- Public multilingual Hugo site: https://amirmojiry.github.io/sorure-iranian-ry/ ; repository `amirmojiry/sorure-iranian-ry`
- Vaasa event calendar: https://www.vaasa.fi/en/events/ → "Enter your event"
- Lähellä.fi: https://www.lahella.fi/en-GB/ ; user guide https://www.lahella.fi/en-GB/user-instructions
- Facebook: https://www.facebook.com/profile.php?id=100090246127295
- WhatsApp/Telegram: community groups; do not invent group IDs, invite links or permissions.

**Never duplicate:** identify the same event by name(s), occurrence date, venue and existing website slug/links. Look in both Sheet and `content/events/` first. Maintain one row and one trilingual set of files throughout its lifecycle. User's latest firsthand correction takes precedence over stale publicity; do not invent facts or event-specific links.

**Two distinct states:**
1. **Upcoming:** register planned event; create three-language website announcement; prepare Vaasa and Lähellä field packs + images; prepare short three-language Facebook and Persian WhatsApp/Telegram invitations. Publish directly *only* with authorised tool/session access, then verify; otherwise return ready-to-paste content.
2. **Completed:** obtain actual recap and authorised event photos; update the **same** Sheet row with observed results; create/update **the same** three-language website page as a retrospective with gallery. A Facebook recap can be prepared. Do not create new misleading upcoming Vaasa/Lähellä listings for a past event.

Record separately: `draft prepared`, `saved draft`, `submitted`, `approved/published`, `verified live`, `blocked`. Never say "published" merely because the agent drafted text or submitted a form. Clarify genuinely missing publication-critical facts (time/place) instead of guessing.

## B. Intake and canonical facts

Read or elicit: multilingual names, exact or approximate date, Helsinki-local start/end time, venue + full address, public audience/age/accessibility, whether free or ticketed, signup method/deadline, organiser, public contact, outline, image(s), image reuse rights, and existing Vaasa/Lähellä/Facebook/website URLs. For completion also obtain **what really happened**, actual duration, aggregate attendance (only if known), and photographs with permission to publish. Never substitute pre-event promises for observed results.

Use Europe/Helsinki with the correct daylight-saving offset at that date; use real calendar dates. A rough season date is only a **sort approximation** and must not be advertised as an exact event date.

## C. Google Sheet: upsert exactly one record

Workbook: `1qYdBHSv-x6_7TnlSnMh7CcI5cb6xwBgjdgWMxkobZdw`. Tab currently `برنامه های برگزارشده انجمن` (includes planned events despite its title). **Always inspect actual header names, data types, validation and candidate rows before writing**, since rows can be sorted and columns can move.

Snapshot of current columns (2026-11-19):

| Col | Header | Use |
| --- | --- | --- |
| A | نام برنامه | Name |
| B | Date | Numeric eight-digit `YYYYMMDD` sorting key, e.g. **number** `20261126` |
| C | تاریخ | Human-readable date; retain uncertainty |
| D | ساعت | Event time range |
| E | مدت (تخمینی) | Duration: preserve the live column's numeric/time formatting |
| F | مکان | Venue and full address |
| G | تعداد شرکت کننده | Real participant count and breakdown, **only after event** |
| H | participantns (approx) | Numeric participant aggregate when actually known; do not present a forecast as real attendance |
| I | مخاطب هدف | Audience |
| J | خلاصه | Description/recap |
| K | لینک ایونت واسا | Verified, event-specific Vaasa URL |
| L | لینک پست فیس بوک | Verified, event-specific Facebook permalink |
| M | برگزارکننده ها | Organisers |
| N | هماهنگ کننده | Coordinator |
| O | لینک ایونت در لهله | Verified, event-specific Lähellä URL |
| P | لینک در ایونت های اوستروبوتنیا | Verified event-specific link if one exists |
| Q | لینک سایت انجمن | The real website event page (normally FA) |
| R | وضعیت برگزاری | Planned / held / cancelled / postponed |
| S | ارجاع به پیام آرشیو | Evidence reference, if available |
| T | نکتهٔ اعتبارسنجی | Date approximations, conflicts, unverified data, pending channel publication |

Rules: search before appending. Write minimal necessary cells only. `Date` must be an **integer**, not text and not a Sheets date serial. Example: "summer 2024" → `20240601` (1 June = meteorological start); explain the approximation in C/T. If a more specific start is given, use it. For an upcoming event set R to `برنامه‌ریزی‌شده؛ هنوز برگزار نشده` and leave actual attendee numbers blank. Once held, set R to `برگزارشده` and record only actual/explicitly estimated numbers. Preserve duration cell type, formulas, styles, neighboring fields and existing verified URLs. Read back the exact changed cells. Do not write generic homepages in event-link fields or claim external publication before verifying a public event URL.

## D. Association website: English, Finnish and Persian

Hugo content files (one stable slug):
- `content/events/<slug>.en.md`
- `content/events/<slug>.fi.md`
- `content/events/<slug>.fa.md`

Use existing event pages as examples; keep metadata consistent. Important frontmatter fields: `title`, `description`, `slug`, `date`, `publishDate`, `lastmod`, `event_date`, `event_date_label`, `date_precision`, `event_year`, `event_type`, `eventcategories`, `eventtags`, `symbol`, `venue`, `cover_image`, `event_gallery` and verified external-specific `facebook`, `vaasa`, `lahella`, `osterbotten`. Begin the article with `{{< event-meta >}}`.

Use exactly one category ID and ≥1 tag ID defined in `data/content_taxonomy.yaml`. Category/tags/year and slug must match in all three language files; localize titles, intro, event-date labels, image alt text and descriptions. Do not fabricate translated street names or other facts.

**Upcoming:** a genuine *future-tense announcement*, never a purported recap. Include confirmed date, time, venue, admission and registration; poster/illustration rather than fake historical event photos. `hugo.toml` currently has `buildFuture = false`: do not use a future `date` or `publishDate` value that hides the article. A nonfuture **publication** timestamp can be used as Hugo `date` with the **real scheduled occurrence** in `event_date`/`event_date_label` and `event_year`; test rendering. The existing archive groups by Hugo date year; if a next-year upcoming event appears in the wrong year, adapt the listing/grouping before delivery. Make its upcoming status visible to readers.

**Completed:** retain slug and original schedule; change tense to factual past, use true activities and actual outcomes, and include authorised real photographs. If no photos are supplied/usable, obtain them or mark the gallery as pending; never generate fictional event-documentary photographs. The repository is **public**: do not commit raw attendance data, internal messages, participant names/private contact details, financial records or identifiable minors without appropriate consent. Only publicly approved aggregate facts may appear.

Photos: `static/img/events/<slug>-01.webp`, `-02.webp` (or actual supported extensions). Use a real `cover_image` and `event_gallery` with localized `alt`. Optimize size, preserve image fidelity and image rights. The site automatically renders photo cards/gallery via `layouts/events/`.

Check `python3 scripts/validate_content.py`, Hugo `hugo --gc --minify --cleanDestinationDir`, then `python3 scripts/verify_generated_site.py` when possible. Verify the `/en/events/<slug>/`, `/fi/events/<slug>/`, `/fa/events/<slug>/` pages and actual GitHub Pages deployment. A commit is not proof that the new page is live.

## E. Vaasa event calendar: upcoming event input pack

User-supplied **English** form fields:
- **Name:** clear English event name.
- **Short description:** English, **≤120 characters, including spaces**; count before sending and check the live counter.
- **Description:** **plain English text only**: no Markdown/HTML, `**`, bullets or other formatting codes. Use short paragraphs, then date/time/venue as bare stand-alone lines **without the labels** `Date:`, `Time:`, or `Location:`.
- **Homepage:** direct English event page if already public; otherwise `https://amirmojiry.github.io/sorure-iranian-ry/en/`.
- **Image:** suitable promotional poster/illustration or authorised relevant photo; attach actual image if the tool supports uploading, otherwise provide the file/URL needed for manual submission.
- **Type:** select a listed actual option, matching the activity.

Visible **Vaasa Type** choices in supplied screenshot:
- Auctions & Market Days
- Conferences, Courses, Fairs & Seminars
- Literature
- Movies
- Museums & Folklore
- Music
- Recreation & Sports
- Seminarier, föreläsningar och möten
- Theatre
- Tours and cruises

Examples: informal discussion/meeting → `Seminarier, föreläsningar och möten` (the Swedish-labelled meetings option visible in the English UI); sports → `Recreation & Sports`; a market → `Auctions & Market Days`; a course/workshop → `Conferences, Courses, Fairs & Seminars`. Recheck live options if changed.

**Paste-ready Description example** (replace event facts; the Description itself has no field-name labels and no special formatting):

    Join us for a relaxed community gathering to meet new people, share ideas and hear about future activities.

    Everyone is welcome, including non-members. Light refreshments will be available.

    Thursday, 26 November 2026
    17:00–19:00
    Korsholmanpuistikko 44, Vaasa

Other live required fields (tickets, language, admission, address, accessibility, submitter/contact) should be filled only with confirmed data; never invent. On submitting, distinguish awaiting review from approved/live. Save **the real public event URL** in Sheet K and site `vaasa:` only after it exists.

## F. Lähellä.fi: upcoming event input pack

Official instructions: https://www.lahella.fi/en-GB/user-instructions . Log in to organisation's existing account, navigate **Activity Announcements** and select the appropriate main group. **Save** can mean draft; **Publish** is separate. Avoid creating another Sorure organisation.

- **English Name:** **≤60 characters**, including spaces; count.
- **Main announcement group** (official instructions): `Hobbies and Leisure` for ordinary social, cultural or leisure events; `Volunteering` for actual volunteer opportunities; `Support and Help` for services supporting everyday life.
- **Themes:** the user's supplied `<select multiple name="theme">` options below (multi-select where genuinely relevant).
- **Activity classification:** another, separate selector shown in the user's **second** screenshot; choose the best matching option from its current live list.
- Complete other required form fields truthfully: event description, date, time, address, city, admission/registration, organiser/contact and image when supported by the form. Select English content if supported; do not invent other length limits.

**Theme labels and exact option values** from supplied HTML:

| Label | Value |
| --- | --- |
| Digital, technology and games | `ht_digi_teknologia` |
| Wellbeing and lifestyle | `ht_hyvinvointi` |
| Internationality | `ht_kansainvalisyys` |
| Culture and art | `ht_kulttuuri` |
| Arts and crafts | `ht_kadentaidot` |
| Nature and animals | `ht_luonto` |
| National defense | `ht_maanpuolustus` |
| Fire and rescue operations | `ht_pelastustoiminta` |
| Sports and exercise | `ht_urheilu` |
| Religions, church missions, spirituality and worldviews | `ht_uskonnot` |
| Advocacy, democracy, human rights and political action | `ht_vaikuttaminen` |

**Activity classification options visible in second screenshot** (for hobby/leisure activities; not necessarily exhaustive):
- Presentations
- Hobbies and recreational activities
- Meeting place and living room activities
- Village and resident activities
- Camps, excursions and trips
- Exhibitions
- Staying, recreation and spending time
- Guides and publications
- Groups and clubs
- Events, activities and lectures

For an informal Iranian community get-together: main group **Hobbies and Leisure**; themes **Internationality** (optionally **Culture and art** only if appropriate); classification **Meeting place and living room activities** or **Village and resident activities**, depending on what the meeting is. For a one-off workshop **Events, activities and lectures**; for sports **Sports and exercise** as a theme. Do not select `Presentations` just because a screenshot shows it highlighted.

**These are three different classification controls**: main group, multi-select theme, activity classification. A future agent must verify the current form/options. After actually publishing, verify public result and save event-specific URL into Sheet O and website `lahella:`. Official instructions confirm `Save` and `Publish` are separate steps.

## G. Facebook, WhatsApp, Telegram

**Upcoming Facebook post:** include a **short trilingual** message in this order: Persian, English, Finnish, separated by exactly `===`. Keep it compact (editorial target about 900–1,200 total characters to avoid overly long previews; **not** a claimed Facebook technical limit). State a friendly reason to come plus time/place and a verified link. Default **no emoji**. Publish only with authorised access, capture the **specific** permalink in Sheet L and website `facebook:`. Do not substitute the association's general FB URL for a specific event.

**Upcoming WhatsApp/Telegram:** one concise **Persian**, friendly, copy-ready message for each (identical is fine), with title, date, start/end, location and a short invitation. Registration/RSVP only when needed; optional link to the event page. No emoji by default, no invented group link, no automatic posting unless the group/account connection is really available.

**Completed:** short trilingual Facebook recap can be prepared with `===` separators, factual activities and thanks, real approved photos. External past-event calendar announcements are **not** recreated. Preserve already published real links.

## H. Runbooks

### H1. Upcoming
1. Read input and live Sheet; find existing event by name/date/venue; resolve confirmed facts.
2. Upsert one planned Sheet row (B numeric sorting key; actual attendance empty).
3. Create/update English/Finnish/Persian public **announcement** (same slug), with promotional artwork if appropriate; confirm published pages. Only after event URL exists, link it in Sheet Q.
4. Prepare complete Vaasa English field pack (including ≤120-char short text, plain full description, exact Type, image), and Lähellä English pack (≤60-char name; main group + themes + category + other confirmed fields + image).
5. Prepare copy-ready short FB (FA/EN/FI + `===`) and WhatsApp/Telegram (Persian) texts.
6. If an authenticated supported tool allows it, submit and verify each external publication; otherwise deliver drafts for manual posting and mark not submitted. Backfill K/L/O and Hugo external links **only when real specific URLs are verified**.
7. Report per-system statuses and any missing details without inventing success.

### H2. Completed
1. Find **same** row and slug; collect real photo(s), facts, attendance and actual activities.
2. Update the record, G/H only with supported actual aggregate numbers, J with retrospective, R with held status; preserve known links.
3. Convert/add the three-language website recap in place; use actual approved gallery and alt text; keep stable slug and event date.
4. Optionally prepare a small Facebook thank-you/recap. Do not submit a new Vaasa/Lähellä "upcoming" event for something already past.
5. Verify build, deployed site, photos and updated Sheet; report statuses.

### H3. Cancelled/rescheduled
Update the same row and slug, correct existing announcement copies, and update **existing** Vaasa/Lähellä/Facebook entries when authorised. Warn about any notices needing manual correction; avoid creating duplicates.

## I. Final response and validation checklist

For **every channel** indicate one of: `updated + verified`, `live + verified`, `submitted, pending approval`, `draft ready to paste`, `blocked by login`, `not attempted`. Include **complete** external field packs and copies when not submitted, and genuine URLs when published.

Check: numeric Sheet Date and preserved cell types; correct planned/held status; no duplicates; accurate public facts; 3 site translations/categories/tags/slugs; future content actually visible and placed under right year; real licensed/consented images; Vaasa 120 chars + plain Description with no `Date:`/`Time:`/`Location:`; Lähellä 60-char title + all three selectors; no invented public URLs; no private info in repo; deployment succeeded.

**Sources:** repo README, Hugo templates and `scripts/validate_content.py`; official Lähellä user guide https://www.lahella.fi/en-GB/user-instructions ; Vaasa calendar https://www.vaasa.fi/en/events/ . Vaasa category labels and Lähellä option values are grounded in the user's screenshots/HTML received 2026-11-19.
