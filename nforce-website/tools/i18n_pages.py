# -*- coding: utf-8 -*-
"""
Copy voor de losse pagina's, in dezelfde vorm als tools/i18n.py.
Wordt onderaan i18n.py geregistreerd via register(add).
"""


def register(add):
    # -----------------------------------------------------------------------
    # Online coaching
    # -----------------------------------------------------------------------
    add("co_title", "Online coaching \u2014 wekelijkse aansturing op jouw cijfers | N-Force Performance",
        "Online coaching \u2014 weekly direction built on your numbers | N-Force Performance",
        "Online-Coaching \u2014 w\u00f6chentliche Steuerung auf Basis deiner Zahlen | N-Force Performance")
    add("co_desc",
        "Online strength &amp; conditioning met programma in de app, videofeedback en hertests elke zes weken. Vanaf \u20ac49 per maand.",
        "Online strength &amp; conditioning with an in-app programme, video feedback and retests every six weeks. From \u20ac49 per month.",
        "Online Strength &amp; Conditioning mit Programm in der App, Video-Feedback und Nachtests alle sechs Wochen. Ab \u20ac49 pro Monat.")
    add("co_eyebrow", "Online coaching", "Online coaching", "Online-Coaching")
    add("co_h1", "Een plan dat elke week meebeweegt met jouw seizoen",
        "A plan that moves with your season, every week",
        "Ein Plan, der sich jede Woche mit deiner Saison bewegt")
    add("co_lede",
        "Je krijgt geen standaardschema met jouw naam erboven. We beginnen met testen, kiezen \u00e9\u00e9n hoofdlijn en stellen die wekelijks bij op basis van wat je uitvoert, hoe je herstelt en wanneer je moet presteren.",
        "You don't get a template with your name on top. We start with testing, pick one main line and adjust it weekly based on what you execute, how you recover and when you have to perform.",
        "Du bekommst keine Vorlage mit deinem Namen darauf. Wir starten mit Tests, w\u00e4hlen eine Hauptlinie und passen sie w\u00f6chentlich an \u2014 nach Umsetzung, Erholung und Wettkampfterminen.")
    add("co_h2_incl", "Wat er in elk traject zit", "What's in every track", "Was in jedem Prozess steckt")
    add("co_incl",
        ("Intake van 45 minuten: kalender, historie, blessures, beschikbare faciliteiten",
         "Testbatterij met de zes onderdelen uit de zelftest en een schriftelijke analyse",
         "Programma in de coaching-app met video per oefening, sets, reps, tempo en RPE",
         "Techniekfeedback op de video's die je uploadt",
         "Hertest na elke zes weken en een nieuw blok op basis van de uitkomst",
         "Aanpassing bij ziekte, extra wedstrijden of een drukke week op school of werk"),
        ("A 45-minute intake: calendar, history, injuries, available facilities",
         "Test battery with the six items from the self-test plus a written analysis",
         "Programme in the coaching app with video per exercise, sets, reps, tempo and RPE",
         "Technique feedback on the videos you upload",
         "Retest every six weeks and a new block based on the outcome",
         "Adjustment when you're ill, have extra fixtures or a heavy week at school or work"),
        ("Intake von 45 Minuten: Kalender, Historie, Verletzungen, verf\u00fcgbare Einrichtungen",
         "Testbatterie mit den sechs Tests aus dem Selbsttest plus schriftliche Analyse",
         "Programm in der Coaching-App mit Video pro \u00dcbung, S\u00e4tzen, Wiederholungen, Tempo und RPE",
         "Technik-Feedback zu den Videos, die du hochl\u00e4dst",
         "Nachtest alle sechs Wochen und ein neuer Block je Ergebnis",
         "Anpassung bei Krankheit, zus\u00e4tzlichen Spielen oder einer vollen Woche in Schule oder Job"))
    add("co_h2_flow", "Hoe het loopt", "How it runs", "Wie es abl\u00e4uft")
    add("co_flow",
        (("Week 0", "Intake, testen, analyse. Je weet aan het eind van de week wat je hoofdlijn wordt en waarom."),
         ("Week 1\u20136", "Eerste blok. Twee tot vier sessies per week, afgestemd op je trainingen op het veld of het ijs."),
         ("Week 6", "Hertest. Alles wat boven de meetfout uitkomt is winst; de rest passen we aan."),
         ("Week 7\u201312", "Tweede blok, meer sportspecifiek. Vanaf hier zie je het effect in wedstrijden.")),
        (("Week 0", "Intake, testing, analysis. By the end of the week you know your main line and why."),
         ("Week 1\u20136", "First block. Two to four sessions a week, aligned with your work on the pitch or the ice."),
         ("Week 6", "Retest. Anything above the measurement error is a gain; the rest gets adjusted."),
         ("Week 7\u201312", "Second block, more sport-specific. From here you feel it in games.")),
        (("Woche 0", "Intake, Tests, Analyse. Am Ende der Woche kennst du deine Hauptlinie und den Grund daf\u00fcr."),
         ("Woche 1\u20136", "Erster Block. Zwei bis vier Einheiten pro Woche, abgestimmt auf Platz oder Eis."),
         ("Woche 6", "Nachtest. Alles \u00fcber dem Messfehler ist Fortschritt; der Rest wird angepasst."),
         ("Woche 7\u201312", "Zweiter Block, sportspezifischer. Ab hier merkst du es im Spiel.")))
    add("co_rtp_h", "Return-to-play", "Return-to-play", "Return-to-Play")
    add("co_rtp_p",
        "Terugkomen van een blessure is geen kwestie van pijnvrij zijn, maar van criteria halen: krachtverschil links-rechts onder de tien procent, sprongsymmetrie, sprint zonder compensatie en een opbouw in wedstrijdbelasting. Ik werk samen met je fysiotherapeut, niet in plaats van.",
        "Coming back from injury isn't about being pain-free, it's about meeting criteria: left-right strength difference under ten percent, jump symmetry, sprinting without compensation and a stepped build-up in match load. I work with your physio, not instead of them.",
        "Nach einer Verletzung z\u00e4hlt nicht Schmerzfreiheit, sondern das Erreichen von Kriterien: Kraftunterschied links-rechts unter zehn Prozent, Sprungsymmetrie, Sprint ohne Ausweichbewegung und ein stufenweiser Aufbau der Spielbelastung. Ich arbeite mit deinem Physiotherapeuten, nicht an seiner Stelle.")
    add("co_faq",
        (("Heb ik een sportschool nodig?", "Voor de meeste trajecten wel: je hebt een barbell, halters en een rek nodig. Kan dat niet, dan bouw ik een variant met bands, gewichtsvesten en sprongwerk \u2014 minder ideaal, maar bruikbaar."),
         ("Hoeveel tijd kost het per week?", "Twee tot vier sessies van 45 tot 75 minuten, plus tien minuten voor je video's en check-in. In het seizoen zakt dat naar twee kortere sessies."),
         ("Kan ik na twaalf weken stoppen?", "Ja. Na de minimale looptijd van twaalf weken is het maandelijks opzegbaar."),
         ("Werkt dit naast mijn teamtraining?", "Dat is precies het uitgangspunt. Je teamtraining is de belangrijkste belasting; mijn programma vult aan en gaat er niet mee concurreren.")),
        (("Do I need a gym?", "For most tracks yes: you need a barbell, dumbbells and a rack. If that's not possible I build a variant with bands, weighted vests and jump work \u2014 less ideal, still usable."),
         ("How much time per week?", "Two to four sessions of 45 to 75 minutes, plus ten minutes for your videos and check-in. In-season that drops to two shorter sessions."),
         ("Can I stop after twelve weeks?", "Yes. After the twelve-week minimum term it's cancellable monthly."),
         ("Does this work alongside team training?", "That's the whole starting point. Team training is your main load; my programme supplements it and won't compete with it.")),
        (("Brauche ich ein Fitnessstudio?", "F\u00fcr die meisten Prozesse ja: Langhantel, Kurzhanteln und ein Rack. Ist das nicht m\u00f6glich, baue ich eine Variante mit B\u00e4ndern, Gewichtsweste und Sprungarbeit \u2014 weniger ideal, aber brauchbar."),
         ("Wie viel Zeit pro Woche?", "Zwei bis vier Einheiten von 45 bis 75 Minuten, plus zehn Minuten f\u00fcr Videos und Check-in. In der Saison sinkt das auf zwei k\u00fcrzere Einheiten."),
         ("Kann ich nach zw\u00f6lf Wochen aufh\u00f6ren?", "Ja. Nach der Mindestlaufzeit von zw\u00f6lf Wochen ist monatlich k\u00fcndbar."),
         ("Funktioniert das neben dem Teamtraining?", "Genau das ist der Ausgangspunkt. Das Teamtraining ist die Hauptbelastung; mein Programm erg\u00e4nzt und konkurriert nicht.")))

    # -----------------------------------------------------------------------
    # Teams
    # -----------------------------------------------------------------------
    add("tm_title", "Teams &amp; clubs \u2014 testdag, rapport per speler en een seizoenslijn | N-Force Performance",
        "Teams &amp; clubs \u2014 test day, per-player report and a season line | N-Force Performance",
        "Teams &amp; Vereine \u2014 Testtag, Bericht pro Spieler und Saisonlinie | N-Force Performance")
    add("tm_desc",
        "Testdag voor de hele selectie, individuele rapporten en een trainingslijn voor het seizoen. Vanaf \u20ac750 per testdag, exclusief btw.",
        "Test day for the full squad, individual reports and a training line for the season. From \u20ac750 per test day, excluding VAT.",
        "Testtag f\u00fcr den ganzen Kader, individuelle Berichte und eine Trainingslinie f\u00fcr die Saison. Ab \u20ac750 pro Testtag, zzgl. MwSt.")
    add("tm_eyebrow", "Teams &amp; clubs", "Teams &amp; clubs", "Teams &amp; Vereine")
    add("tm_h1", "Weet waar je selectie staat \u2014 speler voor speler",
        "Know where your squad stands \u2014 player by player",
        "Wissen, wo dein Kader steht \u2014 Spieler f\u00fcr Spieler")
    add("tm_lede",
        "\u00c9\u00e9n testdag geeft je een objectief beeld van je hele groep: wie mag vol trainen, wie zit in de risicozone en waar liggen de teambrede gaten. Daarna krijg je een lijn die je staf zelf kan uitvoeren.",
        "One test day gives you an objective picture of the whole group: who can train fully, who sits in the risk zone and where the squad-wide gaps are. Then you get a line your own staff can run.",
        "Ein Testtag gibt dir ein objektives Bild der ganzen Gruppe: wer voll trainieren kann, wer in der Risikozone liegt und wo die teamweiten L\u00fccken sind. Danach bekommst du eine Linie, die dein Staff selbst umsetzen kann.")
    add("tm_h2", "Wat je krijgt", "What you get", "Was du bekommst")
    add("tm_items",
        (("Testdag", "Halve of hele dag op locatie. Zes onderdelen per speler, groepen van vier, gemiddeld twintig spelers per halve dag."),
         ("Rapport per speler", "Waarden, positie ten opzichte van de referentiewaarden voor de sport en \u00e9\u00e9n concrete prioriteit per speler."),
         ("Teamrapport", "Spreiding per domein, risicoprofielen en de twee of drie thema's waar de hele groep aan moet werken."),
         ("Seizoenslijn", "Blokindeling rond je wedstrijdkalender, met wat de staf in de zaal doet en wat op het veld of ijs hoort."),
         ("Staf-briefing", "Sessie van een uur waarin ik de uitkomsten en de uitvoering met je staf doorneem."),
         ("Hertest", "Optioneel na tien tot twaalf weken, zodat je ziet of de lijn werkt.")),
        (("Test day", "Half or full day on site. Six items per player, groups of four, on average twenty players per half day."),
         ("Report per player", "Values, position relative to the sport's reference ranges and one concrete priority per player."),
         ("Team report", "Spread per domain, risk profiles and the two or three themes the whole group needs to work on."),
         ("Season line", "Block structure around your fixture calendar, separating gym work from pitch or ice work."),
         ("Staff briefing", "A one-hour session running through the outcomes and the execution with your staff."),
         ("Retest", "Optional after ten to twelve weeks, so you can see whether the line works.")),
        (("Testtag", "Halber oder ganzer Tag vor Ort. Sechs Tests pro Spieler, Gruppen von vier, im Schnitt zwanzig Spieler pro halbem Tag."),
         ("Bericht pro Spieler", "Werte, Position gegen\u00fcber den Referenzbereichen der Sportart und eine konkrete Priorit\u00e4t pro Spieler."),
         ("Teambericht", "Streuung pro Bereich, Risikoprofile und die zwei bis drei Themen f\u00fcr die ganze Gruppe."),
         ("Saisonlinie", "Blockstruktur rund um den Spielkalender, getrennt in Kraftraum und Platz beziehungsweise Eis."),
         ("Staff-Briefing", "Einst\u00fcndige Sitzung, in der ich Ergebnisse und Umsetzung mit dem Staff durchgehe."),
         ("Nachtest", "Optional nach zehn bis zw\u00f6lf Wochen, damit du siehst, ob die Linie funktioniert.")))
    add("tm_price_h", "Investering", "Investment", "Investition")
    add("tm_price_p",
        "Vanaf \u20ac750 per testdag exclusief btw, inclusief rapporten en staf-briefing. Reiskosten binnen Nederland zijn inbegrepen; voor Belgi\u00eb en Duitsland maak ik een aparte opgave. Grotere selecties of meerdere teams: prijs op aanvraag.",
        "From \u20ac750 per test day excluding VAT, including reports and staff briefing. Travel within the Netherlands is included; for Belgium and Germany I quote separately. Larger squads or multiple teams: price on request.",
        "Ab \u20ac750 pro Testtag zzgl. MwSt., inklusive Berichte und Staff-Briefing. Reisekosten innerhalb der Niederlande inklusive; f\u00fcr Belgien und Deutschland erstelle ich ein separates Angebot. Gr\u00f6\u00dfere Kader oder mehrere Teams: Preis auf Anfrage.")
    add("tm_faq",
        (("Hoeveel spelers kunnen er op een dag?", "Ongeveer twintig per halve dag met \u00e9\u00e9n tester. Bij grotere selecties werk ik met een assistent of splitsen we over twee dagdelen."),
         ("Wat hebben we nodig?", "Een zaal of veld van minimaal dertig meter, een krachtruimte voor het squat-onderdeel en een ruimte voor de briefing."),
         ("Krijgen spelers hun eigen resultaten?", "Ja, elke speler krijgt zijn eigen rapport. Het teamrapport gaat naar de staf.")),
        (("How many players fit in a day?", "Around twenty per half day with one tester. For larger squads I bring an assistant or split across two sessions."),
         ("What do we need?", "A hall or pitch of at least thirty metres, a gym space for the squat item and a room for the briefing."),
         ("Do players get their own results?", "Yes, every player gets their own report. The team report goes to the staff.")),
        (("Wie viele Spieler passen an einen Tag?", "Etwa zwanzig pro halbem Tag mit einem Tester. Bei gr\u00f6\u00dferen Kadern bringe ich einen Assistenten mit oder wir teilen auf zwei Einheiten."),
         ("Was brauchen wir?", "Eine Halle oder einen Platz von mindestens drei\u00dfig Metern, einen Kraftraum f\u00fcr die Kniebeuge und einen Raum f\u00fcr das Briefing."),
         ("Bekommen Spieler ihre eigenen Ergebnisse?", "Ja, jeder Spieler bekommt seinen eigenen Bericht. Der Teambericht geht an den Staff.")))

    # -----------------------------------------------------------------------
    # Testing
    # -----------------------------------------------------------------------
    add("te_title", "Testing \u2014 zes onderdelen die je profiel bepalen | N-Force Performance",
        "Testing \u2014 the six items that define your profile | N-Force Performance",
        "Testing \u2014 die sechs Tests, die dein Profil bestimmen | N-Force Performance")
    add("te_desc",
        "Countermovement jump, relatieve squat, 10 en 30 meter sprint, 505 en uithoudingstest: hoe je meet, wat de meetfout is en wat de uitslag betekent.",
        "Countermovement jump, relative squat, 10 and 30 metre sprint, 505 and endurance test: how to measure, the measurement error and what the result means.",
        "Countermovement Jump, relative Kniebeuge, 10 und 30 Meter Sprint, 505 und Ausdauertest: wie du misst, wie gro\u00df der Messfehler ist und was das Ergebnis bedeutet.")
    add("te_eyebrow", "Testing &amp; analyse", "Testing &amp; analysis", "Testing &amp; Analyse")
    add("te_h1", "Zes onderdelen, zeven domeinen, \u00e9\u00e9n conclusie",
        "Six items, seven domains, one conclusion",
        "Sechs Tests, sieben Bereiche, eine Schlussfolgerung")
    add("te_lede",
        "Deze zes tests dekken samen alles wat er in een sprint-, duel- en wendsport gebeurt. Ze zijn met eenvoudig materiaal betrouwbaar te herhalen \u2014 dat is belangrijker dan een duur apparaat dat je \u00e9\u00e9n keer gebruikt.",
        "These six tests together cover everything that happens in a sprint, duel and turning sport. They can be repeated reliably with simple equipment \u2014 which matters more than an expensive device you use once.",
        "Diese sechs Tests decken zusammen alles ab, was in einer Sprint-, Duell- und Wendesportart passiert. Sie sind mit einfachem Material zuverl\u00e4ssig wiederholbar \u2014 das z\u00e4hlt mehr als ein teures Ger\u00e4t, das du einmal benutzt.")
    add("te_table_h", "De testbatterij", "The test battery", "Die Testbatterie")
    add("te_cols", ("Test", "Domein", "Wat je meet", "Meetfout"),
        ("Test", "Domain", "What it measures", "Error"),
        ("Test", "Bereich", "Was gemessen wird", "Messfehler"))
    add("te_rows",
        (("Countermovement jump", "Elasticiteit", "Explosieve kracht met tegenbeweging \u2014 de basis van elke versnelling", "\u00b12 cm"),
         ("Relatieve squat (1RM/kg)", "Kracht", "Maximale kracht ten opzichte van je lichaamsgewicht", "\u00b10,05"),
         ("10 meter sprint", "Acceleratie", "Startkracht en eerste passen \u2014 het meest wedstrijdrelevante stuk", "\u00b10,03 s"),
         ("30 meter sprint", "Topsnelheid", "Vermogen om snelheid vast te houden en verder op te bouwen", "\u00b10,05 s"),
         ("505 change of direction", "Wenden", "Afremmen en opnieuw versnellen over 180 graden", "\u00b10,05 s"),
         ("Yo-Yo IR1 of shuttle", "Motor", "Herhaald vermogen: hoe vaak je een sprint kunt herhalen", "\u00b1120 m")),
        (("Countermovement jump", "Elasticity", "Explosive strength with a countermovement \u2014 the base of every acceleration", "\u00b12 cm"),
         ("Relative squat (1RM/kg)", "Strength", "Maximal strength relative to your body weight", "\u00b10.05"),
         ("10 metre sprint", "Acceleration", "Start strength and first steps \u2014 the most match-relevant segment", "\u00b10.03 s"),
         ("30 metre sprint", "Top speed", "Ability to hold and keep building speed", "\u00b10.05 s"),
         ("505 change of direction", "Turning", "Decelerating and re-accelerating through 180 degrees", "\u00b10.05 s"),
         ("Yo-Yo IR1 or shuttle", "Engine", "Repeat capacity: how often you can repeat a sprint", "\u00b1120 m")),
        (("Countermovement Jump", "Elastizit\u00e4t", "Explosivkraft mit Gegenbewegung \u2014 die Basis jeder Beschleunigung", "\u00b12 cm"),
         ("Relative Kniebeuge (1RM/kg)", "Kraft", "Maximalkraft im Verh\u00e4ltnis zum K\u00f6rpergewicht", "\u00b10,05"),
         ("10-Meter-Sprint", "Beschleunigung", "Startkraft und erste Schritte \u2014 der spielrelevanteste Abschnitt", "\u00b10,03 s"),
         ("30-Meter-Sprint", "H\u00f6chstgeschwindigkeit", "F\u00e4higkeit, Geschwindigkeit zu halten und weiter aufzubauen", "\u00b10,05 s"),
         ("505 Change of Direction", "Wenden", "Abbremsen und erneut beschleunigen \u00fcber 180 Grad", "\u00b10,05 s"),
         ("Yo-Yo IR1 oder Shuttle", "Motor", "Wiederholungsverm\u00f6gen: wie oft du einen Sprint wiederholen kannst", "\u00b1120 m")))
    add("te_how_h", "Zo meet je betrouwbaar", "How to measure reliably", "So misst du zuverl\u00e4ssig")
    add("te_how",
        ("Test altijd op hetzelfde moment van de dag, na dezelfde warming-up en met dezelfde schoenen.",
         "Drie pogingen per test, beste poging telt, twee tot drie minuten rust tussen pogingen.",
         "Sprint op een vlakke, droge ondergrond. Buiten met wind: test met de wind dwars, niet mee.",
         "Test niet binnen 48 uur na een wedstrijd of zware krachtsessie.",
         "Noteer alles: datum, ondergrond, materiaal, gevoel. Zonder context is een cijfer waardeloos."),
        ("Always test at the same time of day, after the same warm-up and in the same shoes.",
         "Three attempts per test, best attempt counts, two to three minutes rest between attempts.",
         "Sprint on a flat, dry surface. Outside with wind: test with a crosswind, not a tailwind.",
         "Don't test within 48 hours of a game or a heavy strength session.",
         "Write everything down: date, surface, equipment, how you felt. A number without context is worthless."),
        ("Teste immer zur gleichen Tageszeit, nach dem gleichen Warm-up und in denselben Schuhen.",
         "Drei Versuche pro Test, der beste z\u00e4hlt, zwei bis drei Minuten Pause zwischen den Versuchen.",
         "Sprinte auf flachem, trockenem Boden. Drau\u00dfen bei Wind: quer testen, nicht mit R\u00fcckenwind.",
         "Teste nicht innerhalb von 48 Stunden nach Spiel oder schwerer Krafteinheit.",
         "Notiere alles: Datum, Untergrund, Material, Gef\u00fchl. Eine Zahl ohne Kontext ist wertlos."))
    add("te_cta_h", "Klaar met meten? Vul je waarden in.", "Done measuring? Enter your numbers.",
        "Fertig gemessen? Gib deine Werte ein.")
    add("te_cta_p",
        "De zelftest zet je waarden naast de referentiewaarden van je sport en geeft direct het handboek dat bij je zwakste domein hoort.",
        "The self-test places your values next to the reference ranges for your sport and immediately gives the handbook matching your weakest domain.",
        "Der Selbsttest stellt deine Werte neben die Referenzbereiche deiner Sportart und nennt sofort das Handbuch, das zu deinem schw\u00e4chsten Bereich passt.")

    # -----------------------------------------------------------------------
    # Zelftest
    # -----------------------------------------------------------------------
    add("st_title", "Zelftest \u2014 zie waar je staat en welk handboek daarbij hoort | N-Force Performance",
        "Self-test \u2014 see where you stand and which handbook fits | N-Force Performance",
        "Selbsttest \u2014 sieh, wo du stehst und welches Handbuch passt | N-Force Performance")
    add("st_desc",
        "Vul je test- en profielgegevens in en krijg per domein je positie plus een rule-based handboekadvies. Gratis, geen account nodig.",
        "Enter your test and profile data and get your position per domain plus a rule-based handbook recommendation. Free, no account needed.",
        "Gib deine Test- und Profildaten ein und erhalte deine Position pro Bereich plus eine regelbasierte Handbuch-Empfehlung. Kostenlos, ohne Konto.")
    add("st_eyebrow", "Zelftest &amp; analyse", "Self-test &amp; analysis", "Selbsttest &amp; Analyse")
    add("st_h1", "Vul je waarden in, krijg je prioriteit",
        "Enter your values, get your priority",
        "Gib deine Werte ein, erhalte deine Priorit\u00e4t")
    add("st_lede",
        "Je hoeft niet alle zes tests te hebben gedaan \u2014 \u00e9\u00e9n waarde is genoeg om te beginnen, meer waarden geven een scherper advies. Er wordt niets opgeslagen op een server: de analyse gebeurt in je browser.",
        "You don't need all six tests \u2014 one value is enough to start, more values sharpen the advice. Nothing is stored on a server: the analysis happens in your browser.",
        "Du brauchst nicht alle sechs Tests \u2014 ein Wert reicht zum Start, mehr Werte sch\u00e4rfen die Empfehlung. Es wird nichts auf einem Server gespeichert: die Analyse l\u00e4uft in deinem Browser.")
    add("st_howto_h", "Wat je straks ziet", "What you'll see", "Was du sehen wirst")
    add("st_howto",
        (("Positie per test", "Een schaal met de referentiebandbreedte voor jouw sport, geslacht en de plek van jouw waarde daarin."),
         ("Zwakste domein", "De domeinen waar je onder de bandbreedte zit, met een korte uitleg wat dat in wedstrijden betekent."),
         ("Handboekadvies", "\u00c9\u00e9n primair handboek plus maximaal twee aanvullende, met per advies de reden erbij.")),
        (("Position per test", "A scale with the reference range for your sport and sex, and where your value sits in it."),
         ("Weakest domain", "The domains where you sit below the range, with a short explanation of what that means in games."),
         ("Handbook advice", "One primary handbook plus a maximum of two additions, each with the reason attached.")),
        (("Position pro Test", "Eine Skala mit dem Referenzbereich f\u00fcr Sportart und Geschlecht und der Lage deines Werts darin."),
         ("Schw\u00e4chster Bereich", "Die Bereiche, in denen du unter dem Bereich liegst, mit kurzer Erkl\u00e4rung f\u00fcr das Spiel."),
         ("Handbuch-Empfehlung", "Ein prim\u00e4res Handbuch plus maximal zwei Erg\u00e4nzungen, jeweils mit Begr\u00fcndung.")))

    # -----------------------------------------------------------------------
    # Handboeken
    # -----------------------------------------------------------------------
    add("hb_title", "Handboeken \u2014 complete trainingsblokken in Core en Pro | N-Force Performance",
        "Handbooks \u2014 complete training blocks in Core and Pro | N-Force Performance",
        "Handb\u00fccher \u2014 komplette Trainingsbl\u00f6cke in Core und Pro | N-Force Performance")
    add("hb_desc",
        "Trainingshandboeken voor kracht, snelheid, wenden, conditie en return-to-play. Core en Pro, in NL, EN en DE, vanaf \u20ac29 met directe download.",
        "Training handbooks for strength, speed, turning, conditioning and return-to-play. Core and Pro, in NL, EN and DE, from \u20ac29 with instant download.",
        "Trainingshandb\u00fccher f\u00fcr Kraft, Schnelligkeit, Wenden, Kondition und Return-to-Play. Core und Pro, in NL, EN und DE, ab \u20ac29 mit Sofort-Download.")
    add("hb_eyebrow", "Handboeken", "Handbooks", "Handb\u00fccher")
    add("hb_h1", "Complete blokken, geen losse oefeningen",
        "Complete blocks, not loose exercises",
        "Komplette Bl\u00f6cke, keine losen \u00dcbungen")
    add("hb_lede",
        "Elk handboek bevat weekschema\u2019s, series, herhalingen, tempo, rust, progressieregels en de testcriteria om naar het volgende blok te gaan. Je krijgt een PDF die je op je telefoon in de zaal gebruikt, in de taal die je kiest.",
        "Every handbook contains weekly schedules, sets, reps, tempo, rest, progression rules and the test criteria to move to the next block. You get a PDF you use on your phone in the gym, in the language you choose.",
        "Jedes Handbuch enth\u00e4lt Wochenpl\u00e4ne, S\u00e4tze, Wiederholungen, Tempo, Pausen, Progressionsregeln und die Testkriterien f\u00fcr den n\u00e4chsten Block. Du bekommst ein PDF f\u00fcr das Handy im Kraftraum, in deiner Sprache.")
    add("hb_core_pro_h", "Core of Pro?", "Core or Pro?", "Core oder Pro?")
    add("hb_core_pro",
        (("Core", "De complete basis: het blok, de oefeningen, de progressie en een korte testhandleiding. Genoeg om zelfstandig zes tot acht weken vooruit te kunnen."),
         ("Pro", "Alles uit Core plus sportspecifieke blokken, langere periodisering, een volledig testprotocol, varianten voor beperkt materiaal en een invulbaar logboek.")),
        (("Core", "The complete base: the block, the exercises, the progression and a short testing guide. Enough to run six to eight weeks independently."),
         ("Pro", "Everything in Core plus sport-specific blocks, longer periodisation, a full test protocol, limited-equipment variants and a fillable log.")),
        (("Core", "Die komplette Basis: der Block, die \u00dcbungen, die Progression und eine kurze Testanleitung. Genug f\u00fcr sechs bis acht Wochen in Eigenregie."),
         ("Pro", "Alles aus Core plus sportspezifische Bl\u00f6cke, l\u00e4ngere Periodisierung, volles Testprotokoll, Varianten f\u00fcr wenig Material und ein ausf\u00fcllbares Logbuch.")))
    add("hb_flow_h", "Hoe het werkt", "How it works", "So funktioniert es")
    add("hb_flow",
        (("01", "Bekijk de preview", "Bij elk handboek zie je voor wie het is, wat je leert en de inhoudsopgave van het blok."),
         ("02", "Zet in je mandje", "Meerdere handboeken combineren kan; je ziet het totaal voordat je afrekent."),
         ("03", "Download", "Na de bestelling ontvang je de PDF in de taal die je kiest, plus updates van dat handboek.")),
        (("01", "Check the preview", "Every handbook shows who it's for, what you'll learn and the block's table of contents."),
         ("02", "Add to cart", "You can combine handbooks; you see the total before you check out."),
         ("03", "Download", "After ordering you receive the PDF in your chosen language, plus updates of that handbook.")),
        (("01", "Vorschau ansehen", "Bei jedem Handbuch siehst du, f\u00fcr wen es ist, was du lernst und das Inhaltsverzeichnis des Blocks."),
         ("02", "In den Warenkorb", "Du kannst Handb\u00fccher kombinieren; du siehst die Summe, bevor du zur Kasse gehst."),
         ("03", "Download", "Nach der Bestellung erh\u00e4ltst du das PDF in deiner Sprache, plus Updates dieses Handbuchs.")))
    add("hb_faq",
        (("In welk formaat krijg ik het handboek?", "Als PDF, geoptimaliseerd voor telefoon en tablet. Pro-versies bevatten daarnaast een invulbaar logboek."),
         ("Kan ik van Core naar Pro upgraden?", "Ja. Je betaalt dan het prijsverschil; mail me je bestelnummer."),
         ("Krijg ik updates?", "Ja. Bij een nieuwe versie van een handboek dat je hebt gekocht, ontvang je die kosteloos."),
         ("Welk handboek moet ik hebben?", "Doe de zelftest. Op basis van je waarden, sport, niveau en fase komt er automatisch \u00e9\u00e9n primair advies uit.")),
        (("What format is the handbook?", "A PDF, optimised for phone and tablet. Pro versions also include a fillable log."),
         ("Can I upgrade from Core to Pro?", "Yes. You pay the price difference; email me your order number."),
         ("Do I get updates?", "Yes. When a handbook you bought gets a new version, you receive it free of charge."),
         ("Which handbook do I need?", "Take the self-test. Based on your values, sport, level and phase it produces one primary recommendation.")),
        (("In welchem Format kommt das Handbuch?", "Als PDF, optimiert f\u00fcr Handy und Tablet. Pro-Versionen enthalten zus\u00e4tzlich ein ausf\u00fcllbares Logbuch."),
         ("Kann ich von Core auf Pro upgraden?", "Ja. Du zahlst die Differenz; schreib mir deine Bestellnummer."),
         ("Bekomme ich Updates?", "Ja. Erscheint eine neue Version eines gekauften Handbuchs, bekommst du sie kostenlos."),
         ("Welches Handbuch brauche ich?", "Mach den Selbsttest. Aus Werten, Sportart, Niveau und Phase ergibt sich automatisch eine prim\u00e4re Empfehlung.")))

    # -----------------------------------------------------------------------
    # Bestellen
    # -----------------------------------------------------------------------
    add("ck_title", "Bestellen | N-Force Performance", "Checkout | N-Force Performance", "Kasse | N-Force Performance")
    add("ck_desc", "Overzicht van je handboeken en afronden van je bestelling.",
        "Overview of your handbooks and completing your order.",
        "\u00dcbersicht deiner Handb\u00fccher und Abschluss der Bestellung.")
    add("ck_eyebrow", "Bestellen", "Checkout", "Kasse")
    add("ck_h1", "Je bestelling afronden", "Complete your order", "Bestellung abschlie\u00dfen")
    add("ck_lede",
        "Controleer je handboeken en rond af. Je ontvangt de PDF in de taal die je hebt gekozen, met updates van datzelfde handboek.",
        "Check your handbooks and complete the order. You receive the PDF in your chosen language, with updates of that same handbook.",
        "Pr\u00fcfe deine Handb\u00fccher und schlie\u00dfe ab. Du erh\u00e4ltst das PDF in deiner Sprache, inklusive Updates dieses Handbuchs.")

    # -----------------------------------------------------------------------
    # Tarieven
    # -----------------------------------------------------------------------
    add("pr_title", "Tarieven \u2014 coaching, handboeken en teams | N-Force Performance",
        "Pricing \u2014 coaching, handbooks and teams | N-Force Performance",
        "Preise \u2014 Coaching, Handb\u00fccher und Teams | N-Force Performance")
    add("pr_desc",
        "Alle tarieven op \u00e9\u00e9n pagina: online coaching vanaf \u20ac49 per maand, handboeken vanaf \u20ac29 en teams vanaf \u20ac750 per testdag.",
        "All rates on one page: online coaching from \u20ac49 per month, handbooks from \u20ac29 and teams from \u20ac750 per test day.",
        "Alle Preise auf einer Seite: Online-Coaching ab \u20ac49 pro Monat, Handb\u00fccher ab \u20ac29 und Teams ab \u20ac750 pro Testtag.")
    add("pr_eyebrow", "Tarieven", "Pricing", "Preise")
    add("pr_h1", "Wat het kost en wat je ervoor krijgt",
        "What it costs and what you get", "Was es kostet und was du bekommst")
    add("pr_lede",
        "Geen instapaanbiedingen die daarna verdubbelen. Maandprijzen zijn inclusief btw, teamtarieven exclusief btw.",
        "No entry offers that double later. Monthly prices include VAT, team rates exclude VAT.",
        "Keine Einstiegsangebote, die sich sp\u00e4ter verdoppeln. Monatspreise inkl. MwSt., Teampreise zzgl. MwSt.")
    add("pr_hb_h", "Handboeken", "Handbooks", "Handb\u00fccher")
    add("pr_hb_p",
        "Core-versies liggen tussen \u20ac29 en \u20ac39, Pro-versies tussen \u20ac79 en \u20ac99. Eenmalige aanschaf, directe download, updates inbegrepen.",
        "Core versions range from \u20ac29 to \u20ac39, Pro versions from \u20ac79 to \u20ac99. One-off purchase, instant download, updates included.",
        "Core-Versionen kosten \u20ac29 bis \u20ac39, Pro-Versionen \u20ac79 bis \u20ac99. Einmalkauf, Sofort-Download, Updates inklusive.")
    add("pr_teams_h", "Teams &amp; clubs", "Teams &amp; clubs", "Teams &amp; Vereine")
    add("pr_faq",
        (("Zit er btw op de maandprijzen?", "Ja, de genoemde maandprijzen zijn inclusief btw. Teamtarieven zijn exclusief btw."),
         ("Kan ik per kwartaal betalen?", "Ja, dat kan bij Performance en Return-to-Play. Meld het bij de intake."),
         ("Is er een studentenkorting?", "Voor spelers onder de achttien en studenten met een geldige kaart geldt tien procent korting op de maandprijs.")),
        (("Do monthly prices include VAT?", "Yes, the monthly prices shown include VAT. Team rates exclude VAT."),
         ("Can I pay quarterly?", "Yes, for Performance and Return-to-Play. Mention it at the intake."),
         ("Is there a student discount?", "Players under eighteen and students with a valid card get ten percent off the monthly price.")),
        (("Sind die Monatspreise inkl. MwSt.?", "Ja, die genannten Monatspreise sind inkl. MwSt. Teampreise sind zzgl. MwSt."),
         ("Kann ich quartalsweise zahlen?", "Ja, bei Performance und Return-to-Play. Sag es beim Intake."),
         ("Gibt es Studentenrabatt?", "Spieler unter achtzehn und Studierende mit g\u00fcltigem Ausweis erhalten zehn Prozent auf den Monatspreis.")))

    # -----------------------------------------------------------------------
    # Over
    # -----------------------------------------------------------------------
    add("ab_title", "Over Nick Bergman | N-Force Performance",
        "About Nick Bergman | N-Force Performance", "\u00dcber Nick Bergman | N-Force Performance")
    add("ab_desc",
        "Performance coach in Tilburg, werkzaam met ijshockeyspelers en teamsporters. Achtergrond, werkwijze en waar ik niet in geloof.",
        "Performance coach in Tilburg, working with ice hockey players and team-sport athletes. Background, method and what I don't believe in.",
        "Performance Coach in Tilburg, arbeitet mit Eishockeyspielern und Teamsportlern. Hintergrund, Vorgehen und was ich nicht glaube.")
    add("ab_eyebrow", "Over Nick", "About Nick", "\u00dcber Nick")
    add("ab_h1", "Ik werk met cijfers omdat gevoel te vaak liegt",
        "I work with numbers because feel lies too often",
        "Ich arbeite mit Zahlen, weil Gef\u00fchl zu oft t\u00e4uscht")
    add("ab_body",
        ("Ik ben Nick Bergman, performance coach in Tilburg. Ik werk dagelijks met ijshockeyspelers en teamsporters aan kracht, snelheid, wenden en robuustheid \u2014 op de vloer en online.",
         "Mijn achtergrond is de Fontys Sporthogeschool, mijn praktijk staat in de zaal en op het ijs. Wat ik daar zie is bijna altijd hetzelfde: spelers die hard werken aan wat ze al kunnen, en het domein dat hen tegenhoudt onaangeroerd laten. Dat is geen motivatieprobleem, dat is een informatieprobleem.",
         "Daarom begint alles bij mij met meten en eindigt het met hertesten. Niet omdat cijfers alles zijn, maar omdat ze het gesprek eerlijk houden. Als een blok niet werkt, wil ik dat na zes weken weten \u2014 niet na een seizoen."),
        ("I'm Nick Bergman, performance coach in Tilburg. I work daily with ice hockey players and team-sport athletes on strength, speed, turning and robustness \u2014 on the floor and online.",
         "My background is Fontys University of Applied Sciences for Sport; my practice is in the gym and on the ice. What I see there is almost always the same: players working hard on what they already do well, leaving the domain that holds them back untouched. That's not a motivation problem, it's an information problem.",
         "So everything starts with measuring and ends with retesting. Not because numbers are everything, but because they keep the conversation honest. If a block doesn't work, I want to know after six weeks \u2014 not after a season."),
        ("Ich bin Nick Bergman, Performance Coach in Tilburg. Ich arbeite t\u00e4glich mit Eishockeyspielern und Teamsportlern an Kraft, Schnelligkeit, Wenden und Robustheit \u2014 in der Halle und online.",
         "Mein Hintergrund ist die Fontys Sporthochschule, meine Praxis liegt im Kraftraum und auf dem Eis. Was ich dort sehe, ist fast immer dasselbe: Spieler arbeiten hart an dem, was sie schon k\u00f6nnen, und lassen den Bereich unangetastet, der sie aufh\u00e4lt. Das ist kein Motivationsproblem, sondern ein Informationsproblem.",
         "Deshalb beginnt bei mir alles mit Messen und endet mit Nachtesten. Nicht weil Zahlen alles sind, sondern weil sie das Gespr\u00e4ch ehrlich halten. Wenn ein Block nicht funktioniert, will ich es nach sechs Wochen wissen \u2014 nicht nach einer Saison."))
    add("ab_principles_h", "Waar ik op werk", "How I work", "Wonach ich arbeite")
    add("ab_principles",
        (("Eerst meten", "Zonder beginwaarden is elke conclusie een mening."),
         ("E\u00e9n hoofdlijn per blok", "Vier doelen tegelijk is geen plan, dat is hoop met een spreadsheet."),
         ("Belasting eerst", "Je teamtraining en wedstrijden zijn de hoofdmoot. Alles wat ik doe past daarnaast."),
         ("Eerlijk over grenzen", "Ben ik niet de juiste persoon of hoort iets bij een fysiotherapeut of arts, dan zeg ik dat.")),
        (("Measure first", "Without baseline numbers every conclusion is an opinion."),
         ("One main line per block", "Four goals at once isn't a plan, it's hope with a spreadsheet."),
         ("Load first", "Your team training and games are the main course. Everything I do fits alongside."),
         ("Honest about limits", "If I'm not the right person, or something belongs with a physio or doctor, I say so.")),
        (("Erst messen", "Ohne Ausgangswerte ist jede Schlussfolgerung eine Meinung."),
         ("Eine Hauptlinie pro Block", "Vier Ziele gleichzeitig sind kein Plan, sondern Hoffnung mit Tabelle."),
         ("Belastung zuerst", "Teamtraining und Spiele sind die Hauptsache. Alles, was ich mache, passt daneben."),
         ("Ehrlich \u00fcber Grenzen", "Bin ich nicht der Richtige oder geh\u00f6rt etwas zu Physio oder Arzt, sage ich das.")))

    # -----------------------------------------------------------------------
    # Performance Check / contact
    # -----------------------------------------------------------------------
    add("ct_title", "Performance Check \u2014 gratis gesprek van 20 minuten | N-Force Performance",
        "Performance Check \u2014 free 20-minute call | N-Force Performance",
        "Performance-Check \u2014 kostenloses 20-Minuten-Gespr\u00e4ch | N-Force Performance")
    add("ct_desc",
        "Gratis gesprek van twintig minuten, online of telefonisch. Je krijgt een eerlijke inschatting van je grootste beperking. Geen verkoopgesprek.",
        "Free twenty-minute call, online or by phone. You get an honest read on your biggest limiter. Not a sales call.",
        "Kostenloses Gespr\u00e4ch von zwanzig Minuten, online oder telefonisch. Du bekommst eine ehrliche Einsch\u00e4tzung deines gr\u00f6\u00dften Limiters. Kein Verkaufsgespr\u00e4ch.")
    add("ct_eyebrow", "Performance Check", "Performance Check", "Performance-Check")
    add("ct_h1", "Twintig minuten, geen verkooppraatje",
        "Twenty minutes, no sales pitch", "Zwanzig Minuten, kein Verkaufsgespr\u00e4ch")
    add("ct_lede",
        "We nemen je sport, kalender, historie en eventuele testwaarden door. Aan het eind weet je wat je grootste beperking is en wat de logische volgende stap is \u2014 een handboek, coaching of gewoon iets anders regelen.",
        "We go through your sport, calendar, history and any test values. At the end you know your biggest limiter and the logical next step \u2014 a handbook, coaching, or simply sorting something else out.",
        "Wir gehen Sportart, Kalender, Historie und eventuelle Testwerte durch. Am Ende kennst du deinen gr\u00f6\u00dften Limiter und den logischen n\u00e4chsten Schritt \u2014 ein Handbuch, Coaching oder einfach etwas anderes regeln.")
    add("ct_steps_h", "Wat er gebeurt", "What happens", "Was passiert")
    add("ct_steps",
        (("1", "Je stuurt het formulier of belt", "Binnen \u00e9\u00e9n werkdag heb je antwoord met twee voorstellen voor een moment."),
         ("2", "Gesprek van twintig minuten", "Online of telefonisch. Kort, concreet, geen presentatie."),
         ("3", "Je krijgt het advies op papier", "Ook als dat betekent dat je bij mij niets hoeft af te nemen.")),
        (("1", "You send the form or call", "Within one working day you get a reply with two suggested slots."),
         ("2", "Twenty-minute call", "Online or by phone. Short, concrete, no presentation."),
         ("3", "You get the advice in writing", "Even if that means you don't need to buy anything from me.")),
        (("1", "Du sendest das Formular oder rufst an", "Innerhalb eines Werktags erh\u00e4ltst du eine Antwort mit zwei Terminvorschl\u00e4gen."),
         ("2", "Gespr\u00e4ch von zwanzig Minuten", "Online oder telefonisch. Kurz, konkret, keine Pr\u00e4sentation."),
         ("3", "Du bekommst die Empfehlung schriftlich", "Auch wenn du dann nichts bei mir kaufen musst.")))
    add("ct_form_h", "Stuur je aanvraag", "Send your request", "Anfrage senden")
    add("ct_f_name", "Naam", "Name", "Name")
    add("ct_f_email", "E-mailadres", "Email address", "E-Mail-Adresse")
    add("ct_f_sport", "Sport en niveau", "Sport and level", "Sportart und Niveau")
    add("ct_f_goal", "Waar loop je tegenaan?", "What are you running into?", "Wo h\u00e4ngst du?")
    add("ct_f_send", "Aanvraag versturen", "Send request", "Anfrage senden")
    add("ct_f_note",
        "Ik gebruik je gegevens alleen om te reageren op deze aanvraag. Zie de privacyverklaring.",
        "I only use your details to reply to this request. See the privacy statement.",
        "Ich nutze deine Daten nur, um auf diese Anfrage zu antworten. Siehe Datenschutzerkl\u00e4rung.")
    add("ct_direct_h", "Liever direct?", "Prefer direct contact?", "Lieber direkt?")
    add("ct_direct_p",
        "Bellen of WhatsApp mag ook. Ik antwoord meestal binnen een paar uur, buiten trainingstijden.",
        "Calling or WhatsApp works too. I usually reply within a few hours, outside training hours.",
        "Anrufen oder WhatsApp geht auch. Ich antworte meist innerhalb weniger Stunden, au\u00dferhalb der Trainingszeiten.")

    # -----------------------------------------------------------------------
    # Juridisch
    # -----------------------------------------------------------------------
    add("pv_title", "Privacyverklaring | N-Force Performance",
        "Privacy statement | N-Force Performance", "Datenschutzerkl\u00e4rung | N-Force Performance")
    add("pv_desc", "Welke gegevens N-Force Performance verwerkt, waarvoor en hoe lang.",
        "Which data N-Force Performance processes, for what purpose and for how long.",
        "Welche Daten N-Force Performance verarbeitet, wof\u00fcr und wie lange.")
    add("pv_h1", "Privacyverklaring", "Privacy statement", "Datenschutzerkl\u00e4rung")
    add("pv_lede",
        "Kort en concreet: ik verwerk zo weinig gegevens als nodig en verkoop niets door.",
        "Short and concrete: I process as little data as necessary and sell nothing on.",
        "Kurz und konkret: ich verarbeite so wenig Daten wie n\u00f6tig und verkaufe nichts weiter.")
    add("pv_blocks",
        (("Wie is verantwoordelijk?", "N-Force Performance, Nick Bergman, Tilburg. KVK 99722283. Contact via nick@nforce-performance.nl."),
         ("Welke gegevens?", "Naam, e-mailadres en de informatie die je zelf in het contactformulier zet. Bij coaching daarnaast testwaarden, blessurehistorie en trainingsgegevens die je aanlevert."),
         ("De zelftest", "De waarden die je in de zelftest invult blijven in je browser. Ze worden niet naar een server verzonden en niet opgeslagen in een database. Je winkelwagen en laatste zelftestresultaat worden lokaal in je browser bewaard, zodat je ze bij terugkomst nog ziet."),
         ("Waarvoor gebruik ik het?", "Om te reageren op je aanvraag, om coaching uit te voeren en om een bestelling af te handelen. Niets anders."),
         ("Hoe lang?", "Contactaanvragen bewaar ik maximaal twaalf maanden. Coachinggegevens tot twee jaar na afloop van het traject, factuurgegevens zeven jaar vanwege de belastingplicht."),
         ("Delen met anderen", "Alleen als het nodig is voor de uitvoering: de coaching-app, e-mail en de betaalprovider. Nooit voor advertentiedoeleinden."),
         ("Jouw rechten", "Inzage, correctie, verwijdering en het intrekken van toestemming. E\u00e9n mail is genoeg; ik reageer binnen vier weken."),
         ("Cookies", "Deze site gebruikt geen tracking- of advertentiecookies. Alleen lokale opslag voor je taalkeuze, winkelwagen en zelftestresultaat.")),
        (("Who is responsible?", "N-Force Performance, Nick Bergman, Tilburg, the Netherlands. Chamber of Commerce 99722283. Contact via nick@nforce-performance.nl."),
         ("Which data?", "Name, email address and whatever you put in the contact form yourself. For coaching also test values, injury history and training data you supply."),
         ("The self-test", "The values you enter in the self-test stay in your browser. They are not sent to a server and not stored in a database. Your cart and latest self-test result are kept locally in your browser so you still see them when you return."),
         ("What do I use it for?", "To reply to your request, to deliver coaching and to handle an order. Nothing else."),
         ("For how long?", "Contact requests for a maximum of twelve months. Coaching data up to two years after the track ends, invoice data seven years due to tax obligations."),
         ("Sharing", "Only where needed for delivery: the coaching app, email and the payment provider. Never for advertising."),
         ("Your rights", "Access, correction, deletion and withdrawal of consent. One email is enough; I reply within four weeks."),
         ("Cookies", "This site uses no tracking or advertising cookies. Only local storage for your language choice, cart and self-test result.")),
        (("Wer ist verantwortlich?", "N-Force Performance, Nick Bergman, Tilburg, Niederlande. Handelsregister 99722283. Kontakt \u00fcber nick@nforce-performance.nl."),
         ("Welche Daten?", "Name, E-Mail-Adresse und was du selbst ins Kontaktformular schreibst. Beim Coaching zus\u00e4tzlich Testwerte, Verletzungshistorie und Trainingsdaten, die du lieferst."),
         ("Der Selbsttest", "Die Werte, die du im Selbsttest eingibst, bleiben in deinem Browser. Sie werden nicht an einen Server gesendet und nicht in einer Datenbank gespeichert. Warenkorb und letztes Selbsttestergebnis werden lokal im Browser behalten."),
         ("Wof\u00fcr nutze ich das?", "Um auf deine Anfrage zu antworten, Coaching durchzuf\u00fchren und eine Bestellung abzuwickeln. Nichts anderes."),
         ("Wie lange?", "Kontaktanfragen maximal zw\u00f6lf Monate. Coachingdaten bis zwei Jahre nach Ende des Prozesses, Rechnungsdaten sieben Jahre aufgrund steuerlicher Pflichten."),
         ("Weitergabe", "Nur wenn f\u00fcr die Ausf\u00fchrung n\u00f6tig: Coaching-App, E-Mail und Zahlungsdienstleister. Nie f\u00fcr Werbung."),
         ("Deine Rechte", "Auskunft, Korrektur, L\u00f6schung und Widerruf der Einwilligung. Eine E-Mail gen\u00fcgt; ich antworte innerhalb von vier Wochen."),
         ("Cookies", "Diese Seite nutzt keine Tracking- oder Werbecookies. Nur lokale Speicherung f\u00fcr Sprachwahl, Warenkorb und Selbsttestergebnis.")))

    add("tc_title", "Algemene voorwaarden | N-Force Performance",
        "Terms and conditions | N-Force Performance", "Allgemeine Gesch\u00e4ftsbedingungen | N-Force Performance")
    add("tc_desc", "Voorwaarden voor coaching, handboeken en teamopdrachten.",
        "Terms for coaching, handbooks and team assignments.",
        "Bedingungen f\u00fcr Coaching, Handb\u00fccher und Teamauftr\u00e4ge.")
    add("tc_h1", "Algemene voorwaarden", "Terms and conditions", "Allgemeine Gesch\u00e4ftsbedingungen")
    add("tc_lede",
        "Geen kleine lettertjes waar je later van schrikt. Dit zijn de afspraken.",
        "No fine print that surprises you later. These are the agreements.",
        "Kein Kleingedrucktes, das dich sp\u00e4ter \u00fcberrascht. Das sind die Vereinbarungen.")
    add("tc_blocks",
        (("Coaching", "Minimale looptijd twaalf weken, daarna maandelijks opzegbaar met een opzegtermijn van veertien dagen. Betaling per maand vooraf. Ik lever een programma, begeleiding en analyse; jij levert uitvoering en eerlijke informatie over belasting en klachten."),
         ("Handboeken", "Digitale producten worden direct geleverd. Omdat het om directe digitale levering gaat, vervalt het herroepingsrecht zodra de download beschikbaar is; dat bevestig je bij de bestelling. Persoonlijk gebruik alleen: doorverkoop of verspreiding is niet toegestaan."),
         ("Teamopdrachten", "Op basis van een schriftelijke opdrachtbevestiging. Kosteloos verzetten tot zeven dagen voor de testdag; daarna wordt vijftig procent in rekening gebracht."),
         ("Gezondheid", "Ik ben geen arts of fysiotherapeut. Bij klachten, pijn of een medische aandoening geldt medisch advies boven mijn advies. Train je met een blessure, dan werk ik alleen mee als je behandelaar dat ondersteunt."),
         ("Aansprakelijkheid", "Deelname is op eigen risico. Aansprakelijkheid is beperkt tot het bedrag van de laatste factuur, behalve bij opzet of grove nalatigheid."),
         ("Toepasselijk recht", "Nederlands recht. Klachten los ik eerst in gesprek op; komen we er niet uit, dan is de rechtbank Zeeland-West-Brabant bevoegd.")),
        (("Coaching", "Minimum term twelve weeks, then cancellable monthly with fourteen days' notice. Payment monthly in advance. I supply the programme, guidance and analysis; you supply execution and honest information about load and complaints."),
         ("Handbooks", "Digital products are delivered immediately. Because delivery is immediate and digital, the right of withdrawal lapses once the download is available; you confirm this at checkout. Personal use only: resale or distribution is not permitted."),
         ("Team assignments", "Based on a written confirmation of assignment. Free rescheduling up to seven days before the test day; after that fifty percent is charged."),
         ("Health", "I am not a doctor or physiotherapist. With complaints, pain or a medical condition, medical advice takes precedence over mine. If you train with an injury, I only cooperate when your practitioner supports it."),
         ("Liability", "Participation is at your own risk. Liability is limited to the amount of the last invoice, except in cases of intent or gross negligence."),
         ("Applicable law", "Dutch law. I resolve complaints in conversation first; if we can't agree, the Zeeland-West-Brabant court has jurisdiction.")),
        (("Coaching", "Mindestlaufzeit zw\u00f6lf Wochen, danach monatlich k\u00fcndbar mit vierzehn Tagen Frist. Zahlung monatlich im Voraus. Ich liefere Programm, Betreuung und Analyse; du lieferst Umsetzung und ehrliche Angaben zu Belastung und Beschwerden."),
         ("Handb\u00fccher", "Digitale Produkte werden sofort geliefert. Wegen der sofortigen digitalen Lieferung erlischt das Widerrufsrecht, sobald der Download verf\u00fcgbar ist; das best\u00e4tigst du bei der Bestellung. Nur pers\u00f6nliche Nutzung: Weiterverkauf oder Verbreitung ist nicht erlaubt."),
         ("Teamauftr\u00e4ge", "Auf Basis einer schriftlichen Auftragsbest\u00e4tigung. Kostenlose Verlegung bis sieben Tage vor dem Testtag; danach werden f\u00fcnfzig Prozent berechnet."),
         ("Gesundheit", "Ich bin kein Arzt und kein Physiotherapeut. Bei Beschwerden, Schmerzen oder einer Erkrankung geht medizinischer Rat vor meinem Rat. Trainierst du mit einer Verletzung, arbeite ich nur mit, wenn dein Behandler das unterst\u00fctzt."),
         ("Haftung", "Teilnahme auf eigenes Risiko. Die Haftung ist auf den Betrag der letzten Rechnung begrenzt, au\u00dfer bei Vorsatz oder grober Fahrl\u00e4ssigkeit."),
         ("Anwendbares Recht", "Niederl\u00e4ndisches Recht. Beschwerden l\u00f6se ich zuerst im Gespr\u00e4ch; kommen wir nicht weiter, ist das Gericht Zeeland-West-Brabant zust\u00e4ndig.")))

    # -----------------------------------------------------------------------
    # 404
    # -----------------------------------------------------------------------
    add("nf_title", "Deze pagina bestaat niet", "This page doesn't exist", "Diese Seite existiert nicht")
    add("nf_lede",
        "De link is oud of er staat een typefout in. Hieronder de pagina's waar de meeste mensen naartoe gaan.",
        "The link is old or contains a typo. Below are the pages most people are looking for.",
        "Der Link ist alt oder enth\u00e4lt einen Tippfehler. Unten die Seiten, die die meisten suchen.")
