# N-Force Performance — website op Railway zetten

Statische site (Caddy in een Docker-container). Alles wat je publiceert staat in `site/`.

```
site/
  index.html      de homepage
  privacy.html    privacyverklaring
  assets/         css, js, favicon, afbeeldingen
  assets/i18n/    nl.json, en.json, de.json — de vertalingen
Caddyfile         webserverconfig (Railway geeft de poort via $PORT)
Dockerfile        bouwt een caddy:2-alpine image met site/ erin
```

---

## Stap 1 — Nieuwe service in je bestaande Railway-project

Je webapp blijft ongemoeid; dit wordt een **tweede service** in hetzelfde project.

**Route A — via GitHub (aanbevolen, want dan deploy je later met een git push)**

1. Maak een nieuwe repo aan, bijvoorbeeld `nforce-website`, en push de inhoud van deze map erin:
   ```bash
   git init
   git add .
   git commit -m "Website N-Force Performance"
   git branch -M main
   git remote add origin git@github.com:<jouw-gebruikersnaam>/nforce-website.git
   git push -u origin main
   ```
2. In Railway: open je project → **+ New** → **GitHub Repo** → kies `nforce-website`.
3. Railway ziet de `Dockerfile` en bouwt automatisch. Geen build command of start command nodig.

**Route B — via de Railway CLI, zonder GitHub**

```bash
npm i -g @railway/cli
railway login
railway link          # kies je bestaande project
railway up            # uploadt deze map en bouwt hem
```

## Stap 2 — Service publiek maken

In de service: **Settings → Networking → Generate Domain**. Je krijgt een `xxx.up.railway.app`-URL. Open die en check of de site er goed uitstaat.

Zet `PORT` **niet** handmatig als variabele — Railway injecteert die zelf en de Caddyfile pakt hem op.

## Stap 3 — Eigen domein koppelen

In Railway: **Settings → Networking → + Custom Domain**. Railway geeft je twee records: een **CNAME** en een **TXT**. Beide zijn verplicht — zonder het TXT-record blijft je domein een 404 geven, ook als de CNAME al werkt ([Railway docs](https://docs.railway.com/networking/domains/working-with-domains)).

Dan in het TransIP-controlepaneel: **Domein → nforce-performance.nl → Geavanceerd Domeinbeheer → DNS**. Zet de schakelaar achter "TransIP instellingen" **uit**, anders overschrijft TransIP je eigen records ([TransIP](https://www.transip.nl/knowledgebase/305-dns-nameservers-aanpassen-via-controlepaneel)).

**Voor een subdomein** (bijvoorbeeld `www` of `coaching`):

| Naam | Type | Waarde |
|---|---|---|
| `www` | CNAME | de Railway-waarde, afgesloten met een punt, bijv. `abc123.up.railway.app.` |
| (zoals Railway aangeeft) | TXT | de verificatiewaarde uit Railway |

De afsluitende punt is belangrijk: zonder die "trailing dot" plakt TransIP je eigen domeinnaam er automatisch achter ([TransIP](https://www.transip.nl/knowledgebase/407-een-cname-record-instellen)).

**Voor het rootdomein** (`nforce-performance.nl` zonder www) kun je geen CNAME gebruiken. TransIP heeft daar een **ALIAS-record** voor: naam `@`, type `ALIAS`, waarde de Railway-hostname met trailing dot ([TransIP](https://www.transip.nl/knowledgebase/een-alias-record-instellen)). Railway ondersteunt ALIAS/CNAME-flattening op de apex ([Railway docs](https://docs.railway.com/networking/domains/working-with-domains)).

Let op: als je een ALIAS op `@` zet, mag je in een MX- of NS-record niet meer naar dat rootdomein verwijzen. Je e-mail-MX-records voor `nick@nforce-performance.nl` moeten dus rechtstreeks naar je mailprovider wijzen, niet naar `@`.

DNS-wijzigingen kunnen tot 72 uur doorwerken, in de praktijk meestal binnen een uur.

## Stap 4 — Aanpassingen doorvoeren

Wijzig een bestand in `site/`, dan:

- Route A: `git commit` + `git push` → Railway deployt automatisch
- Route B: `railway up`

---

## Een taal toevoegen

1. Kopieer `site/assets/i18n/nl.json` naar bijvoorbeeld `fr.json` en vertaal alle waarden. Laat de sleutels exact staan.
2. Voeg de taalcode toe aan de `LANGS`-array bovenaan `site/assets/js/main.js`.
3. Deployen. De taalkiezer in de header pikt de nieuwe taal automatisch op.

De Nederlandse tekst staat als basis in de HTML, dus zonder JavaScript blijft de site volledig leesbaar. Omdat de vertalingen via `fetch` worden geladen, moet je de site via http(s) bekijken en niet door het bestand lokaal te openen.

## Nog invullen in de site

Zoek op `[aanvullen]` in `site/index.html`, `site/privacy.html` en de drie JSON-bestanden in `site/assets/i18n/`. Openstaand: postadres, drie concrete bewaartermijnen, de namen van je verwerkers, of er doorgifte buiten de EER speelt, de definitieve site-URL in de JSON-LD en hreflang-tags, en of je met vaste tarieven wil werken. Pas je iets aan in de zichtbare tekst, pas het dan ook aan in `nl.json`, `en.json` en `de.json`.
