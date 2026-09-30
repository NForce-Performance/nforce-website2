# -*- coding: utf-8 -*-
"""
Paginaopbouw. Elke pagina is een functie die een dict teruggeeft:

    {"title", "description", "content", "crumbs"?, "faq"?, "service"?, "scripts"?}

De blokken hieronder (hero, section, cards, plans, faq_block, ctaband, next_links)
zijn de bouwstenen. Nieuwe pagina: functie toevoegen met dezelfde naam als de
key in tools/routes.py, en de key in routes.PAGES zetten.

NForce relaunch NL v1 (28 Sep 2026): nieuwe home, nieuwe pagina Werkwijze,
contact in plaats van Performance Check, Return-to-Play offline, meetfouten op
de testingpagina uit assets/data/benchmarks.json (één bron).
"""

import json
import math
import os

import routes
from i18n import t, PLANS
from copy_nl import VARIABLES

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# FORMULIER-KOPPELPUNT: zet hier je Formspree-, Basin- of Netlify Forms-endpoint
# (bijvoorbeeld "https://formspree.io/f/abcdwxyz"). Leeg = het formulier opent het
# e-mailprogramma van de bezoeker met de aanvraag ingevuld (zie assets/js/site.js).
FORM_ENDPOINT = ""
CONTACT_EMAIL = "nick@nforce-performance.nl"

RINK = '<div class="rink" aria-hidden="true"></div>'

# Rinkmarkering als structuurelement in de home-hero: blauwe lijn, face-off-cirkel,
# hash marks en doellijn. Lijnen, geen decoratie; lichtblauw alleen op de blauwe lijn.
RINK_ART = """<svg class="hero__art" viewBox="0 0 480 480" fill="none" aria-hidden="true" focusable="false">
  <rect class="rk-blue" x="40" y="0" width="12" height="480"/>
  <line class="rk-line rk-faint" x1="440" y1="0" x2="440" y2="480"/>
  <circle class="rk-line" cx="280" cy="240" r="140"/>
  <circle class="rk-dot" cx="280" cy="240" r="9"/>
  <path class="rk-line" d="M262 100v-22M298 100v-22M262 380v22M298 380v22"/>
</svg>"""


# ---------------------------------------------------------------------------
# Bouwstenen
# ---------------------------------------------------------------------------

def btn(label, href, kind="primary", size=""):
    cls = "btn btn--%s" % kind + (" btn--%s" % size if size else "")
    return '<a class="%s" href="%s">%s</a>' % (cls, href, label)


def actions(*buttons):
    return '<div class="actions">%s</div>' % "".join(buttons)


def hero(lang, eyebrow, h1, lede, buttons, art=""):
    return """<section class="hero">%(rink)s
  %(art)s
  <div class="wrap hero__inner">
    <p class="eyebrow">%(eyebrow)s</p>
    <h1>%(h1)s</h1>
    <p class="lede">%(lede)s</p>
    %(actions)s
  </div>
</section>""" % {"rink": "" if art else RINK, "art": art, "eyebrow": eyebrow, "h1": h1,
                 "lede": lede, "actions": actions(*buttons)}


def hero_ice(lang, eyebrow, h1, lede, buttons):
    """Home-hero met live ijsvlak (assets/js/nf-hero.js). Zonder WebGL of bij
    prefers-reduced-motion blijft de poster (assets/img/hero-ice.jpg) staan."""
    return """<section class="hero hero--ice ice" data-ice="home" data-ice-seed="0">
  <canvas class="ice__canvas" aria-hidden="true"></canvas>
  <div class="wrap hero__inner">
    <p class="eyebrow">%(eyebrow)s</p>
    <h1>%(h1)s</h1>
    <p class="lede">%(lede)s</p>
    %(actions)s
  </div>
</section>""" % {"eyebrow": eyebrow, "h1": h1, "lede": lede, "actions": actions(*buttons)}


def rink_circle(items, center, label, scroll=False):
    """Face-offcirkel: items (titel, tekst) rond de cirkel, genummerd, met een
    lichtblauwe puck die rustig rondgaat. Rechts (of eronder) de genummerde lijst."""
    n = len(items)
    nodes, nums = [], []
    for i in range(n):
        a = math.radians(-90 + 360.0 * i / n)
        x, y = 200 + 150 * math.cos(a), 200 + 150 * math.sin(a)
        lx, ly = 200 + 181 * math.cos(a), 200 + 181 * math.sin(a)
        anchor = "middle" if abs(lx - 200) < 12 else ("start" if lx > 200 else "end")
        nodes.append('<circle class="rc-node" data-i="%d" cx="%.1f" cy="%.1f" r="5"/>' % (i, x, y))
        nums.append('<text class="rc-num" data-i="%d" x="%.1f" y="%.1f" text-anchor="%s">%02d</text>' % (i, lx, ly, anchor, i + 1))
    svg = (
        '<svg class="rc-svg" viewBox="0 0 400 400" role="img" aria-label="%s">'
        '<circle class="rc-ring" cx="200" cy="200" r="150"/>'
        '<circle class="rc-progress" cx="200" cy="200" r="150" transform="rotate(-90 200 200)"/>'
        '<path class="rc-hash" d="M50 178h-22M50 222h-22M350 178h22M350 222h22"/>'
        '%s'
        '<g class="rc-orbit"><circle class="rc-puck" cx="200" cy="50" r="7"/></g>'
        '<circle class="rc-spot" cx="200" cy="200" r="9"/>'
        '<text class="rc-center" x="200" y="236" text-anchor="middle">%s</text>'
        '%s</svg>' % (label, "".join(nodes), center, "".join(nums))
    )
    rows = "".join(
        '<li data-i="%d"><span class="rc-list__n num">%02d</span><div><b>%s</b><span>%s</span></div></li>' % (i, i + 1, title, text)
        for i, (title, text) in enumerate(items)
    )
    # scroll=True: prototype. nf-system.js lights one step at a time while the list scrolls
    # (wide screens, motion allowed); everything else sees the normal static figure.
    return '<div class="rc%s" data-n="%d"><div class="rc-figure">%s</div><ol class="rc-list">%s</ol></div>' % (
        " rc--scroll" if scroll else "", n, svg, rows)


# Pagina's zonder ijs-hero: juridische teksten, bestellen en de foutpagina blijven rustig.
PLAIN_HEROES = ("privacy", "terms", "checkout", "home")


def page_hero(lang, key, eyebrow, h1, lede, buttons=()):
    crumbs = ('<nav class="crumbs" aria-label="Breadcrumb"><a href="%s">%s</a><span>/</span>%s</nav>'
              % (routes.url("home", lang), t("nav_home", lang), t("nav_" + key, lang)))
    if key in PLAIN_HEROES:
        opener = '<section class="page-hero">' + RINK
    else:
        seed = routes.PAGES.index(key) if key in routes.PAGES else 1
        opener = ('<section class="page-hero ice" data-ice="page" data-ice-seed="%d">'
                  '<canvas class="ice__canvas" aria-hidden="true"></canvas>' % seed)
    return """%(opener)s
  <div class="wrap page-hero__inner">
    %(crumbs)s
    <p class="eyebrow">%(eyebrow)s</p>
    <h1>%(h1)s</h1>
    <p class="lede">%(lede)s</p>
    %(actions)s
  </div>
</section>""" % {"opener": opener, "crumbs": crumbs, "eyebrow": eyebrow, "h1": h1,
                 "lede": lede, "actions": actions(*buttons) if buttons else ""}


def section(inner, mod="", extra=""):
    cls = "section" + (" section--%s" % mod if mod else "")
    return '<section class="%s"%s>\n  <div class="wrap">\n%s\n  </div>\n</section>' % (cls, extra, inner)


def head(h, eyebrow=None, lede=None, center=False):
    out = '<div class="section__head%s">' % (" section__head--center" if center else "")
    if eyebrow:
        out += '<p class="eyebrow">%s</p>' % eyebrow
    out += "<h2>%s</h2>" % h
    if lede:
        out += '<p class="lede">%s</p>' % lede
    return out + "</div>"


def cards(items, cols=3):
    """items: (title, text) of (step, title, text)"""
    out = []
    for it in items:
        if len(it) == 3:
            step, title, text = it
            out.append('<article class="card"><span class="card__step">%s</span><h3>%s</h3><p>%s</p></article>'
                       % (step, title, text))
        else:
            title, text = it
            out.append('<article class="card"><h3>%s</h3><p>%s</p></article>' % (title, text))
    return '<div class="grid grid--%d">%s</div>' % (cols, "".join(out))


def linkcards(lang, items, cols=3):
    """items: (routekey, title, text, meta, cta)"""
    out = []
    for key, title, text, meta, cta in items:
        out.append(
            '<a class="card card--link" href="%s"><span class="card__step">%s</span>'
            '<h3>%s</h3><p>%s</p><span class="card__more">%s &rarr;</span></a>'
            % (routes.url(key, lang), meta, title, text, cta)
        )
    return '<div class="grid grid--%d">%s</div>' % (cols, "".join(out))


def ticks(items):
    return '<ul class="ticks">%s</ul>' % "".join("<li>%s</li>" % i for i in items)


def paras(items, lede_first=False):
    return "".join('<p class="lede">%s</p>' % p if (lede_first and i == 0) else "<p>%s</p>" % p
                   for i, p in enumerate(items))


def variables_list():
    rows = "".join(
        '<li><span class="vars__n num">%02d</span><b>%s</b><span>%s</span></li>' % (i, name, question)
        for i, (name, _what, question) in enumerate(VARIABLES, start=1)
    )
    return '<ol class="vars">%s</ol>' % rows


def plans_block(lang):
    out = []
    for p in PLANS:
        flag = ('<span class="plan__flag">%s</span>' % t("plan_recommended", lang)) if p["recommended"] else ""
        out.append(
            '<article class="plan%(feat)s">%(flag)s'
            '<h3 class="plan__name">%(name)s</h3>'
            '<p class="plan__price"><b class="num">&euro;%(price)s</b> <span>%(unit)s</span></p>'
            '<p class="plan__for">%(for)s</p>%(bullets)s'
            '<a class="btn btn--ghost btn--block" href="%(cta)s">%(cta_label)s</a>'
            '</article>' % {
                "feat": " plan--featured" if p["recommended"] else "",
                "flag": flag,
                "name": p["name"][lang],
                "price": p["price"],
                "unit": t(p["unit"], lang),
                "for": p["for"][lang],
                "bullets": ticks(p["bullets"][lang]),
                "cta": routes.url("contact", lang),
                "cta_label": t("plan_choose", lang),
            })
    return '<div class="plans">%s</div>' % "".join(out)


def table(cols, rows, num_last=True):
    thead = "".join("<th>%s</th>" % c for c in cols)
    tbody = "".join(
        "<tr>%s</tr>" % "".join(
            '<td%s>%s</td>' % (' class="num"' if (num_last and i == len(r) - 1) else "", c)
            for i, c in enumerate(r)
        ) for r in rows
    )
    return '<div class="table-wrap"><table><thead><tr>%s</tr></thead><tbody>%s</tbody></table></div>' % (thead, tbody)


def faq_block(lang, pairs):
    items = "".join(
        "<details%s><summary>%s</summary><p>%s</p></details>" % (" open" if i == 0 else "", q, a)
        for i, (q, a) in enumerate(pairs)
    )
    return head(t("faq_h", lang)) + '<div class="faq">%s</div>' % items


def ctaband(lang):
    return ('<div class="ctaband"><div><h2>%s</h2><p class="lede">%s</p></div>%s</div>' % (
        t("cta_band_h", lang), t("cta_band_p", lang),
        actions(btn(t("cta_band_b1", lang), routes.url("contact", lang), "primary", "lg"))))


def next_links(lang, items):
    """items: (routekey, kicker, text)"""
    rows = "".join(
        '<a href="%s"><small>%s</small><b>%s</b><span>%s</span></a>'
        % (routes.url(key, lang), kicker, t("nav_" + key, lang), text)
        for key, kicker, text in items
    )
    return head(t("next_h", lang)) + '<div class="next">%s</div>' % rows


def blocks(items):
    """(kop, tekst) paren als doorlopende tekst — voor privacy en voorwaarden"""
    return "".join("<h2>%s</h2><p class=\"smallprint\">%s</p>" % (h, p) for h, p in items)


# ---------------------------------------------------------------------------
# Meetfouten uit benchmarks.json — dezelfde bron als de zelftest
# ---------------------------------------------------------------------------

def _load_benchmarks():
    path = os.path.join(ROOT, "assets", "data", "benchmarks.json")
    with open(path, encoding="utf-8") as fh:
        return json.load(fh)["tests"]


def _nl_number(x):
    s = ("%g" % x)
    return s.replace(".", ",")


def error_cell(test_id, lang):
    test = _load_benchmarks().get(test_id, {})
    err = test.get("error")
    note = (test.get("errorNote") or {}).get(lang) or (test.get("errorNote") or {}).get("nl") or ""
    if err is None:
        return "Niet gepubliceerd" if lang == "nl" else "Not published"
    unit = test.get("unit", "")
    unit = "" if "lichaamsgewicht" in unit else " " + unit
    cell = "&plusmn;%s%s" % (_nl_number(err) if lang == "nl" else "%g" % err, unit)
    if "geschat" in note.lower():
        cell += " (geschat)"
    return cell


# ---------------------------------------------------------------------------
# Pagina's
# ---------------------------------------------------------------------------

def home(lang):
    hockey = (
        '<div class="split"><div>%s%s</div><div>%s</div></div>'
        % (head(t("home_hockey_h", lang), t("home_hockey_eyebrow", lang)),
           paras(t("home_hockey_p", lang)), ticks(t("home_hockey_ticks", lang)))
    )
    content = (
        hero_ice(lang, t("home_eyebrow", lang), t("home_h1", lang), t("home_lede", lang),
                 (btn(t("home_cta1", lang), routes.url("contact", lang), "primary", "lg"),
                  btn(t("home_cta2", lang), routes.url("method", lang), "ghost", "lg")))
        + section(head(t("home_what_h", lang), t("home_what_eyebrow", lang))
                  + cards(t("home_what", lang), 3))
        + section(head(t("home_vars_h", lang), t("home_vars_eyebrow", lang), t("home_vars_lede", lang))
                  + rink_circle([(name, question) for name, _what, question in VARIABLES],
                                t("home_vars_center", lang), t("home_vars_h", lang), scroll=True)
                  + '<p class="vars__note">%s</p>' % t("home_vars_note", lang)
                  + actions(btn(t("home_vars_cta", lang), routes.url("method", lang), "ghost")), "panel")
        + section(head(t("home_paths_h", lang), t("home_paths_eyebrow", lang))
                  + linkcards(lang, t("home_paths", lang), 3))
        + section(hockey, "panel")
        + section(head(t("home_why_h", lang), t("home_why_eyebrow", lang)) + cards(t("home_why", lang), 4))
        + section(faq_block(lang, t("home_faq", lang)), "tight")
        + section(ctaband(lang))
    )
    return {
        "title": t("home_title", lang),
        "description": t("home_desc", lang),
        "content": content,
        "faq": t("home_faq", lang),
    }


def method(lang):
    var_rows = [(name, what, question) for name, what, question in VARIABLES]
    content = (
        page_hero(lang, "method", t("me_eyebrow", lang), t("me_h1", lang), t("me_lede", lang))
        + section(head(t("me_loop_h", lang))
                  + rink_circle([(title, text) for _n, title, text in t("me_loop", lang)],
                                t("me_loop_center", lang), t("me_loop_h", lang), scroll=True))
        + section(head(t("me_vars_h", lang), None, t("me_vars_lede", lang))
                  + table(t("me_vars_cols", lang), var_rows, num_last=False), "panel")
        + section('<div class="split"><div>%s%s</div><div class="card card--quiet"><h3>%s</h3>%s</div></div>' % (
            head(t("me_hub_h", lang), t("me_hub_eyebrow", lang)), paras(t("me_hub_p", lang)),
            t("me_load_h", lang), ticks(t("me_load", lang))))
        + section(next_links(lang, (
            ("teams", "01", t("tm_h1", lang)),
            ("coaching", "02", t("co_h1", lang)),
            ("testing", "03", t("te_h1", lang)),
        )), "tight")
        + section(ctaband(lang))
    )
    return {"title": t("me_title", lang), "description": t("me_desc", lang), "content": content,
            "crumbs": ["method"]}


def coaching(lang):
    content = (
        page_hero(lang, "coaching", t("co_eyebrow", lang), t("co_h1", lang), t("co_lede", lang),
                  (btn(t("cta_label", lang), routes.url("contact", lang), "primary"),))
        + section('<div class="split"><div>%s%s</div><div class="card card--quiet"><span class="card__step">%s</span><h3>%s</h3><p>%s</p></div></div>' % (
            head(t("co_h2_incl", lang)), ticks(t("co_incl", lang)),
            t("co_limit_step", lang), t("co_limit_h", lang), t("co_limit_p", lang)))
        + section(head(t("co_h2_flow", lang)) + cards(t("co_flow", lang), 4), "panel")
        + section(head(t("plans_h", lang), None, t("plans_lede", lang)) + plans_block(lang))
        + section(faq_block(lang, t("co_faq", lang)), "tight")
        + section(next_links(lang, (
            ("method", "01", t("me_h1", lang)),
            ("handbooks", "02", t("hb_h1", lang)),
            ("pricing", "03", t("pr_h1", lang)),
        )) + '<div class="mt-6">%s</div>' % ctaband(lang))
    )
    return {"title": t("co_title", lang), "description": t("co_desc", lang), "content": content,
            "crumbs": ["coaching"], "faq": t("co_faq", lang),
            "service": {"name": "Individuele coaching (online)",
                        "serviceType": "Sport performance coaching",
                        "areaServed": "NL",
                        "offers": {"@type": "Offer", "price": "49", "priceCurrency": "EUR",
                                   "description": "Vanaf 49 euro per maand, inclusief btw"}}}


def teams(lang):
    content = (
        page_hero(lang, "teams", t("tm_eyebrow", lang), t("tm_h1", lang), t("tm_lede", lang),
                  (btn(t("cta_label", lang), routes.url("contact", lang), "primary"),))
        + section(head(t("tm_h2", lang)) + cards(t("tm_items", lang), 3))
        + section('<div class="split"><div>%s%s</div><div>%s<p class="lede">%s</p></div></div>' % (
            head(t("tm_how_h", lang)), ticks(t("tm_how", lang)),
            head(t("tm_price_h", lang)), t("tm_price_p", lang)), "panel")
        + section(faq_block(lang, t("tm_faq", lang)), "tight")
        + section(ctaband(lang))
    )
    return {"title": t("tm_title", lang), "description": t("tm_desc", lang), "content": content,
            "crumbs": ["teams"], "faq": t("tm_faq", lang),
            "service": {"name": "Teamtestdag en seizoenslijn",
                        "serviceType": "Sports performance testing",
                        "offers": {"@type": "Offer", "price": "750", "priceCurrency": "EUR",
                                   "description": "Vanaf 750 euro per testdag, exclusief btw"}}}


def testing(lang):
    rows = [(name, quality, what, error_cell(test_id, lang))
            for name, quality, what, test_id in t("te_rows", lang)]
    content = (
        page_hero(lang, "testing", t("te_eyebrow", lang), t("te_h1", lang), t("te_lede", lang))
        + section(head(t("te_table_h", lang)) + table(t("te_cols", lang), rows)
                  + '<p class="smallprint mt-4">%s</p>' % t("te_table_note", lang))
        + section(head(t("te_how_h", lang)) + ticks(t("te_how", lang))
                  + '<p class="smallprint mt-6">%s</p>' % t("proof_note", lang), "panel")
        + section('<div class="ctaband"><div><h2>%s</h2><p class="lede">%s</p></div>%s</div>' % (
            t("te_cta_h", lang), t("te_cta_p", lang),
            actions(btn(t("bar_selftest", lang), routes.url("selftest", lang), "ghost", "lg"))))
        + section(next_links(lang, (
            ("method", "01", t("me_h1", lang)),
            ("teams", "02", t("tm_h1", lang)),
            ("contact", "03", t("ct_h1", lang)),
        )), "tight")
    )
    return {"title": t("te_title", lang), "description": t("te_desc", lang), "content": content,
            "crumbs": ["testing"]}


def selftest(lang):
    content = (
        page_hero(lang, "selftest", t("st_eyebrow", lang), t("st_h1", lang), t("st_lede", lang))
        + section(cards(t("st_howto", lang), 3), "tight")
        + section('<div id="st-app"></div>')
        + section(next_links(lang, (
            ("handbooks", "01", t("hb_h1", lang)),
            ("testing", "02", t("te_how_h", lang)),
            ("coaching", "03", t("co_h1", lang)),
        )) + '<div class="mt-6">%s</div>' % ctaband(lang), "panel")
    )
    return {"title": t("st_title", lang), "description": t("st_desc", lang), "content": content,
            "crumbs": ["selftest"],
            "scripts": '<script src="/assets/js/nf-selftest.js" defer></script>'}


def handbooks(lang):
    content = (
        page_hero(lang, "handbooks", t("hb_eyebrow", lang), t("hb_h1", lang), t("hb_lede", lang),
                  (btn(t("bar_selftest", lang), routes.url("selftest", lang), "ghost"),))
        + section('<p class="notice mb-6">%s</p><div id="hb-app"></div>' % t("hb_notice", lang))
        + section(head(t("hb_core_pro_h", lang)) + cards(t("hb_core_pro", lang), 2)
                  + '<div class="mt-6">%s</div>' % (head(t("hb_flow_h", lang)) + cards(t("hb_flow", lang), 3)), "panel")
        + section(faq_block(lang, t("hb_faq", lang)), "tight")
        + section(ctaband(lang))
    )
    return {"title": t("hb_title", lang), "description": t("hb_desc", lang), "content": content,
            "crumbs": ["handbooks"], "faq": t("hb_faq", lang),
            "scripts": '<script src="/assets/js/nf-handbooks.js" defer></script>'}


def checkout(lang):
    content = (
        page_hero(lang, "checkout", t("ck_eyebrow", lang), t("ck_h1", lang), t("ck_lede", lang))
        + section('<div id="co-app"></div>')
    )
    return {"title": t("ck_title", lang), "description": t("ck_desc", lang), "content": content,
            "crumbs": ["handbooks", "checkout"],
            "scripts": '<script src="/assets/js/nf-checkout.js" defer></script>'}


def pricing(lang):
    content = (
        page_hero(lang, "pricing", t("pr_eyebrow", lang), t("pr_h1", lang), t("pr_lede", lang))
        + section(head(t("plans_h", lang), None, t("plans_lede", lang)) + plans_block(lang))
        + section('<div class="split"><div>%s<p class="lede">%s</p>%s</div><div>%s<p class="lede">%s</p>%s</div></div>' % (
            head(t("pr_hb_h", lang)), t("pr_hb_p", lang),
            actions(btn(t("home_hb_cta", lang), routes.url("handbooks", lang), "ghost")),
            head(t("pr_teams_h", lang)), t("tm_price_p", lang),
            actions(btn(t("pr_teams_cta", lang), routes.url("teams", lang), "ghost"))), "panel")
        + section(faq_block(lang, t("pr_faq", lang)), "tight")
        + section(ctaband(lang))
    )
    return {"title": t("pr_title", lang), "description": t("pr_desc", lang), "content": content,
            "crumbs": ["pricing"], "faq": t("pr_faq", lang)}


def about(lang):
    body = t("ab_body", lang)
    content = (
        page_hero(lang, "about", t("ab_eyebrow", lang), t("ab_h1", lang), body[0])
        + section('<div class="split"><div>%s</div><div class="card card--quiet"><span class="card__step">%s</span>'
                  '<h3>Nick Bergman</h3><p>%s</p>'
                  '<p><a href="mailto:%s">%s</a><br>'
                  '<a class="num" href="tel:+31622680892">+31 6 22 68 08 92</a></p>%s</div></div>'
                  % (paras(body[1:]), t("ab_card_step", lang), t("ab_card_role", lang),
                     CONTACT_EMAIL, CONTACT_EMAIL,
                     btn(t("cta_label", lang), routes.url("contact", lang), "primary", "sm")))
        + section(head(t("ab_principles_h", lang)) + cards(t("ab_principles", lang), 4), "panel")
        + section(ctaband(lang))
    )
    return {"title": t("ab_title", lang), "description": t("ab_desc", lang), "content": content,
            "crumbs": ["about"]}


def contact(lang):
    if FORM_ENDPOINT:
        form_open = '<form class="card" action="%s" method="post">' % FORM_ENDPOINT
        mail_note = ""
    else:
        form_open = ('<form class="card" action="#" method="post" data-mailto="%s" data-subject="%s">'
                     % (CONTACT_EMAIL, "Aanvraag via nforce-performance.nl"))
        mail_note = '<p class="faint">%s</p>' % t("ct_f_mailto_note", lang)
    form = (
        form_open
        + '<h3>%s</h3>'
        '<div class="field"><label for="cf-name">%s</label><input id="cf-name" name="naam" data-label="%s" type="text" required autocomplete="name"></div>'
        '<div class="field"><label for="cf-mail">%s</label><input id="cf-mail" name="email" data-label="%s" type="email" required autocomplete="email"></div>'
        '<div class="field"><label for="cf-sport">%s</label><input id="cf-sport" name="sport" data-label="%s" type="text" required></div>'
        '<div class="field"><label for="cf-goal">%s</label><textarea id="cf-goal" name="bericht" data-label="%s" rows="5" required></textarea></div>'
        '<button class="btn btn--primary btn--block" type="submit">%s</button>'
        '<p class="faint">%s</p>%s</form>'
        % (t("ct_form_h", lang),
           t("ct_f_name", lang), t("ct_f_name", lang),
           t("ct_f_email", lang), t("ct_f_email", lang),
           t("ct_f_sport", lang), t("ct_f_sport", lang),
           t("ct_f_goal", lang), t("ct_f_goal", lang),
           t("ct_f_send", lang), t("ct_f_note", lang), mail_note)
    )
    aside = (
        '<div class="card card--quiet"><h3>%s</h3><p>%s</p>'
        '<p><a href="https://wa.me/31622680892" rel="noopener">WhatsApp</a> &middot; '
        '<a class="num" href="tel:+31622680892">+31 6 22 68 08 92</a> &middot; '
        '<a href="mailto:%s">%s</a></p></div>'
        # AGENDA-KOPPELPUNT: plak hier je Cal.com- of Calendly-embed als je
        # bezoekers direct een moment wilt laten kiezen. Zie README.
        % (t("ct_direct_h", lang), t("ct_direct_p", lang), CONTACT_EMAIL, CONTACT_EMAIL)
    )
    content = (
        page_hero(lang, "contact", t("ct_eyebrow", lang), t("ct_h1", lang), t("ct_lede", lang))
        + section(head(t("ct_steps_h", lang)) + cards(t("ct_steps", lang), 3), "tight")
        + section('<div class="split"><div>%s</div><div>%s</div></div>' % (form, aside))
    )
    return {"title": t("ct_title", lang), "description": t("ct_desc", lang), "content": content,
            "crumbs": ["contact"]}


def privacy(lang):
    content = (
        page_hero(lang, "privacy", t("nav_privacy", lang), t("pv_h1", lang), t("pv_lede", lang))
        + section('<div class="narrow">%s</div>' % blocks(t("pv_blocks", lang)))
    )
    return {"title": t("pv_title", lang), "description": t("pv_desc", lang), "content": content,
            "crumbs": ["privacy"]}


def terms(lang):
    content = (
        page_hero(lang, "terms", t("nav_terms", lang), t("tc_h1", lang), t("tc_lede", lang))
        + section('<div class="narrow">%s</div>' % blocks(t("tc_blocks", lang)))
    )
    return {"title": t("tc_title", lang), "description": t("tc_desc", lang), "content": content,
            "crumbs": ["terms"]}


def notfound(lang):
    return (
        page_hero(lang, "home", "404", t("nf_title", lang), t("nf_lede", lang))
        + section(next_links(lang, (
            ("method", "01", t("me_h1", lang)),
            ("teams", "02", t("tm_h1", lang)),
            ("coaching", "03", t("co_h1", lang)),
            ("contact", "04", t("ct_h1", lang)),
        )))
    )


BUILDERS = {
    "home": home, "method": method, "coaching": coaching, "teams": teams, "testing": testing,
    "selftest": selftest, "handbooks": handbooks, "checkout": checkout,
    "pricing": pricing, "about": about, "contact": contact,
    "privacy": privacy, "terms": terms,
}


def build(key, lang):
    return BUILDERS[key](lang)
