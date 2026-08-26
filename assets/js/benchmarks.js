/* ==========================================================================
   N-FORCE PERFORMANCE — referentiewaarden
   --------------------------------------------------------------------------
   !! LET OP — DIT BESTAND BEVAT NOG GEEN ECHTE REFERENTIEWAARDEN !!

   De bereiken hieronder zijn PLAATSHOUDERS. Ze staan er zodat de check
   technisch werkt, niet omdat ze kloppen. Zolang `source` begint met
   "NOG IN TE VULLEN" toont de pagina een zichtbare waarschuwing.

   Vul per test in:
     band            [ondergrens, bovengrens] van je referentiegroep
     axis            [links, rechts] van de schaalbalk
     unit            eenheid zoals je hem op de site toont
     higherIsBetter  true bij sprong/worp, false bij sprint- en shuttletijden
     error           typische meetfout, in dezelfde eenheid
     source          bron · populatie · n & leeftijd · protocol · datum
     below/inside/above   één zin interpretatie per uitkomst

   Regel uit de audit: GEEN BAND ZONDER BRON. Heb je voor een test geen
   bruikbare referentiegroep, verwijder hem dan hier en gebruik op de site
   de interne verdeling van de selectie als vergelijking.
   ========================================================================== */

window.NFORCE_BENCHMARKS = {

  cmj: {
    label: 'Countermovement jump',
    unit: 'cm',
    axis: [20, 70],
    band: [38, 52],
    higherIsBetter: true,
    error: '± 1,4 cm',
    source: 'NOG IN TE VULLEN — bron · populatie · n & leeftijd · protocol · datum',
    below: 'Concentrische sprongkracht is hier waarschijnlijk de beperkende factor.',
    inside: 'Sprongkracht is niet je beperkende factor; de winst zit elders.',
    above: 'Explosiviteit is niet de beperkende factor. Kijk naar de overdracht naar je sport.'
  },

  sj: {
    label: 'Squat jump',
    unit: 'cm',
    axis: [20, 70],
    band: [34, 48],
    higherIsBetter: true,
    error: '± 1,4 cm',
    source: 'NOG IN TE VULLEN — bron · populatie · n & leeftijd · protocol · datum',
    below: 'Krachtproductie vanuit stilstand is beperkt. Vaak een krachtvraagstuk, geen techniekvraagstuk.',
    inside: 'Normale concentrische output. Vergelijk met je CMJ voor je elastische bijdrage.',
    above: 'Sterke concentrische output.'
  },

  broad: {
    label: 'Verspringen vanuit stand',
    unit: 'cm',
    axis: [150, 300],
    band: [215, 255],
    higherIsBetter: true,
    error: '± 4 cm',
    source: 'NOG IN TE VULLEN — bron · populatie · n & leeftijd · protocol · datum',
    below: 'Horizontale krachtproductie blijft achter bij wat je sport vraagt.',
    inside: 'Horizontale explosiviteit op niveau.',
    above: 'Horizontale explosiviteit is niet de beperkende factor.'
  },

  sprint10: {
    label: 'Sprint 10 meter',
    unit: 's',
    axis: [1.5, 2.6],
    band: [1.72, 1.92],
    higherIsBetter: false,
    error: '± 0,03 s',
    source: 'NOG IN TE VULLEN — bron · populatie · n & leeftijd · protocol · datum · starttype',
    below: 'Acceleratie is sterk. Let op of topsnelheid hierbij achterblijft.',
    inside: 'Acceleratie op niveau voor deze groep.',
    above: 'De eerste drie passen kosten je tijd. Vaak een RFD- of krachtvraagstuk.'
  }

};
