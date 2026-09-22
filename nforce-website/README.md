# N-Force Performance — website

Statische site (HTML/CSS/JS) met een kleine Python-generator. Geen build-tools, geen npm, geen framework.
Drie talen: **NL (standaard), EN, DE**. Handboeken, zelftest en aanbevelingslogica zitten in **data**, niet in code.

---

## 1. Snel starten

```bash
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
    handbooks.json      ALLE handboeken (de belangrijkste file voor jou)
    benchmarks.json     testnormen per sport/geslacht/niveau
    rules.json          aanbevelingslogica
    i18n.json           UI-teksten voor de JavaScript
  img/favicon.svg
tools/
  build.py              generator (layout, header/footer, SEO, sitemap)
  pages.py              inhoud van alle pagina's, per pagina één functie
  routes.py             URL-slugs per taal + navigatie
  i18n.py               vaste teksten NL/EN/DE
  i18n_pages.py         pagina-teksten NL/EN/DE
_redirects, netlify.toml, CNAME, .nojekyll, robots.txt, sitemap.xml
```

**Regel:** pas nooit iets aan in `nl/`, `en/`, `de/`, `404.html` of `sitemap.xml`. Die worden bij elke build overschreven. Wijzig `tools/` of `assets/`.

---

## 3. Nieuw handboek toevoegen (alleen data)

Open `assets/data/handbooks.json` en kopieer een bestaand object. Vul in:

| Veld | Betekenis |
|---|---|
| `id` | unieke sleutel, bv. `shoulder-care-core`. Wordt gebruikt in de winkelwagen. |
| `family` | groep waar Core en Pro bij elkaar horen, bv. `shoulder` |
| `version` | `"core"` of `"pro"` |
| `coreVariant` / `proVariant` | id van de tegenhanger (voor upsell). Laat leeg als die niet bestaat. |
| `sports` | `["icehockey","football","teamsport","allround"]` — gebruikt door filters én rules |
| `category` | `strength`, `speed`, `conditioning`, `hockey`, `rehab` |
| `phase` | `offseason`, `preseason`, `inseason`, `rehab`, `allyear` |
| `level` | `["beginner","intermediate","semi-pro","pro"]` |
| `price` | getal in euro's, bv. `39` |
| `compareAt` | oude prijs of `null` |
| `status` | `available`, `presale` of `soon` — bij `soon` verdwijnt de koopknop |
| `pages`, `weeks` | getallen, verschijnen in de badges |
| `languages` | `["nl","en","de"]` |
| `sample` | pad naar een PDF-teaser of `null` |
| `cover` | pad naar een afbeelding of `null` (dan wordt automatisch een typografische cover gerenderd) |
| `recommendFor` | lijst met domeincodes: `strength`, `elastic`, `rfd`, `accel`, `topspeed`, `cod`, `engine`, `injury`, `asymmetry` |
| `badges` | vrije labels per taal |
| `featured` | `true` = zichtbaar in het uitgelichte blok op de homepage |
| `title`, `tagline`, `summary`, `audience`, `learn`, `contents`, `teaserQuote` | **per taal** (`nl`/`en`/`de`) |

`summary` = het blok "Wat het is" in de teaser. `learn` = 3–5 bullets. `contents` = hoofdstukkenlijst; alleen de eerste twee zijn leesbaar, de rest krijgt automatisch een slotje. Zo geef je nooit de volledige inhoud gratis weg.

Daarna: `python3 tools/build.py`. Klaar — de handboekenpagina, filters, homepage, zelftest-aanbevelingen en winkelwagen pakken het nieuwe boek automatisch op.

---

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

**Netlify:** repo koppelen, geen build command, publish directory `.`. `netlify.toml` en `_redirects` staan er al (oude URL's zoals `diensten-online.html` worden doorgestuurd).

**GitHub Pages:** push naar `main`, Pages op root. `.nojekyll` en `CNAME` staan er al. Let op: GitHub Pages leest `_redirects` niet — de legacy-stubs in de root doen daar het doorsturen.

Na elke inhoudelijke wijziging: `python3 tools/build.py` en de gegenereerde bestanden mee committen.
