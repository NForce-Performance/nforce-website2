# NForce — website

> **Relaunch NL v1 (28 Sep 2026) — CONCEPT, wacht op akkoord van Nick.**
> Branch `website-relaunch-nl-v1`. Niets hiervan gaat live zonder expliciet akkoord.
>
> Wat er veranderd is, in het kort:
>
> 1. **Positionering** volgt de goedgekeurde Performance DNA v1: sport performance
>    voor serieuze sporters en teams, ijshockey voorop. Nieuwe pagina *Werkwijze*.
> 2. **Naam** overal *NForce* (Brand Style Guide v1). *Performance Check* heet nu
>    *Contact* (`/nl/contact/`); de oude URL verwijst door.
> 3. **Return-to-Play (€249) staat offline** tot er een medische afstemming ligt.
>    Oude losse pagina's (`/nl/online-coaching/return-to-play/`, `/nl/resultaten/…`)
>    verwijzen door.
> 4. **Alleen NL live** (`LIVE_LANGS` in `tools/build.py`). `/en/` en `/de/`
>    verwijzen tijdelijk naar NL tot de vertaling is goedgekeurd.
> 5. **Alle NL-copy staat in `tools/copy_nl.py`.** EN/DE-teksten in `i18n.py` en
>    `i18n_pages.py` zijn ongewijzigd en worden later vertaald.
> 6. **Huisstijl**: puur zwart/wit, lichtblauw alleen als accent, één lettertype
>    (Archivo, 400 en 700) tot het NForce-lettertype is gekozen. Geen verlopen,
>    schaduwen of scroll-animaties.
> 7. **Fixes**: contactformulier had een placeholder-endpoint (`JOUW-FORM-ID`) en
>    verstuurde niets — nu e-mailfallback tot `FORM_ENDPOINT` in `tools/pages.py`
>    is gezet; "null weken" bij Season Foundations; meetfouten op de testingpagina
>    komen nu uit `assets/data/benchmarks.json` (zelfde bron als de zelftest);
>    onjuiste claim "handboeken in NL, EN en DE" verwijderd; webshop-teksten
>    zeggen nu eerlijk dat bestellen nog niet kan.
>
> 8. **Logo** (aangeleverd door Nick, 28 Sep 2026) gevectoriseerd naar
>    `assets/img/`: `nforce-logo-wit.svg` / `-zwart.svg` (volledig logo),
>    `nforce-mark-wit.svg` / `-zwart.svg` (NF-beeldmerk), `favicon.svg`,
>    `apple-touch-icon.png` en `og-nforce.png` (deelafbeelding 1200 × 630).
>    Header: beeldmerk. Footer: volledig logo. De oude `nf-monogram*`-bestanden
>    worden niet meer gebruikt.
>
> 9. **Grafische laag**: de home-hero is een live ijsvlak in WebGL
>    (`assets/js/nf-hero.js`) met blauwe lijn, face-offcirkel en arenalicht;
>    `assets/img/hero-ice.jpg` is de poster voor browsers zonder WebGL en bij
>    *reduced motion*. Systeem (home) en coachingcyclus (werkwijze) staan in een
>    face-offcirkel met een langzaam draaiende puck (`rink_circle` in
>    `tools/pages.py`). Dit wijkt af van Brand Style Guide v1 §6 en §8 (geen
>    toegepaste effecten) en vraagt een expliciet akkoord van Nick.
>
> **Naam en merk:** de merknaam is *NForce* (Brand Style Guide v1, Decision Log
> D-001). Een merkenonderzoek naar "NForce" is nog niet gedaan — zie de open
> vragen in het relaunchdocument in het NForce-project.

Statische site (HTML/CSS/JS) met een kleine Python-generator. Geen build-tools, geen npm, geen framework.
Drie talen: **NL (standaard), EN, DE**. Handboeken, zelftest en aanbevelingslogica zitten in **data**, niet in code.

---

## 1. Snel starten

```bash
python3 tools/make_handbooks.py # genereert de catalogus + aanbevelingslogica
python3 tools/build.py          # genereert alle pagina's
npx serve . -l 3100             # lokaal bekijken op http://localhost:3100
```

`tools/build.py` is idempotent: je mag het zo vaak draaien als je wilt. Alles wat het genereert wordt overschreven.

---

## 2. Mappenstructuur

```
index.html              taal-dispatcher (stuurt door naar /nl/, /en/ of /de/)
404.html                gegenereerd
nl/ en/ de/             gegenereerde pagina's (NIET met de hand aanpassen)
assets/
  css/site.css          alle styling (handmatig, wordt niet gegenereerd)
  js/
    nf-core.js          data laden, winkelwagen, teaser-modal, prijzen, cards
    nf-handbooks.js     handboekenpagina + filters
    nf-selftest.js      zelftest, benchmarks, rule engine, aanbevelingen
    nf-featured.js      uitgelichte handboeken op de homepage
    nf-checkout.js      besteloverzicht + checkout
    site.js             navigatie, taalwisselaar, scroll-animaties
  data/
    handbooks.json      GEGENEREERD — bewerk tools/make_handbooks.py
    benchmarks.json     testnormen per sport/geslacht/niveau
    rules.json          GEGENEREERD — bewerk tools/make_handbooks.py
    i18n.json           UI-teksten voor de JavaScript
  img/favicon.svg
tools/
  build.py              generator (layout, header/footer, SEO, sitemap, LIVE_LANGS)
  copy_nl.py            alle Nederlandse sitecopy (relaunch NL v1)
  pages.py              inhoud van alle pagina's, per pagina één functie
  routes.py             URL-slugs per taal + navigatie
  i18n.py               vaste teksten NL/EN/DE
  i18n_pages.py         pagina-teksten NL/EN/DE
_redirects, netlify.toml, CNAME, .nojekyll, robots.txt, sitemap.xml
```

**Regel:** pas nooit iets aan in `nl/`, `en/`, `de/`, `404.html` of `sitemap.xml`. Die worden bij elke build overschreven. Wijzig `tools/` of `assets/`.

---

## 3. De handboekcatalogus

De catalogus telt **twaalf handboeken**: zes families in Core en Pro Edition.

| Nr | Familie | Core | Pro (ice hockey) |
|----|---------|------|------------------|
| 01 | Power Foundations | 60 p | 59 p |
| 02 | Strength Foundations | 57 p | 61 p |
| 03 | Speed Foundations | 60 p | 54 p |
| 04 | Agility Foundations | 59 p | 56 p |
| 05 | Season Foundations (in-season) | 57 p | 63 p |
| 06 | Pre-Season Foundations | 58 p | 64 p |

Paginaaantallen, ondertitels en hoofdstukindeling komen uit de PDF's zelf.
Prijzen: Core €39, Pro €79 — één plek om te wijzigen: `PRICE_CORE` / `PRICE_PRO`
bovenin `tools/make_handbooks.py`.

`assets/data/handbooks.json` en `assets/data/rules.json` worden **gegenereerd**:

```bash
python3 tools/make_handbooks.py   # catalogus + aanbevelingslogica
python3 tools/build.py            # alle pagina's
```

Bewerk `tools/make_handbooks.py`, niet de JSON. Elk boek heeft daar één `dict(...)`
met `id`, `family`, `version`, `pages`, `weeks`, `category`, `phase`,
`recommendFor`, `featured` en per taal `title`, `tagline`, `summary`, `audience`,
`learn`, `contents`, `teaserQuote`. Een nieuw boek = één dict erbij plus een regel
in `RULES` die ernaar verwijst.

**Er zijn geen nepkortingen.** `compareAt` staat overal op `null`. Een doorgestreepte
prijs die nooit gevraagd is, past niet bij een merk dat op onderbouwing verkoopt.

## 4. Aanbevelingslogica aanpassen

`assets/data/rules.json`.

- `proUpgrade`: bij welke sport/niveau een Pro-versie voorrang krijgt boven Core, en vanaf hoeveel zwakke domeinen (`alsoWhenWeakDomains`).
- `rules`: lijst met harde voorwaarden. Elke regel heeft:
  - `id`, `weight` (hoger = eerder primair advies)
  - `when`: voorwaarden, bv. `{"weakDomains":["elastic"],"sport":"icehockey","phase":"preseason"}`
  - `recommend`: `family` of concrete `id`
  - `blocksPrimaryOthers`: `true` als deze regel altijd het primaire advies moet zijn (bv. blessure)

De zelftest kiest één primair advies en maximaal twee secundaire. Wil je een nieuwe regel? Voeg een object toe en geef het een gewicht tussen bestaande regels in. Geen code aanpassen.

---

## 5. Benchmarks invullen (nog te doen)

`assets/data/benchmarks.json` staat nu op `"provisional": true` met `"source": "NOG IN TE VULLEN — …"` per test. De site laat daarom een zichtbare disclaimer zien.

Per test vul je in: `source` (bron + jaar), de referentiebanden per sport/geslacht/niveau, en `sem` (meetfout). Zet daarna `"provisional": false` — de disclaimer verdwijnt automatisch voor die test.

---

## 6. Betaalprovider koppelen

Zoek in de code op `KOPPELPUNT`. Twee plekken:

1. `assets/js/nf-core.js` → functie `checkout()` — de knop in de winkelwagen-drawer.
2. `assets/js/nf-checkout.js` → functie `payBlock()` — de besteloverzichtpagina.

Nu is er een mailto-fallback zodat de flow werkt zonder provider. Vervangen door:

- **Stripe Payment Link per handboek** (simpelst): zet per handboek een link in `handbooks.json` (bv. veld `payLink`) en stuur de gebruiker daarheen.
- **Stripe Checkout / Mollie met meerdere regels**: kleine serverless functie nodig (Netlify Function) die de cart omzet in een sessie. Het cart-object staat klaar via `NF.cart.items()`.

---

## 7. Formulier en agenda koppelen

In `tools/pages.py`, functie `contact()`:

- Formspree-placeholder: `https://formspree.io/f/JOUW-FORM-ID` → vervang door je eigen endpoint.
- Agenda-embed: er staat een gemarkeerd blok voor Cal.com of Calendly.

Daarna opnieuw builden.

---

## 8. Taal toevoegen

1. `tools/routes.py`: voeg de taalcode toe aan `LANGS` en zet slugs in `SLUGS`.
2. `tools/i18n.py` en `tools/i18n_pages.py`: voeg de vierde waarde toe aan elke `add(...)`.
3. `assets/data/i18n.json` en `handbooks.json`: voeg de taalsleutel toe.
4. `tools/build.py`: vlag-SVG toevoegen aan `FLAGS`.

Ontbreekt een vertaling, dan valt de site terug op Nederlands in plaats van leeg te blijven.

---

## 9. Afbeeldingen toevoegen

Zet bestanden in `assets/img/` en vul `cover` in bij het handboek. Zonder cover krijgt elk handboek een nette typografische cover met monogram — de site ziet dus nooit leeg uit.

---

## 10. Publiceren

### GitHub Pages (huidige hosting)

De site draait nu op GitHub Pages met een eigen domein. `CNAME` en `.nojekyll`
staan klaar. Publiceren met GitHub Desktop:

1. Open **GitHub Desktop** → *File → Clone repository* → kies je website-repo.
2. Open de gekloonde map in Finder. **Verwijder daar alles behalve de map `.git`.**
   Dat is belangrijk: anders blijven oude bestanden als `diensten-teams.html` met
   de volledige oude inhoud naast de nieuwe redirect-stubs bestaan.
3. Kopieer de **inhoud** van deze map erin — dus `index.html`, `nl/`, `en/`, `de/`,
   `assets/`, `tools/` en de losse bestanden, niet de map zelf.
   Zet in Finder verborgen bestanden aan met **cmd + shift + punt**, zodat
   `.nojekyll` en `.gitignore` meegaan.
4. Terug in GitHub Desktop: je ziet nu de wijzigingen staan. Typ een omschrijving,
   klik **Commit to main** en daarna **Push origin**.
5. Na een paar minuten staat het live. Controleer `/nl/`, `/nl/handboeken/` en
   `/en/`; zie je nog de oude site, doe dan een harde ververs
   (**cmd + shift + R**).

> **Let op:** alle paden zijn root-absoluut (`/assets/…`, `/nl/…`). Dat werkt op een
> eigen domein en op `<gebruiker>.github.io`, maar **niet** op een project-URL als
> `gebruiker.github.io/repo/`.

> `_redirects` en `netlify.toml` worden door GitHub Pages genegeerd. Het doorsturen
> van de oude URL's gebeurt daar door de meta-refresh-stubs in de root
> (`diensten-teams.html` enzovoort). Die zijn iets trager en geven geen echte 301,
> maar ze werken.

### Netlify (aanbevolen alternatief)

Wil je eerst zien of het werkt zonder aan je live site te komen: sleep deze map op
**netlify.com/drop**. Je krijgt binnen een halve minuut een testadres. Koppel je
daarna het repo, dan pakt Netlify `_redirects` en `netlify.toml` wel op en krijg je
echte 301-redirects — beter voor SEO dan de meta-refresh-stubs.

### Na het publiceren

- Dien `sitemap.xml` in bij **Google Search Console**; zonder dat weet je niet of
  je geïndexeerd bent.
- Controleer of `nforce-performance.nl/` en `/index.html` dezelfde pagina tonen.
  Doen ze dat niet, dan zit er nog een verouderde kopie in de cache of een tweede
  deploy in de weg.
- De merknaam is **NForce** (Brand Style Guide v1). Laat vóór livegang een
  merkencheck doen; zie open vragen in het relaunchdocument.
