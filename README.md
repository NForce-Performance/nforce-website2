# N-Force Performance — website

Herbouwde website op basis van de audit van 26 augustus 2026.
Statische HTML, geen framework, geen buildstap nodig om te deployen.

**Volledige strategie en onderbouwing:** https://claude.ai/code/artifact/64b7b4e9-ab88-46f0-bdea-45f0ef27324b

---

## Eerst dit doen

Vijf dingen die nog van jou moeten komen voordat de site live kan:

1. **Beeldmateriaal.** Kopieer je bestaande afbeeldingen naar `assets/img/`.
   Zie `assets/img/README.md` voor de lijst en de twee foto's die nog gemaakt
   moeten worden. Zonder afbeeldingen werkt de site, maar vallen de hero's
   terug op alleen de gradient.
2. **Agenda-embed.** Zet je Cal.com- of Calendly-embed in `tools/content.py`,
   blok `CHECK`, op de plek die daar met een comment is gemarkeerd (of direct in
   `nl/performance-check/index.html` als je zonder build werkt). Dit is de
   grootste conversiewinst van de hele herbouw; doe dit als eerste.
3. **Formulierendpoint.** Vervang `https://formspree.io/f/JOUW-FORM-ID` door je
   eigen endpoint (Formspree, Netlify Forms, Basin).
4. **Referentiewaarden.** `assets/js/benchmarks.js` bevat nu plaatshouders.
   Vul per test bron, populatie, omvang, protocol en meetfout in, en werk
   `/nl/resultaten/referentiewaarden/` bij. Zolang dat niet gebeurd is, staat er
   op beide plekken een zichtbare waarschuwing — laat die staan tot het klopt.
5. **Juridische teksten.** `/nl/privacy/` en `/nl/voorwaarden/` bevatten alleen
   een checklist. Zet je bestaande privacyverklaring erin en laat de algemene
   voorwaarden opstellen of controleren.

---

## Structuur

```
.
├── index.html                  taaldispatcher → /nl/ (Accept-Language, met vaste terugval)
├── 404.html
├── robots.txt                  wijst naar de www-sitemap (was fout in de oude site)
├── sitemap.xml                 met lastmod, gegenereerd door de build
├── CNAME                       www.nforce-performance.nl
├── .nojekyll                   GitHub Pages: geen Jekyll-verwerking
├── _redirects / netlify.toml   echte 301's op Netlify
├── diensten-*.html             redirect-stubs vanaf de oude URL's
├── privacy.html                idem
├── resultaten.html             idem
├── assets/
│   ├── css/site.css            volledige stylesheet
│   ├── js/site.js              nav, reveal, mobiele CTA-balk, benchmarkcheck
│   ├── js/benchmarks.js        referentiewaarden — NOG IN TE VULLEN
│   └── img/                    beeldmateriaal (zie README daar)
├── nl/                         de site
│   ├── index.html
│   ├── online-coaching/
│   │   └── return-to-play/
│   ├── teams/
│   ├── testing/
│   ├── resultaten/
│   │   └── referentiewaarden/
│   ├── over/
│   ├── performance-check/
│   ├── tarieven/
│   ├── privacy/
│   └── voorwaarden/
├── en/  de/                    leeg, structuur klaar (zie README daar)
└── tools/
    ├── build.py                generator
    └── content.py              ALLE TEKST STAAT HIER
```

---

## Content bewerken

De HTML in `nl/` is **gegenereerd**. Bewerk hem niet rechtstreeks — je verliest
je wijziging bij de volgende build en de navigatie loopt uit de pas.

```bash
python3 tools/build.py
```

Alle teksten staan in `tools/content.py`. Navigatie, footer, `<head>` en
gestructureerde data staan in `tools/build.py`. Python 3 is voldoende; er zijn
geen dependencies.

Wil je toch zonder build werken: dat kan, de bestanden in `nl/` zijn gewone
HTML. Je moet dan alleen bij elke navigatiewijziging twaalf bestanden aanpassen.

---

## Deployen

### GitHub Pages
1. Push dit repo naar GitHub.
2. Settings → Pages → Source: `Deploy from a branch`, branch `main`, map `/ (root)`.
3. Custom domain: `www.nforce-performance.nl` (het `CNAME`-bestand staat er al).
4. Zet bij je DNS een CNAME-record van `www` naar `<gebruikersnaam>.github.io`,
   en laat het kale domein `nforce-performance.nl` doorverwijzen naar `www`.
5. Zet "Enforce HTTPS" aan.

> **Let op:** de site gebruikt paden vanaf de root (`/assets/…`, `/nl/…`).
> Dat werkt op een eigen domein en op een `<gebruiker>.github.io`-site, maar
> **niet** op een project-URL als `gebruiker.github.io/repo/`. Gebruik dus een
> custom domain, of pas de paden aan.

### Netlify (aanbevolen voor de redirects)
Sleep de map naar Netlify of koppel het repo. `netlify.toml` en `_redirects`
worden automatisch opgepakt en leveren echte 301's in plaats van
meta-refresh-stubs. Dat is beter voor SEO.

---

## Wat er is veranderd ten opzichte van de oude site

**Structuur**
- Testing & analyse en Resultaten staan nu in de hoofdnavigatie.
- Navigatie bestaat uit pagina's in plaats van ankers.
- `index.html#online` en `diensten-online.html` zijn samengevoegd tot
  `/nl/online-coaching/`.
- Nieuw: Return to Play, Over N-Force, Performance Check, Referentiewaarden,
  Tarieven, Algemene voorwaarden.
- Taalmappen `/nl/ /en/ /de/` staan klaar, zodat later geen URL's hoeven te
  verhuizen.

**Conversie**
- De kennismaking heet nu **Performance Check**, heeft een eigen pagina en een
  plek voor een agenda-embed in plaats van een formulier met wachttijd.
- Elke CTA op de site wijst naar diezelfde pagina, dus hij is meetbaar.
- Pakketvolgorde is €49 → €125 → €249, met Performance uitgelicht.
- "Meest gekozen" is vervangen door "Aanbevolen startpunt"; "Max. 5 plekken"
  door de werkelijke reden dat er een limiet is.
- Btw-status staat nu bij elke prijs, ook bij de €750-teamkaart.
- Vaste CTA-balk op mobiel, verschijnt na de hero.
- Contactformulier van vijf naar drie verplichte velden.

**Visueel**
- Nieuwe `.page-hero`-component: alle subpagina's hebben nu een echte hero met
  mediabeeld, scrim en frostlaag. Dit was de oorzaak van "te veel witruimte,
  headers te klein".
- Kophiërarchie hersteld: H1 (`--text-3xl`) staat altijd boven de sectiekop
  (`--text-2xl`).
- Drie sectieritmes in plaats van één: `--rhythm-air`, `--rhythm-base`,
  `--rhythm-tight`.
- Alle getallen in monospace met `tabular-nums`.
- De blauwe lijn (`.blueline`) als sectiescheiding, één keer per pagina.
- Navigatie-breakpoint van 1120px naar 1024px (getest: geen horizontale overflow op 390 t/m 1440px).
- Genummerde "Ook interessant"-blokken vervangen door contextuele vervolglinks.

**Techniek en SEO**
- `robots.txt` verwijst naar de www-sitemap (was non-www).
- Redirect-stubs vanaf alle oude `.html`-URL's, plus echte 301's op Netlify.
- Zelfverwijzende canonicals, unieke titles en descriptions per pagina.
- Gestructureerde data: `ProfessionalService`, `Person`, `Service`, `FAQPage`,
  `BreadcrumbList`.
- `hreflang` en `x-default` per pagina, klaar voor uitbreiding.
- Hero-afbeelding wordt gepreload met `fetchpriority="high"`.
- `sitemap.xml` met `lastmod`.

---

## Nog te doen na livegang

- Google Search Console en Bing Webmaster Tools instellen, sitemap indienen.
- Google Business Profile aanmaken voor Tilburg.
- De Performance Check als conversie inrichten in je analytics.
- Hero-afbeeldingen converteren naar AVIF of WebP.
- Kennisbank opzetten met artikelen uit het Power Foundations-materiaal.
- Schrijf de merknaam overal voluit als "N-Force Performance"; "N-Force" alleen
  is bezet door andere bedrijven.
