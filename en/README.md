# /en/ — Engelse taalversie

Deze map is bewust leeg. De mappenstructuur staat er al zodat je later een
taal kunt toevoegen zonder één URL om te leggen.

Zo voeg je Engels toe:

1. Zet in `tools/build.py` de variabele `LANG` en de paden op `en`, of maak
   een tweede contentbestand (`tools/content_en.py`) en draai de build per taal.
2. Voeg in de `LAYOUT` de wederkerige hreflang-tags toe:
   `nl`, `en`, `de` en `x-default`.
3. Zet in `assets/js`-loze root `index.html` de taal in de `available`-array,
   zodat de taaldetectie hem meeneemt.
4. Haal in `tools/build.py` bij `LANGSWITCH` het `aria-disabled` weg en maak er
   een echte link van.
5. Voeg de nieuwe URL's toe aan `sitemap.xml` (gebeurt automatisch via de build).

Zet geen lege of half vertaalde pagina's live: een taalversie die niet compleet
is, kost je meer vertrouwen dan hij oplevert.
