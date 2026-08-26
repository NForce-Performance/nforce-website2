#!/usr/bin/env python3
"""
N-Force Performance — statische sitegenerator (zonder afhankelijkheden).

Waarom dit bestand bestaat
--------------------------
De gepubliceerde site in /nl/ is gewone HTML en werkt zonder buildstap: je kunt
het repo zo naar GitHub Pages of Netlify pushen. Maar navigatie, footer en head
staan dan in elk bestand. Dit script houdt die gedeelde onderdelen op één plek.

Gebruik
-------
    python3 tools/build.py

Het schrijft alle pagina's opnieuw weg naar /nl/, plus sitemap.xml en de
redirect-stubs vanaf de oude .html-URL's. Bewerk de inhoud in
tools/content.py, nooit rechtstreeks in de gegenereerde bestanden.
"""

import os
import re
import shutil
from datetime import date

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE = "https://www.nforce-performance.nl"
LANG = "nl"
TODAY = date.today().isoformat()

NAV = [
    ("Online coaching", "/nl/online-coaching/"),
    ("Teams &amp; clubs", "/nl/teams/"),
    ("Testing &amp; analyse", "/nl/testing/"),
    ("Resultaten", "/nl/resultaten/"),
    ("Over N-Force", "/nl/over/"),
]
CTA_URL = "/nl/performance-check/"
CTA_LABEL = "Plan je Performance Check"
CTA_LABEL_SHORT = "Performance Check"


# ---------------------------------------------------------------------------
# Onderdelen
# ---------------------------------------------------------------------------

def nav_html(current):
    out = []
    for label, href in NAV:
        cur = ' aria-current="page"' if current.startswith(href) else ""
        out.append('<a href="%s"%s>%s</a>' % (href, cur, label))
    return "\n        ".join(out)


def mobile_nav_html(current):
    out = []
    for label, href in NAV:
        cur = ' aria-current="page"' if current.startswith(href) else ""
        out.append('<a class="mlink" href="%s"%s>%s</a>' % (href, cur, label))
    return "\n      ".join(out)


LANGSWITCH = """<div class="langswitch" aria-label="Taal">
        <span aria-current="true">NL</span>
        <span aria-disabled="true" title="Binnenkort beschikbaar">EN</span>
        <span aria-disabled="true" title="Binnenkort beschikbaar">DE</span>
      </div>"""

HEADER = """<header class="site-header">
    <div class="wrap site-header__inner">
      <a class="brand" href="/nl/">
        <strong>N-Force Performance</strong>
        <span>Kracht &amp; Conditie</span>
      </a>
      <nav class="nav" aria-label="Hoofdnavigatie">
        {nav}
      </nav>
      {langswitch}
      <a class="btn btn--primary btn--sm header-cta" href="{cta_url}">{cta_short}</a>
      <button class="nav-toggle" type="button" aria-expanded="false" aria-controls="mobile-nav">
        Menu <b aria-hidden="true"></b>
      </button>
    </div>
    <div class="mobile-nav" id="mobile-nav" data-open="false">
      <a class="btn btn--primary" href="{cta_url}">{cta_label}</a>
      {mnav}
      {langswitch}
    </div>
  </header>"""

FOOTER = """<footer class="site-footer">
    <div class="wrap site-footer__grid">
      <div class="site-footer__about">
        <h5>N-Force Performance</h5>
        <p>Strength &amp; conditioning met een nulmeting aan het begin en een hertest aan het eind. Online coaching wereldwijd, teambegeleiding en testdagen in Nederland en Vlaanderen.</p>
      </div>
      <div>
        <h5>Diensten</h5>
        <ul>
          <li><a href="/nl/online-coaching/">Online coaching</a></li>
          <li><a href="/nl/online-coaching/return-to-play/">Return to Play</a></li>
          <li><a href="/nl/teams/">Teams &amp; clubs</a></li>
          <li><a href="/nl/testing/">Testing &amp; analyse</a></li>
          <li><a href="/nl/tarieven/">Tarieven</a></li>
        </ul>
      </div>
      <div>
        <h5>Meer weten</h5>
        <ul>
          <li><a href="/nl/resultaten/">Resultaten &amp; ervaringen</a></li>
          <li><a href="/nl/resultaten/referentiewaarden/">Referentiewaarden</a></li>
          <li><a href="/nl/over/">Over N-Force</a></li>
          <li><a href="/nl/performance-check/">Performance Check</a></li>
          <li><a href="/nl/privacy/">Privacyverklaring</a></li>
          <li><a href="/nl/voorwaarden/">Algemene voorwaarden</a></li>
        </ul>
      </div>
    </div>
    <div class="wrap site-footer__bottom">
      <div>
        Nick Bergman &middot; Tilburg &middot;
        <a href="mailto:nick@nforce-performance.nl">nick@nforce-performance.nl</a> &middot;
        <a href="tel:+31622680892" class="num">+31 6 22 68 08 92</a>
      </div>
      <div>
        <a href="https://www.instagram.com/nforce.performance/" rel="me noopener">Instagram</a> &middot;
        <a href="https://www.linkedin.com/in/nick-bergman-7b9828218" rel="me noopener">LinkedIn</a> &middot;
        <a href="https://wa.me/31622680892" rel="noopener">WhatsApp</a>
      </div>
      <div>KVK <span class="num">99722283</span> &middot; Btw-id <span class="num">NL005406539B11</span> &middot; &copy; 2026</div>
    </div>
  </footer>"""

MOBILEBAR = """<div class="mobilebar" data-show="false">
    <a class="btn btn--primary btn--block" href="{cta_url}">{cta_label}</a>
  </div>"""

LAYOUT = """<!doctype html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{description}">
<link rel="canonical" href="{canonical}">
<link rel="alternate" hreflang="nl" href="{canonical}">
<link rel="alternate" hreflang="x-default" href="{canonical}">
<meta name="robots" content="index, follow, max-image-preview:large">
<meta property="og:type" content="website">
<meta property="og:site_name" content="N-Force Performance">
<meta property="og:locale" content="nl_NL">
<meta property="og:title" content="{og_title}">
<meta property="og:description" content="{description}">
<meta property="og:url" content="{canonical}">
<meta property="og:image" content="{og_image}">
<meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#06080b">
<link rel="icon" href="/assets/img/favicon.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="preconnect" href="https://api.fontshare.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Archivo:ital,wght@0,400..900;1,400..900&family=IBM+Plex+Mono:wght@400;500;600&display=swap">
<link rel="stylesheet" href="https://api.fontshare.com/v2/css?f[]=satoshi@300,400,500,700&display=swap">
<link rel="stylesheet" href="/assets/css/site.css">
<script>document.documentElement.className+=" js";</script>
{preload}
<script type="application/ld+json">{jsonld}</script>
</head>
<body>
<a class="skip" href="#main">Direct naar de inhoud</a>
{header}
<main id="main">
{content}
</main>
{footer}
{mobilebar}
{scripts}
<script src="/assets/js/site.js" defer></script>
</body>
</html>
"""


def jsonld_for(page):
    graph = [{
        "@type": "ProfessionalService",
        "@id": SITE + "/#organisatie",
        "name": "N-Force Performance",
        "description": "Strength & conditioning voor sporters, teams en clubs. Online coaching, teambegeleiding en testdagen.",
        "url": SITE + "/nl/",
        "email": "nick@nforce-performance.nl",
        "telephone": "+31622680892",
        "vatID": "NL005406539B11",
        "taxID": "99722283",
        "priceRange": "€49 - €249 per maand",
        "areaServed": [
            {"@type": "Country", "name": "Nederland"},
            {"@type": "Country", "name": "België"},
        ],
        "address": {"@type": "PostalAddress", "addressLocality": "Tilburg", "addressCountry": "NL"},
        "founder": {"@id": SITE + "/#nick"},
        "sameAs": [
            "https://www.instagram.com/nforce.performance/",
            "https://www.linkedin.com/in/nick-bergman-7b9828218",
        ],
    }, {
        "@type": "Person",
        "@id": SITE + "/#nick",
        "name": "Nick Bergman",
        "jobTitle": "Performance coach / strength & conditioning specialist",
        "worksFor": {"@id": SITE + "/#organisatie"},
        "alumniOf": {"@type": "CollegeOrUniversity", "name": "Fontys Sporthogeschool"},
        "knowsAbout": ["Strength and conditioning", "Return to play", "Sporttesting", "Periodisering"],
        "sameAs": ["https://www.linkedin.com/in/nick-bergman-7b9828218"],
    }]

    crumbs = page.get("crumbs") or []
    if crumbs:
        items = [{"@type": "ListItem", "position": 1, "name": "Home", "item": SITE + "/nl/"}]
        for i, (label, href) in enumerate(crumbs, start=2):
            items.append({"@type": "ListItem", "position": i, "name": strip_tags(label), "item": SITE + href})
        graph.append({"@type": "BreadcrumbList", "itemListElement": items})

    if page.get("service"):
        graph.append(dict({"@type": "Service", "provider": {"@id": SITE + "/#organisatie"}}, **page["service"]))

    if page.get("faq"):
        graph.append({
            "@type": "FAQPage",
            "mainEntity": [
                {"@type": "Question", "name": strip_tags(q),
                 "acceptedAnswer": {"@type": "Answer", "text": strip_tags(a)}}
                for q, a in page["faq"]
            ],
        })

    import json
    return json.dumps({"@context": "https://schema.org", "@graph": graph}, ensure_ascii=False, separators=(",", ":"))


def strip_tags(s):
    return re.sub(r"\s+", " ", re.sub(r"<[^>]+>", "", s)).strip()


def render(page):
    url = page["url"]
    canonical = SITE + url
    preload = ""
    if page.get("hero_img"):
        preload = '<link rel="preload" as="image" href="%s" fetchpriority="high">' % page["hero_img"]
    scripts = page.get("scripts", "")
    html = LAYOUT.format(
        lang=LANG,
        title=page["title"],
        description=page["description"],
        canonical=canonical,
        og_title=page.get("og_title", page["title"]),
        og_image=SITE + page.get("og_image", "/assets/img/og-default.jpg"),
        preload=preload,
        jsonld=jsonld_for(page),
        header=HEADER.format(nav=nav_html(url), mnav=mobile_nav_html(url),
                             langswitch=LANGSWITCH, cta_url=CTA_URL, cta_label=CTA_LABEL,
                             cta_short=CTA_LABEL_SHORT),
        content=page["content"],
        footer=FOOTER,
        mobilebar=MOBILEBAR.format(cta_url=CTA_URL, cta_label=CTA_LABEL),
        scripts=scripts,
    )
    out_dir = os.path.join(ROOT, url.strip("/"))
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "index.html"), "w", encoding="utf-8") as fh:
        fh.write(html)
    return url


# ---------------------------------------------------------------------------
# Redirect-stubs voor de oude URL's
# ---------------------------------------------------------------------------
REDIRECTS = {
    "diensten-online.html": "/nl/online-coaching/",
    "diensten-teams.html": "/nl/teams/",
    "diensten-testing.html": "/nl/testing/",
    "resultaten.html": "/nl/resultaten/",
    "privacy.html": "/nl/privacy/",
}

REDIRECT_TPL = """<!doctype html>
<html lang="nl">
<head>
<meta charset="utf-8">
<title>Verplaatst naar {target}</title>
<link rel="canonical" href="{site}{target}">
<meta name="robots" content="noindex, follow">
<meta http-equiv="refresh" content="0; url={target}">
<script>location.replace("{target}");</script>
</head>
<body style="background:#06080b;color:#b8c2cc;font-family:system-ui,sans-serif;padding:3rem">
<p>Deze pagina is verhuisd naar <a href="{target}" style="color:#7ec8ff">{site}{target}</a>.</p>
</body>
</html>
"""


def write_redirects():
    for old, target in REDIRECTS.items():
        with open(os.path.join(ROOT, old), "w", encoding="utf-8") as fh:
            fh.write(REDIRECT_TPL.format(target=target, site=SITE))


ROOT_DISPATCH = """<!doctype html>
<html lang="nl">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>N-Force Performance — strength &amp; conditioning</title>
<meta name="description" content="Strength &amp; conditioning voor sporters, teams en clubs. Online coaching, teambegeleiding en testdagen.">
<link rel="canonical" href="{site}/nl/">
<link rel="alternate" hreflang="nl" href="{site}/nl/">
<link rel="alternate" hreflang="x-default" href="{site}/nl/">
<meta http-equiv="refresh" content="0; url=/nl/">
<meta name="theme-color" content="#06080b">
<script>
/* Zodra /en/ en /de/ live staan: voeg ze toe aan `available` hieronder.
   De bezoeker komt dan in zijn eigen taal binnen, met /nl/ als vaste terugval. */
(function () {
  var available = ['nl'];
  var wanted = (navigator.languages || [navigator.language || 'nl'])
    .map(function (l) { return String(l).slice(0, 2).toLowerCase(); });
  var pick = 'nl';
  for (var i = 0; i < wanted.length; i++) {
    if (available.indexOf(wanted[i]) !== -1) { pick = wanted[i]; break; }
  }
  location.replace('/' + pick + '/');
})();
</script>
</head>
<body style="background:#06080b;color:#b8c2cc;font-family:system-ui,sans-serif;padding:3rem">
<p>Kies je taal &middot; Choose your language &middot; Sprache w&auml;hlen</p>
<p><a href="/nl/" style="color:#7ec8ff">Nederlands</a></p>
</body>
</html>
"""


def write_root():
    with open(os.path.join(ROOT, "index.html"), "w", encoding="utf-8") as fh:
        fh.write(ROOT_DISPATCH.replace("{site}", SITE))


def write_sitemap(urls):
    prio = {"/nl/": "1.0", "/nl/performance-check/": "0.9"}
    rows = []
    for u in urls:
        if u in ("/nl/privacy/", "/nl/voorwaarden/"):
            p, freq = "0.2", "yearly"
        else:
            p, freq = prio.get(u, "0.7"), "monthly"
        rows.append(
            "  <url>\n    <loc>%s%s</loc>\n    <lastmod>%s</lastmod>\n"
            "    <changefreq>%s</changefreq>\n    <priority>%s</priority>\n  </url>"
            % (SITE, u, TODAY, freq, p)
        )
    xml = ('<?xml version="1.0" encoding="UTF-8"?>\n'
           '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
           + "\n".join(rows) + "\n</urlset>\n")
    with open(os.path.join(ROOT, "sitemap.xml"), "w", encoding="utf-8") as fh:
        fh.write(xml)


def main():
    import content
    urls = []
    for page in content.PAGES:
        urls.append(render(page))
    write_redirects()
    write_root()
    write_sitemap(urls)
    print("Gegenereerd: %d pagina's, %d redirects." % (len(urls), len(REDIRECTS)))
    for u in urls:
        print("  " + u)


if __name__ == "__main__":
    import sys
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    main()
