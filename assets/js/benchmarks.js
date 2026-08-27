/* ==========================================================================
   N-FORCE PERFORMANCE — referentiewaarden (legacy)
   --------------------------------------------------------------------------
   AUTOMATISCH GEGENEREERD door tools/make_benchmarks.py. Niet met de hand
   aanpassen; wijzigingen gaan verloren bij de volgende build.

   Dit bestand bestaat alleen nog voor twee oude resultatenpagina's. Het kent
   maar één band per test, dus hier staat de band voor mannen in het ijshockey.
   De zelftest gebruikt assets/data/benchmarks.json, met banden per sport en
   geslacht, bronnen en waar nodig een waarschuwing bij een geleende band.
   ========================================================================== */

window.NFORCE_BENCHMARKS = {
  cmj: {
    label: 'Countermovement jump',
    unit: 'cm',
    axis: [20, 70],
    band: [40, 46],
    higherIsBetter: true,
    error: '± 1,5 cm',
    source: 'Swedish Hockey League, mannen senior (n = 21, 27,1 ± 5,4 j), ForceDecks krachtplatform 1000 Hz, handen op heupen, beste van 3. CMJ 41,8 ± 4,8 cm; 10 m 1,99 ± 0,08 s met 1080 Sprint, autostart bij 0,2 m/s. Frontiers in Sports and Active Living, 2026. Bron: https://www.frontiersin.org/journals/sports-and-active-living/articles/10.3389/fspor.2026.1920826/full',
    below: 'Sprongkracht is hier de beperkende factor. Dat is bijna altijd een krachtvraagstuk, niet een techniekvraagstuk.',
    inside: 'Sprongkracht is op niveau. De winst zit elders.',
    above: 'Explosiviteit is geen beperking. Kijk naar de overdracht naar je sport.'
  },

  sj: {
    label: 'Squat jump',
    unit: 'cm',
    axis: [15, 65],
    band: [36, 44],
    higherIsBetter: true,
    error: '± 1,5 cm',
    source: 'LET OP: Alle bruikbare squat-jumpdata in ijshockey komt uit één Zwitserse club. Gebruik deze test naast de countermovement jump, nooit als losse drempel. Hoogste Zwitserse competitie, mannen senior (n = 21, 28,4 ± 3,9 j) en tweede competitie U21 (n = 22, 18,8 ± 1,0 j), Hawkin krachtplatform, handen op heupen, beste van 3. CMJ 42,8 ± 3,8 en 40,3 ± 5,0 cm; SJ 40,2 ± 3,7 en 37,1 ± 5,6 cm. Biology of Sport, 2024. Bron: https://pmc.ncbi.nlm.nih.gov/articles/PMC10765453/',
    below: 'Je mist kracht uit stilstand. Dat is zuiver een krachtvraagstuk, want er zit geen elastiek in deze sprong.',
    inside: 'Concentrische kracht is op niveau. Vergelijk hem met je countermovement jump.',
    above: 'Sterk uit stilstand. Zit je countermovement jump niet veel hoger, dan gebruik je je elastiek nog niet.'
  },

  broad: {
    label: 'Verspringen vanuit stand',
    unit: 'cm',
    axis: [150, 320],
    band: [240, 265],
    higherIsBetter: true,
    error: '± 10 cm',
    source: 'LET OP: Er bestaat geen verspringdata voor Europese senior semi-prof spelers. De band loopt tussen elite Zwitserse U20 en een NHL-populatie uit 2003 zonder pogingprotocol. Dit is de zwakst onderbouwde band op deze pagina. Hoogste Zwitserse juniorencompetitie, U20 (n = 19, 17,8 ± 0,9 j). Verspringen vanuit stand met armzwaai, beste van 3: 250 ± 16 cm. Sprint 30 m met Brower-lichtpoorten, voorste voet 1 m achter de eerste poort, snelste van 2: 4,35 ± 0,14 s. Sports, 2021. Bron: https://pdfs.semanticscholar.org/3627/e21cfdfa456a6f112a02a2209ca084873176.pdf',
    below: 'Je krijgt weinig kracht horizontaal de grond in. Dat is dezelfde eigenschap die je eerste passen bepaalt.',
    inside: 'Horizontale explosiviteit op niveau.',
    above: 'Horizontale explosiviteit is een sterk punt. Controleer of je die ook op het ijs kwijt kunt.'
  },

  squatRel: {
    label: 'Squat (1RM / lichaamsgewicht)',
    unit: '× lichaamsgewicht',
    axis: [0.8, 3.0],
    band: [1.7, 2.2],
    higherIsBetter: true,
    error: 'geen gepubliceerde meetfout',
    source: 'LET OP: Geen enkele ijshockeystudie publiceert een relatieve squat voor mannen. De ondergrens is berekend uit groepsgemiddelden van de Noorse competitie, 151 kg bij 84 kg lichaamsgewicht; dat is eigen rekenwerk, geen gepubliceerde waarde. De bovengrens van 2,2 × is de blessuredrempel uit American football. Bij vrouwen komt de band uit een protocol dat geen zuiver 1RM was. Noorse hoogste competitie, mannen senior (n = 848, 23 ± 4 j), grootste Europese dataset. CMJ beste van 3: verdedigers 39,8 ± 5,0 cm, aanvallers 39,7 ± 5,1 cm. Back squat 1RM 151 ± 22 kg bij een groepsgemiddeld lichaamsgewicht van 84 ± 7 kg. Bron: https://vuir.vu.edu.au/44542/1/Fitness_tests%20_and_match_performance_in_a_male_ice_hockey_national_league.pdf',
    below: 'Je krachtbasis is te laag om explosiviteit betrouwbaar te ontwikkelen. Hier begint je winst.',
    inside: 'Krachtbasis is voldoende. Nu is de vraag of je hem kunt uitdrukken in snelheid.',
    above: 'Sterk. Extra kracht levert hier waarschijnlijk minder op dan snelheids- of conditiewerk.'
  },

  sprint10: {
    label: 'Sprint 10 meter',
    unit: 's',
    axis: [1.5, 2.6],
    band: [1.92, 2.07],
    higherIsBetter: false,
    error: '± 0,02 s',
    source: 'Swedish Hockey League, mannen senior (n = 21, 27,1 ± 5,4 j), ForceDecks krachtplatform 1000 Hz, handen op heupen, beste van 3. CMJ 41,8 ± 4,8 cm; 10 m 1,99 ± 0,08 s met 1080 Sprint, autostart bij 0,2 m/s. Frontiers in Sports and Active Living, 2026. Bron: https://www.frontiersin.org/journals/sports-and-active-living/articles/10.3389/fspor.2026.1920826/full',
    below: 'De eerste drie passen kosten je tijd. Meestal een kracht- of mechanicavraagstuk.',
    inside: 'Acceleratie op niveau voor deze groep.',
    above: 'Acceleratie is sterk. Controleer of topsnelheid en remvermogen meekomen.'
  },

  sprint30: {
    label: 'Sprint 30 meter',
    unit: 's',
    axis: [3.6, 5.6],
    band: [4.2, 4.45],
    higherIsBetter: false,
    error: '± 0,03 s',
    source: 'LET OP: Er bestaat geen off-ice 30 meter voor senior semi-prof of prof spelers in Europa. De herenband komt van elite Zwitserse U20-spelers; dat is verdedigbaar omdat off-ice sprint tussen U20 en senior nauwelijks verschilt, maar het blijft een extrapolatie. De damesband komt uit een bron die het starttype niet vermeldt. Hoogste Zwitserse juniorencompetitie, U20 (n = 19, 17,8 ± 0,9 j). Verspringen vanuit stand met armzwaai, beste van 3: 250 ± 16 cm. Sprint 30 m met Brower-lichtpoorten, voorste voet 1 m achter de eerste poort, snelste van 2: 4,35 ± 0,14 s. Sports, 2021. Bron: https://pdfs.semanticscholar.org/3627/e21cfdfa456a6f112a02a2209ca084873176.pdf',
    below: 'Je snelheid vlakt af na de acceleratie. Topsnelheidswerk is hier relevant.',
    inside: 'Topsnelheid op niveau.',
    above: 'Topsnelheid is een sterk punt.'
  },

  cod505: {
    label: '505 richtingverandering',
    unit: 's',
    axis: [2.0, 3.0],
    band: [2.25, 2.45],
    higherIsBetter: false,
    error: '± 0,05 s',
    source: 'LET OP: Er bestaat nul 505-data in ijshockey, op geen enkel niveau en voor geen enkel geslacht. Deze band is geleend uit Schotse junior-elite voetballers van 13 tot 17 jaar. Ijshockeyonderzoek gebruikt de 5-10-5 pro-agility op het ijs; wil je een echte ijshockeyreferentie, gebruik dan die test. Junior-elite voetballers Schotse FA, U15–U17 (n = 32, 13,6 ± 2,0 j). Modified 505 met Witty-poorten, staggered start 0,7 m achter de poort, beste per richting daarna gemiddeld: 2,33 ± 0,08 s. Meetfout ICC 0,84–0,89, CV 1,6–1,8%. Bron: https://pmc.ncbi.nlm.nih.gov/articles/PMC7240391/',
    below: 'Je verliest tijd in de draai. Remvermogen, niet versnellen, is hier de vaardigheid.',
    inside: 'Richtingverandering op niveau.',
    above: 'Sterk in de draai. Dat is in de wedstrijd vaak meer waard dan een snelle 30 meter.'
  },

  yoyo: {
    label: 'Yo-Yo IR1 (afstand)',
    unit: 'm',
    axis: [800, 3200],
    band: [1900, 2400],
    higherIsBetter: true,
    error: '± 125 m',
    source: 'LET OP: Er bestaat geen off-ice Yo-Yo IR1-data voor ijshockey. Een review van 239 Yo-Yo IR1-studies met 4.726 deelnemers bevat geen enkele ijshockeygroep. Deze band is geleend uit Duitse eerste-divisie handbal en Italiaans semi-prof voetbal. Kun je op het ijs testen, dan is 1.850 ± 499 m uit de tweede Deense divisie de best passende semi-prof referentie. Systematische review Yo-Yo IR1 (239 studies, 4.726 deelnemers), supplementaire tabel met lopende Yo-Yo IR1: semi-prof voetbal Italië 2.385 ± 412 m (24,0 ± 6,0 j), semi-prof voetbal Denemarken 2.803 ± 330 m, eerste divisie handbal Duitsland 2.038 ± 537 m (25,2 ± 5,1 j), eerste divisie handbal dames Denemarken 1.436 ± 222 m (25,9 ± 3,8 j). Geen enkele ijshockeygroep. Bron: https://www.frontiersin.org/api/v4/articles/343642/file/Table_1.PDF/343642_supplementary-materials_tables_1_pdf/1',
    below: 'Herhaald vol gas is je beperking. Je zakt in op het moment dat het telt.',
    inside: 'Conditie op niveau voor deze groep.',
    above: 'Conditie is een sterk punt. Extra volume levert hier weinig op.'
  }

};
