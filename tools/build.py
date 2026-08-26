#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
N-Force Performance — statische sitegenerator (geen dependencies).

    python3 tools/build.py

Wat dit script doet
-------------------
* rendert elke pagina in drie talen naar /nl/, /en/ en /de/
* schrijft de root-taaldispatcher, sitemap.xml, robots.txt en redirect-stubs
* houdt navigatie, footer, head, hreflang en gestructureerde data op één plek

Waar staat wat
--------------
    tools/routes.py   URL-slugs per taal          (nieuwe pagina toevoegen)
    tools/i18n.py     alle teksten per taal       (copy aanpassen)
    tools/pages.py    paginaopbouw uit blokken    (structuur aanpassen)
    assets/data/*.json  handboeken, referentiewaarden, regels, UI-teksten

Bewerk NOOIT de gegenereerde HTML in /nl/, /en/ of /de/ — die wordt overschreven.
"""

import json
import os
import re
import sys
from datetime import date

HERE = os.path.dirname(os.path.abspath(__file__))
if HERE not in sys.path:
    sys.path.insert(0, HERE)

import routes
import i18n
import pages

ROOT = os.path.dirname(HERE)
SITE = "https://www.nforce-performance.nl"
LANGS = ("nl", "en", "de")
TODAY = date.today().isoformat()

FLAGS = {
    "nl": '<svg class="flag" viewBox="0 0 9 6" aria-hidden="true"><rect width="9" height="6" fill="#21468B"/><rect width="9" height="4" fill="#fff"/><rect width="9" height="2" fill="#AE1C28"/></svg>',
    "en": '<svg class="flag" viewBox="0 0 60 30" aria-hidden="true"><clipPath id="gb"><path d="M0 0v30h60V0z"/></clipPath><g clip-path="url(#gb)"><path d="M0 0v30h60V0z" fill="#012169"/><path d="M0 0l60 30m0-30L0 30" stroke="#fff" stroke-width="6"/><path d="M0 0l60 30m0-30L0 30" stroke="#C8102E" stroke-width="4"/><path d="M30 0v30M0 15h60" stroke="#fff" stroke-width="10"/><path d="M30 0v30M0 15h60" stroke="#C8102E" stroke-width="6"/></g></svg>',
    "de": '<svg class="flag" viewBox="0 0 5 3" aria-hidden="true"><rect width="5" height="3" fill="#000"/><rect width="5" height="2" y="1" fill="#D00"/><rect width="5" height="1" y="2" fill="#FFCE00"/></svg>',
}
LANGNAMES = {"nl": "Nederlands", "en": "English", "de": "Deutsch"}

LOGO = (
    '<svg viewBox="0 0 32 32" fill="none" aria-hidden="true">'
    '<path d="M4 27V5l24 22V5" stroke="currentColor" stroke-width="3" stroke-linejoin="round"/>'
    '<path d="M4 16h24" stroke="currentColor" stroke-width="1" opacity=".45"/>'
    "</svg>"
)


# ---------------------------------------------------------------------------
# Onderdelen
# ---------------------------------------------------------------------------

def t(key, lang):
    return i18n.t(key, lang)


def nav_items(lang):
    return [(t("nav_" + k, lang), routes.url(k, lang)) for k in routes.NAV]


def nav_html(lang, current, mobile=False):
    out = []
    for label, href in nav_items(lang):
        cur = ' aria-current="page"' if current == href else ""
        cls = ' class="mlink"' if mobile else ""
        out.append('<a%s href="%s"%s>%s</a>' % (cls, href, cur, label))
    return ("\n      " if mobile else "\n        ").join(out)


def langswitch(lang, key):
    menu = []
    for code in LANGS:
        cur = ' aria-current="true"' if code == lang else ""
        menu.append(
            '<a href="%s" hreflang="%s" lang="%s"%s>%s<span>%s</span></a>'
            % (routes.url(key, code), code, code, cur, FLAGS[code], LANGNAMES[code])
        )
    return (
        '<div class="langswitch" data-open="false">'
        '<button class="langswitch__btn" type="button" aria-expanded="false" aria-haspopup="true" aria-label="%s">%s %s</button>'
        '<div class="langswitch__menu">%s</div>'
        "</div>"
    ) % (t("lang_label", lang), FLAGS[lang], lang.upper(), "".join(menu))


def cartbutton(lang):
    return (
        '<button class="cartbtn" type="button" data-open-cart data-empty="true" aria-label="%s">'
        '<svg viewBox="0 0 24 24" fill="none" aria-hidden="true"><path d="M3 4h3l2.4 11.2a2 2 0 0 0 2 1.6h7.3a2 2 0 0 0 2-1.6L21 8H7" stroke="currentColor" stroke-width="1.8" stroke-linejoin="round"/><circle cx="10" cy="20" r="1.4" fill="currentColor"/><circle cx="18" cy="20" r="1.4" fill="currentColor"/></svg>'
        '<span class="cartbtn__count" data-cart-count>0</span></button>'
    ) % t("cart_label", lang)


def header(lang, key):
    cta_url = routes.url("contact", lang)
    return """<header class="site-header">
    <div class="wrap site-header__inner">
      <a class="brand" href="%(home)s" aria-label="N-Force Performance">
        %(logo)s
        <span><b>N-Force Performance</b><span>%(tagline)s</span></span>
      </a>
      <nav class="nav" aria-label="%(navlabel)s">
        %(nav)s
      </nav>
      <div class="header-tools">
        %(lang)s
        %(cart)s
        <a class="btn btn--primary btn--sm header-cta" href="%(cta)s">%(cta_short)s</a>
        <button class="nav-toggle" type="button" aria-expanded="false" aria-controls="mobile-nav">
          %(menu)s <b aria-hidden="true"></b>
        </button>
      </div>
    </div>
    <div class="mobile-nav" id="mobile-nav" data-open="false">
      <a class="btn btn--primary" href="%(cta)s">%(cta_label)s</a>
      %(mnav)s
    </div>
  </header>""" % {
        "home": routes.url("home", lang),
        "logo": LOGO,
        "tagline": t("brand_tagline", lang),
        "navlabel": t("nav_label", lang),
        "nav": nav_html(lang, routes.url(key, lang)),
        "mnav": nav_html(lang, routes.url(key, lang), mobile=True),
        "lang": langswitch(lang, key),
        "cart": cartbutton(lang),
        "cta": cta_url,
        "cta_short": t("cta_short", lang),
        "cta_label": t("cta_label", lang),
        "menu": t("menu", lang),
    }


def footer(lang):
    def li(key):
        return '<li><a href="%s">%s</a></li>' % (routes.url(key, lang), t("nav_" + key, lang))

    return """<footer class="site-footer">
    <div class="wrap site-footer__grid">
      <div>
        <h5>N-Force Performance</h5>
        <p>%(about)s</p>
      </div>
      <div>
        <h5>%(h_services)s</h5>
        <ul>%(services)s</ul>
      </div>
      <div>
        <h5>%(h_more)s</h5>
        <ul>%(more)s</ul>
      </div>
    </div>
    <div class="wrap site-footer__bottom">
      <div>Nick Bergman &middot; Tilburg &middot; <a href="mailto:nick@nforce-performance.nl">nick@nforce-performance.nl</a> &middot; <a class="num" href="tel:+31622680892">+31 6 22 68 08 92</a></div>
      <div><a href="https://www.instagram.com/nforce.performance/" rel="me noopener">Instagram</a> &middot; <a href="https://www.linkedin.com/in/nick-bergman-7b9828218" rel="me noopener">LinkedIn</a> &middot; <a href="https://wa.me/31622680892" rel="noopener">WhatsApp</a></div>
      <div>KVK <span class="num">99722283</span> &middot; Btw-id <span class="num">NL005406539B11</span> &middot; &copy; %(year)s</div>
    </div>
  </footer>""" % {
        "about": t("footer_about", lang),
        "h_services": t("footer_services", lang),
        "h_more": t("footer_more", lang),
        "services": "".join(li(k) for k in ("coaching", "teams", "testing", "pricing")),
        "more": "".join(li(k) for k in ("selftest", "handbooks", "about", "contact", "privacy", "terms")),
        "year": date.today().year,
    }


def mobilebar(lang):
    return (
        '<div class="mobilebar" data-show="false">'
        '<a class="btn btn--ghost btn--sm" href="%s">%s</a>'
        '<a class="btn btn--primary btn--sm" href="%s">%s</a>'
        "</div>"
    ) % (
        routes.url("selftest", lang), t("bar_selftest", lang),
        routes.url("contact", lang), t("cta_short", lang),
    )


LAYOUT = """<!doctype html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{description}">
<link rel="canonical" href="{canonical}">
{hreflang}
<meta name="robots" content="index, follow, max-image-preview:large">
<meta property="og:type" content="website">
<meta property="og:site_name" content="N-Force Performance">
<meta property="og:locale" content="{oglocale}">
<meta property="og:title" content="{og_title}">
<meta property="og:description" content="{description}">
<meta property="og:url" content="{canonical}">
<meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#05070a">
<link rel="icon" href="/assets/img/favicon.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="preconnect" href="https://api.fontshare.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Archivo:wght@500;600;700;800&family=IBM+Plex+Mono:wght@400;500;600&display=swap">
<link rel="stylesheet" href="https://api.fontshare.com/v2/css?f[]=satoshi@400,500,700&display=swap">
<link rel="stylesheet" href="/assets/css/site.css">
<script>document.documentElement.className+=" js";</script>
<script type="application/ld+json">{jsonld}</script>
</head>
<body>
<a class="skip" href="#main">{skip}</a>
{header}
<main id="main">
{content}
</main>
{footer}
{mobilebar}
<script src="/assets/js/nf-core.js" defer></script>
<script src="/assets/js/site.js" defer></script>
{scripts}
</body>
</html>
"""

OGLOCALE = {"nl": "nl_NL", "en": "en_GB", "de": "de_DE"}


def strip_tags(s):
    return re.sub(r"\s+", " ", re.sub(r"<[^>]+>", "", s)).strip()


def hreflang_block(key):
    rows = [
        '<link rel="alternate" hreflang="%s" href="%s%s">' % (code, SITE, routes.url(key, code))
        for code in LANGS
    ]
    rows.append('<link rel="alternate" hreflang="x-default" href="%s%s">' % (SITE, routes.url(key, "nl")))
    return "\n".join(rows)


def jsonld_for(page, lang, key):
    graph = [
        {
            "@type": "ProfessionalService",
            "@id": SITE + "/#organisatie",
            "name": "N-Force Performance",
            "description": strip_tags(t("footer_about", lang)),
            "url": SITE + routes.url("home", lang),
            "email": "nick@nforce-performance.nl",
            "telephone": "+31622680892",
            "vatID": "NL005406539B11",
            "taxID": "99722283",
            "priceRange": "\u20ac29 - \u20ac249",
            "areaServed": [
                {"@type": "Country", "name": "Nederland"},
                {"@type": "Country", "name": "Belgi\u00eb"},
                {"@type": "Country", "name": "Deutschland"},
            ],
            "address": {"@type": "PostalAddress", "addressLocality": "Tilburg", "addressCountry": "NL"},
            "founder": {"@id": SITE + "/#nick"},
            "sameAs": [
                "https://www.instagram.com/nforce.performance/",
                "https://www.linkedin.com/in/nick-bergman-7b9828218",
            ],
        },
        {
            "@type": "Person",
            "@id": SITE + "/#nick",
            "name": "Nick Bergman",
            "jobTitle": "Performance coach / strength & conditioning specialist",
            "worksFor": {"@id": SITE + "/#organisatie"},
            "knowsAbout": ["Strength and conditioning", "Return to play", "Sport testing", "Periodisation", "Ice hockey"],
        },
    ]

    crumbs = page.get("crumbs") or []
    if crumbs:
        items = [{"@type": "ListItem", "position": 1, "name": "Home", "item": SITE + routes.url("home", lang)}]
        for i, ck in enumerate(crumbs, start=2):
            items.append({
                "@type": "ListItem", "position": i,
                "name": strip_tags(t("nav_" + ck, lang)),
                "item": SITE + routes.url(ck, lang),
            })
        graph.append({"@type": "BreadcrumbList", "itemListElement": items})

    if page.get("faq"):
        graph.append({
            "@type": "FAQPage",
            "mainEntity": [
                {"@type": "Question", "name": strip_tags(q),
                 "acceptedAnswer": {"@type": "Answer", "text": strip_tags(a)}}
                for q, a in page["faq"]
            ],
        })

    if page.get("service"):
        graph.append(dict({"@type": "Service", "provider": {"@id": SITE + "/#organisatie"}}, **page["service"]))

    return json.dumps({"@context": "https://schema.org", "@graph": graph},
                      ensure_ascii=False, separators=(",", ":"))


def render(key, lang):
    page = pages.build(key, lang)
    url = routes.url(key, lang)
    html = LAYOUT.format(
        lang=lang,
        title=page["title"],
        description=page["description"],
        canonical=SITE + url,
        hreflang=hreflang_block(key),
        oglocale=OGLOCALE[lang],
        og_title=page.get("og_title", page["title"]),
        jsonld=jsonld_for(page, lang, key),
        skip=t("skip", lang),
        header=header(lang, key),
        content=page["content"],
        footer=footer(lang),
        mobilebar=mobilebar(lang),
        scripts=page.get("scripts", ""),
    )
    out_dir = os.path.join(ROOT, url.strip("/"))
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "index.html"), "w", encoding="utf-8") as fh:
        fh.write(html)
    return url


# ---------------------------------------------------------------------------
# Root, redirects, sitemap, robots
# ---------------------------------------------------------------------------

ROOT_DISPATCH = """<!doctype html>
<html lang="nl">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>N-Force Performance — strength &amp; conditioning</title>
<meta name="description" content="Strength &amp; conditioning voor sporters, teams en clubs. Online coaching, handboeken en testing.">
<link rel="canonical" href="__SITE__/nl/">
<link rel="alternate" hreflang="nl" href="__SITE__/nl/">
<link rel="alternate" hreflang="en" href="__SITE__/en/">
<link rel="alternate" hreflang="de" href="__SITE__/de/">
<link rel="alternate" hreflang="x-default" href="__SITE__/nl/">
<meta http-equiv="refresh" content="0; url=/nl/">
<meta name="theme-color" content="#05070a">
<link rel="stylesheet" href="/assets/css/site.css">
<script>
(function () {
  var available = ['nl', 'en', 'de'];
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
<body>
<div class="wrap section">
<p class="eyebrow">N-Force Performance</p>
<h1>Kies je taal &middot; Choose your language &middot; Sprache w&auml;hlen</h1>
<p class="actions"><a class="btn btn--primary" href="/nl/">Nederlands</a>
<a class="btn btn--ghost" href="/en/">English</a>
<a class="btn btn--ghost" href="/de/">Deutsch</a></p>
</div>
</body>
</html>
"""

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
<body style="background:#05070a;color:#a8b4c2;font-family:system-ui,sans-serif;padding:3rem">
<p>Deze pagina is verhuisd naar <a href="{target}" style="color:#7ec8ff">{site}{target}</a>.</p>
</body>
</html>
"""

# oude URL's van de vorige site -> nieuwe locatie
LEGACY = {
    "diensten-online.html": "coaching",
    "diensten-teams.html": "teams",
    "diensten-testing.html": "testing",
    "resultaten.html": "selftest",
    "privacy.html": "privacy",
}


def write_root():
    with open(os.path.join(ROOT, "index.html"), "w", encoding="utf-8") as fh:
        fh.write(ROOT_DISPATCH.replace("__SITE__", SITE))


def write_redirects():
    lines = ["# Netlify redirects — echte 301's", "/  /nl/  302  Language=nl", "/  /en/  302  Language=en", "/  /de/  302  Language=de"]
    for old, key in LEGACY.items():
        target = routes.url(key, "nl")
        with open(os.path.join(ROOT, old), "w", encoding="utf-8") as fh:
            fh.write(REDIRECT_TPL.format(target=target, site=SITE))
        lines.append("/%s  %s  301!" % (old, target))
    # oude ankers en losse paden
    lines.append("/nl/resultaten/  %s  301!" % routes.url("selftest", "nl"))
    with open(os.path.join(ROOT, "_redirects"), "w", encoding="utf-8") as fh:
        fh.write("\n".join(lines) + "\n")


def write_sitemap(urls):
    prio = {}
    for lang in LANGS:
        prio[routes.url("home", lang)] = "1.0"
        prio[routes.url("selftest", lang)] = "0.9"
        prio[routes.url("handbooks", lang)] = "0.9"
        prio[routes.url("contact", lang)] = "0.8"
    rows = []
    for u in urls:
        low = "0.2" if ("privacy" in u or "voorwaarden" in u or "terms" in u or "agb" in u or "datenschutz" in u or "bestellen" in u or "checkout" in u or "kasse" in u) else None
        p = low or prio.get(u, "0.7")
        freq = "yearly" if low else "monthly"
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


def write_misc():
    with open(os.path.join(ROOT, "robots.txt"), "w", encoding="utf-8") as fh:
        fh.write("User-agent: *\nAllow: /\n\nSitemap: %s/sitemap.xml\n" % SITE)
    with open(os.path.join(ROOT, "CNAME"), "w", encoding="utf-8") as fh:
        fh.write("www.nforce-performance.nl\n")
    open(os.path.join(ROOT, ".nojekyll"), "w").close()
    with open(os.path.join(ROOT, "netlify.toml"), "w", encoding="utf-8") as fh:
        fh.write(
            '[build]\n  publish = "."\n\n'
            '[[headers]]\n  for = "/assets/*"\n  [headers.values]\n'
            '    Cache-Control = "public, max-age=31536000, immutable"\n\n'
            '[[headers]]\n  for = "/*"\n  [headers.values]\n'
            '    X-Content-Type-Options = "nosniff"\n'
            '    Referrer-Policy = "strict-origin-when-cross-origin"\n'
        )
    # 404
    lang = "nl"
    body = pages.notfound(lang)
    html = LAYOUT.format(
        lang=lang, title="404 — " + t("nf_title", lang), description=t("nf_lede", lang),
        canonical=SITE + "/404.html", hreflang="", oglocale=OGLOCALE[lang],
        og_title="404", jsonld="{}", skip=t("skip", lang),
        header=header(lang, "home"), content=body, footer=footer(lang),
        mobilebar="", scripts="",
    )
    with open(os.path.join(ROOT, "404.html"), "w", encoding="utf-8") as fh:
        fh.write(html)


def main():
    urls = []
    for key in routes.PAGES:
        for lang in LANGS:
            urls.append(render(key, lang))
    write_root()
    write_redirects()
    write_sitemap(urls)
    write_misc()
    print("Gegenereerd: %d pagina's (%d talen), %d legacy-redirects."
          % (len(urls), len(LANGS), len(LEGACY)))


if __name__ == "__main__":
    main()
