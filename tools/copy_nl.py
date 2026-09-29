# -*- coding: utf-8 -*-
"""
NForce relaunch NL v1 — alle Nederlandse sitecopy op één plek.

Dit bestand overschrijft de NL-waarden uit tools/i18n.py en tools/i18n_pages.py
en voegt nieuwe keys toe. EN en DE blijven ongewijzigd tot hun vertaling is
goedgekeurd (zie build.LIVE_LANGS).

Bronnen voor deze copy (NForce Command Center, goedgekeurd 28 Sep 2026):
  - Performance DNA v1       positionering, missie, zes variabelen, proof rule
  - Coaching Principles v1   principes, belasting, pijn- en blessuregrenzen
  - Brand Style Guide v1     toon, woordkeuze, webcopy (sectie 10)
  - Content Rules v1         geen claims zonder bewijs, geen hype

Status: CONCEPT. Niets uit dit bestand gaat live zonder akkoord van Nick.
"""

NL_COPY = {
    # -------------------------------------------------------------------
    # Chrome
    # -------------------------------------------------------------------
    "brand_tagline": "Sport performance",
    "cta_short": "Neem contact op",
    "cta_label": "Neem contact op",
    "nav_home": "Home",
    "nav_method": "Werkwijze",
    "nav_coaching": "Individuele coaching",
    "nav_teams": "Teams &amp; clubs",
    "nav_testing": "Testen",
    "nav_selftest": "Zelftest",
    "nav_handbooks": "Handboeken",
    "nav_pricing": "Tarieven",
    "nav_about": "Over NForce",
    "nav_contact": "Contact",
    "nav_checkout": "Interesse melden",
    "cart_label": "Lijst openen",
    "pr_teams_cta": "Bekijk teams &amp; clubs",
    "footer_about": "Sport performance voor serieuze sporters en teams. Coaching, programmering en monitoring in één systeem, ontwikkeld in het ijshockey. Vanuit Tilburg.",
    "footer_services": "Aanbod",
    "footer_more": "Meer",

    # -------------------------------------------------------------------
    # Herbruikbare blokken
    # -------------------------------------------------------------------
    "cta_band_h": "Bespreek je team of je doel",
    "cta_band_p": "Vertel kort wie je bent, wat je doel is en hoe je seizoen eruitziet. Je krijgt binnen 1 werkdag antwoord.",
    "cta_band_b1": "Neem contact op",
    "cta_band_b2": "Doe de zelftest",
    "next_h": "Verder lezen",
    "faq_h": "Veelgestelde vragen",
    "proof_note": "Elk programma volgt de NForce-programmeringsprincipes: opgebouwd vanuit de sport, de wedstrijdkalender en de speler, met een geleidelijke toename van belasting.",

    # -------------------------------------------------------------------
    # Pakketten (individuele coaching)
    # -------------------------------------------------------------------
    "plans_h": "Coachingpakketten",
    "plans_lede": "Twee pakketten, dezelfde NForce-cyclus, met een hertest na elk blok van 6 weken. Minimale looptijd 12 weken, daarna maandelijks opzegbaar. Prijzen per maand, inclusief btw.",
    "plan_recommended": "Aanbevolen startpunt",
    "plan_per_month": "per maand",
    "plan_choose": "Dit pakket bespreken",

    # -------------------------------------------------------------------
    # Home
    # -------------------------------------------------------------------
    "home_title": "NForce — sport performance voor serieuze sporters en teams",
    "home_desc": "NForce verbindt coaching, programmering en monitoring in één performancesysteem. Voor serieuze sporters en teams, ontwikkeld in het ijshockey.",
    "home_eyebrow": "Sport performance · IJshockey voorop",
    "home_h1": "Sport performance voor serieuze sporters en teams",
    "home_lede": "Coaching, programmering en monitoring in één systeem, gebouwd in het ijshockey. Voor teams en sporters met een prestatiedoel in hun sport.",
    "home_cta1": "Neem contact op",
    "home_cta2": "Bekijk de werkwijze",

    "home_what_eyebrow": "Aanpak",
    "home_what_h": "Eén systeem voor training, belasting en beschikbaarheid",
    "home_what": (
        ("Coaching", "De NForce-methode, uitgevoerd door een coach: sessies, begeleiding en bijsturing. Afgestemd met de technische staf, zodat spelers één boodschap krijgen."),
        ("Programmering", "Seizoen, week en sessie, opgebouwd vanuit de sport, de wedstrijdkalender en de speler. In die volgorde."),
        ("Monitoring", "Geplande en uitgevoerde training, interne belasting, readiness, blessures en beschikbaarheid worden elke trainingsweek vastgelegd. Elke aanpassing is te herleiden."),
    ),

    "home_vars_eyebrow": "Het systeem",
    "home_vars_h": "Zes variabelen, één beslissing",
    "home_vars_lede": "NForce stuurt op zes vaste variabelen. Ze beantwoorden samen één vraag: wat is vandaag de juiste training voor deze speler?",
    "home_vars_center": "De coach beslist",
    "home_vars_note": "De data bereidt de beslissing voor. De coach beslist, in gesprek met de speler.",
    "home_vars_cta": "Bekijk de werkwijze",

    "home_paths_eyebrow": "Aanbod",
    "home_paths_h": "Voor teams en individuele sporters",
    "home_paths": (
        ("teams", "Teams &amp; clubs", "Een testdag voor de hele selectie, een rapport per speler en een lijn voor het seizoen, afgestemd met je staf.", "Teams", "Bekijk teams &amp; clubs"),
        ("coaching", "Individuele coaching", "Online begeleiding met een programma dat meebeweegt met je wedstrijden en je belasting. Minimaal 12 weken.", "Sporters", "Bekijk individuele coaching"),
        ("handbooks", "Handboeken", "Complete trainingsblokken om zelfstandig uit te voeren, met Pro-versies voor ijshockey. De webshop is nog niet live; je kunt interesse melden.", "Zelfstandig", "Bekijk handboeken"),
    ),

    "home_hockey_eyebrow": "Waarom ijshockey",
    "home_hockey_h": "Gebouwd in het ijshockey",
    "home_hockey_p": (
        "IJshockey vraagt veel van het lichaam: korte, intensieve shifts, veel richtingsveranderingen, duels en een dicht wedstrijdschema. NForce ontwikkelt zijn methode in die omgeving.",
        "Wat daar werkt, wordt de NForce-standaard. Teamsporten met sprints, duels en richtingsveranderingen vragen om dezelfde aanpak.",
    ),
    "home_hockey_ticks": (
        "Wedstrijden bepalen de week. Training buiten het ijs past om de teamtraining heen.",
        "Intensiteit blijft, volume beweegt mee met het schema.",
        "Beschikbaarheid gaat voor. Blessures wegen mee in elke trainingsbeslissing.",
        "Alle belasting telt: ijstraining, wedstrijden en training buiten het ijs.",
    ),

    "home_why_eyebrow": "Coachingprincipes",
    "home_why_h": "Hoe NForce coacht",
    "home_why": (
        ("De sport is de toets", "Krachtcijfers zijn een middel. Wat telt, is wat terugkomt op het ijs of in de sport van de sporter."),
        ("Uitgevoerd telt", "Het plan is de intentie. De uitgevoerde training stuurt de aanpassing, en het verschil tussen die twee is informatie."),
        ("De coach beslist", "Readiness kan een sessie aanpassen. Het oordeel van de coach en het gesprek met de speler blijven leidend."),
        ("Pijn is een grens", "NForce stelt geen diagnoses en behandelt niet. Bij scherpe, plotselinge of toenemende pijn stopt de training en volgt een doorverwijzing."),
    ),

    "home_faq": (
        ("Voor wie is NForce?", "Voor teams en sporters met een concreet prestatiedoel in hun sport. IJshockey is de leidende sport; teamsporten met sprints, duels en richtingsveranderingen passen ook. NForce werkt niet aan algemene fitnessdoelen."),
        ("Vervangt NForce de trainer of de fysiotherapeut?", "Nee. NForce verzorgt de fysieke kant van prestatie en stemt af met de technische staf. Blessures horen bij een arts of fysiotherapeut; NForce traint binnen hun grenzen."),
        ("Wat is het verschil tussen coaching en een handboek?", "Een handboek is een compleet trainingsblok dat je zelf uitvoert. Bij coaching stuurt een coach je programma bij op je belasting en je wedstrijden: maandelijks in Basis, wekelijks in Performance."),
    ),

    # -------------------------------------------------------------------
    # Werkwijze (nieuw)
    # -------------------------------------------------------------------
    "me_title": "Werkwijze — één cyclus, zes variabelen | NForce",
    "me_desc": "Hoe NForce plant, vastlegt en bijstuurt: de coachingcyclus, zes vaste variabelen en Athlete Hub als beslisondersteuning.",
    "me_eyebrow": "Werkwijze",
    "me_h1": "Eén cyclus, elke trainingsweek",
    "me_lede": "NForce werkt met één vaste cyclus: context, plannen, uitvoeren, vastleggen, evalueren en bijsturen. Elke week, voor elke speler.",
    "me_loop_h": "De coachingcyclus",
    "me_loop_center": "Elke week",
    "me_loop": (
        ("01", "Context", "Wedstrijdschema, seizoensfase, rol en beschikbaarheid bepalen hoe de week eruitziet."),
        ("02", "Plannen", "De coach plant seizoen, week en sessie. Eén kader per selectie, de dosis per speler."),
        ("03", "Uitvoeren", "Elke sessie heeft één doel dat de speler kan benoemen. Eerst waarom, dan wat."),
        ("04", "Vastleggen", "Voor elke sessie wordt readiness vastgelegd, na elke sessie de uitgevoerde training en de interne belasting."),
        ("05", "Evalueren", "Elke week: gepland tegenover uitgevoerd, belasting, readiness en beschikbaarheid."),
        ("06", "Bijsturen", "De coach past aan en legt de reden vast. Elke wijziging heeft een datum, een reden en een verantwoordelijke."),
    ),
    "me_vars_h": "Zes variabelen",
    "me_vars_lede": "Elke variabele beantwoordt een vraag die een trainingsbeslissing kan veranderen. Wat geen beslissing verandert, wordt niet gemeten.",
    "me_vars_cols": ("Variabele", "Wat het vastlegt", "De vraag"),
    "me_hub_eyebrow": "Beslisondersteuning",
    "me_hub_h": "Athlete Hub: de coach beslist",
    "me_hub_p": (
        "Athlete Hub is het beslisondersteunende systeem dat NForce binnen de eigen coaching ontwikkelt. Het is geen los product.",
        "Het doel: de zes variabelen per speler ordenen en laten zien wat aandacht vraagt, met de data die daartoe leidt.",
        "De coach beslist wat er met een signaal gebeurt en legt de reden vast.",
    ),
    "me_load_h": "Belasting en pijn",
    "me_load": (
        "Belasting gaat stapsgewijs omhoog. Grote sprongen worden vermeden, zeker na vakantie, ziekte of blessure.",
        "Zware dagen zijn zwaar, lichte dagen licht. Lichtere weken worden vooraf gepland.",
        "Gemiste training wordt niet ingehaald. Het plan gaat verder vanaf wat is uitgevoerd.",
        "Scherpe, plotselinge of toenemende pijn: stoppen, melden en doorverwijzen.",
        "NForce stelt geen diagnoses, behandelt niet en voorspelt geen hersteltijden.",
    ),

    # -------------------------------------------------------------------
    # Individuele coaching (was: online coaching)
    # -------------------------------------------------------------------
    "co_title": "Individuele coaching — een plan dat meebeweegt met je seizoen | NForce",
    "co_desc": "Online begeleiding voor serieuze sporters: intake, testen, een programma in de app en bijsturing op belasting en wedstrijden. Vanaf €49 per maand.",
    "co_eyebrow": "Individuele coaching",
    "co_h1": "Een plan dat meebeweegt met je seizoen",
    "co_lede": "Voor sporters met een prestatiedoel in hun sport. Je start met een intake en testen en werkt per blok aan één hoofdlijn. Je coach stuurt bij op wat je uitvoert, hoe je herstelt en wanneer je speelt.",
    "co_h2_incl": "Wat er in elk traject zit",
    "co_incl": (
        "Intake van 45 minuten: kalender, trainingshistorie, blessures en faciliteiten",
        "Testbatterij met 6 onderdelen en een schriftelijke analyse",
        "Programma in de coaching-app met video per oefening, sets, herhalingen, tempo en rate of perceived exertion (RPE)",
        "Techniekfeedback op de video's die je uploadt",
        "Hertest na elk blok van 6 weken en een nieuw blok op basis van de uitkomst",
        "Aanpassing bij ziekte, extra wedstrijden of een drukke week op school of werk",
    ),
    "co_limit_step": "Grens",
    "co_limit_h": "Bij pijn of blessure",
    "co_limit_p": "NForce stelt geen diagnoses en behandelt niet. Heb je een blessure, dan bepalen je arts of fysiotherapeut de grenzen en traint NForce daarbinnen.",
    "co_h2_flow": "Hoe een traject loopt",
    "co_flow": (
        ("Week 0", "Intake, testen en analyse. Aan het eind van de week ligt je hoofdlijn vast, met de reden erbij."),
        ("Week 1–6", "Eerste blok: 2 tot 4 sessies per week, afgestemd op je training op het ijs of het veld."),
        ("Week 6", "Hertest. Een verbetering groter dan de meetfout telt als vooruitgang. Blijft de verbetering binnen de meetfout, dan stuurt de coach het blok bij."),
        ("Week 7–12", "Tweede blok, sportspecifieker, gebouwd op de uitkomst van de hertest."),
    ),
    "co_faq": (
        ("Heb ik een sportschool nodig?", "Voor de meeste programma's wel: een halterstang met schijven, dumbbells en een squatrek. Zonder die middelen is een variant met elastieken, een gewichtsvest en sprongwerk mogelijk."),
        ("Hoeveel tijd kost het per week?", "2 tot 4 sessies van 45 tot 75 minuten, plus ongeveer 10 minuten voor video's en de check-in. In het seizoen zijn dat meestal 2 kortere sessies."),
        ("Kan ik na 12 weken stoppen?", "Ja. Na de minimale looptijd van 12 weken is het traject maandelijks opzegbaar."),
        ("Werkt dit naast mijn teamtraining?", "Ja, daar is het op gebouwd. Je teamtraining en wedstrijden tellen mee als belasting; het programma vult aan en concurreert er niet mee."),
    ),

    # -------------------------------------------------------------------
    # Teams & clubs
    # -------------------------------------------------------------------
    "tm_title": "Teams &amp; clubs — testdag, spelersrapport en seizoenslijn | NForce",
    "tm_desc": "Een testdag voor de hele selectie, een rapport per speler en een seizoenslijn voor de staf. IJshockey en andere teamsporten. Vanaf €750 per testdag, exclusief btw.",
    "tm_eyebrow": "Teams &amp; clubs",
    "tm_h1": "Testdag, spelersrapport en seizoenslijn voor je selectie",
    "tm_lede": "Een testdag geeft een gestructureerd beeld van de fysieke kwaliteiten van je selectie. Je krijgt per speler één prioriteit en voor de staf een lijn voor het seizoen.",
    "tm_h2": "Wat je krijgt",
    "tm_items": (
        ("Testdag", "Een halve of hele dag op locatie. 6 onderdelen per speler, in groepen van 4. Ongeveer 20 spelers per halve dag."),
        ("Rapport per speler", "Testwaarden, de positie ten opzichte van gepubliceerde referentiewaarden en één prioriteit per speler."),
        ("Teamrapport", "De spreiding per kwaliteit en de 2 of 3 thema's waar de hele groep aan werkt."),
        ("Seizoenslijn", "Een blokindeling rond je wedstrijdkalender: wat de staf in de krachtruimte doet en wat bij de training op het ijs of veld hoort."),
        ("Stafbriefing", "Een sessie van 1 uur waarin de uitkomsten en de uitvoering met de staf worden doorgenomen."),
        ("Hertest", "Optioneel na 10 tot 12 weken. Dezelfde tests, hetzelfde protocol."),
    ),
    "tm_how_h": "Zo werkt NForce met een staf",
    "tm_how": (
        "Eén boodschap naar de spelers: NForce stemt af met de staf voordat iets de selectie bereikt.",
        "De hoofdcoach blijft verantwoordelijk voor tactiek en de training op het ijs of veld.",
        "Blessures en pijn horen bij de medische staf. NForce traint binnen hun grenzen.",
        "Individuele testdata gaan naar de speler en de staf. Ze worden nooit openbaar gemaakt.",
    ),
    "tm_price_h": "Investering",
    "tm_price_p": "Vanaf €750 per testdag, exclusief btw, inclusief rapporten en stafbriefing. Reiskosten binnen Nederland zijn inbegrepen; voor België en Duitsland volgt een aparte opgave. Grotere selecties of meerdere teams: prijs op aanvraag.",
    "tm_faq": (
        ("Hoeveel spelers kunnen er op een dag?", "Ongeveer 20 per halve dag met één tester. Bij grotere selecties werkt NForce met een assistent of wordt de test over 2 dagdelen verdeeld."),
        ("Wat hebben we nodig?", "Een zaal of veld van minimaal 40 m (30 m sprint plus uitloop), een krachtruimte voor het squatonderdeel en een ruimte voor de briefing."),
        ("Krijgen spelers hun eigen resultaten?", "Ja. Elke speler krijgt zijn eigen rapport. Het teamrapport gaat naar de staf."),
    ),

    # -------------------------------------------------------------------
    # Testing
    # -------------------------------------------------------------------
    "te_title": "Testen — zes tests, één vast protocol | NForce",
    "te_desc": "Countermovement jump, relatieve squat, 10 en 30 m sprint, 505 en Yo-Yo Intermittent Recovery Test: hoe je meet, wat de meetfout is en waar die vandaan komt.",
    "te_eyebrow": "Testen",
    "te_h1": "Zes tests, één vast protocol",
    "te_lede": "Zes tests die met eenvoudig materiaal betrouwbaar te herhalen zijn. Ze meten fysieke kwaliteiten uit sporten met sprints, duels en richtingsveranderingen: kracht, elasticiteit, acceleratie, topsnelheid, wenden en herhaald vermogen.",
    "te_table_h": "De testbatterij",
    "te_cols": ("Test", "Kwaliteit", "Wat je meet", "Meetfout"),
    "te_rows": (
        ("Countermovement jump", "Elasticiteit", "Explosieve kracht met tegenbeweging", "cmj"),
        ("Relatieve squat: maximaal gewicht voor 1 herhaling (1RM) ÷ lichaamsgewicht", "Kracht", "Maximale kracht ten opzichte van je lichaamsgewicht", "squatRel"),
        ("Sprint 10 m", "Acceleratie", "Startkracht en de eerste passen", "sprint10"),
        ("Sprint 30 m", "Topsnelheid", "Snelheid opbouwen en vasthouden", "sprint30"),
        ("505-richtingsverandering", "Wenden", "Afremmen en opnieuw versnellen over 180°", "cod505"),
        ("Yo-Yo Intermittent Recovery Test niveau 1 (Yo-Yo IR1)", "Herhaald vermogen", "Het vermogen om intensieve inspanningen te herhalen", "yoyo"),
    ),
    "te_table_note": "Meetfouten komen uit dezelfde bronnen als de referentiewaarden in de zelftest. Waar geen meetfout is gepubliceerd, staat dat erbij. Een verschil kleiner dan de meetfout telt niet als vooruitgang.",
    "te_how_h": "Zo meet je betrouwbaar",
    "te_how": (
        "Test altijd op hetzelfde moment van de dag, na dezelfde warming-up en met dezelfde schoenen.",
        "Sprint- en sprongtests: 3 pogingen, de beste telt, 2 tot 3 minuten rust. De squattest en de Yo-Yo IR1 volgen hun eigen protocol.",
        "Sprint op een vlakke, droge ondergrond. Buiten bij wind: sprint met zijwind, nooit met wind mee.",
        "Test niet binnen 48 uur na een wedstrijd of een zware krachtsessie.",
        "Noteer datum, ondergrond, materiaal en hoe je je voelde. Een cijfer zonder context is niet te interpreteren.",
    ),
    "te_cta_h": "Vergelijk je waarden in de zelftest",
    "te_cta_p": "De zelftest zet je waarden naast gepubliceerde referentiewaarden, met bron per test, en geeft een handboekadvies.",

    # -------------------------------------------------------------------
    # Zelftest
    # -------------------------------------------------------------------
    "st_title": "Zelftest — zie waar je staat per kwaliteit | NForce",
    "st_desc": "Vul je testwaarden in en zie per kwaliteit waar je staat ten opzichte van gepubliceerde referentiewaarden, met bron per test. Gratis, zonder account.",
    "st_eyebrow": "Zelftest",
    "st_h1": "Je testwaarden naast gepubliceerde referentiewaarden",
    "st_lede": "Eén testwaarde is genoeg om te beginnen; meer waarden geven een scherper beeld. De analyse gebeurt in je browser en wordt niet naar een server verzonden.",
    "st_howto": (
        ("Positie per test", "Een schaal met de referentieband voor jouw sport en referentiegroep, en de plek van jouw waarde daarin. Met bron per test."),
        ("Zwakste kwaliteit", "De kwaliteiten waar je onder de referentieband zit, met een korte uitleg wat dat voor je sport betekent."),
        ("Handboekadvies", "Eén primair handboek en maximaal 2 aanvullende, met per advies de reden."),
    ),

    # -------------------------------------------------------------------
    # Handboeken
    # -------------------------------------------------------------------
    "hb_title": "Handboeken — complete trainingsblokken in Core en Pro | NForce",
    "hb_desc": "Trainingshandboeken voor kracht, snelheid, wenden en conditie, met Pro-versies voor ijshockey. Nederlandstalig. Core €39, Pro €79.",
    "hb_eyebrow": "Handboeken",
    "hb_h1": "Complete trainingsblokken om zelf uit te voeren",
    "hb_lede": "Elk handboek bevat weekschema's, sets, herhalingen, tempo, rust, progressieregels en de testcriteria voor het volgende blok. Je krijgt een Nederlandstalige pdf voor telefoon en tablet.",
    "hb_notice": "<strong>De webshop is nog niet live.</strong> Zet handboeken op je lijst en meld interesse. Je betaalt nu niets en krijgt bericht zodra bestellen mogelijk is.",
    "hb_core_pro_h": "Verschil tussen Core en Pro",
    "hb_core_pro": (
        ("Core", "De basis: het blok, de oefeningen, de progressie en een korte testhandleiding. Genoeg voor een volledig blok zelfstandige training; de duur staat per handboek vermeld."),
        ("Pro", "Alles uit Core, plus sportspecifieke blokken voor ijshockey, een volledig testprotocol, varianten voor beperkt materiaal en een invulbaar logboek."),
    ),
    "hb_flow_h": "Hoe het werkt",
    "hb_flow": (
        ("01", "Bekijk de preview", "Bij elk handboek zie je voor wie het is, wat je leert en de inhoudsopgave van het blok."),
        ("02", "Zet handboeken op je lijst", "Kies één of meer handboeken. Je ziet het totaal voordat je interesse meldt."),
        ("03", "Meld interesse", "Je krijgt bericht zodra bestellen mogelijk is. Je betaalt nu niets."),
    ),
    "hb_faq": (
        ("Wanneer kan ik bestellen?", "De webshop is nog niet live. Zet handboeken op je lijst en meld interesse; je krijgt bericht zodra bestellen mogelijk is."),
        ("In welk formaat en welke taal?", "Als pdf voor telefoon en tablet, in het Nederlands. Pro-versies bevatten ook een invulbaar logboek."),
        ("Kan ik van Core naar Pro overstappen?", "Ja. Je betaalt dan het prijsverschil."),
        ("Welk handboek past bij mij?", "Doe de zelftest. Op basis van je waarden, sport, niveau en seizoensfase volgt één primair advies, met de reden erbij."),
    ),

    # -------------------------------------------------------------------
    # Interesse melden (was: bestellen)
    # -------------------------------------------------------------------
    "ck_title": "Interesse melden | NForce",
    "ck_desc": "Overzicht van de handboeken op je lijst en interesse melden.",
    "ck_eyebrow": "Handboeken",
    "ck_h1": "Handboeken op je lijst",
    "ck_lede": "Controleer de handboeken op je lijst en meld interesse. Je betaalt nu niets.",

    # -------------------------------------------------------------------
    # Tarieven
    # -------------------------------------------------------------------
    "pr_title": "Tarieven — coaching, handboeken en teams | NForce",
    "pr_desc": "Individuele coaching vanaf €49 per maand, handboeken vanaf €39 en teamtestdagen vanaf €750.",
    "pr_eyebrow": "Tarieven",
    "pr_h1": "Wat het kost en wat je krijgt",
    "pr_lede": "Maandprijzen voor coaching zijn inclusief btw. Teamtarieven zijn exclusief btw.",
    "pr_hb_h": "Handboeken",
    "pr_hb_p": "Core-versies kosten €39, Pro-versies €79. Eenmalige aanschaf, inclusief updates. De webshop is nog niet live; je kunt nu interesse melden.",
    "pr_teams_h": "Teams &amp; clubs",
    "pr_faq": (
        ("Zit er btw op de maandprijzen?", "Ja. De maandprijzen voor coaching zijn inclusief btw. Teamtarieven zijn exclusief btw."),
        ("Kan ik per kwartaal betalen?", "Ja, bij het Performance-pakket. Geef het aan bij de intake."),
        ("Is er korting voor jongeren en studenten?", "Spelers onder de 18 en studenten met een geldige studentenkaart krijgen 10% korting op de maandprijs."),
    ),

    # -------------------------------------------------------------------
    # Over NForce
    # -------------------------------------------------------------------
    "ab_title": "Over NForce — missie, werkwijze en oprichter | NForce",
    "ab_desc": "NForce is opgericht door Nick Bergman, performance coach. Missie, werkwijze en waar NForce voor staat.",
    "ab_eyebrow": "Achtergrond",
    "ab_h1": "Sport performance, ontwikkeld in het ijshockey",
    "ab_body": (
        "NForce verbetert de sportspecifieke prestatie van serieuze sporters en teams, met gestructureerde coaching, programmering vanuit de sport en beslisondersteuning op basis van data.",
        "NForce is opgericht door Nick Bergman, performance coach met een achtergrond aan de Fontys Sporthogeschool. Hij werkt met ijshockeyspelers en teamsporters aan kracht, snelheid, wenden en belastbaarheid.",
        "NForce werkt met één vaste cyclus: context, plannen, uitvoeren, vastleggen, evalueren en bijsturen. Data maakt de beslissing scherper; de coach neemt die, in gesprek met de speler.",
        "NForce is geen fitness-, lifestyle- of wellnessmerk en werkt niet aan algemene fitnessdoelen.",
    ),
    "ab_card_step": "Oprichter",
    "ab_card_role": "NForce · Tilburg",
    "ab_principles_h": "Waar NForce voor staat",
    "ab_principles": (
        ("Prestatie eerst", "Alles wat NForce doet, moet terugkomen op het ijs of in de sport van de sporter."),
        ("Sportspecifiek", "Training volgt uit de eisen van de sport, de positie en het seizoen. Niet uit algemene fitnessschema's."),
        ("Gepland en vastgelegd", "Elke sessie wordt vooraf gepland en achteraf vastgelegd. Elke afwijking krijgt een reden."),
        ("Data informeert", "Data maakt beslissingen scherper. De coach neemt ze."),
    ),

    # -------------------------------------------------------------------
    # Contact (was: Performance Check)
    # -------------------------------------------------------------------
    "ct_title": "Contact — bespreek je team of je doel | NForce",
    "ct_desc": "Neem contact op met NForce. Een eerste gesprek duurt 20 minuten, online of telefonisch, en is kosteloos.",
    "ct_eyebrow": "Contact",
    "ct_h1": "Bespreek je team of je doel",
    "ct_lede": "Een eerste gesprek duurt 20 minuten, online of telefonisch, en is kosteloos. Het gaat over je sport, je kalender, je historie en eventuele testwaarden. Daarna hoor je welke vervolgstap past, ook als die niet bij NForce ligt.",
    "ct_steps_h": "Wat er gebeurt",
    "ct_steps": (
        ("1", "Stuur het formulier of bel", "Binnen 1 werkdag krijg je antwoord met 2 voorstellen voor een tijdstip."),
        ("2", "Gesprek van 20 minuten", "Online of telefonisch. Kort en concreet."),
        ("3", "Advies op papier", "Je ontvangt het advies schriftelijk, met de vervolgstap die past."),
    ),
    "ct_form_h": "Stuur je aanvraag",
    "ct_f_name": "Naam",
    "ct_f_email": "E-mailadres",
    "ct_f_sport": "Team of sport en niveau",
    "ct_f_goal": "Wat is je doel?",
    "ct_f_send": "Aanvraag versturen",
    "ct_f_note": "Je gegevens worden alleen gebruikt om op je aanvraag te reageren. Zie de <a href=\"/nl/privacy/\">privacyverklaring</a>.",
    "ct_f_mailto_note": "Na versturen opent je e-mailprogramma met je aanvraag klaar om te verzenden.",
    "ct_direct_h": "Direct contact",
    "ct_direct_p": "Je kunt ook bellen, appen of mailen. Je krijgt binnen 1 werkdag antwoord.",

    # -------------------------------------------------------------------
    # Privacy en voorwaarden: alleen naam en toon. Inhoud wacht op juridische toets.
    # -------------------------------------------------------------------
    "pv_title": "Privacyverklaring | NForce",
    "pv_desc": "Welke gegevens NForce verwerkt, waarvoor en hoe lang.",
    "tc_title": "Algemene voorwaarden | NForce",
    "tc_lede": "De afspraken voor coaching, handboeken en teamopdrachten.",

    # -------------------------------------------------------------------
    # 404
    # -------------------------------------------------------------------
    "nf_title": "Deze pagina bestaat niet",
    "nf_lede": "De link is verouderd of bevat een typefout. Hieronder de belangrijkste pagina's.",
}

# De zes v1-variabelen (Performance DNA v1, sectie 10). Eén bron voor home en werkwijze.
VARIABLES = (
    ("Geplande training", "De voorgeschreven training per speler en sessie", "Wat moest de speler doen?"),
    ("Uitgevoerde training", "Wat de speler werkelijk deed", "Is het plan uitgevoerd?"),
    ("Interne belasting", "Hoe zwaar de training voor de speler was", "Past de huidige belasting bij deze speler?"),
    ("Readiness", "De toestand van de speler vóór de training", "Moet de sessie van vandaag worden aangepast?"),
    ("Blessures", "Huidige en eerdere blessures en de beschikbaarheid", "Waarvoor is deze speler beschikbaar?"),
    ("Team- en spelercontext", "Wedstrijdschema, seizoensfase, rol en selectie", "Hoe lees je de cijfers?"),
)

# Privacy: alleen de merknaam in het eerste blok aanpassen; de rest blijft staan
# tot de juridische toets (Decision Rules v1, sectie 9: prepare only).
PV_RESPONSIBLE = ("Wie is verantwoordelijk?",
                  "NForce, Nick Bergman, Tilburg. KVK 99722283. Contact via nick@nforce-performance.nl.")


def apply(S):
    """Zet de NL-waarden in de tekstregistry. Nieuwe keys krijgen alleen NL."""
    for key, value in NL_COPY.items():
        entry = S.setdefault(key, {"nl": None, "en": None, "de": None})
        entry["nl"] = value
    blocks = list(S["pv_blocks"]["nl"])
    blocks[0] = PV_RESPONSIBLE
    S["pv_blocks"]["nl"] = tuple(blocks)
