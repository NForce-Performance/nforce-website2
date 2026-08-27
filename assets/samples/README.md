# Inkijkexemplaren

Hier komen de inkijkexemplaren van de handboeken. Eén per handboek, met de
bestandsnaam `<handboek-id>-inkijk.pdf`, bijvoorbeeld
`power-foundations-core-inkijk.pdf`.

Deze bestanden zet je hier niet met de hand neer. Ze worden gemaakt door
`tools/make_samples.py`.

## Werkwijze

1. Zet de volledige PDF's in `_bron/handboeken/`, met de handboek-id als
   bestandsnaam. Die map staat in `.gitignore`, dus de volledige boeken komen
   nooit in de repo en nooit op de live site.

2. Installeer de enige afhankelijkheid:

   ```
   pip3 install pymupdf
   ```

3. Draai:

   ```
   python3 tools/make_samples.py
   python3 tools/make_handbooks.py
   python3 tools/build.py
   ```

## Wat er in een inkijkexemplaar zit

- Een eigen omslag in de huisstijl, met titel, ondertitel, "X van Y pagina's",
  de prijs inclusief btw en het webadres.
- Acht pagina's uit het boek zelf: de eerste vier, plus vier uit ongeveer
  veertig procent van het boek. Iemand die alleen een inhoudsopgave ziet, koopt
  niets, dus er moet echt programmawerk bij zitten.
- Op elke geleende pagina een voettekst met "Inkijkexemplaar", het webadres en
  het paginanummer binnen het inkijkexemplaar.
- Een afsluitpagina met wat er in de volledige uitgave staat, de prijs en het
  webadres.

## Automatisch aan en uit

`tools/make_handbooks.py` kijkt per handboek of `<id>-inkijk.pdf` in deze map
bestaat. Zo ja, dan vult het het veld `sample` in `assets/data/handbooks.json`
en verschijnt de inkijkknop op de site. Zo nee, dan blijft `sample` op `null` en
is er geen knop. Er kan dus nooit een 404 achter die knop zitten.

## Aantal pagina's aanpassen

```
python3 tools/make_samples.py --pages 10
python3 tools/make_samples.py --only speed-foundations-pro
python3 tools/make_samples.py --list
```
