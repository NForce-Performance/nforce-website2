# -*- coding: utf-8 -*-
"""
URL-structuur van de site — één plek voor alle paden.

Nieuwe pagina toevoegen:
  1. voeg een key toe aan SLUGS met de slug per taal
  2. zet de key in PAGES (en in NAV als hij in het hoofdmenu moet)
  3. maak een builder met dezelfde naam in tools/pages.py
"""

LANGS = ("nl", "en", "de")

SLUGS = {
    "home":      {"nl": "",                 "en": "",                 "de": ""},
    "method":    {"nl": "werkwijze",        "en": "method",           "de": "methode"},
    "coaching":  {"nl": "online-coaching",  "en": "online-coaching",  "de": "online-coaching"},
    "teams":     {"nl": "teams",            "en": "teams",            "de": "teams"},
    "testing":   {"nl": "testing",          "en": "testing",          "de": "testing"},
    "selftest":  {"nl": "zelftest",         "en": "self-test",        "de": "selbsttest"},
    "handbooks": {"nl": "handboeken",       "en": "handbooks",        "de": "handbuecher"},
    "checkout":  {"nl": "bestellen",        "en": "checkout",         "de": "kasse"},
    "pricing":   {"nl": "tarieven",         "en": "pricing",          "de": "preise"},
    "about":     {"nl": "over",             "en": "about",            "de": "ueber"},
    "contact":   {"nl": "contact",          "en": "contact",          "de": "kontakt"},
    "privacy":   {"nl": "privacy",          "en": "privacy",          "de": "datenschutz"},
    "terms":     {"nl": "voorwaarden",      "en": "terms",            "de": "agb"},
}

# volgorde in sitemap en build
PAGES = ("home", "method", "teams", "coaching", "handbooks", "testing", "selftest",
         "pricing", "about", "contact", "checkout", "privacy", "terms")

# hoofdmenu
NAV = ("method", "teams", "coaching", "handbooks", "about")

# oude slugs die na de relaunch doorverwijzen (per taal): key -> oude slug
OLD_SLUGS = {"contact": "performance-check"}


def url(key, lang):
    slug = SLUGS[key][lang]
    return "/%s/" % lang if not slug else "/%s/%s/" % (lang, slug)
