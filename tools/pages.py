# -*- coding: utf-8 -*-
"""
Paginaopbouw. Elke pagina is een functie die een dict teruggeeft:

    {"title", "description", "content", "crumbs"?, "faq"?, "service"?, "scripts"?}

De blokken hieronder (hero, section, cards, plans, faq_block, ctaband, next_links)
zijn de bouwstenen. Nieuwe pagina: functie toevoegen met dezelfde naam als de
key in tools/routes.py, en de key in routes.PAGES zetten.
"""

import routes
from i18n import t, PLANS

RINK = ('<div class="rink" aria-hidden="true"></div>')


# ---------------------------------------------------------------------------
# Bouwstenen
# ---------------------------------------------------------------------------

def btn(label, href, kind="primary", size=""):
    cls = "btn btn--%s" % kind + (" btn--%s" % size if size else "")
    return '<a class="%s" href="%s">%s</a>' % (cls, href, label)


def actions(*buttons):
    return '<div class="actions">%s</div>' % "".join(buttons)


def hero(lang, eyebrow, h1, lede, buttons, stats=None):
    proof = ""
    if stats:
        proof = '<div class="hero__proof">%s</div>' % "".join(
            '<div><b class="num">%s</b><span>%s</span></div>' % (v, l) for v, l in stats
        )
    return """<section class="hero">%(rink)s
  <div class="wrap hero__inner">
    <p class="eyebrow">%(eyebrow)s</p>
    <h1>%(h1)s</h1>
    <p class="lede">%(lede)s</p>
    %(actions)s
    %(proof)s
  </div>
</section>""" % {"rink": RINK, "eyebrow": eyebrow, "h1": h1, "lede": lede,
                 "actions": actions(*buttons), "proof": proof}


def page_hero(lang, key, eyebrow, h1, lede, buttons=()):
    crumbs = ('<nav class="crumbs" aria-label="Breadcrumb"><a href="%s">%s</a><span>/</span>%s</nav>'
              % (routes.url("home", lang), t("nav_home", lang), t("nav_" + key, lang)))
    return """<section class="page-hero">%(rink)s
  <div class="wrap page-hero__inner">
    %(crumbs)s
    <p class="eyebrow">%(eyebrow)s</p>
    <h1>%(h1)s</h1>
    <p class="lede">%(lede)s</p>
    %(actions)s
  </div>
</section>""" % {"rink": RINK, "crumbs": crumbs, "eyebrow": eyebrow, "h1": h1,
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
            out.append('<article class="card reveal"><span class="card__step">%s</span><h3>%s</h3><p>%s</p></article>'
                        % (step, title, text))
        else:
            title, text = it
            out.append('<article class="card reveal"><h3>%s</h3><p>%s</p></article>' % (title, text))
    return '<div class="grid grid--%d">%s</div>' % (cols, "".join(out))


def linkcards(lang, items):
    """items: (routekey, title, text, meta, cta)"""
    out = []
    for key, title, text, meta, cta in items:
        out.append(
            '<a class="card card--link reveal" href="%s"><span class="card__step">%s</span>'
            '<h3>%s</h3><p>%s</p><span class="card__more">%s &rarr;</span></a>'
            % (routes.url(key, lang), meta, title, text, cta)
        )
    return '<div class="grid grid--2">%s</div>' % "".join(out)


def ticks(items):
    return '<ul class="ticks">%s</ul>' % "".join("<li>%s</li>" % i for i in items)


def plans_block(lang):
    out = []
    for p in PLANS:
        flag = ('<span class="plan__flag">%s</span>' % t("plan_recommended", lang)) if p["recommended"] else ""
        out.append(
            '<article class="plan%(feat)s reveal">%(flag)s'
            '<h3 class="plan__name">%(name)s</h3>'
            '<p class="plan__price"><b class="num">&euro;%(price)s</b> <span>%(unit)s</span></p>'
            '<p class="plan__for">%(for)s</p>%(bullets)s'
            '<a class="btn btn--%(kind)s btn--block" href="%(cta)s">%(cta_label)s</a>'
            '</article>' % {
                "feat": " plan--featured" if p["recommended"] else "",
                "flag": flag,
                "name": p["name"][lang],
                "price": p["price"],
                "unit": t(p["unit"], lang),
                "for": p["for"][lang],
                "bullets": ticks(p["bullets"][lang]),
                "kind": "primary" if p["recommended"] else "ghost",
                "cta": routes.url("contact", lang),
                "cta_label": t("plan_choose", lang),
            })
    return '<div class="plans">%s</div>' % "".join(out)


def table(cols, rows):
    thead = "".join("<th>%s</th>" % c for c in cols)
    tbody = "".join(
        "<tr>%s</tr>" % "".join(
            '<td%s>%s</td>' % (' class="num"' if i == len(r) - 1 else "", c) for i, c in enumerate(r)
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
    return ('<div class="ctaband reveal"><h2>%s</h2><p class="lede">%s</p>%s</div>' % (
        t("cta_band_h", lang), t("cta_band_p", lang),
        actions(btn(t("cta_band_b1", lang), routes.url("contact", lang), "primary", "lg"),
                btn(t("cta_band_b2", lang), routes.url("selftest", lang), "ghost"))))


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
# Pagina's
# ---------------------------------------------------------------------------

def home(lang):
    content = (
        hero(lang, t("home_eyebrow", lang), t("home_h1", lang), t("home_lede", lang),
             (btn(t("home_cta1", lang), routes.url("selftest", lang), "primary", "lg"),
              btn(t("home_cta2", lang), routes.url("coaching", lang), "ghost")),
             t("home_stats", lang))
        + section(head(t("home_paths_h", lang), t("home_paths_eyebrow", lang))
                  + linkcards(lang, t("home_paths", lang)))
        + section(head(t("home_method_h", lang), t("home_method_eyebrow", lang))
                  + cards(t("home_method", lang), 3)
                  + '<p class="smallprint mt-6">%s</p>' % t("proof_note", lang), "panel")
        + section(head(t("home_hb_h", lang), t("home_hb_eyebrow", lang), t("home_hb_lede", lang))
                  + '<div class="hb-grid" id="hb-featured"></div>'
                  + actions(btn(t("home_hb_cta", lang), routes.url("handbooks", lang), "ghost")))
        + '<div class="wrap"><div class="blueline"></div></div>'
        + section(head(t("home_why_h", lang)) + cards(t("home_why", lang), 3))
        + section(faq_block(lang, t("home_faq", lang)), "tight")
        + section(ctaband(lang))
    )
    return {
        "title": t("home_title", lang),
        "description": t("home_desc", lang),
        "content": content,
        "faq": t("home_faq", lang),
        "scripts": '<script src="/assets/js/nf-featured.js" defer></script>',
    }


def coaching(lang):
    content = (
        page_hero(lang, "coaching", t("co_eyebrow", lang), t("co_h1", lang), t("co_lede", lang),
                  (btn(t("cta_label", lang), routes.url("contact", lang), "primary"),
                   btn(t("cta_band_b2", lang), routes.url("selftest", lang), "ghost")))
        + section('<div class="split"><div>%s%s</div><div class="card">%s<h3>%s</h3><p>%s</p>%s</div></div>' % (
            head(t("co_h2_incl", lang)), ticks(t("co_incl", lang)),
            '<span class="card__step">RTP</span>', t("co_rtp_h", lang), t("co_rtp_p", lang),
            btn(t("plan_choose", lang), routes.url("contact", lang), "ghost", "sm")))
        + section(head(t("co_h2_flow", lang)) + cards(t("co_flow", lang), 4), "panel")
        + section(head(t("plans_h", lang), None, t("plans_lede", lang)) + plans_block(lang))
        + section(faq_block(lang, t("co_faq", lang)), "tight")
        + section(next_links(lang, (
            ("selftest", "01", t("bar_selftest", lang)),
            ("handbooks", "02", t("home_hb_cta", lang)),
            ("pricing", "03", t("pr_h1", lang)),
        )) + '<div class="mt-6">%s</div>' % ctaband(lang))
    )
    return {"title": t("co_title", lang), "description": t("co_desc", lang), "content": content,
            "crumbs": ["coaching"], "faq": t("co_faq", lang),
            "service": {"name": "Online strength & conditioning coaching",
                        "serviceType": "Personal training online",
                        "areaServed": "NL, BE, DE",
                        "offers": {"@type": "Offer", "price": "49", "priceCurrency": "EUR",
                                   "description": "Vanaf 49 euro per maand, inclusief btw"}}}


def teams(lang):
    content = (
        page_hero(lang, "teams", t("tm_eyebrow", lang), t("tm_h1", lang), t("tm_lede", lang),
                  (btn(t("cta_label", lang), routes.url("contact", lang), "primary"),))
        + section(head(t("tm_h2", lang)) + cards(t("tm_items", lang), 3))
        + section('<div class="split"><div>%s<p class="lede">%s</p></div><div class="card">%s<h3>%s</h3><p>%s</p>%s</div></div>' % (
            head(t("tm_price_h", lang)), t("tm_price_p", lang),
            '<span class="card__step">01</span>', t("te_cta_h", lang), t("te_cta_p", lang),
            btn(t("bar_selftest", lang), routes.url("selftest", lang), "ghost", "sm")), "panel")
        + section(faq_block(lang, t("tm_faq", lang)), "tight")
        + section(ctaband(lang))
    )
    return {"title": t("tm_title", lang), "description": t("tm_desc", lang), "content": content,
            "crumbs": ["teams"], "faq": t("tm_faq", lang),
            "service": {"name": "Team testing en seizoensplanning",
                        "serviceType": "Sports performance testing",
                        "offers": {"@type": "Offer", "price": "750", "priceCurrency": "EUR",
                                   "description": "Vanaf 750 euro per testdag, exclusief btw"}}}


def testing(lang):
    content = (
        page_hero(lang, "testing", t("te_eyebrow", lang), t("te_h1", lang), t("te_lede", lang),
                  (btn(t("bar_selftest", lang), routes.url("selftest", lang), "primary"),))
        + section(head(t("te_table_h", lang)) + table(t("te_cols", lang), t("te_rows", lang)))
        + section(head(t("te_how_h", lang)) + ticks(t("te_how", lang))
                  + '<p class="smallprint mt-6">%s</p>' % t("proof_note", lang), "panel")
        + section('<div class="ctaband reveal"><h2>%s</h2><p class="lede">%s</p>%s</div>' % (
            t("te_cta_h", lang), t("te_cta_p", lang),
            actions(btn(t("bar_selftest", lang), routes.url("selftest", lang), "primary", "lg"),
                    btn(t("home_hb_cta", lang), routes.url("handbooks", lang), "ghost"))))
        + section(next_links(lang, (
            ("teams", "01", t("tm_h1", lang)),
            ("coaching", "02", t("co_h1", lang)),
            ("contact", "03", t("cta_band_b1", lang)),
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
        + section('<div id="hb-app"></div>')
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
            actions(btn(t("nav_teams", lang), routes.url("teams", lang), "ghost"))), "panel")
        + section(faq_block(lang, t("pr_faq", lang)), "tight")
        + section(ctaband(lang))
    )
    return {"title": t("pr_title", lang), "description": t("pr_desc", lang), "content": content,
            "crumbs": ["pricing"], "faq": t("pr_faq", lang)}


def about(lang):
    body = "".join('<p class="lede">%s</p>' % p if i == 0 else "<p>%s</p>" % p
                   for i, p in enumerate(t("ab_body", lang)))
    content = (
        page_hero(lang, "about", t("ab_eyebrow", lang), t("ab_h1", lang), t("ab_body", lang)[0])
        + section('<div class="split"><div>%s</div><div class="card"><span class="card__step">N-FORCE</span>'
                  '<h3>Nick Bergman</h3><p>Tilburg &middot; Fontys Sporthogeschool</p>'
                  '<p><a href="mailto:nick@nforce-performance.nl">nick@nforce-performance.nl</a><br>'
                  '<a class="num" href="tel:+31622680892">+31 6 22 68 08 92</a></p>%s</div></div>'
                  % ("".join("<p>%s</p>" % p for p in t("ab_body", lang)[1:]),
                     btn(t("cta_band_b1", lang), routes.url("contact", lang), "primary", "sm")))
        + section(head(t("ab_principles_h", lang)) + cards(t("ab_principles", lang), 4), "panel")
        + section(ctaband(lang))
    )
    return {"title": t("ab_title", lang), "description": t("ab_desc", lang), "content": content,
            "crumbs": ["about"]}


def contact(lang):
    # FORMULIER-KOPPELPUNT: vervang de action door je eigen Formspree-, Basin-
    # of Netlify Forms-endpoint. Zie README, sectie "Formulier koppelen".
    form = (
        '<form class="card" action="https://formspree.io/f/JOUW-FORM-ID" method="post">'
        '<h3>%s</h3>'
        '<div class="field"><label for="cf-name">%s</label><input id="cf-name" name="naam" type="text" required autocomplete="name"></div>'
        '<div class="field"><label for="cf-mail">%s</label><input id="cf-mail" name="email" type="email" required autocomplete="email"></div>'
        '<div class="field"><label for="cf-sport">%s</label><input id="cf-sport" name="sport" type="text" required></div>'
        '<div class="field"><label for="cf-goal">%s</label><textarea id="cf-goal" name="bericht" rows="5" required></textarea></div>'
        '<button class="btn btn--primary btn--block" type="submit">%s</button>'
        '<p class="faint">%s</p></form>'
        % (t("ct_form_h", lang), t("ct_f_name", lang), t("ct_f_email", lang),
           t("ct_f_sport", lang), t("ct_f_goal", lang), t("ct_f_send", lang), t("ct_f_note", lang))
    )
    aside = (
        '<div class="card"><span class="card__step">01</span><h3>%s</h3><p>%s</p>'
        '<p><a href="https://wa.me/31622680892" rel="noopener">WhatsApp</a> &middot; '
        '<a class="num" href="tel:+31622680892">+31 6 22 68 08 92</a> &middot; '
        '<a href="mailto:nick@nforce-performance.nl">E-mail</a></p></div>'
        # AGENDA-KOPPELPUNT: plak hier je Cal.com- of Calendly-embed als je
        # bezoekers direct een slot wilt laten kiezen. Zie README.
        % (t("ct_direct_h", lang), t("ct_direct_p", lang))
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
            ("selftest", "01", t("st_h1", lang)),
            ("handbooks", "02", t("hb_h1", lang)),
            ("coaching", "03", t("co_h1", lang)),
            ("contact", "04", t("ct_h1", lang)),
        )))
    )


BUILDERS = {
    "home": home, "coaching": coaching, "teams": teams, "testing": testing,
    "selftest": selftest, "handbooks": handbooks, "checkout": checkout,
    "pricing": pricing, "about": about, "contact": contact,
    "privacy": privacy, "terms": terms,
}


def build(key, lang):
    return BUILDERS[key](lang)
