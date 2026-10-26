"""Renders a service page body from structured content (bodies/<slug>.py).

Pages that ship their own bodies/<slug>.html (e.g. water-heater-installation) are used as-is;
every other service page is described as data and rendered here, so all pages share one layout.
"""
from html import escape

# Line icons (24x24, stroke) shared by related-service cards and hero panels
ICONS = {
    'bathroom-remodels': '<path d="M4 21V6.5A2.5 2.5 0 0 1 6.5 4H11v2"/><path d="M7 9.5a4 3.5 0 0 1 8 0Z"/><path d="M8.6 12.6l-.5 1.6M11 12.6v2M13.4 12.6l.5 1.6M9.6 16.6l-.5 1.6M12.4 16.6l.5 1.6"/>',
    'water-filtration-treatment': '<path d="M12 3.2S6 9.6 6 14a6 6 0 0 0 12 0c0-4.4-6-10.8-6-10.8Z"/><path d="M8.6 13.5h6.8M9.4 16.5h5.2"/>',
    'gas-systems': '<path d="M12 21a6 6 0 0 0 6-6c0-4.5-3.5-6.5-4.5-11-1.8 1.6-2.6 3.8-2.4 6.2C10 9.5 9.3 8.6 9 7.5 7.2 9.3 6 11.8 6 15a6 6 0 0 0 6 6Z"/><path d="M12 21a2.6 2.6 0 0 1-2.6-2.6c0-1.8 1.4-2.8 2.6-4.4 1.2 1.6 2.6 2.6 2.6 4.4A2.6 2.6 0 0 1 12 21Z"/>',
    'well-systems-pressure-tanks': '<path d="M4.9 18.1a8.5 8.5 0 1 1 14.2 0"/><path d="M12 14.5l3-3"/><circle cx="12" cy="14.5" r="1.4"/><path d="M12 6v1.4M6.6 8.4l1 1M17.4 8.4l-1 1M4.6 13.6H6M19.4 13.6H18"/><path d="M8 20.5h8"/>',
    'fixture-installation-repair': '<path d="M3 7.5v6"/><path d="M3 9h11.5a4.5 4.5 0 0 1 4.5 4.5V15h-3.4v-1.2a1.3 1.3 0 0 0-1.3-1.3H3"/><path d="M9 9V6M6.5 6h5"/><path d="M17.3 21a1.5 1.5 0 0 1-1.5-1.5c0-.9 1.5-2.5 1.5-2.5s1.5 1.6 1.5 2.5a1.5 1.5 0 0 1-1.5 1.5Z"/>',
    'water-heater-installation': '<rect x="6.5" y="4.5" width="11" height="14.5" rx="2.2"/><path d="M10 4.5V2.5M14 4.5V2.5M8.5 21v-2M15.5 21v-2M6.5 8.5h11"/><path d="M12 16.5a1.7 1.7 0 0 1-1.7-1.7c0-1.1 1.7-2.8 1.7-2.8s1.7 1.7 1.7 2.8a1.7 1.7 0 0 1-1.7 1.7Z"/>',
    'leak-frozen-pipe-repair': '<path d="M2.5 7.5h8M2.5 12.5h8M13.5 7.5h8M13.5 12.5h8"/><rect x="10.5" y="5.5" width="3" height="9" rx=".8"/><path d="M12 22a1.7 1.7 0 0 1-1.7-1.7c0-1.1 1.7-2.9 1.7-2.9s1.7 1.8 1.7 2.9A1.7 1.7 0 0 1 12 22Z"/>',
    'plumbing-repairs': '<path d="M14.7 6.3a4 4 0 0 0-5.4 5.4L3.6 17.4a1.8 1.8 0 0 0 2.6 2.6l5.7-5.7a4 4 0 0 0 5.4-5.4l-2.5 2.5-2.4-.6-.6-2.4Z"/>',
    'toilet-repair-replacement': '<rect x="5" y="3" width="8" height="6.5" rx="1.2"/><path d="M3.5 10.5h16.5a6.5 6.5 0 0 1-6.5 6.5h-3.5a6.5 6.5 0 0 1-6.5-6.5Z"/><path d="M8.5 16.8 8 21h8l-.4-4.2"/>',
}


def icon(slug, cls='svc-icon'):
    return (f'<svg class="{cls}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" '
            f'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{ICONS[slug]}</svg>')


WHY_DEFAULT = [
    ('bi-patch-check', 'Licensed master plumber', 'Your work is done by a Connecticut licensed master plumber who knows the code and does the job right.'),
    ('bi-person-check', 'Owner-operated', 'You work directly with Cliff from the first call to the final walkthrough. No call centers, no hand-offs.'),
    ('bi-geo-alt', 'Local &amp; responsive', 'Based in New Milford and serving towns across Western Connecticut, with a typical response within 2&ndash;3 hours.'),
    ('bi-file-earmark-text', 'Clear quotes first', 'We come out, talk through your options and give you a written quote before any work begins.'),
]


def _block(b):
    t = b['type']
    if t == 'checklist':
        lis = '\n'.join(f'                <li><i class="bi bi-check2"></i>{i}</li>' for i in b['items'])
        return f'              <ul class="check-list">\n{lis}\n              </ul>'
    if t == 'cards':
        cls = 'info-grid cols-3' if b.get('cols', 3) == 3 else 'info-grid'
        cards = '\n'.join(f'                <div class="info-card"><h3>{h}</h3><p>{p}</p></div>' for h, p in b['items'])
        return f'              <div class="{cls}">\n{cards}\n              </div>'
    if t == 'options':
        cls = 'info-grid cols-3' if len(b['items']) == 3 else 'info-grid'
        out = []
        for tag, h, p, bullets in b['items']:
            ul = ''.join(f'<li>{x}</li>' for x in bullets)
            out.append(f'''                <div class="info-card">
                  <span class="info-tag">{tag}</span>
                  <h3>{h}</h3>
                  <p>{p}</p>
                  <ul>{ul}</ul>
                </div>''')
        return f'              <div class="{cls}">\n' + '\n'.join(out) + '\n              </div>'
    if t == 'consider':
        rows = '\n'.join(f'                <div><dt>{dt}</dt><dd>{dd}</dd></div>' for dt, dd in b['items'])
        return f'              <dl class="consider-list">\n{rows}\n              </dl>'
    if t == 'steps':
        lis = '\n'.join(f'                <li><h3>{h}</h3><p>{p}</p></li>' for h, p in b['items'])
        return f'              <ol class="svc-steps" style="--steps:{len(b["items"])}">\n{lis}\n              </ol>'
    if t == 'why':
        items = b.get('items') or WHY_DEFAULT
        out = '\n'.join(f'                <div class="why-item"><span class="icon-box"><i class="bi {ic}"></i></span><div><h3>{h}</h3><p>{p}</p></div></div>'
                        for ic, h, p in items)
        return f'              <div class="why-grid">\n{out}\n              </div>'
    raise ValueError(f'unknown block type {t}')


def _section(s):
    parts = [f'            <section id="{s["id"]}">',
             f'              <p class="eyebrow">{s["eyebrow"]}</p>',
             f'              <h2>{s["h2"]}</h2>']
    if s.get('intro'):
        parts.append(f'              <p class="section-intro">{s["intro"]}</p>')
    for p in s.get('paras', []):
        parts.append(f'              <p>{p}</p>')
    for b in s.get('blocks', []):
        parts.append(_block(b))
    if s.get('callout'):
        parts.append(f'              <div class="svc-callout">\n                <p>{s["callout"]}</p>\n              </div>')
    parts.append('            </section>')
    return '\n'.join(parts)


def _hero_media(mod):
    h = mod.HERO
    if h.get('image'):
        im = h['image']
        return f'''            <figure class="svc-hero-media">
              <!-- Swap for your best {escape(mod.SERVICE_NAME.lower())} photo (portrait works best). -->
              <img src="{{ROOT}}{im['src']}" alt="{im['alt']}" width="{im['w']}" height="{im['h']}">
              <figcaption>{im['caption']}</figcaption>
            </figure>'''
    p = h['panel']
    lis = '\n'.join(f'                <li><i class="bi bi-check2"></i>{x}</li>' for x in p['items'])
    return f'''            <!-- Add a real job photo here later: replace this panel with a <figure class="svc-hero-media">. -->
            <div class="svc-hero-panel">
              <span class="icon-box">{icon(mod.SLUG)}</span>
              <p class="svc-hero-panel-title">{p['title']}</p>
              <ul class="svc-hero-panel-list">
{lis}
              </ul>
              <div class="svc-hero-panel-call">
                <span>{p.get('call_text', 'Questions? Talk to a master plumber.')}</span>
                <a href="tel:{{TEL}}" class="btn btn-cream"><i class="bi bi-telephone me-2"></i>{{PHONE}}</a>
              </div>
            </div>'''


def _related(mod, services, svc_href_token):
    cards = []
    for slug, blurb in mod.RELATED:
        name = services[slug]['name'].replace('&', '&amp;')
        cards.append(f'''          <div class="col-md-6 col-lg-4">
            <article class="service-card">
              <span class="icon-box">{icon(slug)}</span>
              <h3>{name}</h3>
              <p>{blurb}</p>
              <a href="{{SVC:{slug}}}" class="link-more">Learn more <i class="bi bi-chevron-right"></i></a>
            </article>
          </div>''')
    return '\n'.join(cards)


def _options(opts):
    out = []
    for i, (value, label) in enumerate(opts):
        sel = ' selected' if i == 0 else ''
        out.append(f'                          <option value="{value}"{sel}>{label}</option>')
    return '\n'.join(out)


def render(mod, services):
    h, e, r, c = mod.HERO, mod.ESTIMATE, mod.REVIEW, mod.CTA
    sections = '\n\n'.join(_section(s) for s in mod.SECTIONS)
    long_q = ' class="long"' if len(r['quote']) > 260 else ''
    honeypot = ('<div class="hp-field" aria-hidden="true"><label>Leave this field empty<input type="text" '
                'name="company_website" tabindex="-1" autocomplete="off"></label></div>')
    return f'''  <main id="top" class="page-service">

    <!-- ============ SERVICE HERO ============ -->
    <section class="svc-hero">
      <div class="container-xxl px-3 px-lg-4">
{{BREADCRUMB}}
        <div class="row g-4 g-lg-5 align-items-center">
          <div class="col-lg-6 col-xl-7">
            <p class="eyebrow"><span class="dot"></span>{h['eyebrow']}</p>
            <h1 class="svc-title">{h['h1']}</h1>
            <p class="svc-lead">{h['lead']}</p>
            <div class="svc-hero-actions">
              <a href="#estimate" class="btn btn-brand">{h['cta']} <i class="bi bi-chevron-right ms-1"></i></a>
              <a href="tel:{{TEL}}" class="btn btn-outline-ink"><i class="bi bi-telephone me-2"></i>{{PHONE}}</a>
            </div>
            <ul class="svc-trust">
              <li><span class="star">★</span> 4.9 from 200+ reviews</li>
              <li><i class="bi bi-patch-check"></i> Licensed master plumber</li>
              <li><i class="bi bi-clock"></i> Response within 2&ndash;3 hours</li>
            </ul>
          </div>
          <div class="col-lg-6 col-xl-5">
{_hero_media(mod)}
          </div>
        </div>
      </div>
    </section>

    <!-- ============ MAIN CONTENT ============ -->
    <section class="section svc-content" id="details">
      <div class="container-xxl px-3 px-lg-4">
        <div class="row g-4 g-lg-5">
          <article class="col-12 svc-article svc-article-full">

{sections}

          </article>
        </div>
      </div>
    </section>

{{SERVICE_AREA}}
    <!-- ============ ESTIMATE + REVIEW ============ -->
    <section class="section pt-0" id="estimate">
      <div class="container-xxl px-3 px-lg-4">
        <div class="estimate-card">
          <div class="row g-0">
            <div class="col-lg-7">
              <div class="estimate-main">
                <p class="eyebrow">Free estimate</p>
                <h2 class="section-title">{e['heading']}</h2>
                <p class="lead-text">{e['lead']}</p>
                <ol class="next-steps">
                  <li><strong>Send your details</strong>Takes about a minute.</li>
                  <li><strong>We call you back</strong>Typically within 2&ndash;3 hours.</li>
                  <li><strong>Free on-site quote</strong>Written, no obligation.</li>
                </ol>

                <div id="quoteFormWrap">
                  <form id="quoteForm" class="estimate-form" action="{{ROOT}}send-lead.php" method="post" novalidate>
                    {honeypot}
                    <div class="row g-3">
                      <div class="col-md-6">
                        <label for="fullName" class="form-label">Full name</label>
                        <input type="text" class="form-control" id="fullName" name="fullName" placeholder="Jordan Reyes" autocomplete="name" required>
                        <div class="invalid-feedback">Please enter your name.</div>
                      </div>
                      <div class="col-md-6">
                        <label for="phone" class="form-label">Phone number</label>
                        <input type="tel" class="form-control" id="phone" name="phone" placeholder="(860) 555-0142" inputmode="tel" autocomplete="tel" pattern="\\(\\d{{3}}\\) \\d{{3}}-\\d{{4}}" required>
                        <div class="invalid-feedback">Enter a 10-digit phone number.</div>
                      </div>
                      <div class="col-md-6">
                        <label for="zip" class="form-label">Property ZIP code</label>
                        <input type="text" class="form-control" id="zip" name="zip" placeholder="06776" inputmode="numeric" maxlength="5" pattern="\\d{{5}}" autocomplete="postal-code" required>
                        <div class="invalid-feedback">Enter a 5-digit ZIP code.</div>
                      </div>
                      <div class="col-md-6">
                        <label for="projectType" class="form-label">Type of project</label>
                        <select class="form-select" id="projectType" name="projectType" required>
{_options(e['options'])}
                        </select>
                      </div>
                      <div class="col-12">
                        <div class="d-flex justify-content-between align-items-baseline">
                          <label for="projectDetails" class="form-label">{e['details_label']}</label>
                          <span class="char-count" id="detailsCount" aria-live="polite">0 / 1000</span>
                        </div>
                        <textarea class="form-control" id="projectDetails" name="projectDetails" rows="3" maxlength="1000" placeholder="{e['placeholder']}" required></textarea>
                        <div class="invalid-feedback">Please add a few details about the job.</div>
                      </div>
                      <input type="hidden" name="sourcePage" value="{mod.SERVICE_NAME.replace('&', '&amp;')}">
                    </div>
                    <div class="mt-4">
                      <button type="submit" class="btn btn-brand">Request my free quote <i class="bi bi-chevron-right ms-1"></i></button>
                      <p class="form-note">No spam · Free, no-obligation quote</p>
                    </div>
                  </form>
                </div>

                <div id="quoteSuccess" class="estimate-success d-none" role="status" aria-live="polite">
                  <div class="success-icon"><i class="bi bi-check-lg"></i></div>
                  <h3 class="quote-title">Thanks, <span id="successName">neighbor</span>!</h3>
                  <p class="lead-text mb-4">Your request is in. We&rsquo;ll give you a call shortly to schedule your visit.</p>
                  <button type="button" class="btn btn-outline-ink" id="resetQuote">Submit another request</button>
                </div>
              </div>
            </div>

            <div class="col-lg-5">
              <div class="estimate-review">
                <p class="eyebrow">From a customer</p>
                <span class="stars" aria-label="5 out of 5 stars">★★★★★</span>
                <blockquote{long_q}>&ldquo;{r['quote']}&rdquo;</blockquote>
                <div class="reviewer">
                  <span class="avatar">{r['initials']}</span>
                  <div><div class="name">{r['name']}</div><div class="place">{r['place']}</div></div>
                </div>
                <div class="review-spacer"></div>
                <ul class="estimate-facts">
                  <li><i class="bi bi-star-fill"></i> 4.9 average from 200+ reviews</li>
                  <li><i class="bi bi-patch-check"></i> Licensed master plumber</li>
                  <li><i class="bi bi-house-check"></i> Free, no-obligation on-site quote</li>
                </ul>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- ============ FAQ ============ -->
    <section class="section pt-0" id="faq">
      <div class="container-xxl px-3 px-lg-4">
        <div class="row g-4">
          <div class="col-lg-5 col-xl-4">
            <div class="faq-intro">
              <p class="eyebrow">{mod.FAQ_EYEBROW}</p>
              <h2 class="section-title">{mod.FAQ_HEADING}</h2>
              <p class="faq-note d-none d-md-block">Have a question we didn&rsquo;t cover? Call <a href="tel:{{TEL}}">{{PHONE}}</a> and talk to a master plumber.</p>
            </div>
          </div>
          <div class="col-lg-7 offset-xl-1">
            <div class="accordion faq-accordion" id="svcFaq">
{{FAQ_ITEMS}}
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- ============ RELATED SERVICES ============ -->
    <section class="section pt-0" id="related">
      <div class="container-xxl px-3 px-lg-4">
        <p class="eyebrow">Related services</p>
        <h2 class="section-title mb-4">{mod.RELATED_HEADING}</h2>
        <div class="row g-3 g-lg-4">
{_related(mod, services, None)}
        </div>
      </div>
    </section>

    <!-- ============ FINAL CTA ============ -->
    <section class="section pt-0" id="contact">
      <div class="container-xxl px-3 px-lg-4">
        <div class="cta-band">
          <div class="cta-copy">
            <h2>{c['h2']}</h2>
            <p>{c['p']}</p>
          </div>
          <div class="cta-actions">
            <a href="#estimate" class="btn btn-cream">{c.get('button', 'Get my free quote')} <i class="bi bi-chevron-right ms-1"></i></a>
            <a href="tel:{{TEL}}" class="btn btn-outline-cream"><i class="bi bi-telephone me-2"></i>{{PHONE}}</a>
          </div>
        </div>
      </div>
    </section>
  </main>
'''
