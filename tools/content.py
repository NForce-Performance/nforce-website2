# -*- coding: utf-8 -*-
"""
N-Force Performance — alle paginacontent.

Bewerk hier, niet in de gegenereerde HTML. Draai daarna: python3 tools/build.py
"""

# ---------------------------------------------------------------------------
# Herbruikbare blokken
# ---------------------------------------------------------------------------

def page_hero(eyebrow, h1, lede, img=None, alt="", crumbs=(), cta=None):
    crumb_html = ""
    if crumbs:
        parts = ['<a href="/nl/">Home</a>']
        for label, href in crumbs[:-1]:
            parts.append('<span>/</span><a href="%s">%s</a>' % (href, label))
        parts.append('<span>/</span>%s' % crumbs[-1][0])
        crumb_html = '<nav class="crumbs" aria-label="Kruimelpad">%s</nav>' % "".join(parts)

    media = ""
    if img:
        media = '<img src="%s" alt="%s" width="1600" height="900" fetchpriority="high" onerror="this.style.display=&#39;none&#39;">' % (img, alt)

    cta_html = ""
    if cta:
        cta_html = ('<div class="actions"><a class="btn btn--primary" href="%s">%s</a>'
                    '<a class="btn btn--ghost" href="%s">%s</a></div>' % cta)

    return """<section class="page-hero">
  <div class="page-hero__media">%s</div>
  <div class="page-hero__scrim"></div>
  <div class="wrap page-hero__inner">
    %s
    <p class="eyebrow">%s</p>
    <h1>%s</h1>
    <p class="lede">%s</p>
    %s
  </div>
</section>""" % (media, crumb_html, eyebrow, h1, lede, cta_html)


def ctaband(title, body, primary=("/nl/performance-check/", "Plan je Performance Check"),
            secondary=None):
    sec = ""
    if secondary:
        sec = '<a class="btn btn--ghost" href="%s">%s</a>' % secondary
    return """<section class="section section--air">
  <div class="wrap">
    <div class="ctaband reveal">
      <h2>%s</h2>
      <p>%s</p>
      <div class="actions">
        <a class="btn btn--primary" href="%s">%s</a>
        %s
      </div>
      <p class="faint">Gratis &middot; twintig minuten &middot; online of telefonisch &middot; geen verkoopgesprek.</p>
    </div>
  </div>
</section>""" % (title, body, primary[0], primary[1], sec)


def next_links(items):
    cards = "".join(
        '<a href="%s"><small>%s</small><b>%s</b><span>%s &rarr;</span></a>' % (href, kicker, title, cta)
        for href, kicker, title, cta in items
    )
    return """<section class="section section--tight">
  <div class="wrap">
    <h2 class="visually-hidden" style="position:absolute;left:-9999px">Verder lezen</h2>
    <div class="next">%s</div>
  </div>
</section>""" % cards


def faq_block(title, items, lede=""):
    rows = "".join(
        "<details><summary>%s</summary><p>%s</p></details>" % (q, a) for q, a in items
    )
    lede_html = '<p class="lede">%s</p>' % lede if lede else ""
    return """<section class="section" id="vragen">
  <div class="wrap">
    <div class="section__head">
      <p class="eyebrow">Vragen</p>
      <h2>%s</h2>
      %s
    </div>
    <div class="faq reveal">%s</div>
  </div>
</section>""" % (title, lede_html, rows)


PLANS = """<div class="plans">
      <div class="plan">
        <div class="plan__head">
          <p class="plan__name">Basis</p>
          <p class="plan__price"><b>&euro;49</b><span>per maand</span></p>
          <p class="plan__for">Voor sporters die zelfstandig trainen, maar met structuur in plaats van gokwerk.</p>
        </div>
        <ul class="ticks">
          <li>Blokprogramma op jouw sport en niveau</li>
          <li>Maandelijks aangepast</li>
          <li>Vragen stellen via de app</li>
        </ul>
        <a class="btn btn--ghost" href="/nl/performance-check/">Bespreek dit pakket</a>
      </div>

      <div class="plan plan--featured">
        <span class="plan__flag">Aanbevolen startpunt</span>
        <div class="plan__head">
          <p class="plan__name">Performance</p>
          <p class="plan__price"><b>&euro;125</b><span>per maand</span></p>
          <p class="plan__for">Voor de atleet die serieus vooruit wil en zijn progressie zwart-op-wit wil zien.</p>
        </div>
        <ul class="ticks">
          <li>Programma op maat, elke vier weken herzien</li>
          <li>Wekelijkse evaluatie van belasting, herstel en slaap</li>
          <li>Videofeedback op twee oefeningen per maand</li>
          <li>Nulmeting en hertest na twaalf weken</li>
          <li>Afstemming met trainer of fysiotherapeut op verzoek</li>
        </ul>
        <a class="btn btn--primary" href="/nl/performance-check/">Bespreek dit pakket</a>
      </div>

      <div class="plan">
        <div class="plan__head">
          <p class="plan__name">Return-to-Play</p>
          <p class="plan__price"><b>&euro;249</b><span>per maand</span></p>
          <p class="plan__for">Voor terugkeer na een blessure of een piekperiode richting het seizoen.</p>
        </div>
        <ul class="ticks">
          <li>Volledig op maat, wekelijks bijgesteld</li>
          <li>Wekelijkse videocall en snelle support</li>
          <li>Onbeperkte videofeedback</li>
          <li>Maandelijkse testing</li>
          <li>Standaard afstemming met fysiotherapeut of medische staf</li>
        </ul>
        <a class="btn btn--ghost" href="/nl/performance-check/">Bespreek dit pakket</a>
        <p class="plan__note">Ik neem hier maximaal vijf trajecten tegelijk aan, omdat wekelijkse videocalls en onbeperkte feedback niet schalen.</p>
      </div>
    </div>

    <div class="plan plan--team" style="margin-top:1rem">
      <div class="plan__head">
        <p class="plan__name">Teams &amp; clubs</p>
        <p class="plan__price"><b>vanaf &euro;750</b><span>per testdag, excl. btw</span></p>
        <p class="plan__for">Begeleiding op locatie is altijd maatwerk: groepsgrootte, faciliteiten, seizoensfase en de rest van de staf bepalen de opzet. Seizoenstrajecten krijgen na de kennismaking een vast voorstel.</p>
      </div>
      <div class="actions">
        <a class="btn btn--ghost" href="/nl/teams/">Bekijk teambegeleiding</a>
        <a class="btn btn--ghost" href="/nl/performance-check/">Vraag een voorstel aan</a>
      </div>
    </div>

    <p class="smallprint" style="margin-top:1.25rem">
      Alle maandprijzen zijn inclusief btw. Een traject start met minimaal twaalf weken, omdat meetbare progressie tijd, consistentie en een goede evaluatie vraagt; daarna is het maandelijks opzegbaar. Teams en clubs ontvangen een offerte exclusief btw.
    </p>"""


# ---------------------------------------------------------------------------
# 1. HOME
# ---------------------------------------------------------------------------

HOME_FAQ = [
    ("Hoe lang zit ik vast aan een pakket?",
     "De minimale looptijd is twaalf weken. Dat is geen verkooptruc: korter dan een blok van twaalf weken kun je niet eerlijk meten of het gewerkt heeft. Daarna loopt het maandelijks door en kun je elke maand opzeggen. Raak je geblesseerd of valt je seizoen anders uit, dan pauzeren we in overleg."),
    ("Heb ik een sportschool nodig voor online coaching?",
     "Voor de meeste programma&rsquo;s wel, omdat externe belasting nu eenmaal het gereedschap is. Heb je alleen een beperkte ruimte of thuismateriaal, zeg dat in de Performance Check. Dan kijken we of ik je verantwoord kan begeleiden of dat je beter af bent met iets anders."),
    ("Hoe snel merk ik resultaat?",
     "De eerste weken merk je vooral betere uitvoering en herstel. Meetbare verbetering in kracht en explosiviteit zie je doorgaans bij de hertest na twaalf weken. Wat je precies wint hangt af van je startpunt, je trainingsleeftijd en hoe consequent je traint. Daarom beloof ik vooraf geen cijfers, maar meten we ze achteraf."),
    ("Hoe ga je om met blessures en samenwerking met een fysiotherapeut?",
     "Ik behandel geen blessures, dat is het domein van de fysiotherapeut of arts. Wat ik wel doe: het programma aanpassen aan wat je wel aankunt, en samen met de behandelaar de opbouw naar volledige wedstrijdbelasting uitzetten."),
    ("Werk je ook met jeugdteams?",
     "Ja. Bij jeugd ligt de nadruk op bewegingskwaliteit, techniek en een rustige opbouw van belasting, passend bij leeftijd en ontwikkeling. Zware belasting is geen doel op zich. Rapportages over minderjarige spelers deel ik alleen met de vooraf afgesproken personen, met toestemming van ouders."),
]

HOME = {
    "url": "/nl/",
    "title": "Online strength &amp; conditioning voor sporters | N-Force Performance",
    "og_title": "N-Force Performance — trainen met bewijs, niet met aannames",
    "description": "Persoonlijke krachttraining met een nulmeting bij de start en een hertest na twaalf weken, van de performance coach van Tilburg Trappers. Plan een gratis Performance Check van twintig minuten.",
    "og_image": "/assets/img/hero.jpg",
    "hero_img": "/assets/img/hero.jpg",
    "faq": HOME_FAQ,
    "service": {
        "name": "Online strength & conditioning coaching",
        "serviceType": "Personal training en sportbegeleiding",
        "url": "https://www.nforce-performance.nl/nl/online-coaching/",
        "offers": [
            {"@type": "Offer", "name": "Basis", "price": "49", "priceCurrency": "EUR"},
            {"@type": "Offer", "name": "Performance", "price": "125", "priceCurrency": "EUR"},
            {"@type": "Offer", "name": "Return-to-Play", "price": "249", "priceCurrency": "EUR"},
        ],
    },
    "content": """
<!-- 01 · HERO -->
<section class="hero">
  <div class="hero__media">
    <img src="/assets/img/hero.jpg" alt="IJshockeyspeler doet off-ice krachttraining met een zwaar beladen halterstang in een donkere krachtruimte met koud licht." width="1600" height="900" fetchpriority="high" onerror="this.style.display=&#39;none&#39;">
  </div>
  <div class="hero__scrim"></div>
  <div class="wrap hero__inner">
    <p class="eyebrow">Strength &amp; conditioning &middot; online en op locatie</p>
    <h1>Trainen met bewijs, niet met aannames.</h1>
    <p class="lede">Je begint met een nulmeting, je traint twaalf weken gericht, en de hertest laat zwart-op-wit zien wat er veranderd is. Voor ambitieuze sporters, teams en clubs.</p>
    <div class="actions">
      <a class="btn btn--primary" href="/nl/performance-check/">Plan je Performance Check</a>
      <a class="btn btn--ghost" href="#hoe-het-werkt">Zo werkt het <span class="btn__arrow" aria-hidden="true">&darr;</span></a>
    </div>
    <p class="reassure">Gratis, twintig minuten, online. Geen verkoopgesprek &mdash; als ik niet de juiste persoon voor je ben, hoor je dat in het gesprek en niet erna.</p>
  </div>
</section>

<!-- 02 · BEWIJSSTRIP -->
<div class="proofstrip">
  <div class="wrap">
    <ul>
      <li>Performance coach bij Tilburg Trappers (Oberliga)</li>
      <li>Afgestudeerd aan Fontys Sporthogeschool</li>
      <li>Strength &amp; conditioning en sportmedische training</li>
      <li>Coaching in het Nederlands, Engels of Duits</li>
    </ul>
  </div>
</div>

<!-- 03 · ROUTER -->
<section class="section section--air" id="voor-wie">
  <div class="wrap">
    <div class="section__head reveal">
      <p class="eyebrow">Voor wie</p>
      <h2>Drie routes, &eacute;&eacute;n manier van werken</h2>
      <p class="lede">Ik werk het liefst met mensen die al gemotiveerd zijn en vooral structuur en onderbouwing missen. Kies de route die op jou van toepassing is.</p>
    </div>
    <div class="grid grid--3 reveal">

      <article class="card card--link">
        <p class="card__label">01 &middot; Individuele atleet</p>
        <h3>Online coaching</h3>
        <p>Je traint al serieus, maar je weet niet of je het goede doet. Je krijgt een programma dat past bij je sport, je seizoen en je agenda &mdash; en cijfers die laten zien of het werkt.</p>
        <ul class="ticks">
          <li>Programma op maat in de app, elke vier weken herzien</li>
          <li>Wekelijkse evaluatie en videofeedback op techniek</li>
          <li>Nulmeting bij de start, hertest na twaalf weken</li>
        </ul>
        <a class="textlink" href="/nl/online-coaching/">Bekijk online coaching <span aria-hidden="true">&rarr;</span></a>
      </article>

      <article class="card card--link">
        <p class="card__label">02 &middot; Team of club</p>
        <h3>Teams &amp; clubs</h3>
        <p>De meeste teams trainen kracht erbovenop in plaats van erin. Ik bouw de fysieke opbouw in rond je wedstrijdkalender, met testmomenten door het seizoen heen.</p>
        <ul class="ticks">
          <li>Seizoensperiodisering rond je kalender</li>
          <li>Nulmeting van de selectie, hertesten per blok</li>
          <li>Rapportage per speler en overzicht voor de staf</li>
        </ul>
        <a class="textlink" href="/nl/teams/">Bekijk teambegeleiding <span aria-hidden="true">&rarr;</span></a>
      </article>

      <article class="card card--link">
        <p class="card__label">03 &middot; Terugkeer na blessure</p>
        <h3>Return to Play</h3>
        <p>De fase tussen de laatste fysiobehandeling en volledige wedstrijdbelasting. Precies waar het bij veel sporters misgaat, en waar zelden iemand de regie neemt.</p>
        <ul class="ticks">
          <li>Opbouw in afstemming met je fysiotherapeut</li>
          <li>Objectieve criteria in plaats van gevoel</li>
          <li>Maandelijkse testing tot je weer wedstrijdfit bent</li>
        </ul>
        <a class="textlink" href="/nl/online-coaching/return-to-play/">Bekijk Return to Play <span aria-hidden="true">&rarr;</span></a>
      </article>

    </div>
    <p class="smallprint" style="margin-top:1.5rem">Wil je alleen weten waar je staat, zonder traject? Dat kan ook &mdash; bekijk <a href="/nl/testing/">testing &amp; analyse</a>.</p>
  </div>
</section>

<hr class="blueline">

<!-- 04 · HOE HET WERKT -->
<section class="section section--air" id="hoe-het-werkt">
  <div class="wrap">
    <div class="section__head reveal">
      <p class="eyebrow">Hoe het werkt</p>
      <h2>Meten. Trainen. Hertesten.</h2>
      <p class="lede">Zonder nulmeting is elke trainingskeuze een aanname. Daarom begint en eindigt elk blok met dezelfde tests, onder dezelfde omstandigheden.</p>
    </div>

    <div class="cycle reveal" style="margin-bottom:3rem">
      <div class="cycle__item">
        <h4>Meten</h4>
        <p>Kracht, snelheid en explosiviteit bij de start, met vaste protocollen die je zelf kunt uitvoeren of die ik op locatie afneem.</p>
      </div>
      <div class="cycle__item">
        <h4>Trainen</h4>
        <p>Twaalf weken gericht werken in blokken van vier weken, met bijsturing op belasting en herstel.</p>
      </div>
      <div class="cycle__item">
        <h4>Hertesten</h4>
        <p>Dezelfde tests, dezelfde omstandigheden. Het verschil is je resultaat &mdash; en het bepaalt wat er in het volgende blok verandert.</p>
      </div>
    </div>

    <div class="steps reveal">
      <div class="step">
        <div class="step__n">01</div>
        <div class="step__body">
          <h4>Performance Check</h4>
          <p>Twintig minuten over je sport, je doel en je context. Je krijgt een inschatting van je grootste beperkende factor en welke test daar uitsluitsel over geeft. Ik zeg eerlijk of ik de juiste persoon voor je ben.</p>
        </div>
      </div>
      <div class="step">
        <div class="step__n">02</div>
        <div class="step__body">
          <h4>Intake en nulmeting</h4>
          <p>Trainingsuren, belastbaarheid, blessurehistorie, faciliteiten en doelen. Daarna voer je onder instructie de testbatterij uit die bij jouw sport past.</p>
        </div>
      </div>
      <div class="step">
        <div class="step__n">03</div>
        <div class="step__body">
          <h4>Blokken van vier weken</h4>
          <p>Je programma loopt in blokken. Elke week een korte evaluatie, elke vier weken een herziening op basis van hoe het ging &mdash; niet op basis van een schema dat in januari geschreven is.</p>
        </div>
      </div>
      <div class="step">
        <div class="step__n">04</div>
        <div class="step__body">
          <h4>Hertest na twaalf weken</h4>
          <p>Dezelfde protocollen, dezelfde omstandigheden. Zo zie je wat er veranderd is en waar de volgende winst zit. Daarna begint de cyclus opnieuw, op je nieuwe niveau.</p>
        </div>
      </div>
    </div>

    <div class="actions" style="margin-top:2rem">
      <a class="btn btn--ghost" href="/nl/resultaten/">Bekijk een voorbeeldrapport <span class="btn__arrow" aria-hidden="true">&rarr;</span></a>
    </div>
  </div>
</section>

<!-- 05 · BEWIJS -->
<section class="section section--air section--panel" id="bewijs">
  <div class="wrap">
    <div class="section__head reveal">
      <p class="eyebrow">Bewijs</p>
      <h2>Waar sta jij?</h2>
      <p class="lede">Vul een eigen testwaarde in en zie waar die valt binnen het referentiebereik. Er wordt niets opgeslagen en niets verstuurd.</p>
    </div>

    <div class="split">
      <div class="bench reveal" data-bench>
        <div class="bench__form">
          <div class="field">
            <label for="bench-test">Test</label>
            <select id="bench-test" data-bench-test></select>
          </div>
          <div class="field">
            <label for="bench-value">Jouw waarde</label>
            <input id="bench-value" type="text" inputmode="decimal" placeholder="bijv. 46" data-bench-value>
          </div>
        </div>
        <div>
          <div class="meter" data-bench-meter></div>
          <div class="meter__scale" data-bench-scale></div>
        </div>
        <p class="bench__out" data-bench-out></p>
        <p class="faint"><strong>Referentiegroep:</strong> <span data-bench-source></span></p>
      </div>

      <div class="reveal" style="display:flex;flex-direction:column;gap:1.25rem">
        <div class="notice">
          <p class="notice__label">Eerst dit</p>
          <p>&Eacute;&eacute;n test zegt weinig. Een volledig profiel zegt waar je moet beginnen &mdash; en bij welke test het verschil groot genoeg is om er een trainingsbeslissing op te baseren.</p>
        </div>
        <p class="muted">Elke referentiewaarde op deze site vermeldt de bron, de populatie, de omvang, het protocol en de meetfout. Is er voor een test geen bruikbare referentiegroep, dan staat dat er ook, en dient je waarde als nulpunt voor je hertest in plaats van als oordeel.</p>
        <a class="textlink" href="/nl/resultaten/referentiewaarden/">Zo zijn de referentiewaarden opgebouwd <span aria-hidden="true">&rarr;</span></a>
        <p class="faint">De eerste hertestronde loopt. Ervaringen van sporters, staf en fysiotherapeuten komen hier zodra ze er zijn &mdash; met naam, in hun eigen woorden, en alleen met toestemming.</p>
      </div>
    </div>
  </div>
</section>

<!-- 06 · PAKKETTEN -->
<section class="section section--air" id="tarieven">
  <div class="wrap">
    <div class="section__head reveal">
      <p class="eyebrow">Tarieven</p>
      <h2>Online coaching pakketten</h2>
      <p class="lede">Kies het niveau dat past bij jouw doel. Twijfel je? Dan zoeken we dat in de Performance Check uit, ook als het antwoord is dat je mij nog niet nodig hebt.</p>
    </div>
    <div class="reveal">""" + PLANS + """</div>
  </div>
</section>

<!-- 07 · OVER N-FORCE -->
<section class="section section--air section--panel" id="over">
  <div class="wrap">
    <div class="split">
      <div class="reveal" style="display:flex;flex-direction:column;gap:1.25rem">
        <p class="eyebrow">Over N-Force</p>
        <h2>Sterker worden is niet hetzelfde als sneller worden</h2>
        <p class="muted">De meeste sporters worden in de gym meetbaar sterker zonder dat het op het veld of het ijs iets oplevert. Niet omdat ze te weinig doen, maar omdat kracht en explosiviteit verwante maar verschillende eigenschappen zijn &mdash; en omdat vrijwel niemand meet of de training werkt.</p>
        <p class="muted">N-Force Performance bestaat om dat op te lossen: een programma dat past bij de sport, de atleet en de seizoensfase, en een meting die laat zien of het klopt.</p>
        <p class="muted">Ik ben Nick Bergman, performance coach bij Tilburg Trappers en afgestudeerd aan Fontys Sporthogeschool, met specialisatie in strength &amp; conditioning en sportmedische training. In een topsportomgeving is geen ruimte voor aannames. Die manier van werken neem ik mee naar elke atleet en elke club waarmee ik werk.</p>
        <a class="textlink" href="/nl/over/">De aanpak achter N-Force <span aria-hidden="true">&rarr;</span></a>
      </div>
      <div class="split__media reveal">
        <img src="/assets/img/detail.jpg" alt="Stilleven in koud licht: opengeslagen notitieboek met een trainingsschema naast een ijshockeystick." width="900" height="675" loading="lazy" onerror="this.style.display=&#39;none&#39;">
      </div>
    </div>
  </div>
</section>

""" + ctaband(
        "Twintig minuten, en je weet waar je aan begint",
        "In de Performance Check kijken we of online coaching, teambegeleiding of alleen een testdag past bij jouw situatie. Jij vertelt waar je nu staat, ik geef eerlijk aan wat zinvol is en wat niet.",
        secondary=("/nl/tarieven/", "Alle tarieven vergelijken"),
    ) + faq_block(
        "Wat sporters en clubs meestal vragen",
        HOME_FAQ,
    ),
}


# ---------------------------------------------------------------------------
# 2. ONLINE COACHING
# ---------------------------------------------------------------------------

ONLINE_FAQ = [
    ("Heb ik een sportschool nodig?",
     "Voor de meeste programma&rsquo;s wel, omdat externe belasting nu eenmaal het gereedschap is. Heb je alleen een beperkte ruimte of thuismateriaal, zeg dat in de Performance Check, dan kijken we of ik je verantwoord kan begeleiden of dat je beter af bent met iets anders."),
    ("Wat als ik geblesseerd raak?",
     "Dan passen we het programma aan in plaats van dat je stilvalt. Bij een blessure die behandeling vraagt werk ik samen met jouw fysiotherapeut; ik stel geen diagnoses en neem hun werk niet over."),
    ("Kan ik pauzeren?",
     "Ja, in overleg. Vakantie, examens, een seizoen dat anders loopt: daar doe ik niet moeilijk over. Na de eerste twaalf weken kun je bovendien maandelijks opzeggen."),
    ("In welke taal krijg ik begeleiding?",
     "In het Nederlands, Engels of Duits. Je programma, je feedback en de gesprekken lopen in de taal die jij kiest."),
    ("Moet ik zelf kunnen testen?",
     "Ja, en dat is eenvoudiger dan het klinkt. Je krijgt testprotocollen met instructievideo&rsquo;s die je met een telefoon en een meetlint kunt uitvoeren. Wat telt is dat je elke keer op dezelfde manier meet."),
]

ONLINE = {
    "url": "/nl/online-coaching/",
    "title": "Online coaching: programma, begeleiding en hertest | N-Force",
    "description": "Een trainingsprogramma dat elke vier weken meebeweegt, wekelijkse evaluatie, videofeedback op techniek en een hertest na twaalf weken. Vanaf €49 per maand.",
    "og_image": "/assets/img/online.jpg",
    "hero_img": "/assets/img/online.jpg",
    "crumbs": [("Online coaching", "/nl/online-coaching/")],
    "faq": ONLINE_FAQ,
    "service": {
        "name": "Online strength & conditioning coaching",
        "serviceType": "Online personal coaching",
        "url": "https://www.nforce-performance.nl/nl/online-coaching/",
        "areaServed": {"@type": "Place", "name": "Wereldwijd"},
    },
    "content": page_hero(
        "Online coaching",
        "Jouw programma, waar je ook traint",
        "Je hoeft niet in Tilburg te wonen om er iets aan te hebben. Wat telt is dat je programma past bij jouw sport, jouw agenda en jouw herstel, en dat iemand meekijkt of het ook echt werkt.",
        img="/assets/img/online.jpg",
        alt="Atleet bekijkt zijn trainingsprogramma op een telefoon tussen twee oefeningen door.",
        crumbs=[("Online coaching", "/nl/online-coaching/")],
        cta=("/nl/performance-check/", "Plan je Performance Check", "#wat-je-krijgt", "Wat je krijgt"),
    ) + """
<section class="section section--air" id="wat-je-krijgt">
  <div class="wrap">
    <div class="split">
      <div class="reveal" style="display:flex;flex-direction:column;gap:1.25rem">
        <p class="eyebrow">Voor wie dit werkt</p>
        <h2>Voor atleten die willen weten of ze vooruitgaan, in plaats van dat te hopen</h2>
        <ul class="ticks">
          <li>Individuele atleten in ijssport, zaalsport en veldsport</li>
          <li>Sporters die naast hun teamtrainingen gericht willen bouwen</li>
          <li>Atleten in het buitenland &mdash; begeleiding in het Nederlands, Engels of Duits</li>
          <li>Sporters die terugkomen van een blessure en het goed willen opbouwen</li>
        </ul>
        <p class="muted">Wat het <strong>niet</strong> is: een algemeen schema van internet met jouw naam erboven, en geen begeleiding voor wie primair esthetisch traint of nog geen basistechniek heeft. Daar ben ik niet de juiste persoon voor, en dat zeg ik liever vooraf.</p>
      </div>
      <div class="reveal" style="display:flex;flex-direction:column;gap:1.25rem">
        <p class="eyebrow">Wat je krijgt</p>
        <h2>Een programma dat elke vier weken meebeweegt</h2>
        <ul class="ticks">
          <li><strong>Programma op maat in de app</strong>, met video bij elke oefening</li>
          <li><strong>Wekelijkse evaluatie</strong> van belasting, herstel en slaap</li>
          <li><strong>Videofeedback op je techniek</strong></li>
          <li><strong>Testprotocollen die je zelf kunt uitvoeren</strong>, met een hertest na twaalf weken</li>
          <li><strong>Bereikbaarheid voor vragen tussendoor</strong></li>
          <li><strong>Afstemming met je trainer of fysiotherapeut</strong> als dat helpt</li>
        </ul>
      </div>
    </div>
  </div>
</section>

<hr class="blueline">

<section class="section section--air">
  <div class="wrap">
    <div class="section__head reveal">
      <p class="eyebrow">Hoe het loopt</p>
      <h2>Van intake tot hertest</h2>
      <p class="lede">Vier stappen, twaalf weken, en aan het eind een meting in plaats van een gevoel.</p>
    </div>
    <div class="steps reveal">
      <div class="step">
        <div class="step__n">01</div>
        <div class="step__body">
          <h4>Performance Check &mdash; gratis</h4>
          <p>Twintig minuten, online of telefonisch. Je vertelt waar je naartoe wilt, ik vertel eerlijk of ik daarbij de juiste persoon ben.</p>
        </div>
      </div>
      <div class="step">
        <div class="step__n">02</div>
        <div class="step__body">
          <h4>Intake en nulmeting</h4>
          <p>Doelen, wedstrijdkalender, blessurehistorie, beschikbare tijd en faciliteiten. Daarna voer je onder instructie een testbatterij uit die past bij jouw sport.</p>
        </div>
      </div>
      <div class="step">
        <div class="step__n">03</div>
        <div class="step__body">
          <h4>Blokken van vier weken</h4>
          <p>Je programma loopt in blokken. Elke week een korte evaluatie, elke vier weken een herziening op basis van hoe het ging.</p>
        </div>
      </div>
      <div class="step">
        <div class="step__n">04</div>
        <div class="step__body">
          <h4>Hertest na twaalf weken</h4>
          <p>Dezelfde protocollen, dezelfde omstandigheden. Zo zie je zwart-op-wit wat er veranderd is en waar de volgende winst zit.</p>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="section section--air section--panel">
  <div class="wrap">
    <div class="section__head reveal">
      <p class="eyebrow">Tarieven</p>
      <h2>Wat het kost</h2>
    </div>
    <div class="reveal">""" + PLANS + """</div>
  </div>
</section>

""" + ctaband(
        "Twijfel je welk pakket past?",
        "Dat zoeken we in de Performance Check uit, ook als het antwoord is dat je mij nog niet nodig hebt.",
    ) + faq_block("Wat atleten meestal vragen", ONLINE_FAQ) + next_links([
        ("/nl/online-coaching/return-to-play/", "Verdieping", "Return to Play", "Terugkeer na blessure"),
        ("/nl/resultaten/", "Bewijs", "Resultaten &amp; ervaringen", "Zo ziet een rapport eruit"),
    ]),
}


# ---------------------------------------------------------------------------
# 3. RETURN TO PLAY
# ---------------------------------------------------------------------------

RTP_FAQ = [
    ("Vervangt dit mijn fysiotherapeut?",
     "Nee, en dat is een principekwestie. Ik behandel geen blessures en stel geen diagnoses. Ik neem de fase erna voor mijn rekening: van &lsquo;klachtenvrij bij de fysio&rsquo; naar &lsquo;volledige wedstrijdbelasting aankunnen&rsquo;. Waar de behandeling nog loopt, werk ik in afstemming met je behandelaar."),
    ("Wanneer is het moment om te beginnen?",
     "Meestal zodra je behandelaar zegt dat belasting weer opgebouwd mag worden. Eerder kan ook: bij een blessure aan &eacute;&eacute;n been kun je vaak al gericht doortrainen met de rest van je lichaam, zodat je niet twaalf weken achteruitgaat terwijl je herstelt."),
    ("Hoe weet ik of ik echt klaar ben om terug te keren?",
     "Op criteria, niet op gevoel of op een datum. Links-rechtsverschil bij sprong- en krachttests, herstel van sprintvermogen, verdragen van herhaalde belasting en het uitblijven van klachtenreactie na 24 uur. Die criteria staan vooraf vast, zodat de beslissing niet in een emotioneel moment genomen wordt."),
    ("Werk je samen met mijn fysiotherapeut of de medische staf van mijn club?",
     "Standaard, en het liefst vanaf het begin. Bij het Return-to-Play traject is die afstemming inbegrepen: &eacute;&eacute;n lijn tussen revalidatie en krachttraining voorkomt dat je twee programma&rsquo;s tegelijk volgt die elkaar tegenwerken."),
]

RTP = {
    "url": "/nl/online-coaching/return-to-play/",
    "title": "Return to Play — van laatste fysiobehandeling naar wedstrijdfit",
    "description": "Begeleiding in de fase waar het bij veel sporters misgaat: tussen revalidatie en volledige wedstrijdbelasting, met objectieve criteria en in afstemming met je fysiotherapeut.",
    "og_image": "/assets/img/rtp.jpg",
    "hero_img": "/assets/img/rtp.jpg",
    "crumbs": [("Online coaching", "/nl/online-coaching/"), ("Return to Play", "/nl/online-coaching/return-to-play/")],
    "faq": RTP_FAQ,
    "service": {
        "name": "Return to Play begeleiding",
        "serviceType": "Sportmedische trainingsbegeleiding na blessure",
        "url": "https://www.nforce-performance.nl/nl/online-coaching/return-to-play/",
        "offers": [{"@type": "Offer", "name": "Return-to-Play", "price": "249", "priceCurrency": "EUR"}],
    },
    "content": page_hero(
        "Return to Play",
        "De fase waar het meestal misgaat",
        "Je fysiotherapeut zegt dat je klachtenvrij bent. Je team verwacht je terug. En daartussen zit een periode waarin niemand de regie heeft. Dat is precies de fase die ik voor mijn rekening neem.",
        img="/assets/img/rtp.jpg",
        alt="Atleet werkt aan eenbenige landingscontrole in een krachtruimte, met een coach die de uitvoering beoordeelt.",
        crumbs=[("Online coaching", "/nl/online-coaching/"), ("Return to Play", "/nl/online-coaching/return-to-play/")],
        cta=("/nl/performance-check/", "Plan je Performance Check", "#criteria", "Op welke criteria"),
    ) + """
<section class="section section--air">
  <div class="wrap">
    <div class="section__head reveal">
      <p class="eyebrow">Het probleem</p>
      <h2>Klachtenvrij is niet hetzelfde als wedstrijdfit</h2>
      <p class="lede">Revalidatie stopt doorgaans bij het verdwijnen van klachten. Wedstrijdsport begint pas bij herhaalde maximale belasting. Tussen die twee punten zit een gat van weken tot maanden, en daar valt de begeleiding vaak weg.</p>
    </div>
    <div class="grid grid--3 reveal">
      <div class="card">
        <p class="card__label">Wat er misgaat</p>
        <h3>Te vroeg terug</h3>
        <p>De datum bepaalt de terugkeer in plaats van de criteria. Het gevolg is een herbelasting op een been dat nog tien tot twintig procent zwakker is dan het andere &mdash; en dat is precies het patroon achter herhaalde blessures.</p>
      </div>
      <div class="card">
        <p class="card__label">Wat er misgaat</p>
        <h3>Te lang stilstaan</h3>
        <p>Wie drie maanden niets doet met de rest van zijn lichaam, komt zwakker terug dan hij hoefde. Bij een blessure aan &eacute;&eacute;n been kun je vaak gewoon doortrainen &mdash; alleen anders.</p>
      </div>
      <div class="card">
        <p class="card__label">Wat er misgaat</p>
        <h3>Twee programma&rsquo;s tegelijk</h3>
        <p>Revalidatieoefeningen van de fysio, krachttraining van de coach, en niemand die ze op elkaar afstemt. Het resultaat is te veel volume op precies het weefsel dat rust nodig heeft.</p>
      </div>
    </div>
  </div>
</section>

<hr class="blueline">

<section class="section section--air section--panel" id="criteria">
  <div class="wrap">
    <div class="split">
      <div class="reveal" style="display:flex;flex-direction:column;gap:1.25rem">
        <p class="eyebrow">Hoe ik werk</p>
        <h2>Criteria in plaats van een datum</h2>
        <p class="muted">Voordat we beginnen leggen we vast waaraan je moet voldoen om een stap verder te mogen. Die criteria zijn meetbaar, ze staan op papier, en ze zijn niet onderhandelbaar op een dag waarop je je goed voelt.</p>
        <ul class="ticks">
          <li><strong>Links-rechtsverschil</strong> bij eenbenige sprong- en krachttests binnen een vooraf afgesproken marge</li>
          <li><strong>Landings- en remkwaliteit</strong> beoordeeld op video, niet op gevoel</li>
          <li><strong>Herhaalde belasting</strong> verdragen zonder klachtenreactie binnen 24 uur</li>
          <li><strong>Sprint- en richtingsveranderingscapaciteit</strong> terug op je eigen uitgangswaarde</li>
          <li><strong>Volledige teamtraining</strong> afgerond voordat er wedstrijdminuten volgen</li>
        </ul>
      </div>
      <div class="reveal" style="display:flex;flex-direction:column;gap:1.25rem">
        <p class="eyebrow">Wat je krijgt</p>
        <h2>Het Return-to-Play traject</h2>
        <ul class="ticks">
          <li>Volledig op maat, wekelijks bijgesteld</li>
          <li>Wekelijkse videocall en snelle support tussendoor</li>
          <li>Onbeperkte videofeedback op uitvoering</li>
          <li>Maandelijkse testing met vaste protocollen</li>
          <li>Standaard afstemming met je fysiotherapeut of de medische staf</li>
          <li>Een schriftelijk terugkeerplan dat je met je club kunt delen</li>
        </ul>
        <p class="plan__price"><b>&euro;249</b><span>per maand, incl. btw</span></p>
        <p class="faint">Minimale looptijd twaalf weken, daarna maandelijks opzegbaar. Ik neem hier maximaal vijf trajecten tegelijk aan, omdat wekelijkse videocalls en onbeperkte feedback niet schalen.</p>
      </div>
    </div>
  </div>
</section>

<section class="section section--air">
  <div class="wrap">
    <div class="notice reveal">
      <p class="notice__label">Waar de grens ligt</p>
      <p>Ik ben geen fysiotherapeut en geen arts. Ik behandel geen blessures, stel geen diagnoses en beoordeel geen weefselherstel. Wat ik doe is de belasting opbouwen binnen de kaders die je behandelaar aangeeft, en meten of die opbouw klopt. Loopt je behandeling nog, dan begin ik pas na overleg met je behandelaar.</p>
    </div>
  </div>
</section>

""" + ctaband(
        "Bespreek je situatie in twintig minuten",
        "Vertel wat je hebt gehad, waar je nu staat en wat je behandelaar zegt. Ik geef aan of dit traject zinvol is, en zo niet, wat wel.",
    ) + faq_block("Wat sporters en behandelaars meestal vragen", RTP_FAQ) + next_links([
        ("/nl/online-coaching/", "Terug", "Online coaching", "Het reguliere traject"),
        ("/nl/testing/", "Meten", "Testing &amp; analyse", "Objectief uitgangspunt"),
    ]),
}


# ---------------------------------------------------------------------------
# 4. TEAMS
# ---------------------------------------------------------------------------

TEAMS_FAQ = [
    ("Werken jullie ook met jeugdteams?",
     "Ja, en daar gelden andere regels. Bij jeugd ligt de nadruk op bewegingskwaliteit, belastbaarheid en een opbouw die past bij de biologische leeftijd, niet op maximale kracht. Rapportages over minderjarige spelers deel ik alleen met de personen die vooraf zijn afgesproken, met toestemming van ouders."),
    ("Moeten wij eigen materiaal hebben?",
     "Niet per se. Ik werk met wat er is en bouw het programma om jullie faciliteiten heen. Ontbreekt er iets essentieels, dan zeg ik dat eerlijk en zoeken we een alternatief of een oplossing binnen budget."),
    ("Hoe zit het met spelers die revalideren?",
     "Die vallen niet buiten de boot. Ik stem af met jullie fysiotherapeut zodat revalidatie en krachttraining &eacute;&eacute;n lijn vormen, en bouw de terugkeer naar wedstrijdbelasting stapsgewijs op in plaats van in &eacute;&eacute;n keer."),
    ("Komen jullie ook buiten Noord-Brabant?",
     "Binnen ongeveer een uur rijden van Tilburg is dat standaard: heel Noord-Brabant, Zuid-Holland, Gelderland, Limburg en Vlaanderen. Daarbuiten in overleg, met reiskosten in het voorstel."),
    ("Wat kost een seizoenstraject?",
     "Dat hangt af van groepsgrootte, aantal contactmomenten, testfrequentie en reisafstand. Losse testdagen beginnen bij &euro;750 exclusief btw. Voor een seizoenstraject krijg je na de kennismaking een vast voorstel, zodat je vooraf weet waar je aan toe bent."),
]

TEAMS = {
    "url": "/nl/teams/",
    "title": "Kracht &amp; conditie voor teams en clubs | N-Force Performance",
    "description": "Seizoensperiodisering rond je wedstrijdkalender, testdagen en rapportage per speler. Op locatie in Noord-Brabant, Zuid-Holland, Gelderland, Limburg en Vlaanderen.",
    "og_image": "/assets/img/teams.jpg",
    "hero_img": "/assets/img/teams.jpg",
    "crumbs": [("Teams &amp; clubs", "/nl/teams/")],
    "faq": TEAMS_FAQ,
    "service": {
        "name": "Strength & conditioning voor teams en clubs",
        "serviceType": "Teambegeleiding en seizoensperiodisering",
        "url": "https://www.nforce-performance.nl/nl/teams/",
    },
    "content": page_hero(
        "Teams &amp; clubs",
        "Kracht die in het seizoen past",
        "De meeste teams trainen kracht erbovenop in plaats van erin. Het gevolg is zware benen op wedstrijddagen en een selectie die in de tweede seizoenshelft inzakt.",
        img="/assets/img/teams.jpg",
        alt="IJshockeyteam traint gezamenlijk met halters in een krachtruimte naast de ijsbaan.",
        crumbs=[("Teams &amp; clubs", "/nl/teams/")],
        cta=("/nl/performance-check/", "Vraag een voorstel aan", "#wat-je-krijgt", "Wat je krijgt"),
    ) + """
<section class="section section--air" id="wat-je-krijgt">
  <div class="wrap">
    <div class="split">
      <div class="reveal" style="display:flex;flex-direction:column;gap:1.25rem">
        <p class="eyebrow">Voor wie dit werkt</p>
        <h2>Voor clubs die willen kunnen uitleggen waarom er getraind wordt zoals er getraind wordt</h2>
        <ul class="ticks">
          <li>Teams in ijssport, zaalsport en veldsport</li>
          <li>Jeugdopleidingen die een doorlopende leerlijn willen</li>
          <li>Clubs zonder eigen kracht- en conditiespecialist</li>
          <li>Staf die kracht en revalidatie beter wil laten aansluiten</li>
        </ul>
      </div>
      <div class="reveal" style="display:flex;flex-direction:column;gap:1.25rem">
        <p class="eyebrow">Wat je krijgt</p>
        <h2>Een seizoensopzet met meetmomenten, geen los schema</h2>
        <ul class="ticks">
          <li><strong>Seizoensperiodisering</strong> rond je wedstrijdkalender</li>
          <li><strong>Nulmeting van de hele selectie</strong> en hertesten per blok</li>
          <li><strong>Programma per blok</strong>, aangepast op belasting en wedstrijddichtheid</li>
          <li><strong>Rapportage per speler</strong> en een overzicht voor de staf</li>
          <li><strong>Afstemming</strong> met trainers, fysiotherapeut en medische staf</li>
          <li><strong>Begeleiding op locatie</strong> of instructie van jullie eigen staf</li>
        </ul>
      </div>
    </div>
  </div>
</section>

<hr class="blueline">

<section class="section section--air section--panel">
  <div class="wrap">
    <div class="section__head reveal">
      <p class="eyebrow">Hoe het loopt</p>
      <h2>Van kennismaking tot seizoensrapport</h2>
    </div>
    <div class="steps reveal">
      <div class="step">
        <div class="step__n">01</div>
        <div class="step__body">
          <h4>Kennismaking en scan</h4>
          <p>We bespreken je selectie, je kalender, je faciliteiten en waar het volgens de staf misgaat. Daar komt een voorstel uit met een concrete opzet en prijs.</p>
        </div>
      </div>
      <div class="step">
        <div class="step__n">02</div>
        <div class="step__body">
          <h4>Nulmeting van de selectie</h4>
          <p>Een testdag met sprint-, sprong- en krachttesten die passen bij jullie sport. Elke speler krijgt een nulpunt, het team krijgt een profiel.</p>
        </div>
      </div>
      <div class="step">
        <div class="step__n">03</div>
        <div class="step__body">
          <h4>Programma per blok</h4>
          <p>Blokken van vier tot zes weken met een duidelijke opbouw in belasting, afgestemd op wedstrijddichtheid en de trainingen op het veld of het ijs.</p>
        </div>
      </div>
      <div class="step">
        <div class="step__n">04</div>
        <div class="step__body">
          <h4>Hertesten en bijstellen</h4>
          <p>Aan het einde van elk blok meten we opnieuw met dezelfde protocollen. Wat werkte gaat door, wat achterbleef passen we aan.</p>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="section section--air">
  <div class="wrap">
    <div class="section__head reveal">
      <p class="eyebrow">Praktisch</p>
      <h2>Werkgebied en tarieven</h2>
    </div>
    <div class="tablewrap reveal">
      <table>
        <caption class="visually-hidden" style="position:absolute;left:-9999px">Werkgebied en tarieven voor teams en clubs</caption>
        <thead>
          <tr><th scope="col">Onderdeel</th><th scope="col">Hoe het werkt</th><th scope="col">Indicatie</th></tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Losse testdag</strong></td>
            <td>Sprint, sprong en kracht voor de hele selectie, rapport per speler plus teamoverzicht binnen een week.</td>
            <td><span class="num">vanaf &euro;750</span> excl. btw</td>
          </tr>
          <tr>
            <td><strong>Seizoenstraject</strong></td>
            <td>Periodisering, blokprogramma&rsquo;s, testmomenten en rapportage over het hele seizoen.</td>
            <td>Vast voorstel na kennismaking</td>
          </tr>
          <tr>
            <td><strong>Stafbegeleiding</strong></td>
            <td>Ik lever het programma en de testopzet, jullie eigen staf voert uit met instructie en periodieke evaluatie.</td>
            <td>Op offerte</td>
          </tr>
          <tr>
            <td><strong>Werkgebied</strong></td>
            <td>Op locatie binnen ongeveer een uur rijden van Tilburg: heel Noord-Brabant, Zuid-Holland, Gelderland, Limburg en Vlaanderen.</td>
            <td>Daarbuiten in overleg</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</section>

""" + ctaband(
        "Benieuwd hoe dit voor jouw selectie uitpakt?",
        "Dat kost een gesprek van twintig minuten. We bespreken je kalender, je faciliteiten en waar het volgens de staf misgaat &mdash; daarna krijg je een voorstel met een concrete opzet en prijs.",
        primary=("/nl/performance-check/", "Vraag een voorstel aan"),
        secondary=("/nl/testing/", "Eerst alleen een testdag"),
    ) + faq_block("Wat clubs meestal vragen", TEAMS_FAQ) + next_links([
        ("/nl/testing/", "Instap", "Testing &amp; analyse", "Losse testdag voor je selectie"),
        ("/nl/resultaten/", "Bewijs", "Resultaten &amp; ervaringen", "Zo ziet een teamprofiel eruit"),
    ]),
}


# ---------------------------------------------------------------------------
# 5. TESTING
# ---------------------------------------------------------------------------

TESTING_FAQ = [
    ("Hoeveel atleten kunnen er op een dag?",
     "Een selectie van ongeveer twintig spelers past in een dagdeel, mits er genoeg ruimte is om in groepjes te rouleren. Grotere groepen verdelen we over meerdere dagdelen, zodat de kwaliteit van de metingen niet lijdt onder de haast."),
    ("Wat gebeurt er met de gegevens?",
     "Testresultaten zijn persoonsgegevens en bij gezondheidsinformatie zelfs bijzondere persoonsgegevens. Ik deel ze alleen met de vooraf afgesproken personen, bij minderjarigen met toestemming van ouders, en gebruik ze niet voor promotie zonder aparte toestemming."),
    ("Is een hertest verplicht?",
     "Nee, maar zonder hertest weet je niet of het gewerkt heeft. De echte waarde van testen zit in de vergelijking, niet in de eerste uitslag."),
    ("Waarmee worden onze waarden vergeleken?",
     "Met een referentiegroep waarvan de bron, de populatie, de omvang, het protocol en de meetfout in het rapport staan. Is er voor een test geen bruikbare referentie op jullie niveau, dan staat dat er ook en gebruiken we de interne verdeling van de selectie."),
]

TESTING = {
    "url": "/nl/testing/",
    "title": "Sporttestdag voor clubs en atleten — sprint, sprong, kracht",
    "description": "Binnen een dagdeel een objectief beeld van je selectie of van jezelf, met een rapport waar concrete trainingsbeslissingen uit volgen. Testdagen vanaf €750.",
    "og_image": "/assets/img/testing.jpg",
    "hero_img": "/assets/img/testing.jpg",
    "crumbs": [("Testing &amp; analyse", "/nl/testing/")],
    "faq": TESTING_FAQ,
    "service": {
        "name": "Testing & analyse",
        "serviceType": "Sportfysieke testafname en rapportage",
        "url": "https://www.nforce-performance.nl/nl/testing/",
        "offers": [{"@type": "Offer", "name": "Testdag", "price": "750", "priceCurrency": "EUR",
                    "valueAddedTaxIncluded": False}],
    },
    "content": page_hero(
        "Testing &amp; analyse",
        "Weten waar je staat, in cijfers",
        "Zonder nulmeting is elke trainingskeuze een aanname. Een testdag levert je binnen een dagdeel een objectief beeld op van je selectie of van jezelf, en een rapport waar concrete trainingsbeslissingen uit volgen.",
        img="/assets/img/testing.jpg",
        alt="Sprinttest met tijdpoortjes op een atletiekbaan, coach noteert de uitslag.",
        crumbs=[("Testing &amp; analyse", "/nl/testing/")],
        cta=("/nl/performance-check/", "Testdag aanvragen", "#wat-meten-we", "Wat we meten"),
    ) + """
<section class="section section--air" id="wat-meten-we">
  <div class="wrap">
    <div class="split">
      <div class="reveal" style="display:flex;flex-direction:column;gap:1.25rem">
        <p class="eyebrow">Voor wie dit werkt</p>
        <h2>Voor wie een nulpunt nodig heeft</h2>
        <ul class="ticks">
          <li>Clubs die aan het begin van het seizoen een nulpunt willen</li>
          <li>Teams die na een blok willen weten of het gewerkt heeft</li>
          <li>Individuele atleten die hun sterke en zwakke kanten in kaart willen</li>
          <li>Praktijken die een objectieve maat willen bij terugkeer naar sport</li>
        </ul>
      </div>
      <div class="reveal" style="display:flex;flex-direction:column;gap:1.25rem">
        <p class="eyebrow">Wat we meten</p>
        <h2>Zes onderdelen, vaste protocollen</h2>
        <ul class="ticks">
          <li>Sprint over <span class="num">10</span> en <span class="num">30</span> meter met tijdregistratie</li>
          <li>Sprongkracht: countermovement jump en squat jump</li>
          <li>Kracht en krachtuithouding, met inschatting van maximaalkracht</li>
          <li>Links-rechtsverschillen en belastbaarheid</li>
          <li>Bewegingskwaliteit bij de basisoefeningen</li>
          <li>Rapport per atleet plus een teamoverzicht met vergelijking</li>
        </ul>
      </div>
    </div>
  </div>
</section>

<hr class="blueline">

<section class="section section--air section--panel">
  <div class="wrap">
    <div class="section__head reveal">
      <p class="eyebrow">Hoe het loopt</p>
      <h2>Van aanvraag tot adviesgesprek</h2>
    </div>
    <div class="steps reveal">
      <div class="step">
        <div class="step__n">01</div>
        <div class="step__body">
          <h4>Aanvraag en afstemming</h4>
          <p>We bepalen welke testen zinvol zijn voor jouw sport en doel, en wat er praktisch nodig is aan ruimte, tijd en materiaal.</p>
        </div>
      </div>
      <div class="step">
        <div class="step__n">02</div>
        <div class="step__body">
          <h4>Testdag</h4>
          <p>Op locatie, in een vaste volgorde met standaard warming-up zodat de uitslagen vergelijkbaar zijn. Een selectie van twintig spelers past doorgaans in een dagdeel.</p>
        </div>
      </div>
      <div class="step">
        <div class="step__n">03</div>
        <div class="step__body">
          <h4>Rapport</h4>
          <p>Binnen een week ontvang je een rapport: per atleet de uitslagen met context, en voor teams een overzicht waarin je snel ziet waar de aandacht heen moet.</p>
        </div>
      </div>
      <div class="step">
        <div class="step__n">04</div>
        <div class="step__body">
          <h4>Adviesgesprek</h4>
          <p>We lopen de uitkomsten door en vertalen ze naar trainingskeuzes, ook als je daarna zelf verder gaat zonder mij.</p>
        </div>
      </div>
    </div>
    <p class="smallprint" style="margin-top:2rem">Testdagen vanaf <span class="num">&euro;750</span> exclusief btw, afhankelijk van groepsgrootte, reisafstand en de omvang van de rapportage. Testing kan los, of als vast onderdeel van een seizoenstraject. Werkgebied: op locatie binnen ongeveer een uur rijden van Tilburg &mdash; heel Noord-Brabant, Zuid-Holland, Gelderland, Limburg en Vlaanderen. Daarbuiten in overleg, met reiskosten in het voorstel.</p>
  </div>
</section>

""" + ctaband(
        "Wil je weten waar je selectie staat?",
        "Vertel in twintig minuten wat je wilt weten en van hoeveel spelers. Daarna krijg je een voorstel met testopzet, dagdeel en prijs.",
        primary=("/nl/performance-check/", "Testdag aanvragen"),
        secondary=("/nl/resultaten/", "Bekijk een voorbeeldrapport"),
    ) + faq_block("Wat clubs en atleten meestal vragen", TESTING_FAQ) + next_links([
        ("/nl/resultaten/referentiewaarden/", "Onderbouwing", "Referentiewaarden", "Waar de bereiken vandaan komen"),
        ("/nl/teams/", "Vervolg", "Teams &amp; clubs", "Van testdag naar seizoenstraject"),
    ]),
}


# ---------------------------------------------------------------------------
# 6. RESULTATEN
# ---------------------------------------------------------------------------

RESULTATEN = {
    "url": "/nl/resultaten/",
    "title": "Resultaten, testrapporten en referentiewaarden | N-Force",
    "description": "Zo ziet een testrapport eruit, zo zijn de referentiebereiken opgebouwd, en zo vergelijk je je eigen waarde. Geen beloftes, wel metingen.",
    "og_image": "/assets/img/testing.jpg",
    "crumbs": [("Resultaten", "/nl/resultaten/")],
    "scripts": '<script src="/assets/js/benchmarks.js"></script>',
    "content": page_hero(
        "Resultaten &amp; ervaringen",
        "Wat het oplevert",
        "Geen beloftes, maar metingen en ervaringen van de mensen met wie ik werk. Cijfers staan hier geanonimiseerd, quotes alleen met toestemming van de betrokkene.",
        img="/assets/img/testing.jpg",
        alt="Coach noteert testuitslagen op een klembord naast een sprintopstelling.",
        crumbs=[("Resultaten", "/nl/resultaten/")],
    ) + """
<section class="section section--air" id="check">
  <div class="wrap">
    <div class="section__head reveal">
      <p class="eyebrow">Zelf proberen</p>
      <h2>Waar sta jij?</h2>
      <p class="lede">Vul een eigen testwaarde in en zie waar die valt binnen het referentiebereik. Er wordt niets opgeslagen en niets verstuurd.</p>
    </div>

    <div class="split">
      <div class="bench reveal" data-bench>
        <div class="bench__form">
          <div class="field">
            <label for="bench-test">Test</label>
            <select id="bench-test" data-bench-test></select>
          </div>
          <div class="field">
            <label for="bench-value">Jouw waarde</label>
            <input id="bench-value" type="text" inputmode="decimal" placeholder="bijv. 46" data-bench-value>
          </div>
        </div>
        <div>
          <div class="meter" data-bench-meter></div>
          <div class="meter__scale" data-bench-scale></div>
        </div>
        <p class="bench__out" data-bench-out></p>
        <p class="faint"><strong>Referentiegroep:</strong> <span data-bench-source></span></p>
      </div>
      <div class="reveal" style="display:flex;flex-direction:column;gap:1.25rem">
        <div class="notice">
          <p class="notice__label">Hoe je dit leest</p>
          <p>Een referentiebereik is geen rapportcijfer. Het zegt waar de middenmoot van een vergelijkbare groep ligt, meer niet. Wat je ermee doet hangt af van je sport, je positie en je overige waarden. &Eacute;&eacute;n test zegt weinig; een volledig profiel zegt waar je moet beginnen.</p>
        </div>
        <a class="textlink" href="/nl/resultaten/referentiewaarden/">Bron, populatie en meetfout per test <span aria-hidden="true">&rarr;</span></a>
      </div>
    </div>
  </div>
</section>

<hr class="blueline">

<section class="section section--air section--panel">
  <div class="wrap">
    <div class="section__head reveal">
      <p class="eyebrow">Rapportage</p>
      <h2>Wat je terugkrijgt na een test</h2>
      <p class="lede">Een uitslag is pas nuttig als hij een beslissing verandert. Zo ziet een pagina uit zo&rsquo;n rapport eruit.</p>
    </div>

    <div class="notice notice--todo reveal" style="margin-bottom:1.5rem">
      <p class="notice__label">Voorbeeld, geen echte speler</p>
      <p>Onderstaande waarden zijn verzonnen en dienen alleen om de opzet te laten zien.</p>
    </div>

    <div class="readout reveal">
      <div class="readout__row">
        <div class="readout__top">
          <span class="readout__test">Verspringen vanuit stand</span>
          <span class="readout__val">258 cm</span>
        </div>
        <p>Boven het referentiebereik. Explosiviteit is niet de beperkende factor.</p>
        <p class="readout__dec"><b>Beslissing:</b> geen extra sprongvolume. Die tijd gaat naar de overdracht naar snelheid op het ijs.</p>
      </div>
      <div class="readout__row">
        <div class="readout__top">
          <span class="readout__test">Sit and reach</span>
          <span class="readout__val">&minus;7 cm</span>
        </div>
        <p>Raakt de tenen niet. Beperkte achterste keten en heup, terwijl de rest van het profiel sterk is.</p>
        <p class="readout__dec"><b>Beslissing:</b> mobiliteitsvlag. Acht minuten na elke sessie, dagelijks op vrije dagen. Geen aanpassing aan het krachtblok.</p>
      </div>
      <div class="readout__row">
        <div class="readout__top">
          <span class="readout__test">5-10-5 shuttle</span>
          <span class="readout__val">5,33 s</span>
        </div>
        <p>Buiten het bereik dat we voor deze groep hanteren, net als de rest van de selectie. Bij iemand die 258 centimeter springt is dat geen behendigheidsprobleem maar een tijdmeting die niet vergelijkbaar is.</p>
        <p class="readout__dec"><b>Beslissing:</b> geen conclusie op deze test. Hertest onder identieke omstandigheden, en tot die tijd de interne verdeling van de selectie gebruiken in plaats van een externe band.</p>
      </div>
    </div>

    <p class="smallprint" style="margin-top:1.5rem">Elk rapport vermeldt welke referentiegroep is gebruikt en waar die vandaan komt. Is er geen passende referentie, dan staat dat er ook, en is de waarde een startpunt voor de hertest in plaats van een oordeel.</p>
  </div>
</section>

<section class="section section--air">
  <div class="wrap">
    <div class="split">
      <div class="reveal" style="display:flex;flex-direction:column;gap:1.25rem">
        <p class="eyebrow">Ervaringen</p>
        <h2>Wat spelers en staf zeggen</h2>
        <p class="muted">De eerste hertestronde loopt. Ervaringen van spelers, staf en fysiotherapeuten komen hier zodra ze er zijn &mdash; met naam, rol en in hun eigen woorden, en alleen met toestemming.</p>
        <p class="muted">N-Force Performance is net gestart. Ik zet hier liever niets neer dan iets wat ik niet kan onderbouwen: geen gekochte reviews, geen cijfers zonder hertest, geen namen zonder toestemming. Wat er straks staat, is echt gemeten en echt gezegd.</p>
        <p class="muted">In de tussentijd kun je me beoordelen op waar ik werk, wat ik heb geleerd, hoe ik te werk ga, en op het gesprek zelf.</p>
      </div>
      <div class="reveal">
        <div class="card">
          <p class="card__label">Met mij gewerkt?</p>
          <h3>Dan hoor ik graag wat het je heeft opgeleverd</h3>
          <p>Ook als het tegenviel. Drie vragen helpen om er iets bruikbaars van te maken:</p>
          <ul class="ticks">
            <li>Waar liep je tegenaan voordat we begonnen?</li>
            <li>Wat hebben we concreet gedaan?</li>
            <li>Wat merk je nu, op het veld, in je herstel of in de cijfers?</li>
          </ul>
          <p class="faint">Je bepaalt zelf of je met naam, alleen met voornaam of anoniem wordt genoemd, en je kunt het altijd laten weghalen.</p>
          <a class="textlink" href="mailto:nick@nforce-performance.nl?subject=Mijn%20ervaring%20met%20N-Force">Stuur je ervaring <span aria-hidden="true">&rarr;</span></a>
        </div>
      </div>
    </div>
  </div>
</section>

""" + ctaband(
        "Zelf meetbaar vooruit? Begin met een nulmeting.",
        "In twintig minuten bepalen we welke test uitsluitsel geeft over jouw grootste beperkende factor, en of een traject zinvol is.",
    ) + next_links([
        ("/nl/resultaten/referentiewaarden/", "Onderbouwing", "Referentiewaarden", "Bron, populatie en meetfout"),
        ("/nl/testing/", "Meten", "Testing &amp; analyse", "Testdag voor jou of je team"),
    ]),
}


# ---------------------------------------------------------------------------
# 7. REFERENTIEWAARDEN
# ---------------------------------------------------------------------------

REFERENTIE = {
    "url": "/nl/resultaten/referentiewaarden/",
    "title": "Referentiewaarden: bron, populatie en meetfout | N-Force",
    "description": "Elke referentiewaarde op deze site komt ergens vandaan. Hier staat per test welke groep, welke omvang, welk protocol en welke meetfout er achter zit.",
    "og_image": "/assets/img/testing.jpg",
    "crumbs": [("Resultaten", "/nl/resultaten/"), ("Referentiewaarden", "/nl/resultaten/referentiewaarden/")],
    "content": page_hero(
        "Onderbouwing",
        "Waar de referentiewaarden vandaan komen",
        "Een bereik zonder bron is een mening met een getal erbij. Daarom staat hier per test welke groep is gebruikt, hoe groot die was, welk protocol is gevolgd en hoe groot de meetfout is.",
        crumbs=[("Resultaten", "/nl/resultaten/"), ("Referentiewaarden", "/nl/resultaten/referentiewaarden/")],
    ) + """
<section class="section section--air">
  <div class="wrap">
    <div class="notice notice--todo reveal" style="margin-bottom:2rem">
      <p class="notice__label">Nog in te vullen</p>
      <p>De bereiken in de check op de resultatenpagina staan er nu als plaatshouder, zodat de werking zichtbaar is. Ze zijn nog niet onderbouwd en mogen niet als norm gelezen worden. Vul ze in <code>assets/js/benchmarks.js</code> in en werk deze pagina bij; verwijder daarna dit blok.</p>
    </div>

    <div class="section__head reveal">
      <p class="eyebrow">De regel</p>
      <h2>Geen band zonder bron</h2>
      <p class="lede">Elke referentiewaarde die ik toon, is voorzien van zes velden. Ontbreekt een van die velden, dan toon ik de waarde niet als band maar als interne vergelijking binnen de eigen selectie.</p>
    </div>

    <div class="tablewrap reveal">
      <table>
        <thead><tr><th scope="col">Veld</th><th scope="col">Wat er staat</th><th scope="col">Waarom het uitmaakt</th></tr></thead>
        <tbody>
          <tr><td><strong>Bron</strong></td><td>Auteur, publicatie en jaar, of &ldquo;eigen metingen N-Force&rdquo;.</td><td>Zonder herkomst kun je de waarde niet controleren en dus niet vertrouwen.</td></tr>
          <tr><td><strong>Populatie</strong></td><td>Sport, geslacht, niveau en seizoensfase.</td><td>Een band voor eerstedivisiespelers zegt weinig over een jeugdselectie.</td></tr>
          <tr><td><strong>Omvang en leeftijd</strong></td><td>Aantal gemeten personen en de leeftijdsrange.</td><td>Bij een kleine groep is het bereik breder dan het lijkt.</td></tr>
          <tr><td><strong>Protocol</strong></td><td>Uitvoering, hulpmiddel, aantal pogingen en welke telt.</td><td>Een CMJ met armzwaai levert andere cijfers dan een met handen op de heupen.</td></tr>
          <tr><td><strong>Meetfout</strong></td><td>Typische fout in dezelfde eenheid als de test.</td><td>Verschillen kleiner dan de meetfout zijn ruis, geen vooruitgang.</td></tr>
          <tr><td><strong>Laatst bijgewerkt</strong></td><td>Datum van de laatste controle of aanvulling.</td><td>Referenties verouderen; een datum maakt zichtbaar hoe actueel ze zijn.</td></tr>
        </tbody>
      </table>
    </div>
  </div>
</section>

<hr class="blueline">

<section class="section section--air section--panel">
  <div class="wrap">
    <div class="section__head reveal">
      <p class="eyebrow">Per test</p>
      <h2>De tests die ik gebruik</h2>
      <p class="lede">Vul per test de zes velden in. Zolang een veld leeg is, staat de test hier met de vermelding dat er nog geen onderbouwde band is.</p>
    </div>

    <div class="tablewrap reveal">
      <table>
        <thead><tr><th scope="col">Test</th><th scope="col">Meet</th><th scope="col">Protocol</th><th scope="col">Referentie</th></tr></thead>
        <tbody>
          <tr><td><strong>Countermovement jump</strong></td><td>Explosieve kracht met elastische bijdrage</td><td>Handen op de heupen, beste van drie, contactmat of app</td><td>Nog in te vullen</td></tr>
          <tr><td><strong>Squat jump</strong></td><td>Concentrische kracht vanuit stilstand</td><td>Drie seconden stilstaan in halve hurkzit, geen tegenbeweging</td><td>Nog in te vullen</td></tr>
          <tr><td><strong>Verspringen vanuit stand</strong></td><td>Horizontale explosiviteit</td><td>Beide voeten gelijk, meting bij dichtstbijzijnde contactpunt</td><td>Nog in te vullen</td></tr>
          <tr><td><strong>Sprint 10 m</strong></td><td>Acceleratie</td><td>Staande start, tijdpoortjes, beste van drie, volledige rust</td><td>Nog in te vullen</td></tr>
          <tr><td><strong>Sprint 30 m</strong></td><td>Acceleratie en topsnelheid</td><td>Zelfde start en poortjes, tussentijd op 10 m</td><td>Nog in te vullen</td></tr>
          <tr><td><strong>Laterale sprong links/rechts</strong></td><td>Eenbenige explosiviteit en asymmetrie</td><td>Drie per been, verschil in procenten gerapporteerd</td><td>Nog in te vullen</td></tr>
          <tr><td><strong>5-10-5 shuttle</strong></td><td>Richtingsverandering</td><td>Vaste ondergrond en schoeisel, beste van twee</td><td>Geen bruikbare band &mdash; interne verdeling</td></tr>
        </tbody>
      </table>
    </div>

    <div class="notice reveal" style="margin-top:2rem">
      <p class="notice__label">Als er geen referentie is</p>
      <p>Voor sommige tests bestaat op dit niveau geen bruikbare referentiegroep, of zijn de gepubliceerde waarden gemeten met apparatuur die niet vergelijkbaar is met de mijne. In dat geval staat er geen band. Je waarde wordt dan vergeleken met de rest van je selectie en dient als nulpunt voor je hertest. Dat is minder spannend en een stuk eerlijker.</p>
    </div>
  </div>
</section>

""" + ctaband(
        "Wil je je eigen waarden laten meten?",
        "Een testdag levert je binnen een dagdeel een profiel met vaste protocollen, en een rapport waarin per test staat waarmee vergeleken is.",
        primary=("/nl/testing/", "Bekijk testing &amp; analyse"),
        secondary=("/nl/performance-check/", "Plan je Performance Check"),
    ) + next_links([
        ("/nl/resultaten/", "Terug", "Resultaten &amp; ervaringen", "De check en het voorbeeldrapport"),
        ("/nl/testing/", "Meten", "Testing &amp; analyse", "Testdag voor jou of je team"),
    ]),
}


# ---------------------------------------------------------------------------
# 8. OVER
# ---------------------------------------------------------------------------

OVER = {
    "url": "/nl/over/",
    "title": "Over N-Force Performance en Nick Bergman",
    "description": "Waarom N-Force bestaat: sporters worden in de gym sterker zonder sneller te worden, en vrijwel niemand meet of de training werkt. Dit is de aanpak daarachter.",
    "og_image": "/assets/img/detail.jpg",
    "hero_img": "/assets/img/detail.jpg",
    "crumbs": [("Over N-Force", "/nl/over/")],
    "content": page_hero(
        "Over N-Force",
        "Kracht is capaciteit. Wat je ermee doet is de vraag.",
        "De meeste sporters worden in de gym meetbaar sterker zonder dat het op het veld of het ijs iets oplevert. N-Force Performance bestaat om dat gat te dichten &mdash; met een systeem, en met een meting die laat zien of het klopt.",
        img="/assets/img/detail.jpg",
        alt="Stilleven in koud licht: opengeslagen notitieboek met een trainingsschema naast een ijshockeystick.",
        crumbs=[("Over N-Force", "/nl/over/")],
    ) + """
<section class="section section--air">
  <div class="wrap wrap--narrow">
    <div class="section__head reveal">
      <p class="eyebrow">Het probleem</p>
      <h2>Sterker worden is niet hetzelfde als sneller worden</h2>
    </div>
    <div class="measure reveal" style="display:flex;flex-direction:column;gap:1.25rem">
      <p class="muted">Je bent het afgelopen jaar sterker geworden. Je squat is omhoog gegaan, je trekt meer van de grond, en in de gym voel je verschil. Op het veld voel je dat verschil niet.</p>
      <p class="muted">Dat is geen inbeelding en het is geen kwestie van harder willen. Kracht en explosiviteit zijn verwante eigenschappen, maar ze zijn niet hetzelfde en ze ontstaan niet op dezelfde manier. In de meeste sportsituaties heb je geen driehonderd milliseconden om je maximale kracht op te bouwen &mdash; je hebt er honderdvijftig, soms minder. Wat er in dat venster gebeurt, bepaalt je prestatie.</p>
      <p class="muted">Daar komt bij dat er vrijwel nooit gemeten wordt. Zonder eenvoudige, herhaalbare tests weet niemand of een programma werkt. Er wordt op gevoel gestuurd, en gevoel is een slechte sensor voor explosiviteit.</p>
    </div>
  </div>
</section>

<hr class="blueline">

<section class="section section--air section--panel">
  <div class="wrap">
    <div class="section__head reveal">
      <p class="eyebrow">De aanpak</p>
      <h2>Drie principes waar niet van afgeweken wordt</h2>
    </div>
    <div class="grid grid--3 reveal">
      <div class="card">
        <p class="card__label">01</p>
        <h3>Meten, niet aannemen</h3>
        <p>Elk traject begint met een nulmeting en eindigt met dezelfde tests onder dezelfde omstandigheden. De uitslag bepaalt wat er verandert, niet een onderbuikgevoel. Verschillen kleiner dan de meetfout tellen niet mee.</p>
      </div>
      <div class="card">
        <p class="card__label">02</p>
        <h3>Passen bij de week die je hebt</h3>
        <p>Afgestemd op je sport, je seizoensfase, je faciliteiten en je agenda. Een programma dat alleen werkt in een ideale week werkt in de praktijk nooit. Loopt je belasting of herstel anders, dan gaat het programma mee.</p>
      </div>
      <div class="card">
        <p class="card__label">03</p>
        <h3>Eerlijk over wat niet kan</h3>
        <p>Geen beloftes over centimeters, geen gekochte reviews, geen schaarste die niet klopt. Als ik niet de juiste persoon voor je ben, hoor je dat in het eerste gesprek. Dat kost me af en toe een klant en het is de reden dat de rest blijft.</p>
      </div>
    </div>
  </div>
</section>

<section class="section section--air">
  <div class="wrap">
    <div class="split">
      <div class="reveal" style="display:flex;flex-direction:column;gap:1.25rem">
        <p class="eyebrow">De coach</p>
        <h2>Nick Bergman</h2>
        <p class="muted">Ik ben performance coach bij Tilburg Trappers, dat uitkomt in de Duitse Oberliga, en afgestudeerd aan Fontys Sporthogeschool met specialisatie in strength &amp; conditioning en sportmedische training.</p>
        <p class="muted">In een topsportomgeving is geen ruimte voor aannames. Een programma moet passen bij de sport, de atleet en de fase van het seizoen, en er moet gemeten worden of het werkt &mdash; want in februari zie je precies wie in augustus goed heeft opgebouwd. Die manier van werken neem ik mee naar elke atleet en elke club waarmee ik werk, of dat nu een selectie is of iemand die in zijn eentje in een sportschool traint.</p>
        <ul class="ticks">
          <li>Strength &amp; conditioning specialist</li>
          <li>Sportmedische achtergrond en return to play</li>
          <li>Dagelijkse praktijkervaring in een topsportomgeving</li>
          <li>Begeleiding in het Nederlands, Engels of Duits</li>
        </ul>
      </div>
      <div class="split__media reveal">
        <img src="/assets/img/about.jpg" alt="Nick Bergman aan het werk langs de boarding tijdens een training." width="900" height="675" loading="lazy" onerror="this.style.display=&#39;none&#39;">
      </div>
    </div>
  </div>
</section>

<section class="section section--air section--panel">
  <div class="wrap">
    <div class="notice reveal">
      <p class="notice__label">Waar de grens ligt</p>
      <p>Ik ben geen fysiotherapeut en geen arts. Ik behandel geen blessures en stel geen diagnoses. Wat ik doe is training: belasting opbouwen, meten en bijsturen &mdash; waar nodig in afstemming met je behandelaar. Die grens houd ik strak, omdat het de enige manier is om er voor beide partijen iets aan te hebben.</p>
    </div>
  </div>
</section>

""" + ctaband(
        "Benieuwd of dit bij je past?",
        "Twintig minuten, gratis, en aan het eind weet je of een traject zinvol is. Ook als het antwoord nee is.",
    ) + next_links([
        ("/nl/online-coaching/", "Diensten", "Online coaching", "Voor individuele atleten"),
        ("/nl/teams/", "Diensten", "Teams &amp; clubs", "Voor selecties en staf"),
    ]),
}


# ---------------------------------------------------------------------------
# 9. PERFORMANCE CHECK
# ---------------------------------------------------------------------------

CHECK_FAQ = [
    ("Is dit echt gratis?",
     "Ja. Er komt geen factuur en er is geen verplichting. Het kost mij twintig minuten en het bespaart ons allebei tijd als blijkt dat we niet bij elkaar passen."),
    ("Is dit een verkoopgesprek?",
     "Nee. Ik werk niet met kortingen, timers of druk. Als coaching op dit moment niet het juiste is voor je, zeg ik dat en krijg je van mij een suggestie voor wat wel."),
    ("Moet ik iets voorbereiden?",
     "Nee, maar het helpt als je weet welke sport en op welk niveau je speelt, hoeveel je nu traint, en wat je concreet wilt bereiken. Heb je recente testwaarden of een verslag van je fysiotherapeut, neem die er dan bij."),
    ("Kan het ook in het Engels of Duits?",
     "Ja. Geef het door bij het boeken, dan voeren we het gesprek in de taal die jij wilt."),
    ("Ik wil liever eerst mailen.",
     "Dat kan. Gebruik het formulier onderaan deze pagina of mail rechtstreeks naar nick@nforce-performance.nl. Ik reageer meestal binnen &eacute;&eacute;n werkdag."),
]

CHECK = {
    "url": "/nl/performance-check/",
    "title": "Performance Check — gratis gesprek van twintig minuten",
    "description": "Twintig minuten, gratis en online. Je krijgt een inschatting van je grootste beperkende factor, welke test daar uitsluitsel over geeft, en of coaching zinvol is.",
    "og_image": "/assets/img/hero.jpg",
    "crumbs": [("Performance Check", "/nl/performance-check/")],
    "faq": CHECK_FAQ,
    "service": {
        "name": "Performance Check",
        "serviceType": "Gratis kennismakingsgesprek",
        "url": "https://www.nforce-performance.nl/nl/performance-check/",
        "offers": [{"@type": "Offer", "price": "0", "priceCurrency": "EUR"}],
    },
    "content": page_hero(
        "Gratis &middot; twintig minuten &middot; online",
        "De Performance Check",
        "Geen intakeformulier, geen wachttijd. Je kiest een tijdstip, we bellen twintig minuten, en daarna weet je waar je staat en of ik daarbij iets te bieden heb.",
        crumbs=[("Performance Check", "/nl/performance-check/")],
    ) + """
<section class="section section--air">
  <div class="wrap">
    <div class="split">
      <div class="reveal" style="display:flex;flex-direction:column;gap:1.25rem">
        <p class="eyebrow">Wat je eruit haalt</p>
        <h2>Drie dingen, in twintig minuten</h2>
        <ul class="ticks">
          <li><strong>Een inschatting van je grootste beperkende factor.</strong> Kracht, snelheid van krachtopbouw, elastische capaciteit of belastbaarheid &mdash; op basis van wat je vertelt over je sport en je training.</li>
          <li><strong>Welke test daar uitsluitsel over geeft.</strong> Concreet, met protocol, zodat je hem desnoods zelf kunt uitvoeren.</li>
          <li><strong>Of begeleiding zinvol is, en welke vorm.</strong> Online coaching, alleen een testdag, teambegeleiding &mdash; of voorlopig niets.</li>
        </ul>
        <div class="notice">
          <p class="notice__label">Wat het niet is</p>
          <p>Geen verkoopgesprek. Als ik niet de juiste persoon voor je ben, hoor je dat in dit gesprek en niet erna. Er volgt geen aanbod met een houdbaarheidsdatum en ik bel niet achteraf na.</p>
        </div>
      </div>

      <div class="reveal" style="display:flex;flex-direction:column;gap:1rem">
        <p class="eyebrow">Kies een tijdstip</p>
        <!-- ================================================================
             AGENDA-EMBED
             Vervang het blok hieronder door je Cal.com- of Calendly-embed.

             Cal.com voorbeeld:
             <div style="width:100%;height:100%;overflow:scroll" id="my-cal-inline"></div>
             <script type="text/javascript">...cal embed snippet...</script>

             Calendly voorbeeld:
             <div class="calendly-inline-widget"
                  data-url="https://calendly.com/JOUW-NAAM/performance-check"
                  style="min-width:320px;height:700px"></div>
             <script src="https://assets.calendly.com/assets/external/widget.js" async></script>
             ================================================================ -->
        <div class="embedbox">
          <div>
            <p><strong>Hier komt je boekingsagenda.</strong></p>
            <p style="margin-top:.75rem">Plaats hier de embed van Cal.com of Calendly met een slot van twintig minuten. Zolang die er niet staat, kunnen bezoekers het formulier hieronder gebruiken &mdash; maar dat kost je conversie, dus zet dit als eerste live.</p>
          </div>
        </div>
        <p class="faint">Liever direct contact? <a href="https://wa.me/31622680892" rel="noopener">WhatsApp</a> of bel <a class="num" href="tel:+31622680892">+31 6 22 68 08 92</a>.</p>
      </div>
    </div>
  </div>
</section>

<hr class="blueline">

<section class="section section--air section--panel">
  <div class="wrap">
    <div class="split">
      <div class="reveal">
        <p class="eyebrow">Liever mailen</p>
        <h2>Drie velden, meer heb ik niet nodig</h2>
        <p class="muted" style="margin-top:1rem">Vul dit in en ik reageer meestal binnen &eacute;&eacute;n werkdag. Deel hier nog geen medische details of blessuregegevens &mdash; die bespreken we in het gesprek.</p>
      </div>
      <form class="form reveal" action="https://formspree.io/f/JOUW-FORM-ID" method="POST">
        <!-- Vervang het action-adres door je eigen formulierendpoint
             (Formspree, Netlify Forms, Basin of je eigen backend). -->
        <div class="field">
          <label for="f-naam">Naam</label>
          <input id="f-naam" name="naam" type="text" required autocomplete="name">
        </div>
        <div class="field">
          <label for="f-mail">E-mailadres</label>
          <input id="f-mail" name="email" type="email" required autocomplete="email">
        </div>
        <div class="field">
          <label for="f-onderwerp">Waar gaat het over?</label>
          <select id="f-onderwerp" name="onderwerp">
            <option>Online coaching</option>
            <option>Return to Play</option>
            <option>Teams &amp; clubs</option>
            <option>Testing &amp; analyse</option>
            <option>Iets anders</option>
          </select>
          <span class="field__hint">Sport, niveau en je hoofdvraag mogen erbij, maar hoeft niet.</span>
        </div>
        <div class="field">
          <label for="f-bericht">Bericht</label>
          <textarea id="f-bericht" name="bericht"></textarea>
        </div>
        <div class="hp" aria-hidden="true">
          <label for="f-website">Laat dit veld leeg</label>
          <input id="f-website" name="_gotcha" type="text" tabindex="-1" autocomplete="off">
        </div>
        <button class="btn btn--primary" type="submit">Verstuur bericht</button>
        <p class="faint">Je gegevens gebruik ik alleen om je vraag te beantwoorden. Zie de <a href="/nl/privacy/">privacyverklaring</a>.</p>
      </form>
    </div>
  </div>
</section>

""" + faq_block("Wat mensen vooraf vragen", CHECK_FAQ) + next_links([
        ("/nl/online-coaching/", "Diensten", "Online coaching", "Voor individuele atleten"),
        ("/nl/teams/", "Diensten", "Teams &amp; clubs", "Voor selecties en staf"),
    ]),
}


# ---------------------------------------------------------------------------
# 10. TARIEVEN
# ---------------------------------------------------------------------------

TARIEVEN = {
    "url": "/nl/tarieven/",
    "title": "Tarieven online coaching, teams en testdagen | N-Force",
    "description": "Online coaching vanaf €49 per maand, Return-to-Play €249, testdagen vanaf €750 exclusief btw. Minimale looptijd twaalf weken, daarna maandelijks opzegbaar.",
    "crumbs": [("Tarieven", "/nl/tarieven/")],
    "content": page_hero(
        "Tarieven",
        "Wat het kost, en waarom",
        "Alle prijzen staan open op deze pagina. Wat je betaalt hangt af van hoeveel begeleiding je nodig hebt, niet van hoe goed je onderhandelt.",
        crumbs=[("Tarieven", "/nl/tarieven/")],
    ) + """
<section class="section section--air">
  <div class="wrap">
    <div class="reveal">""" + PLANS + """</div>
  </div>
</section>

<hr class="blueline">

<section class="section section--air section--panel">
  <div class="wrap">
    <div class="section__head reveal">
      <p class="eyebrow">Naast elkaar</p>
      <h2>Wat zit er in welk pakket</h2>
    </div>
    <div class="tablewrap reveal">
      <table>
        <thead>
          <tr>
            <th scope="col">Onderdeel</th>
            <th scope="col">Basis <span class="num">&euro;49</span></th>
            <th scope="col">Performance <span class="num">&euro;125</span></th>
            <th scope="col">Return-to-Play <span class="num">&euro;249</span></th>
          </tr>
        </thead>
        <tbody>
          <tr><td><strong>Programma op maat</strong></td><td>Blokprogramma op sport en niveau</td><td>Volledig op maat</td><td>Volledig op maat</td></tr>
          <tr><td><strong>Herziening</strong></td><td>Maandelijks</td><td>Elke vier weken</td><td>Wekelijks</td></tr>
          <tr><td><strong>Evaluatie</strong></td><td>Vragen via de app</td><td>Wekelijks, schriftelijk</td><td>Wekelijkse videocall</td></tr>
          <tr><td><strong>Videofeedback</strong></td><td>&mdash;</td><td>Twee oefeningen per maand</td><td>Onbeperkt</td></tr>
          <tr><td><strong>Testing</strong></td><td>Protocollen om zelf uit te voeren</td><td>Nulmeting en hertest na twaalf weken</td><td>Maandelijks</td></tr>
          <tr><td><strong>Afstemming fysio of trainer</strong></td><td>&mdash;</td><td>Op verzoek</td><td>Standaard</td></tr>
        </tbody>
      </table>
    </div>
    <p class="smallprint" style="margin-top:1.5rem">Alle maandprijzen zijn inclusief btw. Minimale looptijd twaalf weken, daarna maandelijks opzegbaar. Teams en clubs ontvangen een offerte exclusief btw.</p>
  </div>
</section>

<section class="section section--air">
  <div class="wrap">
    <div class="section__head reveal">
      <p class="eyebrow">Teams, clubs en testdagen</p>
      <h2>Op locatie is altijd maatwerk</h2>
    </div>
    <div class="tablewrap reveal">
      <table>
        <thead><tr><th scope="col">Onderdeel</th><th scope="col">Wat je krijgt</th><th scope="col">Indicatie</th></tr></thead>
        <tbody>
          <tr><td><strong>Losse testdag</strong></td><td>Sprint, sprong en kracht voor de selectie, rapport per speler plus teamoverzicht binnen een week.</td><td><span class="num">vanaf &euro;750</span> excl. btw</td></tr>
          <tr><td><strong>Seizoenstraject</strong></td><td>Periodisering, blokprogramma&rsquo;s, testmomenten en rapportage over het hele seizoen.</td><td>Vast voorstel na kennismaking</td></tr>
          <tr><td><strong>Stafbegeleiding</strong></td><td>Programma en testopzet van mij, uitvoering door jullie eigen staf met instructie.</td><td>Op offerte</td></tr>
          <tr><td><strong>Reiskosten</strong></td><td>Binnen ongeveer een uur rijden van Tilburg inbegrepen; daarbuiten apart in het voorstel.</td><td>Vooraf inzichtelijk</td></tr>
        </tbody>
      </table>
    </div>
  </div>
</section>

""" + ctaband(
        "Weet je niet welk pakket past?",
        "Dat is precies waar de Performance Check voor is. Twintig minuten, gratis, en het antwoord mag ook zijn dat je nog geen coaching nodig hebt.",
    ),
}


# ---------------------------------------------------------------------------
# 11 & 12. JURIDISCH — plaatshouders
# ---------------------------------------------------------------------------

PRIVACY = {
    "url": "/nl/privacy/",
    "title": "Privacyverklaring | N-Force Performance",
    "description": "Hoe N-Force Performance omgaat met persoonsgegevens, testresultaten en gegevens van minderjarige sporters.",
    "crumbs": [("Privacyverklaring", "/nl/privacy/")],
    "content": page_hero(
        "Juridisch",
        "Privacyverklaring",
        "Hoe ik omga met je gegevens, met testresultaten en met gegevens van minderjarige sporters.",
        crumbs=[("Privacyverklaring", "/nl/privacy/")],
    ) + """
<section class="section section--air">
  <div class="wrap wrap--narrow">
    <div class="notice notice--todo reveal" style="margin-bottom:2rem">
      <p class="notice__label">Nog over te zetten</p>
      <p>Plak hier de tekst van je bestaande privacyverklaring (nu op <code>/privacy.html</code>). Ik heb deze niet overgenomen omdat een juridische tekst niet gegenereerd hoort te worden &mdash; hij moet kloppen met wat je feitelijk doet.</p>
    </div>
    <div class="measure reveal" style="display:flex;flex-direction:column;gap:1.25rem">
      <h2>Waar de tekst in elk geval op in moet gaan</h2>
      <ul class="ticks">
        <li>Welke gegevens je verzamelt via het formulier, de agenda en tijdens coaching</li>
        <li>Testresultaten als persoonsgegevens, en gezondheidsgegevens als bijzondere persoonsgegevens</li>
        <li>Met wie je gegevens deelt: trainers, fysiotherapeuten, medische staf &mdash; en dat dit vooraf wordt afgesproken</li>
        <li>Minderjarige sporters en toestemming van ouders</li>
        <li>Bewaartermijnen, en hoe iemand inzage, correctie of verwijdering vraagt</li>
        <li>Verwerkers die je gebruikt: coaching-app, agendatool, formulierendienst, e-mail en hosting</li>
        <li>Je contactgegevens en het recht om een klacht in te dienen bij de Autoriteit Persoonsgegevens</li>
      </ul>
      <p class="faint">Vragen over je gegevens? Mail <a href="mailto:nick@nforce-performance.nl">nick@nforce-performance.nl</a>.</p>
    </div>
  </div>
</section>
""",
}

VOORWAARDEN = {
    "url": "/nl/voorwaarden/",
    "title": "Algemene voorwaarden | N-Force Performance",
    "description": "Voorwaarden voor online coaching, teambegeleiding en testdagen van N-Force Performance.",
    "crumbs": [("Algemene voorwaarden", "/nl/voorwaarden/")],
    "content": page_hero(
        "Juridisch",
        "Algemene voorwaarden",
        "Wat je van mij mag verwachten, wat ik van jou verwacht, en hoe we omgaan met looptijd, pauzeren en opzeggen.",
        crumbs=[("Algemene voorwaarden", "/nl/voorwaarden/")],
    ) + """
<section class="section section--air">
  <div class="wrap wrap--narrow">
    <div class="notice notice--todo reveal" style="margin-bottom:2rem">
      <p class="notice__label">Nog op te stellen</p>
      <p>Deze pagina is nieuw. Laat de tekst opstellen of controleren door iemand met juridische kennis &mdash; bij een dienst waar maandbedragen, minderjarige sporters en een medische context samenkomen is dat geen formaliteit. Verwijder dit blok zodra de tekst staat.</p>
    </div>
    <div class="measure reveal" style="display:flex;flex-direction:column;gap:1.25rem">
      <h2>Onderwerpen die erin horen</h2>
      <ul class="ticks">
        <li>Wie je bent: bedrijfsnaam, KVK <span class="num">99722283</span>, btw-id <span class="num">NL005406539B11</span></li>
        <li>Looptijd van twaalf weken, maandelijkse opzegging daarna, en hoe pauzeren werkt</li>
        <li>Betaling, facturatie en wat er gebeurt bij te late betaling</li>
        <li>Annuleren en verzetten van testdagen en gesprekken</li>
        <li>Wat de dienst wel en niet is: training, geen medische behandeling of diagnose</li>
        <li>Verantwoordelijkheid van de sporter voor het melden van klachten en beperkingen</li>
        <li>Aansprakelijkheid en je beroepsaansprakelijkheidsverzekering</li>
        <li>Intellectueel eigendom van programma&rsquo;s, testprotocollen en rapporten</li>
        <li>Toepasselijk recht en geschillenregeling</li>
      </ul>
      <p class="faint">Vragen over de voorwaarden? Mail <a href="mailto:nick@nforce-performance.nl">nick@nforce-performance.nl</a>.</p>
    </div>
  </div>
</section>
""",
}


PAGES = [HOME, ONLINE, RTP, TEAMS, TESTING, RESULTATEN, REFERENTIE, OVER, CHECK, TARIEVEN, PRIVACY, VOORWAARDEN]
