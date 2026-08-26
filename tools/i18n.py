# -*- coding: utf-8 -*-
"""
Alle sitecopy, per taal. Structuur is bewust plat: één key, drie talen.

    t("home_h1", "de")

Copy aanpassen  -> pas de waarde aan en run tools/build.py
Taal toevoegen  -> zie README, sectie "Taal toevoegen"

Waarden mogen strings, tuples of lijsten zijn. Bij ontbrekende vertaling valt
de functie terug op Nederlands, zodat de build nooit stukloopt.
"""

NL, EN, DE = "nl", "en", "de"

S = {}


def add(key, nl, en, de):
    S[key] = {NL: nl, EN: en, DE: de}


def t(key, lang):
    entry = S.get(key)
    if entry is None:
        raise KeyError("Onbekende tekst-key: %s" % key)
    return entry.get(lang) or entry[NL]


# ---------------------------------------------------------------------------
# Chrome: navigatie, header, footer
# ---------------------------------------------------------------------------
add("skip", "Naar hoofdinhoud", "Skip to content", "Zum Inhalt springen")
add("brand_tagline", "Strength &amp; conditioning", "Strength &amp; conditioning", "Strength &amp; Conditioning")
add("nav_label", "Hoofdmenu", "Main menu", "Hauptmen\u00fc")
add("lang_label", "Taal kiezen", "Choose language", "Sprache w\u00e4hlen")
add("cart_label", "Winkelwagen openen", "Open cart", "Warenkorb \u00f6ffnen")
add("menu", "Menu", "Menu", "Men\u00fc")
add("cta_short", "Performance Check", "Performance Check", "Performance-Check")
add("cta_label", "Gratis Performance Check", "Free Performance Check", "Kostenloser Performance-Check")
add("bar_selftest", "Doe de zelftest", "Take the self-test", "Selbsttest starten")

add("nav_home", "Home", "Home", "Start")
add("nav_coaching", "Online coaching", "Online coaching", "Online-Coaching")
add("nav_teams", "Teams &amp; clubs", "Teams &amp; clubs", "Teams &amp; Vereine")
add("nav_testing", "Testing", "Testing", "Testing")
add("nav_selftest", "Zelftest", "Self-test", "Selbsttest")
add("nav_handbooks", "Handboeken", "Handbooks", "Handb\u00fccher")
add("nav_pricing", "Tarieven", "Pricing", "Preise")
add("nav_about", "Over Nick", "About Nick", "\u00dcber Nick")
add("nav_contact", "Performance Check", "Performance Check", "Performance-Check")
add("nav_checkout", "Bestellen", "Checkout", "Kasse")
add("nav_privacy", "Privacy", "Privacy", "Datenschutz")
add("nav_terms", "Voorwaarden", "Terms", "AGB")

add("footer_about",
    "Strength &amp; conditioning voor sporters die meetbaar sneller, sterker en robuuster willen worden. Online coaching, testing en handboeken \u2014 vanuit Tilburg, voor spelers en teams in Nederland, Belgi\u00eb en Duitsland.",
    "Strength &amp; conditioning for athletes who want to get measurably faster, stronger and more robust. Online coaching, testing and handbooks \u2014 based in Tilburg, working with players and teams across the Netherlands, Belgium and Germany.",
    "Strength &amp; Conditioning f\u00fcr Sportler, die messbar schneller, st\u00e4rker und robuster werden wollen. Online-Coaching, Testing und Handb\u00fccher \u2014 aus Tilburg, f\u00fcr Spieler und Teams in den Niederlanden, Belgien und Deutschland.")
add("footer_services", "Diensten", "Services", "Leistungen")
add("footer_more", "Meer", "More", "Mehr")

# ---------------------------------------------------------------------------
# Herbruikbare blokken
# ---------------------------------------------------------------------------
add("cta_band_h", "Weet je binnen 20 minuten waar je winst zit",
    "Know where your gain is within 20 minutes",
    "In 20 Minuten wei\u00dft du, wo dein Gewinn liegt")
add("cta_band_p",
    "De Performance Check is gratis, duurt twintig minuten en is g\u00e9\u00e9n verkoopgesprek. Je krijgt een eerlijke inschatting van je grootste beperking en het advies dat daarbij hoort \u2014 ook als dat betekent dat je bij mij niets hoeft af te nemen.",
    "The Performance Check is free, takes twenty minutes and is not a sales call. You get an honest read on your biggest limiter and the advice that follows from it \u2014 even if that means you don't need to buy anything.",
    "Der Performance-Check ist kostenlos, dauert zwanzig Minuten und ist kein Verkaufsgespr\u00e4ch. Du bekommst eine ehrliche Einsch\u00e4tzung deines gr\u00f6\u00dften Limiters und die passende Empfehlung \u2014 auch wenn du dann nichts kaufen musst.")
add("cta_band_b1", "Plan je Performance Check", "Book your Performance Check", "Performance-Check buchen")
add("cta_band_b2", "Eerst zelf meten", "Measure yourself first", "Erst selbst messen")
add("next_h", "Waar wil je heen?", "Where do you want to go next?", "Wie geht es weiter?")
add("pagenav_label", "Op deze pagina", "On this page", "Auf dieser Seite")
add("pagenav_more", "Verder op de site", "Elsewhere on the site", "Weiter auf der Seite")
add("faq_h", "Veelgestelde vragen", "Frequently asked questions", "H\u00e4ufige Fragen")
add("proof_note",
    "Alle programma\u2019s zijn opgebouwd volgens de principes uit de kracht- en sprintliteratuur: progressive overload, kwaliteit boven volume en periodisering rond je wedstrijdkalender.",
    "Every programme is built on established strength and sprint literature: progressive overload, quality over volume and periodisation around your competition calendar.",
    "Jedes Programm folgt den Prinzipien der Kraft- und Sprintliteratur: progressive Overload, Qualit\u00e4t vor Volumen und Periodisierung rund um deinen Wettkampfkalender.")

# ---------------------------------------------------------------------------
# Coachingpakketten (gebruikt op home, coaching en tarieven)
# ---------------------------------------------------------------------------
add("plans_h", "Coachingpakketten", "Coaching packages", "Coaching-Pakete")
add("plans_lede",
    "Drie trajecten, één werkwijze: meten, plannen, uitvoeren, hertesten. Minimale looptijd twaalf weken — korter dan dat is er geen eerlijke conclusie te trekken. Maandprijzen inclusief btw, maandelijks opzegbaar na de eerste twaalf weken.",
    "Three tracks, one method: measure, plan, execute, retest. Minimum term is twelve weeks — anything shorter gives no honest conclusion. Monthly prices include VAT, cancellable monthly after the first twelve weeks.",
    "Drei Wege, eine Methode: messen, planen, umsetzen, nachtesten. Mindestlaufzeit zwölf Wochen — kürzer lässt sich kein ehrliches Fazit ziehen. Monatspreise inkl. MwSt., nach den ersten zwölf Wochen monatlich kündbar.")
add("plan_recommended", "Aanbevolen startpunt", "Recommended starting point", "Empfohlener Einstieg")
add("plan_per_month", "per maand", "per month", "pro Monat")
add("plan_choose", "Dit pakket bespreken", "Discuss this package", "Dieses Paket besprechen")

PLANS = (
    {
        "id": "basis", "price": "49", "unit": "plan_per_month", "recommended": False,
        "name": {NL: "Basis", EN: "Base", DE: "Basis"},
        "for": {
            NL: "Voor de sporter die zelfstandig traint en vooral een goed plan mist.",
            EN: "For the athlete who trains independently and mainly lacks a solid plan.",
            DE: "Für Sportler, die selbstständig trainieren und vor allem einen guten Plan brauchen.",
        },
        "bullets": {
            NL: ("Intake en testanalyse", "Maandelijks programma in de app", "Techniekfeedback op video, 1× per week", "Hertest na elke blok van zes weken"),
            EN: ("Intake and test analysis", "Monthly programme in the app", "Video technique feedback, once a week", "Retest after every six-week block"),
            DE: ("Intake und Testanalyse", "Monatliches Programm in der App", "Technik-Feedback per Video, 1× pro Woche", "Nachtest nach jedem Sechs-Wochen-Block"),
        },
    },
    {
        "id": "performance", "price": "125", "unit": "plan_per_month", "recommended": True,
        "name": {NL: "Performance", EN: "Performance", DE: "Performance"},
        "for": {
            NL: "Voor de competitieve speler die in het seizoen scherp wil blijven en in de voorbereiding stappen wil maken.",
            EN: "For the competitive player who wants to stay sharp in-season and make real jumps in pre-season.",
            DE: "Für Wettkampfspieler, die in der Saison scharf bleiben und in der Vorbereitung Schritte machen wollen.",
        },
        "bullets": {
            NL: ("Alles uit Basis", "Programma per week bijgesteld op belasting en wedstrijden", "Videofeedback binnen 24 uur", "Maandelijks videogesprek van 30 minuten", "Sprint-, spring- en krachtblokken op je kalender afgestemd"),
            EN: ("Everything in Base", "Weekly adjustments based on load and fixtures", "Video feedback within 24 hours", "Monthly 30-minute video call", "Sprint, jump and strength blocks aligned to your calendar"),
            DE: ("Alles aus Basis", "Wöchentliche Anpassung an Belastung und Spiele", "Video-Feedback innerhalb von 24 Stunden", "Monatliches Videogespräch von 30 Minuten", "Sprint-, Sprung- und Kraftblöcke auf deinen Kalender abgestimmt"),
        },
    },
    {
        "id": "rtp", "price": "249", "unit": "plan_per_month", "recommended": False,
        "name": {NL: "Return-to-Play", EN: "Return-to-Play", DE: "Return-to-Play"},
        "for": {
            NL: "Voor de speler die terugkomt van een blessure en criteriumgestuurd wil opbouwen. Maximaal vijf trajecten tegelijk.",
            EN: "For the player coming back from injury who wants criteria-based progression. Maximum five tracks at a time.",
            DE: "Für Spieler nach einer Verletzung, die kriteriengesteuert aufbauen wollen. Maximal fünf Prozesse gleichzeitig.",
        },
        "bullets": {
            NL: ("Alles uit Performance", "Criteria per fase: pas door als de test het toelaat", "Links-rechtsverschillen en pijnscores wekelijks gemonitord", "Afstemming met je fysiotherapeut of arts", "Terugkeer naar wedstrijd in stappen, niet in één sprong"),
            EN: ("Everything in Performance", "Criteria per phase: progress only when the test allows it", "Left-right differences and pain scores tracked weekly", "Alignment with your physio or doctor", "Return to competition in steps, not one jump"),
            DE: ("Alles aus Performance", "Kriterien pro Phase: weiter nur, wenn der Test es zulässt", "Seitenunterschiede und Schmerzwerte wöchentlich überwacht", "Abstimmung mit Physiotherapeut oder Arzt", "Rückkehr zum Wettkampf in Schritten, nicht in einem Sprung"),
        },
    },
)

# ---------------------------------------------------------------------------
# Home
# ---------------------------------------------------------------------------
add("home_title", "N-Force Performance — sneller, sterker, robuuster worden met een meetbaar plan",
    "N-Force Performance — get faster, stronger and more robust with a measurable plan",
    "N-Force Performance — schneller, stärker und robuster mit einem messbaren Plan")
add("home_desc",
    "Online strength &amp; conditioning voor sporters en teams. Meet je profiel in vijf minuten, krijg een rule-based advies en train met een plan dat op jouw cijfers is gebouwd.",
    "Online strength &amp; conditioning for athletes and teams. Measure your profile in five minutes, get a rule-based recommendation and train from a plan built on your numbers.",
    "Online Strength &amp; Conditioning für Sportler und Teams. Miss dein Profil in fünf Minuten, erhalte eine regelbasierte Empfehlung und trainiere nach einem Plan, der auf deinen Zahlen basiert.")
add("home_eyebrow", "Strength &amp; conditioning · Tilburg &amp; online",
    "Strength &amp; conditioning · Tilburg &amp; online",
    "Strength &amp; Conditioning · Tilburg &amp; online")
add("home_h1", "Train niet harder. Train op de één plek waar jij nu het meeste wint.",
    "Don't train harder. Train the one thing that gives you the most right now.",
    "Trainiere nicht härter. Trainiere die eine Stelle, an der du jetzt am meisten gewinnst.")
add("home_lede",
    "De meeste sporters trainen hard en toch scheef: veel volume op wat al goed is, te weinig op de rem die hen tegenhoudt. Vul je testwaarden in, zie per domein waar je staat ten opzichte van je sport en niveau, en krijg direct het handboek of traject dat daarbij hoort.",
    "Most athletes train hard but lopsided: plenty of volume on what already works, too little on the brake that actually holds them back. Enter your test numbers, see where you stand per domain for your sport and level, and get the handbook or programme that fits.",
    "Die meisten Sportler trainieren hart, aber schief: viel Volumen für das, was schon funktioniert, zu wenig für die Bremse, die sie wirklich aufhält. Gib deine Testwerte ein, sieh pro Bereich, wo du für Sport und Niveau stehst, und erhalte direkt das passende Handbuch oder Programm.")
add("home_cta1", "Start de zelftest · 5 min", "Start the self-test · 5 min", "Selbsttest starten · 5 Min.")
add("home_cta2", "Bekijk online coaching", "See online coaching", "Online-Coaching ansehen")
add("home_stats",
    (("6", "testonderdelen in de zelftest"), ("3", "talen: NL · EN · DE"), ("12", "weken minimale looptijd"), ("20", "minuten gratis Performance Check")),
    (("6", "tests in the self-test"), ("3", "languages: NL · EN · DE"), ("12", "weeks minimum term"), ("20", "minutes free Performance Check")),
    (("6", "Tests im Selbsttest"), ("3", "Sprachen: NL · EN · DE"), ("12", "Wochen Mindestlaufzeit"), ("20", "Minuten kostenloser Check")))

add("home_paths_eyebrow", "Kies je route", "Choose your route", "Wähle deinen Weg")
add("home_paths_h", "Vier manieren om te beginnen", "Four ways to start", "Vier Möglichkeiten zu starten")
add("home_paths",
    (("selftest", "Zelftest &amp; analyse", "Vul je sprong-, sprint- en krachtwaarden in. Je ziet per domein of je onder, binnen of boven de referentiewaarde voor jouw sport zit — met een duidelijke conclusie in plaats van losse cijfers.", "Gratis · 5 minuten", "Doe de zelftest"),
     ("handbooks", "Handboeken", "Complete blokken van zes tot twaalf weken in Core en Pro. Je koopt het boek dat bij je uitslag past, niet een willekeurig programma van internet.", "Vanaf €29 · direct download", "Bekijk handboeken"),
     ("coaching", "Online coaching", "Wekelijkse aansturing, techniekfeedback op video en een programma dat meebeweegt met je wedstrijden en belasting.", "Vanaf €49 per maand", "Bekijk coaching"),
     ("teams", "Teams &amp; clubs", "Testdag voor de hele selectie, een rapport per speler en een teambrede lijn voor het seizoen. Voor clubs die willen weten waar hun groep staat.", "Vanaf €750 per testdag", "Bekijk teams")),
    (("selftest", "Self-test &amp; analysis", "Enter your jump, sprint and strength numbers. You see per domain whether you sit below, inside or above the reference range for your sport — with a clear conclusion instead of loose data.", "Free · 5 minutes", "Take the self-test"),
     ("handbooks", "Handbooks", "Complete six to twelve week blocks in Core and Pro. You buy the book that matches your result, not a random programme off the internet.", "From €29 · instant download", "Browse handbooks"),
     ("coaching", "Online coaching", "Weekly direction, video technique feedback and a programme that moves with your fixtures and load.", "From €49 per month", "See coaching"),
     ("teams", "Teams &amp; clubs", "A test day for the full squad, a report per player and one season-wide line for the group. For clubs that want to know where their squad stands.", "From €750 per test day", "See teams")),
    (("selftest", "Selbsttest &amp; Analyse", "Gib deine Sprung-, Sprint- und Kraftwerte ein. Du siehst pro Bereich, ob du unter, innerhalb oder über dem Referenzbereich für deine Sportart liegst — mit klarer Schlussfolgerung statt loser Zahlen.", "Kostenlos · 5 Minuten", "Selbsttest starten"),
     ("handbooks", "Handbücher", "Komplette Blöcke von sechs bis zwölf Wochen in Core und Pro. Du kaufst das Buch, das zu deinem Ergebnis passt — nicht ein beliebiges Programm aus dem Netz.", "Ab €29 · Sofort-Download", "Handbücher ansehen"),
     ("coaching", "Online-Coaching", "Wöchentliche Steuerung, Technik-Feedback per Video und ein Programm, das sich an Spiele und Belastung anpasst.", "Ab €49 pro Monat", "Coaching ansehen"),
     ("teams", "Teams &amp; Vereine", "Testtag für den ganzen Kader, ein Bericht pro Spieler und eine teamweite Linie für die Saison. Für Vereine, die wissen wollen, wo ihre Gruppe steht.", "Ab €750 pro Testtag", "Teams ansehen")))

add("home_method_eyebrow", "Werkwijze", "Method", "Vorgehen")
add("home_method_h", "Meten, plannen, hertesten", "Measure, plan, retest", "Messen, planen, nachtesten")
add("home_method",
    (("01", "Meten", "Zes onderdelen: countermovement jump, relatieve squat, 10 en 30 meter sprint, 505-richtingsverandering en een uithoudingstest. Samen dekken die kracht, elasticiteit, acceleratie, topsnelheid, wenden en motor."),
     ("02", "Plannen", "Je zwakste domein bepaalt de hoofdlijn van het blok, je kalender bepaalt de timing. Nooit vier doelen tegelijk — één hoofdlijn en twee onderhoudslijnen."),
     ("03", "Hertesten", "Elke zes weken opnieuw dezelfde tests. Boven de meetfout is het winst, daaronder is het ruis. Zo weet je of het plan werkt in plaats van dat je het hoopt.")),
    (("01", "Measure", "Six items: countermovement jump, relative squat, 10 and 30 metre sprint, 505 change of direction and an endurance test. Together they cover strength, elasticity, acceleration, top speed, turning and engine."),
     ("02", "Plan", "Your weakest domain sets the main theme of the block, your calendar sets the timing. Never four goals at once — one main line and two maintenance lines."),
     ("03", "Retest", "The same tests again every six weeks. Above the measurement error it's a gain, below it it's noise. That way you know the plan works instead of hoping it does.")),
    (("01", "Messen", "Sechs Tests: Countermovement Jump, relative Kniebeuge, 10 und 30 Meter Sprint, 505-Richtungswechsel und ein Ausdauertest. Zusammen decken sie Kraft, Elastizität, Beschleunigung, Höchstgeschwindigkeit, Wenden und Motor ab."),
     ("02", "Planen", "Dein schwächster Bereich bestimmt die Hauptlinie des Blocks, dein Kalender die Zeitplanung. Nie vier Ziele gleichzeitig — eine Hauptlinie und zwei Erhaltungslinien."),
     ("03", "Nachtesten", "Alle sechs Wochen dieselben Tests. Über dem Messfehler ist es Fortschritt, darunter Rauschen. So weißt du, ob der Plan funktioniert, statt es zu hoffen.")))

add("home_hb_eyebrow", "Handboeken", "Handbooks", "Handbücher")
add("home_hb_h", "Uitgelichte handboeken", "Featured handbooks", "Ausgewählte Handbücher")
add("home_hb_lede",
    "Elk handboek is een compleet blok: weekschema’s, sets, reps, tempo, progressie en de criteria om door te gaan. Core is de complete basis, Pro voegt sportspecifieke blokken, testprotocollen en langere periodisering toe.",
    "Every handbook is a complete block: weekly schedules, sets, reps, tempo, progression and the criteria to move on. Core is the complete base, Pro adds sport-specific blocks, test protocols and longer periodisation.",
    "Jedes Handbuch ist ein kompletter Block: Wochenpläne, Sätze, Wiederholungen, Tempo, Progression und die Kriterien zum Weitergehen. Core ist die komplette Basis, Pro ergänzt sportspezifische Blöcke, Testprotokolle und längere Periodisierung.")
add("home_hb_cta", "Alle handboeken bekijken", "See all handbooks", "Alle Handbücher ansehen")

add("home_why_h", "Waarom dit anders werkt", "Why this works differently", "Warum das anders funktioniert")
add("home_why",
    (("Advies uit regels, niet uit gevoel", "De zelftest gebruikt vaste voorwaarden: welk domein onder de referentiewaarde ligt, in welke fase je zit en op welk niveau je speelt bepalen samen welk handboek bovenaan komt. Dezelfde invoer geeft altijd hetzelfde advies."),
     ("Meetfout staat er gewoon bij", "Bij elke test zie je de meetfout. Een verbetering die daarbinnen valt noem ik geen progressie. Dat is minder spectaculair en veel bruikbaarder."),
     ("Belasting boven bewondering", "Een plan dat niet past naast je trainingen en wedstrijden is geen goed plan. Volume gaat omlaag in het seizoen, kwaliteit blijft.")),
    (("Advice from rules, not from feel", "The self-test uses fixed conditions: which domain sits below the reference range, which phase you're in and what level you play at together decide which handbook comes first. The same input always gives the same advice."),
     ("Measurement error is shown", "Every test shows its measurement error. An improvement inside that margin is not progress. Less spectacular, far more usable."),
     ("Load over admiration", "A plan that doesn't fit alongside your practices and games is not a good plan. Volume drops in-season, quality stays.")),
    (("Empfehlung aus Regeln, nicht aus Gefühl", "Der Selbsttest nutzt feste Bedingungen: welcher Bereich unter dem Referenzwert liegt, in welcher Phase du bist und auf welchem Niveau du spielst, bestimmen zusammen, welches Handbuch oben steht. Dieselbe Eingabe ergibt immer dieselbe Empfehlung."),
     ("Messfehler wird mitgezeigt", "Bei jedem Test siehst du den Messfehler. Eine Verbesserung innerhalb dieser Spanne nenne ich keinen Fortschritt. Weniger spektakulär, deutlich brauchbarer."),
     ("Belastung vor Bewunderung", "Ein Plan, der nicht neben Training und Spielen passt, ist kein guter Plan. Volumen sinkt in der Saison, Qualität bleibt.")))

add("home_faq",
    (("Voor wie is dit bedoeld?", "Voor sporters vanaf ongeveer zestien jaar die serieus trainen: ijshockey, voetbal, handbal en andere teamsporten met sprints, duels en richtingsveranderingen. Ook voor teams en clubs die hun selectie willen testen."),
     ("Heb ik apparatuur nodig voor de zelftest?", "Nee. Een meetlint, een stopwatch of telefoon en een sportzaal of veld is genoeg. Bij elke test staat precies hoe je meet en hoe groot de meetfout is."),
     ("Wat is het verschil tussen een handboek en coaching?", "Een handboek is een compleet plan dat je zelf uitvoert. Coaching is hetzelfde plan plus wekelijkse aansturing, videofeedback en aanpassing op je belasting. Veel spelers beginnen met een handboek en stappen later over."),
     ("Kan ik in het Duits of Engels begeleid worden?", "Ja. De site, de handboeken en de begeleiding zijn beschikbaar in Nederlands, Engels en Duits.")),
    (("Who is this for?", "Athletes from roughly sixteen years old who train seriously: ice hockey, football, handball and other team sports with sprints, duels and changes of direction. Also for teams and clubs that want to test their squad."),
     ("Do I need equipment for the self-test?", "No. A tape measure, a stopwatch or phone and a gym or pitch is enough. Every test states exactly how to measure and how large the measurement error is."),
     ("What's the difference between a handbook and coaching?", "A handbook is a complete plan you run yourself. Coaching is the same plan plus weekly direction, video feedback and adjustment to your load. Many players start with a handbook and move up later."),
     ("Can I be coached in German or English?", "Yes. The site, the handbooks and the coaching are available in Dutch, English and German.")),
    (("Für wen ist das gedacht?", "Für Sportler ab etwa sechzehn Jahren, die ernsthaft trainieren: Eishockey, Fußball, Handball und andere Teamsportarten mit Sprints, Duellen und Richtungswechseln. Auch für Teams und Vereine, die ihren Kader testen wollen."),
     ("Brauche ich Ausrüstung für den Selbsttest?", "Nein. Maßband, Stoppuhr oder Handy und eine Halle oder ein Platz genügen. Bei jedem Test steht genau, wie du misst und wie groß der Messfehler ist."),
     ("Was ist der Unterschied zwischen Handbuch und Coaching?", "Ein Handbuch ist ein kompletter Plan, den du selbst umsetzt. Coaching ist derselbe Plan plus wöchentliche Steuerung, Video-Feedback und Anpassung an deine Belastung. Viele Spieler starten mit einem Handbuch und wechseln später."),
     ("Kann ich auf Deutsch oder Englisch betreut werden?", "Ja. Website, Handbücher und Betreuung sind auf Niederländisch, Englisch und Deutsch verfügbar.")))

# Copy van de losse pagina's registreren
import i18n_pages
i18n_pages.register(add)
