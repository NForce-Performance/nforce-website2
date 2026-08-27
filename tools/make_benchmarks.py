# -*- coding: utf-8 -*-
"""
Genereert assets/data/benchmarks.json en assets/js/benchmarks.js.

Waarom een generator
--------------------
De referentiewaarden stonden op twee plekken: in assets/data/benchmarks.json
(gebruikt door de zelftest) en in assets/js/benchmarks.js (gebruikt door twee
oude resultatenpagina's). Die twee liepen uiteen. Nu komen ze uit dit bestand,
dus ze kunnen niet meer verschillen. Pas hier aan, niet in de output.

De regel uit de audit
---------------------
GEEN BAND ZONDER BRON. Elke band hieronder heeft een SOURCES-vermelding met de
populatie, n, leeftijd, protocol, jaar en de exacte URL. Waar de band uit een
andere sport of leeftijdsgroep is geleend, staat dat in NOTES en toont de site
dat naast de balk. Waar geen bruikbare bron bestaat, staat er geen band; de
zelftest slaat die combinatie dan over in plaats van een getal te verzinnen.

Onderzoek uitgevoerd 27 augustus 2026. Volledige bronnenlijst met alle
gemiddelden en standaarddeviaties staat in het onderzoeksdocument bij de
projectbestanden (webshop/stap8-referentiewaarden-onderzoek.md).

Draaien:
    python3 tools/make_benchmarks.py
"""
import json
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# --------------------------------------------------------------------------
# Bronnen. Elke sleutel wordt vanuit de tests aangeroepen.
# --------------------------------------------------------------------------
SOURCES = {
    "shl2026": {
        "short": 'Swedish Hockey League, Frontiers 2026',
        "label": "Swedish Hockey League, mannen senior (n = 21, 27,1 ± 5,4 j), "
                 "ForceDecks krachtplatform 1000 Hz, handen op heupen, beste van 3. "
                 "CMJ 41,8 ± 4,8 cm; 10 m 1,99 ± 0,08 s met 1080 Sprint, "
                 "autostart bij 0,2 m/s. Frontiers in Sports and Active Living, 2026.",
        "url": "https://www.frontiersin.org/journals/sports-and-active-living/articles/10.3389/fspor.2026.1920826/full",
    },
    "swiss2024": {
        "short": 'Zwitserse competitie, Biology of Sport 2024',
        "label": "Hoogste Zwitserse competitie, mannen senior (n = 21, 28,4 ± 3,9 j) en "
                 "tweede competitie U21 (n = 22, 18,8 ± 1,0 j), Hawkin krachtplatform, "
                 "handen op heupen, beste van 3. CMJ 42,8 ± 3,8 en 40,3 ± 5,0 cm; "
                 "SJ 40,2 ± 3,7 en 37,1 ± 5,6 cm. Biology of Sport, 2024.",
        "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC10765453/",
    },
    "norway": {
        "short": 'Noorse competitie, n = 848',
        "label": "Noorse hoogste competitie, mannen senior (n = 848, 23 ± 4 j), grootste "
                 "Europese dataset. CMJ beste van 3: verdedigers 39,8 ± 5,0 cm, "
                 "aanvallers 39,7 ± 5,1 cm. Back squat 1RM 151 ± 22 kg bij een "
                 "groepsgemiddeld lichaamsgewicht van 84 ± 7 kg.",
        "url": "https://vuir.vu.edu.au/44542/1/Fitness_tests%20_and_match_performance_in_a_male_ice_hockey_national_league.pdf",
    },
    "sdhl2023": {
        "short": 'SDHL dames, Sports 2023',
        "label": "Hoogste Zweedse damescompetitie SDHL (n = 13, 21,5 ± 5,1 j), "
                 "Kistler krachtplatform, handen op heupen, beste van 3: "
                 "CMJ 34,0 ± 4,9 cm. Meetfout ICC 0,98, CV 3,02%, "
                 "verandering groter dan 2,3 cm is echt. Sports, 2023.",
        "url": "https://pdfs.semanticscholar.org/edb1/a5d562a2d09b45c31e0c504a76e056300a8a.pdf",
    },
    "swissjunior2021": {
        "short": 'Zwitserse U20, Sports 2021',
        "label": "Hoogste Zwitserse juniorencompetitie, U20 (n = 19, 17,8 ± 0,9 j). "
                 "Verspringen vanuit stand met armzwaai, beste van 3: 250 ± 16 cm. "
                 "Sprint 30 m met Brower-lichtpoorten, voorste voet 1 m achter de "
                 "eerste poort, snelste van 2: 4,35 ± 0,14 s. Sports, 2021.",
        "url": "https://pdfs.semanticscholar.org/3627/e21cfdfa456a6f112a02a2209ca084873176.pdf",
    },
    "nhl2003": {
        "short": 'NHL-spelers, 2003',
        "label": "Aankomende en actieve NHL-spelers (n = 57), verspringen vanuit stand "
                 "100 ± 7,2 inch = 254 ± 18 cm. Pogingprotocol niet vermeld, 2003.",
        "url": "https://orthoarchives.com/en/orthoscience/article/W2054947935",
    },
    "china": {
        "short": 'Chinese damesselectie',
        "label": "Nationale damesselectie, elitekamp (n = 23, 15 met WK-ervaring). "
                 "Verspringen beste van 3: 202,7 ± 13,0 cm. Sprint 30 m beste van 2: "
                 "4,93 ± 0,14 s. Back squat / lichaamsgewicht 1,32 ± 0,17. "
                 "Let op: het squatprotocol was geen zuiver 1RM.",
        "url": "https://eu-opensci.org/index.php/sport/article/view/9158",
    },
    "squatinjury2020": {
        "short": 'Squat en blessurerisico, JSCR 2020',
        "label": "Universiteitsatleten, American football (n = 46 mannen) en "
                 "softbal/volleybal (n = 25 vrouwen). Relatieve back squat 1RM "
                 "2,20 ± 0,38 × lichaamsgewicht bij niet-geblesseerden versus "
                 "1,89 ± 0,35 bij wie in het seizoen uitviel. De auteurs noemen "
                 "2,2 × als drempel voor mannen en 1,6 × voor vrouwen. JSCR, 2020.",
        "url": "https://journals.lww.com/nsca-jscr/fulltext/2020/05000/barbell_squat_relative_strength_as_an_identifier.7.aspx",
    },
    "collegiate2016": {
        "short": 'Collegiate voetbal, Sports 2016',
        "label": "Collegiate voetballers (n = 20 mannen, n = 16 vrouwen). "
                 "CMJ 58,5 ± 6,5 en 41,9 ± 5,0 cm; SJ 54,8 ± 6,7 en 40,2 ± 4,7 cm; "
                 "sprint 30 m 4,16 ± 0,14 en 4,78 ± 0,22 s. "
                 "Apparaat, starttype en pogingselectie niet vermeld. Sports, 2016.",
        "url": "https://www.mdpi.com/2075-4663/4/1/11",
    },
    "cod505youth": {
        "short": 'Schotse junior-elite voetbal, 505',
        "label": "Junior-elite voetballers Schotse FA, U15–U17 (n = 32, 13,6 ± 2,0 j). "
                 "Modified 505 met Witty-poorten, staggered start 0,7 m achter de "
                 "poort, beste per richting daarna gemiddeld: 2,33 ± 0,08 s. "
                 "Meetfout ICC 0,84–0,89, CV 1,6–1,8%.",
        "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC7240391/",
    },
    "yoyoreview": {
        "short": 'Yo-Yo IR1 review, 239 studies',
        "label": "Systematische review Yo-Yo IR1 (239 studies, 4.726 deelnemers), "
                 "supplementaire tabel met lopende Yo-Yo IR1: semi-prof voetbal "
                 "Italië 2.385 ± 412 m (24,0 ± 6,0 j), semi-prof voetbal Denemarken "
                 "2.803 ± 330 m, eerste divisie handbal Duitsland 2.038 ± 537 m "
                 "(25,2 ± 5,1 j), eerste divisie handbal dames Denemarken "
                 "1.436 ± 222 m (25,9 ± 3,8 j). Geen enkele ijshockeygroep.",
        "url": "https://www.frontiersin.org/api/v4/articles/343642/file/Table_1.PDF/343642_supplementary-materials_tables_1_pdf/1",
    },
    "denmark2019": {
        "short": 'Deense divisies, JSCR 2019',
        "label": "Beste Deense divisie (n = 164, 23,5 ± 4,4 j) en tweede divisie "
                 "(n = 132, 19,4 ± 3,1 j). Yo-Yo IR1 op het ijs: 2.434 ± 414 m en "
                 "1.850 ± 499 m. Dit is de geschaatste variant, niet de "
                 "lopende off-ice test. JSCR, 2019.",
        "url": "https://pubmed.ncbi.nlm.nih.gov/31343551/",
    },
    "sensors2025": {
        "short": 'Sprintmeetfout, Sensors 2025',
        "label": "Goed getrainde mannelijke teamsporters (n = 30, 19,6 ± 2,4 j), "
                 "lichtpoorten met bewegingsstartsensor. Meetfout 10 m: CV 0,67%, "
                 "typical error 0,012 s, kleinste aantoonbare verschil 0,044 s. "
                 "Voor 20 m: CV 0,52%, typical error 0,016 s. Sensors, 2025.",
        "url": "https://www.mdpi.com/1424-8220/25/7/2077",
    },
    "broadreliability": {
        "short": 'Verspringen betrouwbaarheid, 2024',
        "label": "Nationale U16-selecties Tsjechië (n = 40) en Polen (n = 23). "
                 "Verspringen vanuit stand: verschil tussen pogingen 0,3 ± 12,9 cm, "
                 "ICC 0,97. Sports Medicine Open, 2024.",
        "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC11307188/",
    },
    "yoyoreliability": {
        "short": 'Yo-Yo IR1 meetfout, Biology of Sport 2015',
        "label": "Jeugdvoetballers profclub België, drie opeenvolgende weken. "
                 "Yo-Yo IR1 meetfout: typical error 74–172 m, CV 3,0–7,5%, "
                 "ICC 0,87–0,95. Twee tests in dezelfde week kunnen door meetfout "
                 "alleen al 9 tot 28% verschillen. Biology of Sport, 2015.",
        "url": "https://www.scienceopen.com/document_file/933cda6d-aae5-4f9c-ad38-608e5692bd86/PubMedCentral/933cda6d-aae5-4f9c-ad38-608e5692bd86.pdf",
    },
}


def nl_en_de(nl, en, de):
    return {"nl": nl, "en": en, "de": de}


# --------------------------------------------------------------------------
# De tests
# --------------------------------------------------------------------------
TESTS = {

    # ----------------------------------------------------------------- CMJ
    "cmj": dict(
        domain="elastic", unit="cm", higherIsBetter=True, axis=[20, 70],
        error=1.5, provisional=False,
        label=nl_en_de("Countermovement jump", "Countermovement jump", "Countermovement Jump"),
        help=nl_en_de(
            "Sprong met tegenbeweging, handen op de heupen. Beste van drie pogingen.",
            "Jump with countermovement, hands on hips. Best of three attempts.",
            "Sprung mit Gegenbewegung, Hände an der Hüfte. Bester von drei Versuchen."),
        protocol=nl_en_de(
            "Krachtplatform of sprongmat, handen op de heupen, geen armzwaai, beste van drie. "
            "Meet je met armzwaai of met een Vertec, dan valt je waarde hoger uit en geldt deze band niet.",
            "Force plate or jump mat, hands on hips, no arm swing, best of three. Measuring with arm "
            "swing or a Vertec gives higher values and this band no longer applies.",
            "Kraftmessplatte oder Sprungmatte, Hände an der Hüfte, kein Armschwung, bester von drei. "
            "Mit Armschwung oder Vertec fallen die Werte höher aus und dieses Band gilt nicht."),
        bands={
            "icehockey": {"m": [40, 46], "f": [30, 39]},
            "football": {"m": [52, 65], "f": [37, 47]},
            "default": {"m": [38, 50], "f": [29, 42]},
        },
        sources=["shl2026", "swiss2024", "norway", "sdhl2023", "collegiate2016"],
        notes={
            "football": nl_en_de(
                "Geleend uit collegiate voetbal. Die bron vermeldt geen apparaat en geen "
                "pogingprotocol, dus behandel de band als indicatief.",
                "Borrowed from collegiate soccer. That source reports neither device nor attempt "
                "protocol, so treat the band as indicative.",
                "Aus dem College-Fußball übernommen. Die Quelle nennt weder Gerät noch "
                "Versuchsprotokoll, das Band ist daher nur ein Anhaltspunkt."),
            "default": nl_en_de(
                "Afgeleid van de ijshockey- en voetbaldata, geen eigen bron per sport.",
                "Derived from the ice hockey and soccer data, no dedicated source per sport.",
                "Aus den Eishockey- und Fußballdaten abgeleitet, keine eigene Quelle je Sportart."),
        },
        errorNote=nl_en_de(
            "Meetfout op krachtplatform: CV rond 3%, ongeveer 1,5 cm. Pas een verschil van "
            "meer dan 2,3 cm is met zekerheid echt.",
            "Measurement error on a force plate: CV around 3%, roughly 1.5 cm. Only a difference "
            "above 2.3 cm is certainly real.",
            "Messfehler auf der Kraftmessplatte: CV etwa 3%, rund 1,5 cm. Erst ein Unterschied "
            "über 2,3 cm ist sicher echt."),
        verdict={
            "below": nl_en_de(
                "Sprongkracht is hier de beperkende factor. Dat is bijna altijd een krachtvraagstuk, niet een techniekvraagstuk.",
                "Jump output is the limiting factor here. That is nearly always a strength issue, not a technique issue.",
                "Sprungkraft ist hier der limitierende Faktor. Das ist fast immer ein Kraft- und kein Technikproblem."),
            "inside": nl_en_de(
                "Sprongkracht is op niveau. De winst zit elders.",
                "Jump output is on level. The gain sits elsewhere.",
                "Sprungkraft ist auf Niveau. Der Gewinn liegt woanders."),
            "above": nl_en_de(
                "Explosiviteit is geen beperking. Kijk naar de overdracht naar je sport.",
                "Power is not a limitation. Look at transfer into your sport.",
                "Explosivität ist keine Einschränkung. Prüfe den Transfer in deine Sportart."),
        },
    ),

    # ------------------------------------------------------------------ SJ
    "sj": dict(
        domain="rfd", unit="cm", higherIsBetter=True, axis=[15, 65],
        error=1.5, provisional=True,
        label=nl_en_de("Squat jump", "Squat jump", "Squat Jump"),
        help=nl_en_de(
            "Sprong uit een stilstaande halve hurkzit, zonder tegenbeweging. Beste van drie.",
            "Jump from a held half squat, without countermovement. Best of three.",
            "Sprung aus gehaltener halber Hocke, ohne Gegenbewegung. Bester von drei."),
        protocol=nl_en_de(
            "Handen op de heupen, drie seconden stil in de hurkzit, elke neerwaartse beweging "
            "vóór de afzet maakt de poging ongeldig. Beste van drie.",
            "Hands on hips, hold the squat for three seconds; any downward movement before "
            "take-off voids the attempt. Best of three.",
            "Hände an der Hüfte, drei Sekunden in der Hocke halten; jede Abwärtsbewegung vor "
            "dem Absprung macht den Versuch ungültig. Bester von drei."),
        bands={
            "icehockey": {"m": [36, 44]},
            "football": {"m": [48, 61], "f": [35, 45]},
            "default": {"m": [34, 46]},
        },
        sources=["swiss2024", "collegiate2016"],
        notes={
            "icehockey": nl_en_de(
                "Alle bruikbare squat-jumpdata in ijshockey komt uit één Zwitserse club. "
                "Gebruik deze test naast de countermovement jump, nooit als losse drempel.",
                "All usable squat jump data in ice hockey comes from a single Swiss club. Use this "
                "test alongside the countermovement jump, never as a standalone threshold.",
                "Alle brauchbaren Squat-Jump-Daten im Eishockey stammen aus einem einzigen "
                "Schweizer Klub. Nutze den Test neben dem Countermovement Jump, nie allein."),
            "football": nl_en_de(
                "Geleend uit collegiate voetbal, zonder vermeld apparaat of protocol.",
                "Borrowed from collegiate soccer, with no device or protocol reported.",
                "Aus dem College-Fußball übernommen, ohne genanntes Gerät oder Protokoll."),
        },
        errorNote=nl_en_de(
            "Er is geen gepubliceerde meetfout voor de squat jump. De 1,5 cm hieronder is "
            "overgenomen van de countermovement jump en dus een aanname.",
            "No published measurement error exists for the squat jump. The 1.5 cm below is "
            "carried over from the countermovement jump and is therefore an assumption.",
            "Für den Squat Jump gibt es keinen veröffentlichten Messfehler. Die 1,5 cm unten "
            "sind vom Countermovement Jump übernommen und damit eine Annahme."),
        verdict={
            "below": nl_en_de(
                "Je mist kracht uit stilstand. Dat is zuiver een krachtvraagstuk, want er zit geen elastiek in deze sprong.",
                "You lack force from a dead stop. That is purely a strength issue, since this jump has no elastic contribution.",
                "Dir fehlt Kraft aus dem Stand. Das ist ein reines Kraftproblem, denn dieser Sprung hat keinen elastischen Anteil."),
            "inside": nl_en_de(
                "Concentrische kracht is op niveau. Vergelijk hem met je countermovement jump.",
                "Concentric force is on level. Compare it with your countermovement jump.",
                "Konzentrische Kraft ist auf Niveau. Vergleiche sie mit deinem Countermovement Jump."),
            "above": nl_en_de(
                "Sterk uit stilstand. Zit je countermovement jump niet veel hoger, dan gebruik je je elastiek nog niet.",
                "Strong from a dead stop. If your countermovement jump is not much higher, you are not yet using your elastic capacity.",
                "Stark aus dem Stand. Liegt dein Countermovement Jump nicht deutlich höher, nutzt du deine Elastizität noch nicht."),
        },
    ),

    # --------------------------------------------------------------- BROAD
    "broad": dict(
        domain="rfd", unit="cm", higherIsBetter=True, axis=[150, 320],
        error=10, provisional=True,
        label=nl_en_de("Verspringen vanuit stand", "Standing broad jump", "Standweitsprung"),
        help=nl_en_de(
            "Twee voeten achter de lijn, armzwaai toegestaan. Beste van drie.",
            "Both feet behind the line, arm swing allowed. Best of three.",
            "Beide Füße hinter der Linie, Armschwung erlaubt. Bester von drei."),
        protocol=nl_en_de(
            "Staande start, armzwaai toegestaan. Meet van de startlijn tot het laatste "
            "contactpunt, dus de hiel van de achterste voet. Beste van drie.",
            "Standing start, arm swing allowed. Measure from the start line to the last point "
            "of contact, the heel of the rear foot. Best of three.",
            "Stehender Start, Armschwung erlaubt. Messung von der Startlinie bis zum letzten "
            "Kontaktpunkt, der Ferse des hinteren Fußes. Bester von drei."),
        bands={
            "icehockey": {"m": [240, 265], "f": [190, 216]},
            "default": {"m": [225, 260], "f": [185, 215]},
        },
        sources=["swissjunior2021", "nhl2003", "china", "broadreliability"],
        notes={
            "icehockey": nl_en_de(
                "Er bestaat geen verspringdata voor Europese senior semi-prof spelers. De band "
                "loopt tussen elite Zwitserse U20 en een NHL-populatie uit 2003 zonder "
                "pogingprotocol. Dit is de zwakst onderbouwde band op deze pagina.",
                "No broad jump data exists for European senior semi-pro players. The band runs "
                "between elite Swiss U20 players and a 2003 NHL population with no attempt "
                "protocol reported. This is the weakest band on this page.",
                "Für europäische Senior-Halbprofis gibt es keine Standweitsprungdaten. Das Band "
                "reicht von Schweizer U20-Elite bis zu einer NHL-Population von 2003 ohne "
                "Versuchsprotokoll. Das schwächste Band auf dieser Seite."),
            "default": nl_en_de(
                "Afgeleid van de ijshockeydata, geen eigen bron per sport.",
                "Derived from the ice hockey data, no dedicated source per sport.",
                "Aus den Eishockeydaten abgeleitet, keine eigene Quelle je Sportart."),
        },
        errorNote=nl_en_de(
            "Het verschil tussen twee pogingen was 0,3 ± 12,9 cm. Reken daarom met minstens "
            "10 cm meetfout, ook al is de betrouwbaarheidscoëfficiënt hoog.",
            "The difference between two attempts was 0.3 ± 12.9 cm. Assume at least 10 cm of "
            "measurement error, even though the reliability coefficient is high.",
            "Der Unterschied zwischen zwei Versuchen betrug 0,3 ± 12,9 cm. Rechne daher mit "
            "mindestens 10 cm Messfehler, auch wenn der Reliabilitätskoeffizient hoch ist."),
        verdict={
            "below": nl_en_de(
                "Je krijgt weinig kracht horizontaal de grond in. Dat is dezelfde eigenschap die je eerste passen bepaalt.",
                "You put little force into the ground horizontally. That is the same quality that drives your first steps.",
                "Du bringst wenig Kraft horizontal in den Boden. Genau diese Eigenschaft bestimmt deine ersten Schritte."),
            "inside": nl_en_de(
                "Horizontale explosiviteit op niveau.",
                "Horizontal power on level.",
                "Horizontale Explosivität auf Niveau."),
            "above": nl_en_de(
                "Horizontale explosiviteit is een sterk punt. Controleer of je die ook op het ijs kwijt kunt.",
                "Horizontal power is a strength. Check whether you can express it on the ice as well.",
                "Horizontale Explosivität ist eine Stärke. Prüfe, ob du sie auch auf dem Eis umsetzen kannst."),
        },
    ),

    # ------------------------------------------------------------ SQUAT REL
    "squatRel": dict(
        domain="strength", unit="× lichaamsgewicht", unitEn="× body weight",
        unitDe="× Körpergewicht", higherIsBetter=True, axis=[0.8, 3.0],
        error=None, provisional=True,
        label=nl_en_de("Squat (1RM / lichaamsgewicht)", "Squat (1RM / body weight)",
                       "Squat (1RM / Körpergewicht)"),
        help=nl_en_de(
            "Je zwaarste squat gedeeld door je lichaamsgewicht. Een geschatte 1RM uit 3–5 reps mag ook.",
            "Your heaviest squat divided by body weight. An estimated 1RM from 3–5 reps is fine.",
            "Dein schwerster Squat geteilt durch das Körpergewicht. Ein geschätztes 1RM aus 3–5 Wiederholungen genügt."),
        protocol=nl_en_de(
            "Back squat, heupplooi onder de knie, opbouwen naar 90% van je vorige 1RM en dan "
            "maximaal drie pogingen. Een uit 3–5 reps geschatte 1RM is acceptabel maar minder nauwkeurig.",
            "Back squat, hip crease below the knee, build to 90% of your previous 1RM and then a "
            "maximum of three attempts. A 1RM estimated from 3–5 reps is acceptable but less precise.",
            "Back Squat, Hüftfalte unter Knie, Steigerung auf 90% des vorherigen 1RM, dann maximal "
            "drei Versuche. Ein aus 3–5 Wiederholungen geschätztes 1RM ist akzeptabel, aber ungenauer."),
        bands={
            "icehockey": {"m": [1.70, 2.20], "f": [1.15, 1.50]},
            "default": {"m": [1.85, 2.55], "f": [1.34, 1.92]},
        },
        sources=["norway", "china", "squatinjury2020"],
        notes={
            "icehockey": nl_en_de(
                "Geen enkele ijshockeystudie publiceert een relatieve squat voor mannen. De "
                "ondergrens is berekend uit groepsgemiddelden van de Noorse competitie, 151 kg "
                "bij 84 kg lichaamsgewicht; dat is eigen rekenwerk, geen gepubliceerde waarde. "
                "De bovengrens van 2,2 × is de blessuredrempel uit American football. Bij "
                "vrouwen komt de band uit een protocol dat geen zuiver 1RM was.",
                "No ice hockey study publishes a relative squat for men. The lower bound is "
                "calculated from Norwegian league group means, 151 kg at 84 kg body weight; that "
                "is our own arithmetic, not a published value. The 2.2 × upper bound is the "
                "injury threshold from American football. For women the band comes from a "
                "protocol that was not a true 1RM.",
                "Keine Eishockeystudie veröffentlicht einen relativen Squat für Männer. Die "
                "Untergrenze ist aus Gruppenmittelwerten der norwegischen Liga berechnet, 151 kg "
                "bei 84 kg Körpergewicht; das ist eigene Rechnung, kein publizierter Wert. Die "
                "Obergrenze von 2,2 × ist die Verletzungsschwelle aus dem American Football. Bei "
                "Frauen stammt das Band aus einem Protokoll, das kein echtes 1RM war."),
            "default": nl_en_de(
                "Geleend uit universitaire American football, softbal en volleybal.",
                "Borrowed from university American football, softball and volleyball.",
                "Aus universitärem American Football, Softball und Volleyball übernommen."),
        },
        errorNote=nl_en_de(
            "Er is geen gepubliceerde meetfout voor de back squat 1RM. De praktische grens is "
            "je kleinste schijfsprong: met stappen van 2,5 kg is de resolutie ongeveer 1,25 kg.",
            "No published measurement error exists for the back squat 1RM. The practical limit is "
            "your smallest plate increment: with 2.5 kg steps the resolution is about 1.25 kg.",
            "Für das Back-Squat-1RM gibt es keinen veröffentlichten Messfehler. Die praktische "
            "Grenze ist die kleinste Scheibenstufe: bei 2,5-kg-Schritten etwa 1,25 kg."),
        verdict={
            "below": nl_en_de(
                "Je krachtbasis is te laag om explosiviteit betrouwbaar te ontwikkelen. Hier begint je winst.",
                "Your strength base is too low to develop power reliably. This is where your gain starts.",
                "Deine Kraftbasis ist zu niedrig, um Explosivität zuverlässig zu entwickeln. Hier beginnt dein Gewinn."),
            "inside": nl_en_de(
                "Krachtbasis is voldoende. Nu is de vraag of je hem kunt uitdrukken in snelheid.",
                "Strength base is sufficient. The question now is whether you can express it as speed.",
                "Kraftbasis ist ausreichend. Jetzt geht es um die Umsetzung in Schnelligkeit."),
            "above": nl_en_de(
                "Sterk. Extra kracht levert hier waarschijnlijk minder op dan snelheids- of conditiewerk.",
                "Strong. Extra strength will likely return less here than speed or conditioning work.",
                "Stark. Zusätzliche Kraft bringt hier wahrscheinlich weniger als Schnelligkeits- oder Konditionsarbeit."),
        },
    ),

    # ------------------------------------------------------------ SPRINT 10
    "sprint10": dict(
        domain="accel", unit="s", higherIsBetter=False, axis=[1.5, 2.6],
        error=0.02, provisional=False,
        label=nl_en_de("Sprint 10 meter", "10 metre sprint", "10-Meter-Sprint"),
        help=nl_en_de(
            "Staande start, eigen commando. Beste van drie pogingen, met volledige rust.",
            "Standing start, own command. Best of three attempts with full rest.",
            "Stehender Start, eigenes Kommando. Bester von drei Versuchen mit voller Pause."),
        protocol=nl_en_de(
            "Rechtopstaande staande start, de tijd begint bij je eerste beweging. Dat is wat een "
            "1080 Sprint of bewegingssensor doet. Zet je een lichtpoort op de startlijn of ga je "
            "een halve meter achter de poort staan, dan meet je een halve tot drie tiende seconde "
            "sneller en geldt deze band niet meer.",
            "Upright standing start, timing begins at your first movement. That is what a 1080 "
            "Sprint or a motion sensor does. Placing a light gate on the start line, or standing "
            "half a metre behind it, gives times up to three tenths faster and this band no longer applies.",
            "Aufrechter stehender Start, die Zeit beginnt bei der ersten Bewegung. Genau das macht "
            "ein 1080 Sprint oder ein Bewegungssensor. Eine Lichtschranke auf der Startlinie oder "
            "ein halber Meter Abstand liefert bis zu drei Zehntel schnellere Zeiten und dieses "
            "Band gilt dann nicht."),
        bands={
            "icehockey": {"m": [1.92, 2.07]},
            "default": {"m": [1.92, 2.07]},
        },
        sources=["shl2026", "sensors2025"],
        notes={
            "default": nl_en_de(
                "Geen eigen bron per sport; dit is de ijshockeyband. Sprinttijden uit andere "
                "sporten zijn met een ander starttype gemeten en dus niet vergelijkbaar.",
                "No dedicated source per sport; this is the ice hockey band. Sprint times from "
                "other sports were measured with a different start type and are not comparable.",
                "Keine eigene Quelle je Sportart; dies ist das Eishockeyband. Sprintzeiten "
                "anderer Sportarten wurden mit anderem Starttyp gemessen und sind nicht vergleichbar."),
        },
        errorNote=nl_en_de(
            "Meetfout ongeveer 0,02 s. Pas een verschil boven 0,04 s is aantoonbaar echt.",
            "Measurement error is about 0.02 s. Only a difference above 0.04 s is demonstrably real.",
            "Messfehler etwa 0,02 s. Erst ein Unterschied über 0,04 s ist nachweisbar echt."),
        verdict={
            "below": nl_en_de(
                "De eerste drie passen kosten je tijd. Meestal een kracht- of mechanicavraagstuk.",
                "The first three steps cost you time. Usually a strength or mechanics issue.",
                "Die ersten drei Schritte kosten dich Zeit. Meist ein Kraft- oder Mechanikproblem."),
            "inside": nl_en_de(
                "Acceleratie op niveau voor deze groep.",
                "Acceleration on level for this group.",
                "Beschleunigung auf Niveau für diese Gruppe."),
            "above": nl_en_de(
                "Acceleratie is sterk. Controleer of topsnelheid en remvermogen meekomen.",
                "Acceleration is strong. Check that top speed and braking keep up.",
                "Beschleunigung ist stark. Prüfe, ob Höchstgeschwindigkeit und Bremsvermögen mithalten."),
        },
    ),

    # ------------------------------------------------------------ SPRINT 30
    "sprint30": dict(
        domain="topspeed", unit="s", higherIsBetter=False, axis=[3.6, 5.6],
        error=0.03, provisional=True,
        label=nl_en_de("Sprint 30 meter", "30 metre sprint", "30-Meter-Sprint"),
        help=nl_en_de(
            "Lichtpoorten, voorste voet 1 meter achter de eerste poort. Snelste van twee.",
            "Light gates, front foot 1 metre behind the first gate. Fastest of two.",
            "Lichtschranken, vorderer Fuß 1 Meter hinter der ersten Schranke. Schnellster von zwei."),
        protocol=nl_en_de(
            "Lichtpoorten op 0 en 30 meter, staande start met de voorste voet 1 meter achter de "
            "eerste poort, snelste van twee met twee minuten rust. Dit is een ander starttype dan "
            "bij de 10 meter hierboven; vergelijk de twee tijden dus niet onderling.",
            "Light gates at 0 and 30 metres, standing start with the front foot 1 metre behind the "
            "first gate, fastest of two with two minutes rest. This is a different start type from "
            "the 10 metre above, so do not compare the two times with each other.",
            "Lichtschranken bei 0 und 30 Metern, stehender Start mit dem vorderen Fuß 1 Meter "
            "hinter der ersten Schranke, schnellster von zwei mit zwei Minuten Pause. Anderer "
            "Starttyp als beim 10-Meter-Sprint oben, die Zeiten sind nicht untereinander vergleichbar."),
        bands={
            "icehockey": {"m": [4.20, 4.45], "f": [4.80, 5.05]},
            "default": {"m": [4.20, 4.50], "f": [4.80, 5.10]},
        },
        sources=["swissjunior2021", "china", "sensors2025"],
        notes={
            "icehockey": nl_en_de(
                "Er bestaat geen off-ice 30 meter voor senior semi-prof of prof spelers in Europa. "
                "De herenband komt van elite Zwitserse U20-spelers; dat is verdedigbaar omdat "
                "off-ice sprint tussen U20 en senior nauwelijks verschilt, maar het blijft een "
                "extrapolatie. De damesband komt uit een bron die het starttype niet vermeldt.",
                "No off-ice 30 metre exists for senior semi-pro or pro players in Europe. The "
                "men's band comes from elite Swiss U20 players, which is defensible because "
                "off-ice sprinting barely differs between U20 and senior, but it remains an "
                "extrapolation. The women's band comes from a source that does not report the start type.",
                "Es gibt keinen Off-Ice-30-Meter-Wert für Senior-Halbprofis oder Profis in Europa. "
                "Das Männerband stammt von Schweizer U20-Elitespielern; das ist vertretbar, da sich "
                "Off-Ice-Sprints zwischen U20 und Senioren kaum unterscheiden, bleibt aber eine "
                "Extrapolation. Das Frauenband stammt aus einer Quelle ohne Angabe des Starttyps."),
            "default": nl_en_de(
                "Afgeleid van de ijshockeyband, geen eigen bron per sport.",
                "Derived from the ice hockey band, no dedicated source per sport.",
                "Aus dem Eishockeyband abgeleitet, keine eigene Quelle je Sportart."),
        },
        errorNote=nl_en_de(
            "Voor 30 meter is geen meetfout gepubliceerd. De 0,03 s hieronder is geschat op basis "
            "van de gepubliceerde 20 meter-waarde en dus een aanname.",
            "No measurement error has been published for 30 metres. The 0.03 s below is estimated "
            "from the published 20 metre value and is therefore an assumption.",
            "Für 30 Meter ist kein Messfehler veröffentlicht. Die 0,03 s unten sind aus dem "
            "publizierten 20-Meter-Wert geschätzt und damit eine Annahme."),
        verdict={
            "below": nl_en_de(
                "Je snelheid vlakt af na de acceleratie. Topsnelheidswerk is hier relevant.",
                "Your speed flattens off after acceleration. Top-speed work is relevant here.",
                "Deine Geschwindigkeit flacht nach der Beschleunigung ab. Höchstgeschwindigkeitsarbeit ist hier relevant."),
            "inside": nl_en_de("Topsnelheid op niveau.", "Top speed on level.",
                               "Höchstgeschwindigkeit auf Niveau."),
            "above": nl_en_de("Topsnelheid is een sterk punt.", "Top speed is a strength.",
                              "Höchstgeschwindigkeit ist eine Stärke."),
        },
    ),

    # --------------------------------------------------------------- 505 COD
    "cod505": dict(
        domain="cod", unit="s", higherIsBetter=False, axis=[2.0, 3.0],
        error=0.05, provisional=True,
        label=nl_en_de("505 richtingverandering", "505 change of direction",
                       "505 Richtungswechsel"),
        help=nl_en_de(
            "Aanloop 10 meter, 180 graden draaien op de lijn, 5 meter terug. Beste van twee per been.",
            "10 metre approach, 180 degree turn on the line, 5 metres back. Best of two per leg.",
            "10 Meter Anlauf, 180-Grad-Wende an der Linie, 5 Meter zurück. Bester von zwei pro Bein."),
        protocol=nl_en_de(
            "Modified 505: 10 meter rechte sprint, 180 graden draaien op een vooraf bepaald been, "
            "5 meter terug. De poort staat 0,7 meter achter de startlijn en meet de laatste "
            "5 meter plus de draai plus de 5 meter terug. Twee pogingen per been, beste per "
            "richting, daarna het gemiddelde van links en rechts.",
            "Modified 505: 10 metre straight sprint, 180 degree turn on a predetermined leg, "
            "5 metres back. The gate sits 0.7 metres behind the start line and times the final "
            "5 metres plus the turn plus the 5 metres back. Two attempts per leg, best per "
            "direction, then the average of left and right.",
            "Modified 505: 10 Meter Sprint, 180-Grad-Wende auf einem festgelegten Bein, 5 Meter "
            "zurück. Die Schranke steht 0,7 Meter hinter der Startlinie und misst die letzten "
            "5 Meter plus Wende plus 5 Meter zurück. Zwei Versuche pro Bein, bester je Richtung, "
            "dann der Mittelwert aus links und rechts."),
        bands={
            "icehockey": {"m": [2.25, 2.45]},
            "football": {"m": [2.25, 2.45]},
            "default": {"m": [2.25, 2.45]},
        },
        sources=["cod505youth", "denmark2019"],
        notes={
            "icehockey": nl_en_de(
                "Er bestaat nul 505-data in ijshockey, op geen enkel niveau en voor geen enkel "
                "geslacht. Deze band is geleend uit Schotse junior-elite voetballers van 13 tot "
                "17 jaar. Ijshockeyonderzoek gebruikt de 5-10-5 pro-agility op het ijs; wil je "
                "een echte ijshockeyreferentie, gebruik dan die test.",
                "There is zero 505 data in ice hockey, at any level or for either sex. This band "
                "is borrowed from Scottish junior-elite soccer players aged 13 to 17. Ice hockey "
                "research uses the 5-10-5 pro agility on the ice; for a genuine ice hockey "
                "reference, use that test instead.",
                "Es gibt keine 505-Daten im Eishockey, auf keinem Niveau und für kein Geschlecht. "
                "Dieses Band ist von schottischen Junior-Elite-Fußballern von 13 bis 17 Jahren "
                "übernommen. Die Eishockeyforschung nutzt die 5-10-5 Pro Agility auf dem Eis; für "
                "eine echte Eishockeyreferenz nimm diesen Test."),
        },
        errorNote=nl_en_de(
            "Meetfout ongeveer 0,05 s. Pas een verschil van ongeveer 0,1 s is betekenisvol.",
            "Measurement error is about 0.05 s. Only a difference of around 0.1 s is meaningful.",
            "Messfehler etwa 0,05 s. Erst ein Unterschied von rund 0,1 s ist bedeutsam."),
        verdict={
            "below": nl_en_de(
                "Je verliest tijd in de draai. Remvermogen, niet versnellen, is hier de vaardigheid.",
                "You lose time in the turn. Braking, not accelerating, is the skill here.",
                "Du verlierst Zeit in der Wende. Bremsen, nicht Beschleunigen, ist hier die Fähigkeit."),
            "inside": nl_en_de("Richtingverandering op niveau.", "Change of direction on level.",
                               "Richtungswechsel auf Niveau."),
            "above": nl_en_de(
                "Sterk in de draai. Dat is in de wedstrijd vaak meer waard dan een snelle 30 meter.",
                "Strong in the turn. In a game that is often worth more than a fast 30 metres.",
                "Stark in der Wende. Im Spiel oft wertvoller als eine schnelle 30-Meter-Zeit."),
        },
    ),

    # ---------------------------------------------------------------- YO-YO
    "yoyo": dict(
        domain="engine", unit="m", higherIsBetter=True, axis=[800, 3200],
        error=125, provisional=True,
        label=nl_en_de("Yo-Yo IR1 (afstand)", "Yo-Yo IR1 (distance)", "Yo-Yo IR1 (Distanz)"),
        help=nl_en_de(
            "Totale afstand in meters bij de lopende intermittent recovery test niveau 1. Geen Yo-Yo gedaan? Laat leeg.",
            "Total distance in metres on the running intermittent recovery test level 1. No Yo-Yo? Leave blank.",
            "Gesamtdistanz in Metern beim laufenden Intermittent-Recovery-Test Level 1. Kein Yo-Yo gemacht? Leer lassen."),
        protocol=nl_en_de(
            "Lopende versie: 2 × 20 meter shuttles op het tempo van een geluidssignaal, met "
            "10 seconden actief herstel over 2 × 5 meter. Score is de totale afstand. De "
            "geschaatste variant op het ijs levert andere getallen en hoort hier niet in.",
            "Running version: 2 × 20 metre shuttles paced by an audio signal, with 10 seconds of "
            "active recovery over 2 × 5 metres. The score is total distance. The skated variant on "
            "ice produces different numbers and does not belong here.",
            "Laufende Version: 2 × 20 Meter Shuttles im Takt eines Signaltons, mit 10 Sekunden "
            "aktiver Erholung über 2 × 5 Meter. Score ist die Gesamtdistanz. Die geskatete "
            "Variante auf dem Eis liefert andere Zahlen und gehört hier nicht hin."),
        bands={
            "icehockey": {"m": [1900, 2400], "f": [1200, 1650]},
            "football": {"m": [1975, 2800]},
            "handball": {"m": [1500, 2575], "f": [1200, 1650]},
            "default": {"m": [1900, 2400], "f": [1200, 1650]},
        },
        sources=["yoyoreview", "denmark2019", "yoyoreliability"],
        notes={
            "icehockey": nl_en_de(
                "Er bestaat geen off-ice Yo-Yo IR1-data voor ijshockey. Een review van 239 "
                "Yo-Yo IR1-studies met 4.726 deelnemers bevat geen enkele ijshockeygroep. Deze "
                "band is geleend uit Duitse eerste-divisie handbal en Italiaans semi-prof "
                "voetbal. Kun je op het ijs testen, dan is 1.850 ± 499 m uit de tweede Deense "
                "divisie de best passende semi-prof referentie.",
                "No off-ice Yo-Yo IR1 data exists for ice hockey. A review of 239 Yo-Yo IR1 "
                "studies covering 4,726 participants contains no ice hockey group at all. This "
                "band is borrowed from German first division handball and Italian semi-pro "
                "soccer. If you can test on ice, 1,850 ± 499 m from the Danish second division "
                "is the closest semi-pro reference.",
                "Für Eishockey gibt es keine Off-Ice-Yo-Yo-IR1-Daten. Eine Übersicht von 239 "
                "Yo-Yo-IR1-Studien mit 4.726 Teilnehmern enthält keine einzige Eishockeygruppe. "
                "Dieses Band ist aus der deutschen Handball-Bundesliga und dem italienischen "
                "Halbprofi-Fußball übernommen. Kannst du auf dem Eis testen, sind 1.850 ± 499 m "
                "aus der zweiten dänischen Division die passendste Halbprofi-Referenz."),
            "handball": nl_en_de(
                "Herenband uit de Duitse eerste divisie, damesband uit de Deense eerste divisie.",
                "Men's band from the German first division, women's band from the Danish first division.",
                "Männerband aus der deutschen ersten Liga, Frauenband aus der dänischen ersten Liga."),
            "default": nl_en_de(
                "Geleend uit handbal en voetbal, geen eigen bron per sport.",
                "Borrowed from handball and soccer, no dedicated source per sport.",
                "Aus Handball und Fußball übernommen, keine eigene Quelle je Sportart."),
        },
        errorNote=nl_en_de(
            "Meetfout 100 tot 150 meter. Twee tests in dezelfde week kunnen door meetfout alleen "
            "al 9 tot 28% verschillen; pas ongeveer vijf shuttles winst is duidelijk echt.",
            "Measurement error is 100 to 150 metres. Two tests in the same week can differ by 9 to "
            "28% from measurement error alone; only about five shuttles of gain is clearly real.",
            "Messfehler 100 bis 150 Meter. Zwei Tests in derselben Woche können allein durch "
            "Messfehler um 9 bis 28% abweichen; erst etwa fünf Shuttles Zuwachs sind klar echt."),
        verdict={
            "below": nl_en_de(
                "Herhaald vol gas is je beperking. Je zakt in op het moment dat het telt.",
                "Repeated max effort is your limitation. You fade when it counts.",
                "Wiederholte Maximalleistung ist deine Grenze. Du brichst ein, wenn es zählt."),
            "inside": nl_en_de("Conditie op niveau voor deze groep.",
                               "Conditioning on level for this group.",
                               "Kondition auf Niveau für diese Gruppe."),
            "above": nl_en_de(
                "Conditie is een sterk punt. Extra volume levert hier weinig op.",
                "Conditioning is a strength. Extra volume returns little here.",
                "Kondition ist eine Stärke. Zusätzliches Volumen bringt hier wenig."),
        },
    ),
}

ORDER = ["cmj", "sj", "broad", "squatRel", "sprint10", "sprint30", "cod505", "yoyo"]

DOMAINS = {
    "strength": nl_en_de("Maximale kracht", "Maximal strength", "Maximalkraft"),
    "elastic": nl_en_de("Sprongkracht", "Jump output", "Sprungkraft"),
    "rfd": nl_en_de("Explosiviteit", "Rate of force development", "Explosivität"),
    "accel": nl_en_de("Acceleratie", "Acceleration", "Beschleunigung"),
    "topspeed": nl_en_de("Topsnelheid", "Top speed", "Höchstgeschwindigkeit"),
    "cod": nl_en_de("Richtingverandering", "Change of direction", "Richtungswechsel"),
    "engine": nl_en_de("Conditie", "Conditioning", "Kondition"),
}

PROVISIONAL_NOTICE = nl_en_de(
    "Elke referentieband hieronder heeft een bron met populatie, aantal, leeftijd en protocol. "
    "Voor een deel van de tests bestaat geen ijshockeydata en is de band geleend uit een andere "
    "sport of leeftijdsgroep; dat staat er dan bij. Lees die banden als richting, niet als norm.",
    "Every reference band below has a source with population, sample size, age and protocol. For "
    "some tests no ice hockey data exists and the band is borrowed from another sport or age "
    "group; that is stated where it applies. Read those bands as direction, not as a standard.",
    "Jedes Referenzband unten hat eine Quelle mit Population, Stichprobe, Alter und Protokoll. "
    "Für einige Tests gibt es keine Eishockeydaten und das Band ist aus einer anderen Sportart "
    "oder Altersgruppe übernommen; das ist dann angegeben. Lies diese Bänder als Richtung, nicht "
    "als Norm.")

README = ("Referentiewaarden per test, per sport en geslacht. Gegenereerd door "
          "tools/make_benchmarks.py — pas daar aan, niet hier. Regel uit de audit: geen band "
          "zonder bron. Elke test heeft 'sources' met populatie, n, leeftijd, protocol, jaar en "
          "URL. Waar de band uit een andere sport of leeftijdsgroep is geleend staat dat in "
          "'notes' per sport. Ontbreekt een geslacht bij een sport, dan bestaat er geen bron voor "
          "die combinatie en slaat de zelftest de test over; hij vult dan niet stilzwijgend de "
          "herenband in. 'error' mag null zijn als er geen gepubliceerde meetfout is; "
          "'errorNote' legt dat uit.")


def build():
    tests = {}
    for tid in ORDER:
        t = dict(TESTS[tid])
        srcs = []
        for key in t.pop("sources"):
            s = SOURCES[key]
            if not s.get("short"):
                raise SystemExit("bron zonder korte naam: " + key)
            srcs.append({"short": s["short"], "label": s["label"], "url": s["url"]})
        t["sources"] = srcs
        tests[tid] = t
    return {
        "_readme": README,
        "researchedOn": "2026-08-27",
        "provisionalNotice": PROVISIONAL_NOTICE,
        "domains": DOMAINS,
        "tests": tests,
    }


def write_legacy_js(data):
    """
    Schrijft assets/js/benchmarks.js uit dezelfde gegevens. Twee oude
    resultatenpagina's laden dat bestand nog; zo kan het niet meer afwijken van
    de JSON. Het oude formaat kent één band, geen banden per sport, dus daar
    gaat de ijshockeyband voor mannen in.
    """
    lines = [
        "/* ==========================================================================",
        "   N-FORCE PERFORMANCE — referentiewaarden (legacy)",
        "   --------------------------------------------------------------------------",
        "   AUTOMATISCH GEGENEREERD door tools/make_benchmarks.py. Niet met de hand",
        "   aanpassen; wijzigingen gaan verloren bij de volgende build.",
        "",
        "   Dit bestand bestaat alleen nog voor twee oude resultatenpagina's. Het kent",
        "   maar één band per test, dus hier staat de band voor mannen in het ijshockey.",
        "   De zelftest gebruikt assets/data/benchmarks.json, met banden per sport en",
        "   geslacht, bronnen en waar nodig een waarschuwing bij een geleende band.",
        "   ========================================================================== */",
        "",
        "window.NFORCE_BENCHMARKS = {",
    ]
    for i, tid in enumerate(ORDER):
        t = data["tests"][tid]
        band = (t["bands"].get("icehockey") or t["bands"]["default"]).get("m")
        if not band:
            continue
        err = t["error"]
        err_txt = ("\u00b1 %s %s" % (str(err).replace(".", ","), t["unit"])) if err is not None \
            else "geen gepubliceerde meetfout"
        src = t["sources"][0]
        source = "%s Bron: %s" % (src["label"], src["url"])
        note = t.get("notes", {}).get("icehockey")
        if note:
            source = "LET OP: %s %s" % (note["nl"], source)

        def js(s):
            return "'" + str(s).replace("\\", "\\\\").replace("'", "\\'") + "'"

        lines += [
            "  %s: {" % tid,
            "    label: %s," % js(t["label"]["nl"]),
            "    unit: %s," % js(t["unit"]),
            "    axis: [%s, %s]," % (t["axis"][0], t["axis"][1]),
            "    band: [%s, %s]," % (band[0], band[1]),
            "    higherIsBetter: %s," % ("true" if t["higherIsBetter"] else "false"),
            "    error: %s," % js(err_txt),
            "    source: %s," % js(source),
            "    below: %s," % js(t["verdict"]["below"]["nl"]),
            "    inside: %s," % js(t["verdict"]["inside"]["nl"]),
            "    above: %s" % js(t["verdict"]["above"]["nl"]),
            "  }%s" % ("," if i < len(ORDER) - 1 else ""),
            "",
        ]
    lines += ["};", ""]
    with open(os.path.join(ROOT, "assets/js/benchmarks.js"), "w", encoding="utf-8") as f:
        f.write("\n".join(lines))


def main():
    data = build()

    # Zelfcontrole: geen band zonder bron, en geen band zonder een geldig bereik.
    fouten = []
    for tid, t in data["tests"].items():
        if not t["sources"]:
            fouten.append("%s heeft geen bron" % tid)
        for sport, per_gender in t["bands"].items():
            for g, band in per_gender.items():
                if not band or len(band) != 2:
                    fouten.append("%s/%s/%s heeft geen geldig bereik" % (tid, sport, g))
                    continue
                lo, hi = band
                if lo >= hi:
                    fouten.append("%s/%s/%s: ondergrens niet kleiner dan bovengrens" % (tid, sport, g))
                if not (t["axis"][0] <= lo and hi <= t["axis"][1]):
                    fouten.append("%s/%s/%s valt buiten de as %s" % (tid, sport, g, t["axis"]))
    if fouten:
        raise SystemExit("Controle mislukt:\n  " + "\n  ".join(fouten))

    with open(os.path.join(ROOT, "assets/data/benchmarks.json"), "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=1)
    write_legacy_js(data)

    print("benchmarks.json: %d tests, %d domeinen" % (len(data["tests"]), len(data["domains"])))
    for tid in ORDER:
        t = data["tests"][tid]
        combos = sum(len(v) for v in t["bands"].values())
        print("  %-9s %-9s %d banden, %d bron(nen)%s"
              % (tid, t["domain"], combos, len(t["sources"]),
                 ", voorlopig" if t["provisional"] else ""))
    print("benchmarks.js:   legacy-bestand opnieuw geschreven uit dezelfde gegevens")


if __name__ == "__main__":
    main()
