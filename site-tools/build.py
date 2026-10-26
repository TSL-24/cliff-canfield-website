"""Static page generator for the Cliff Canfield Plumbing website.

- Takes the header/footer straight from index.html so every page stays in sync.
- Wraps each page body (bodies/<slug>.html + bodies/<slug>.py) in the shared layout.
- Adds the SEO pieces every page needs (breadcrumbs, service-area section, structured data,
  and - once SITE_URL is set - canonical/OG URLs, BreadcrumbList, sitemap.xml and robots.txt).
- Runs an SEO check on every page and refuses to write pages that fail it.
See SEO-GUIDE.md for the rules.

Usage: python build.py            (builds ../website)
       python build.py <path-to-site>
       python build.py --force    (overwrite pages even if they were edited by hand)

Hand edits are protected: if a generated page was edited directly since the last build, it is
NOT overwritten. Copy the change into its template in bodies/ (or ask Claude to), then rebuild.
"""
import json, re, sys, os, hashlib, html as htmllib
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.dont_write_bytecode = True
from datetime import date
from urllib.parse import urljoin, urlparse

HERE = os.path.dirname(os.path.abspath(__file__))
# Default: the 'website' folder next to this 'site-tools' folder (Web/website)
FORCE = '--force' in sys.argv
ARGS = [a for a in sys.argv[1:] if not a.startswith('--')]
SITE = ARGS[0] if ARGS else os.path.join(os.path.dirname(HERE), 'website')
MANIFEST = os.path.join(HERE, '.build-manifest.json')  # fingerprints of what the build last wrote

# ---------------------------------------------------------------------------
# Business facts - the single source of truth for every page
# ---------------------------------------------------------------------------
SITE_URL = None          # e.g. 'https://www.cliffcanfieldplumbing.com' - set once the domain is known
BUSINESS = dict(
    name='Cliff Canfield Plumbing',
    phone_display='1 (860) 248-1218',
    phone_tel='+18602481218',
    phone_schema='+1-860-248-1218',
    city='New Milford', region='CT', country='US',
    license=None,        # e.g. 'P-1 #123456' - shown in schema once filled in
)
TOWNS = ['New Milford', 'Brookfield', 'Danbury', 'Newtown', 'Bethel', 'Redding', 'Ridgefield',
         'Easton', 'Wilton', 'Weston', 'Westport', 'Southbury', 'Roxbury']


def slugify(s):
    return re.sub(r'[^a-z0-9]+', '-', s.lower().replace('&', 'and')).strip('-')


# group: 'large' = larger projects, 'service' = repairs & everyday service
SERVICES = [
    dict(slug='bathroom-remodels', name='Bathroom Remodels', group='large'),
    dict(slug='water-heater-installation', name='Water Heater Installation', group='large'),
    dict(slug='water-filtration-treatment', name='Water Filtration & Treatment', group='large'),
    dict(slug='well-systems-pressure-tanks', name='Well Systems & Pressure Tanks', group='large'),
    dict(slug='gas-systems', name='Gas Systems', group='large'),
    dict(slug='plumbing-repairs', name='Plumbing Repairs', group='service'),
    dict(slug='fixture-installation-repair', name='Fixture Installation & Repair', group='service'),
    dict(slug='leak-frozen-pipe-repair', name='Leaks & Frozen Pipes', group='service'),
    dict(slug='toilet-repair-replacement', name='Toilet Repair & Replacement', group='service'),
]
BY_SLUG = {s['slug']: s for s in SERVICES}
GROUP_LABEL = {'large': 'Larger projects', 'service': 'Repairs &amp; everyday service'}

# Page sections and where their bodies live. Future: 'service-area', 'project', 'blog'.
SECTIONS = {'services': 'bodies', 'service-area': 'bodies-locations', 'project': 'bodies-projects', 'blog': 'bodies-blog'}


def built(section, slug):
    folder = os.path.join(HERE, SECTIONS[section])
    return any(os.path.exists(os.path.join(folder, slug + ext)) for ext in ('.html', '.py'))


def svc_href(slug, root, home):
    """Link to a service page, or to the homepage services section until that page exists."""
    return f'{root}services/{slug}/' if built('services', slug) else f'{home}#services'


def town_href(town, root, home):
    """Link to a location page, or to the homepage service-area section until it exists."""
    slug = slugify(town)
    return f'{root}service-area/{slug}/' if built('service-area', slug) else None


def esc(s):
    return s.replace('&', '&amp;') if '&amp;' not in s else s


# ---------------------------------------------------------------------------
# Shared header / footer pieces
# ---------------------------------------------------------------------------
def dropdown(root, home, current=None):
    cols = []
    for g in ('large', 'service'):
        items = []
        for s in SERVICES:
            if s['group'] != g:
                continue
            active = ' active" aria-current="page' if s['slug'] == current else ''
            items.append(f'                      <li><a class="dropdown-item{active}" href="{svc_href(s["slug"], root, home)}">{esc(s["name"])}</a></li>')
        cols.append(f'''                  <div>
                    <p class="services-menu-title">{GROUP_LABEL[g]}</p>
                    <ul>
{chr(10).join(items)}
                    </ul>
                  </div>''')
    return f'''<li class="nav-item dropdown nav-services">
              <a class="nav-link dropdown-toggle{' active' if current else ''}" href="{home}#services" role="button" data-bs-toggle="dropdown" aria-expanded="false">Services</a>
              <div class="dropdown-menu services-menu">
                <div class="services-menu-grid">
{chr(10).join(cols)}
                </div>
                <a class="services-menu-all" href="{home}#services">View all services <i class="bi bi-chevron-right"></i></a>
              </div>
            </li>'''


def replace_services_li(header, root, home, current=None):
    m = re.search(r'<li class="nav-item dropdown nav-services">.*?View all services <i class="bi bi-chevron-right"></i></a>\s*</div>\s*</li>', header, re.S)
    if not m:
        m = re.search(r'<li class="nav-item"><a class="nav-link" href="[^"]*#services">Services</a></li>', header)
    assert m, 'Services menu item not found'
    return header[:m.start()] + dropdown(root, home, current) + header[m.end():]


FOOTER_SERVICE_MAP = {
    'Water Filtration & Treatment': 'water-filtration-treatment', 'Gas Systems': 'gas-systems',
    'Well Systems & Pressure Tanks': 'well-systems-pressure-tanks', 'Water Heaters': 'water-heater-installation',
    'Complete Bathroom Remodels': 'bathroom-remodels', 'Fixture Installation & Repair': 'fixture-installation-repair',
}


def link_footer_services(footer, root, home):
    def sub(m):
        slug = FOOTER_SERVICE_MAP.get(htmllib.unescape(m.group(2)))
        return f'<li><a href="{svc_href(slug, root, home)}">{m.group(2)}</a></li>' if slug else m.group(0)
    return re.sub(r'<li><a href="([^"]*)">([^<]+)</a></li>', sub, footer)


def relink(block, root, home):
    """Rewrite homepage-relative links for a page that lives below the site root."""
    block = block.replace('href="#top"', f'href="{home or "./"}"')
    block = re.sub(r'href="#([\w-]+)"', lambda m: f'href="{home}#{m.group(1)}"', block)
    block = block.replace('href="reviews.html"', f'href="{root}reviews.html"')
    return block


# ---------------------------------------------------------------------------
# Generated SEO components
# ---------------------------------------------------------------------------
def breadcrumb_html(trail):
    """trail: list of (label, href or None). Last item is the current page."""
    items = []
    for i, (label, href) in enumerate(trail):
        if i == len(trail) - 1:
            items.append(f'            <li class="breadcrumb-item active" aria-current="page">{label}</li>')
        else:
            items.append(f'            <li class="breadcrumb-item"><a href="{href}">{label}</a></li>')
    return '        <nav class="svc-breadcrumb" aria-label="Breadcrumb">\n          <ol class="breadcrumb">\n' + '\n'.join(items) + '\n          </ol>\n        </nav>'


def service_area_html(mod, root, home):
    chips = []
    for t in TOWNS:
        href = town_href(t, root, home)
        chips.append(f'                  <li><a href="{href}">{t}</a></li>' if href else f'                  <li>{t}</li>')
    return f'''    <!-- ============ SERVICE AREA (generated) ============ -->
    <section class="section pt-0" id="service-area">
      <div class="container-xxl px-3 px-lg-4">
        <div class="svc-area">
          <div class="row g-4 align-items-center">
            <div class="col-lg-6">
              <p class="eyebrow">Service area</p>
              <h2 class="section-title">{mod.AREA_HEADING}</h2>
              <p class="svc-area-text">{mod.AREA_TEXT}</p>
            </div>
            <div class="col-lg-6">
              <ul class="area-chips svc-area-chips" aria-label="Towns we serve">
{chr(10).join(chips)}
              </ul>
              <p class="svc-area-note">Don&rsquo;t see your town? Call <a href="tel:{BUSINESS["phone_tel"]}">{BUSINESS["phone_display"]}</a> &mdash; we likely cover it.</p>
            </div>
          </div>
        </div>
      </div>
    </section>
'''


def faq_html(faqs, prefix='sfaq'):
    items = []
    for i, (q, a) in enumerate(faqs, 1):
        items.append(f'''              <div class="accordion-item">
                <h3 class="accordion-header">
                  <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#{prefix}{i}" aria-expanded="false" aria-controls="{prefix}{i}">{q}</button>
                </h3>
                <div id="{prefix}{i}" class="accordion-collapse collapse" data-bs-parent="#svcFaq">
                  <div class="accordion-body">{a}</div>
                </div>
              </div>''')
    return '\n'.join(items)


def business_schema():
    b = {
        '@type': 'Plumber', 'name': BUSINESS['name'], 'telephone': BUSINESS['phone_schema'],
        'address': {'@type': 'PostalAddress', 'addressLocality': BUSINESS['city'], 'addressRegion': BUSINESS['region'], 'addressCountry': BUSINESS['country']},
        'areaServed': [{'@type': 'City', 'name': f'{t}, CT'} for t in TOWNS],
    }
    if SITE_URL:
        b['url'] = SITE_URL + '/'
        b['@id'] = SITE_URL + '/#business'
    if BUSINESS['license']:
        b['hasCredential'] = {'@type': 'EducationalOccupationalCredential', 'credentialCategory': 'license', 'name': f'Connecticut Master Plumber License {BUSINESS["license"]}'}
    return b


def jsonld_blocks(mod, url_path, trail):
    biz = business_schema()
    svc = {'@context': 'https://schema.org', '@type': 'Service', 'serviceType': mod.SERVICE_NAME,
           'name': f'{mod.SERVICE_NAME} in {BUSINESS["city"]}, {BUSINESS["region"]}',
           'description': htmllib.unescape(mod.DESCRIPTION), 'provider': biz, 'areaServed': biz['areaServed']}
    if SITE_URL:
        svc['url'] = SITE_URL + url_path
        if getattr(mod, 'IMAGE', None):
            svc['image'] = SITE_URL + '/' + mod.IMAGE
    data = [svc, {'@context': 'https://schema.org', '@type': 'FAQPage',
                  'mainEntity': [{'@type': 'Question', 'name': htmllib.unescape(q),
                                  'acceptedAnswer': {'@type': 'Answer', 'text': htmllib.unescape(re.sub('<[^>]+>', '', a))}} for q, a in mod.FAQS]}]
    if SITE_URL:
        crumbs = []
        for label, href in trail:
            if href is not None and '#' in href:
                continue  # anchors aren't valid breadcrumb URLs (e.g. Services until a /services/ hub page exists)
            if href is None:
                url = SITE_URL + url_path
            else:
                url = SITE_URL + '/' + href.replace('../', '').lstrip('./')
            crumbs.append({'@type': 'ListItem', 'position': len(crumbs) + 1, 'name': htmllib.unescape(label), 'item': url})
        data.append({'@context': 'https://schema.org', '@type': 'BreadcrumbList', 'itemListElement': crumbs})
    return '\n'.join(f'  <script type="application/ld+json">\n{json.dumps(d, indent=2, ensure_ascii=False)}\n  </script>' for d in data)


# ---------------------------------------------------------------------------
# Page assembly
# ---------------------------------------------------------------------------
def build_service(mod, body):
    section, slug = 'services', mod.SLUG
    root = home = '../../'
    url_path = f'/{section}/{slug}/'
    trail = [('Home', home), ('Services', f'{home}#services'), (esc(mod.SERVICE_NAME), None)]
    src = open(os.path.join(SITE, 'index.html')).read()

    head = src[:src.index('<body>')]
    head = re.sub(r'<title>.*?</title>', f'<title>{mod.TITLE}</title>', head, flags=re.S)
    head = re.sub(r'<meta name="description" content=".*?">', f'<meta name="description" content="{mod.DESCRIPTION}">', head)
    head = head.replace('href="css/styles.css"', f'href="{root}css/styles.css"')
    seo = ['  <meta name="robots" content="index, follow">', '  <meta property="og:type" content="website">',
           f'  <meta property="og:site_name" content="{BUSINESS["name"]}">',
           f'  <meta property="og:title" content="{mod.TITLE}">', f'  <meta property="og:description" content="{mod.DESCRIPTION}">',
           '  <meta property="og:locale" content="en_US">']
    if SITE_URL:
        seo += [f'  <link rel="canonical" href="{SITE_URL}{url_path}">', f'  <meta property="og:url" content="{SITE_URL}{url_path}">']
        og_image = getattr(mod, 'IMAGE', None) or 'images/hero-plumbing.jpg'
        seo.append(f'  <meta property="og:image" content="{SITE_URL}/{og_image}">')
    head = head.replace('<meta name="viewport" content="width=device-width, initial-scale=1">',
                        '<meta name="viewport" content="width=device-width, initial-scale=1">\n' + '\n'.join(seo))
    head = head.replace('</head>', jsonld_blocks(mod, url_path, trail) + '\n</head>')

    header = src[src.index('  <!-- ============ HEADER'):src.index('</header>') + len('</header>')]
    header = relink(replace_services_li(header, root, home, current=slug), root, home)
    header = header.replace(f'href="{home}#quote" class="btn btn-outline-ink"', 'href="#estimate" class="btn btn-outline-ink"')
    tail = src[src.index('  <!-- ============ FOOTER'):]
    tail = relink(link_footer_services(tail, root, home), root, home)
    tail = tail.replace(f'<a href="{home}#quote" class="btn btn-brand">', '<a href="#estimate" class="btn btn-brand">')
    tail = tail.replace('src="js/main.js"', f'src="{root}js/main.js"')

    body = body.replace('{BREADCRUMB}', breadcrumb_html(trail))
    body = body.replace('{SERVICE_AREA}', service_area_html(mod, root, home))
    body = body.replace('{FAQ_ITEMS}', faq_html(mod.FAQS))
    body = body.replace('{ROOT}', root).replace('{HOME}', home)
    body = body.replace('{PHONE}', BUSINESS['phone_display']).replace('{TEL}', BUSINESS['phone_tel'])
    body = re.sub(r'\{SVC:([\w-]+)\}', lambda m: svc_href(m.group(1), root, home), body)
    out = head + '<body>\n\n' + header + '\n\n' + body + '\n' + tail
    return os.path.join(SITE, section, slug, 'index.html'), url_path, out


# ---------------------------------------------------------------------------
# SEO check - errors block the build, warnings are printed
# ---------------------------------------------------------------------------
def sha(text):
    return hashlib.sha256(text.encode('utf-8')).hexdigest()


def visible_text(s):
    main = s[s.index('<main'):s.index('</main>')]
    main = re.sub(r'<(script|style)[^>]*>.*?</\1>', ' ', main, flags=re.S)
    main = re.sub(r'<!--.*?-->', ' ', main, flags=re.S)
    return re.sub(r'\s+', ' ', htmllib.unescape(re.sub(r'<[^>]+>', ' ', main))).strip()


def seo_check(path, url_path, out, mod, rules, pending=None):
    pending = pending or {}
    errors, warns = [], []
    title = htmllib.unescape(re.search(r'<title>(.*?)</title>', out, re.S).group(1))
    desc = htmllib.unescape(re.search(r'<meta name="description" content="(.*?)"', out).group(1))
    kw, city = mod.KEYWORD.lower(), BUSINESS['city'].lower()
    text = visible_text(out); low = text.lower()
    words = re.findall(r"[A-Za-z0-9'’-]+", text)
    h1s = re.findall(r'<h1[^>]*>(.*?)</h1>', out, re.S)

    if len(title) > 65: errors.append(f'title is {len(title)} chars (max 65)')
    if kw not in title.lower()[:50] or city not in title.lower()[:50]: errors.append('keyword and city must both appear in the first 50 chars of the title')
    if not 120 <= len(desc) <= 155: errors.append(f'meta description is {len(desc)} chars (target 120-155)')
    if kw not in desc.lower(): errors.append('keyword missing from meta description')
    if len(h1s) != 1: errors.append(f'{len(h1s)} <h1> tags (need exactly 1)')
    elif kw not in htmllib.unescape(re.sub('<[^>]+>', '', h1s[0])).lower() or city not in h1s[0].lower():
        errors.append('H1 must contain the keyword and the city')
    if kw not in ' '.join(words[:150]).lower(): errors.append('keyword not in the first 150 words')
    if not any(kw in htmllib.unescape(h).lower() for h in re.findall(r'<h2[^>]*>(.*?)</h2>', out, re.S)): errors.append('keyword not in any H2')
    if low.count(city) < 4: errors.append(f'city "{BUSINESS["city"]}" appears {low.count(city)}x in visible text (need 4+)')
    towns_named = sum(1 for t in TOWNS if t.lower() in low)
    if towns_named < 8: errors.append(f'only {towns_named} towns named in visible text (need 8+)')
    for k in getattr(mod, 'SECONDARY_KEYWORDS', []):
        if k.lower() not in low: warns.append(f'secondary keyword "{k}" not in visible text')
    if len(words) < rules['min_words']: errors.append(f'{len(words)} words (need {rules["min_words"]}+)')
    if len(mod.FAQS) != rules['faqs']: errors.append(f'{len(mod.FAQS)} FAQs (need {rules["faqs"]})')
    if 'related' in rules and len(re.findall(r'<article class="service-card', out)) != rules['related']:
        errors.append(f'need exactly {rules["related"]} related service cards')
    for img in re.findall(r'<img[^>]*>', out):
        if not re.search(r'alt="[^"]{8,}"', img): errors.append(f'image missing a descriptive alt: {img[:80]}')
        if 'width=' not in img or 'height=' not in img: warns.append(f'image missing width/height: {img[:80]}')
    left = re.findall(r'\{[A-Z_]+(?::[\w-]+)?\}', out)
    if left: errors.append(f'unfilled placeholders: {sorted(set(left))}')
    if 'id="estimate"' not in out or 'tel:' not in out: errors.append('page needs an #estimate form and a call link')
    # links
    for h in re.findall(r'(?:href|src)="([^"]+)"', out):
        if h.startswith(('http', 'tel:', 'mailto:', 'data:')): continue
        u = urlparse(urljoin('https://x.test' + url_path, h))
        target = u.path + 'index.html' if u.path.endswith('/') else u.path
        fp = os.path.join(SITE, target.lstrip('/'))
        if u.path == url_path:
            page_html = out
        elif u.path in pending:
            page_html = pending[u.path]          # page being built in this same run
        else:
            page_html = open(fp, encoding='utf-8').read() if os.path.exists(fp) and fp.endswith('.html') else None
        if u.path != url_path and u.path not in pending and not os.path.exists(fp):
            errors.append(f'broken link: {h}')
        elif u.fragment and page_html is not None and f'id="{u.fragment}"' not in page_html:
            errors.append(f'broken anchor: {h}')
    return errors, warns, dict(title=len(title), desc=len(desc), words=len(words), city=low.count(city), towns=towns_named)


SERVICE_RULES = dict(min_words=1000, faqs=5, related=3)


# ---------------------------------------------------------------------------
# Root pages, sitemap, robots
# ---------------------------------------------------------------------------
HOME_CARD_MAP = {
    'Bathroom Remodels': 'bathroom-remodels', 'Water Filtration & Treatment': 'water-filtration-treatment',
    'Gas Systems': 'gas-systems', 'Well Systems & Pressure Tanks': 'well-systems-pressure-tanks',
    'Fixture Installation & Repair': 'fixture-installation-repair', 'Water Heater Installation': 'water-heater-installation',
}


def link_home_cards(s):
    a, b = s.index('id="services"'), s.index('<!-- ============ ABOUT')
    sec = s[a:b]
    def sub(m):
        slug = HOME_CARD_MAP.get(htmllib.unescape(m.group(2).strip()))
        if not slug or not built('services', slug):
            return m.group(0)
        return re.sub(r'<a href="[^"]*" class="link-more">', f'<a href="services/{slug}/" class="link-more">', m.group(0))
    sec = re.sub(r'(<article class="service-card[^"]*">.*?<h3>(.*?)</h3>.*?</article>)', sub, sec, flags=re.S)
    return s[:a] + sec + s[b:]


def update_root_pages():
    for name, home in (('index.html', ''), ('reviews.html', 'index.html')):
        p = os.path.join(SITE, name)
        s = open(p).read()
        a, b = s.index('  <!-- ============ HEADER'), s.index('</header>')
        s = s[:a] + replace_services_li(s[a:b], '', home) + s[b:]
        f = s.index('  <!-- ============ FOOTER')
        s = s[:f] + link_footer_services(s[f:], '', home)
        if name == 'index.html':
            s = link_home_cards(s)
        open(p, 'w').write(s)


def write_sitemap(url_paths):
    if not SITE_URL:
        print('  (sitemap.xml / robots.txt / canonical tags skipped - set SITE_URL once the domain is known)')
        return
    today = date.today().isoformat()
    urls = ['/', '/reviews.html'] + url_paths
    xml = ['<?xml version="1.0" encoding="UTF-8"?>', '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    xml += [f'  <url><loc>{SITE_URL}{u}</loc><lastmod>{today}</lastmod></url>' for u in urls]
    xml.append('</urlset>')
    open(os.path.join(SITE, 'sitemap.xml'), 'w').write('\n'.join(xml) + '\n')
    open(os.path.join(SITE, 'robots.txt'), 'w').write(f'User-agent: *\nAllow: /\n\nSitemap: {SITE_URL}/sitemap.xml\n')
    print('  wrote sitemap.xml and robots.txt')


if __name__ == '__main__':
    import importlib.util
    pages, failed = [], False
    manifest = json.load(open(MANIFEST)) if os.path.exists(MANIFEST) else {}
    folder = os.path.join(HERE, SECTIONS['services'])
    rendered = []
    for fn in sorted(os.listdir(folder)):
        if not fn.endswith('.py'):
            continue
        spec = importlib.util.spec_from_file_location(fn[:-3], os.path.join(folder, fn))
        mod = importlib.util.module_from_spec(spec); spec.loader.exec_module(mod)
        html_body = os.path.join(folder, mod.SLUG + '.html')
        if os.path.exists(html_body):
            body = open(html_body, encoding='utf-8').read()
        else:
            import service_template
            body = service_template.render(mod, BY_SLUG)
        path, url_path, out = build_service(mod, body)
        rendered.append((mod, path, url_path, out))
    pending = {url_path: out for _, _, url_path, out in rendered}

    for mod, path, url_path, out in rendered:
        errors, warns, stats = seo_check(path, url_path, out, mod, SERVICE_RULES, pending)
        print(f'{url_path}  title {stats["title"]} · desc {stats["desc"]} · {stats["words"]} words · city x{stats["city"]} · {stats["towns"]} towns')
        for w in warns: print('  warning:', w)
        if errors:
            failed = True
            for e in errors: print('  ERROR:', e)
            print('  -> not written')
            continue
        rel = os.path.relpath(path, SITE).replace(os.sep, '/')
        if os.path.exists(path) and not FORCE:
            current = open(path, encoding='utf-8').read()
            if current != out and manifest.get(rel) != sha(current):
                failed = True
                print(f'  HAND EDITS DETECTED in {rel} - not overwritten.')
                print('  -> copy the change into its template in bodies/, then rebuild (or use --force to discard it)')
                pages.append(url_path)
                continue
        os.makedirs(os.path.dirname(path), exist_ok=True)
        open(path, 'w', encoding='utf-8').write(out)
        manifest[rel] = sha(out)
        pages.append(url_path)
    json.dump(manifest, open(MANIFEST, 'w'), indent=2)
    update_root_pages()
    write_sitemap(pages)
    sys.exit(1 if failed else 0)
