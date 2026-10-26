# SEO & Local SEO Rules — Cliff Canfield Plumbing

Every page on the site is built with these rules. `build.py` enforces the ones marked **[checked]**
and will refuse to write a page that fails them.

## Goal
Rank for "[service] + [town]" searches across our 13 Western Connecticut towns and turn visitors
into calls and form leads.

## URL structure (clean URLs)
- Services: `/services/<service-name>/`
- Locations: `/service-area/<town-name>/`
- Projects: `/project/<project-name>/`
- Blog: `/blog/<post-name>/`
- Each page is a folder with an `index.html`. Links are relative, so the site works on any host.

## Titles & descriptions
- **[checked]** Title ≤ 65 characters; the main keyword **and** "New Milford" in the first 50 characters.
  Pattern: `New Milford <Service> | Cliff Canfield Plumbing` (the brand can be cut off by Google; the keyword can't).
- **[checked]** Meta description 120–155 characters and contains the main keyword. Mention a nearby town
  and a reason to click (licensed master plumber, free on-site quote).

## Headings & content
- **[checked]** Exactly one H1 containing the main keyword and "New Milford".
- **[checked]** Main keyword in the first 150 words and in at least one H2.
- **[checked]** Service pages: 1,000+ words of genuinely useful content.
- **[warned]** Secondary keywords (e.g. "tankless water heater") used naturally at least once — write for people, never stuff.
- Write about what the homeowner actually needs: signs, options, cost factors, process, why us.
- Only state business facts we can stand behind (license, response time, owner-operated, free quote).
  No invented prices, warranties, years in business or reviews.

## Local signals
- **[checked]** "New Milford" appears 4+ times in visible text.
- **[checked]** 8+ of our towns named in visible text. Every service page gets the generated
  **Service area** section listing all 13 towns; when a location page exists its chip links to it automatically.
- Mention local specifics where true and useful: well water, hard water, older CT homes, oil/gas boilers,
  cold winters and frozen pipes.

## Trust & conversion
- **[checked]** Every service page has an `#estimate` form and a click-to-call link.
- Use a **real** customer review only. Prefer a review that mentions the service and town.
- Show the license number (once available), real job photos and Cliff by name.

## Images
- **[checked]** Every image has a descriptive alt (8+ characters) — describe the actual job.
- **[warned]** Width and height set on every image (prevents layout shift).
- Use real job photos, ~1200px wide for heroes, compressed JPEG/WebP, descriptive file names.

## FAQ
- **[checked]** Exactly 5 service-specific questions: cost, scope, process/timing, repair vs replace, scheduling.
- Answers are generated into FAQPage structured data automatically. (Google no longer shows FAQ dropdowns
  for most businesses, but the content still helps match real questions.)

## Internal linking
- **[checked]** Exactly 3 related service cards per service page; no broken links or anchors.
- Services menu, footer and homepage cards update automatically as pages are built.
- Location, project and blog pages should link to the relevant service pages (and vice versa).

## Structured data (generated)
- `Service` + `Plumber` (name, phone, New Milford address locality, 13 towns served).
- `FAQPage` from the page's FAQs.
- Once `SITE_URL` is set in `build.py`: canonical tag, `og:url`, absolute `og:image`, `BreadcrumbList`,
  `sitemap.xml` and `robots.txt`.

## Launch checklist (outside the website)
1. Set `SITE_URL` (and `BUSINESS['license']`) in `build.py` and rebuild.
2. Google Business Profile as a service-area business covering all 13 towns; add each service with a link to its page.
3. Google Search Console: verify the domain and submit `sitemap.xml`.
4. Ask customers for **Google** reviews that mention the service and town.
5. Keep name, phone and service area identical on Google, Angi, BBB, Yelp, Facebook and the CT license lookup.
6. Connect the quote form to email/CRM so leads actually arrive.

## Adding or editing a service page
- Each service page is one content file: `site-tools/bodies/<service-name>.py` (hero, six content sections,
  estimate form options, review, FAQs, related services, final CTA). The layout comes from `service_template.py`,
  so every page stays identical in structure. (The water heater page uses its own `.html` body.)
- To edit wording, change the content file and run `python build.py` in `site-tools`. The SEO check runs first.
- Hero image: set `image=dict(src=..., alt=..., caption=..., w=..., h=...)` for a real job photo (portrait, ~960x1200),
  or `panel=dict(title=..., items=[...])` for the dark "common jobs" panel when no photo is available yet.
- Reviews: use a real customer review, ideally one that mentions this service. Mark shortened quotes with an ellipsis.
- Related services: exactly three, chosen because a customer for this service is likely to need them too.
