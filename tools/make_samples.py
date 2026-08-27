# -*- coding: utf-8 -*-
"""
Maakt inkijkexemplaren van de twaalf handboeken.

Wat het doet
------------
Neemt per handboek de volledige PDF, knipt daar een aantal pagina's uit, zet er
een eigen omslag voor en een afsluitpagina achter, stempelt op elke geleende
pagina een voettekst, en schrijft het resultaat naar assets/samples/.

Gebruik
-------
1. Zet de twaalf volledige PDF's in _bron/handboeken/ met de handboek-id als
   bestandsnaam, bijvoorbeeld:

       _bron/handboeken/power-foundations-core.pdf
       _bron/handboeken/power-foundations-pro.pdf
       ...

   De map _bron/ staat in .gitignore: de volledige boeken komen dus nooit in de
   repo en dus ook niet op de live site terecht.

2. Installeer de enige afhankelijkheid:

       pip3 install pymupdf

3. Draai:

       python3 tools/make_samples.py

   Daarna:

       python3 tools/make_handbooks.py
       python3 tools/build.py

   make_handbooks.py zet het veld "sample" automatisch op het juiste pad voor
   elk handboek waarvoor een inkijkexemplaar bestaat.

Losse opties
------------
    python3 tools/make_samples.py --only power-foundations-core
    python3 tools/make_samples.py --pages 10
    python3 tools/make_samples.py --list      (alleen tonen wat het zou doen)
"""
import argparse
import os
import sys

try:
    import fitz  # pymupdf
except ImportError:
    sys.exit("pymupdf ontbreekt. Installeer met:  pip3 install pymupdf")

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC_DIR = os.path.join(ROOT, "_bron", "handboeken")
OUT_DIR = os.path.join(ROOT, "assets", "samples")
LOGO = os.path.join(ROOT, "assets", "img", "nf-monogram-wit.png")

SITE = "nforce-performance.nl"

# Merkkleuren, gelijk aan de site
INK = (0.043, 0.071, 0.125)      # #0b1220 donkerblauw
PAPER = (1, 1, 1)
ACCENT = (0.494, 0.784, 1.0)     # #7ec8ff
MUTED = (0.62, 0.67, 0.75)

# Hoeveel pagina's een inkijkexemplaar bevat, exclusief omslag en afsluitpagina
DEFAULT_PAGES = 8


def load_books():
    """Leest de boekgegevens uit make_handbooks.py zonder dat bestand te kopiëren."""
    sys.path.insert(0, os.path.join(ROOT, "tools"))
    import make_handbooks as mh
    out = []
    for b in mh.BOOKS:
        out.append({
            "id": b["id"],
            "nr": b["nr"],
            "title": b["title"]["nl"],
            "tagline": b["tagline"]["nl"],
            "pages": b["pages"],
            "version": b["version"],
            "price": mh.PRICE_CORE if b["version"] == "core" else mh.PRICE_PRO,
            "learn": b["learn"]["nl"],
        })
    return out


def pick_pages(total, want):
    """
    Kiest welke pagina's mee mogen (0-based).

    Eerst de opening, want daar staat waar het boek over gaat. Daarna een blok
    uit het midden, want daar staat het echte werk. Iemand die alleen een
    inhoudsopgave ziet, koopt niets.
    """
    if total <= want:
        return list(range(total))
    front = min(4, want)
    middle = want - front
    start = int(total * 0.42)
    start = max(front, min(start, total - middle))
    return list(range(front)) + list(range(start, start + middle))


def wrap(text, font, size, width):
    """Breekt tekst af op woordgrenzen binnen een gegeven breedte."""
    words = text.split()
    lines, line = [], ""
    for w in words:
        probe = (line + " " + w).strip()
        if fitz.get_text_length(probe, fontname=font, fontsize=size) <= width:
            line = probe
        else:
            if line:
                lines.append(line)
            line = w
    if line:
        lines.append(line)
    return lines


def draw_logo(page, x, y, height):
    if not os.path.exists(LOGO):
        return
    img = fitz.open(LOGO)
    w, h = img[0].rect.width, img[0].rect.height
    img.close()
    width = height * (w / h)
    page.insert_image(fitz.Rect(x, y, x + width, y + height), filename=LOGO)


def cover_page(doc, book, shown, rect):
    page = doc.new_page(width=rect.width, height=rect.height)
    W, H = rect.width, rect.height
    m = 56

    page.draw_rect(fitz.Rect(0, 0, W, H), color=None, fill=INK)
    page.draw_rect(fitz.Rect(0, 0, W, 6), color=None, fill=ACCENT)

    draw_logo(page, m, m, 34)

    page.insert_text((W - m - fitz.get_text_length("INKIJKEXEMPLAAR", "hebo", 10),
                      m + 24), "INKIJKEXEMPLAAR",
                     fontname="hebo", fontsize=10, color=ACCENT)

    y = H * 0.34
    page.insert_text((m, y), book["nr"], fontname="hebo", fontsize=13, color=ACCENT)
    y += 42

    for line in wrap(book["title"], "hebo", 34, W - 2 * m):
        page.insert_text((m, y), line, fontname="hebo", fontsize=34, color=PAPER)
        y += 42

    y += 10
    for line in wrap(book["tagline"], "helv", 13, W - 2 * m - 40):
        page.insert_text((m, y), line, fontname="helv", fontsize=13, color=MUTED)
        y += 20

    y = H - m - 96
    page.draw_line(fitz.Point(m, y), fitz.Point(W - m, y), color=(0.16, 0.20, 0.28), width=0.8)
    y += 24

    left = "%d van %d pagina's" % (shown, book["pages"])
    page.insert_text((m, y), left, fontname="hebo", fontsize=11, color=PAPER)
    page.insert_text((m, y + 18), "Volledige uitgave EUR %d, incl. btw" % book["price"],
                     fontname="helv", fontsize=10, color=MUTED)

    right = SITE
    page.insert_text((W - m - fitz.get_text_length(right, "hebo", 11), y),
                     right, fontname="hebo", fontsize=11, color=ACCENT)
    page.insert_text((W - m - fitz.get_text_length("N-Force Performance", "helv", 10), y + 18),
                     "N-Force Performance", fontname="helv", fontsize=10, color=MUTED)
    return page


def stamp(page, shown_index, shown_total):
    """Zet een voettekst op een geleende pagina, zonder de inhoud te overschrijven."""
    r = page.rect
    bar_h = 24
    bar = fitz.Rect(0, r.height - bar_h, r.width, r.height)
    page.draw_rect(bar, color=None, fill=INK, fill_opacity=0.92)

    left = "Inkijkexemplaar  ·  %s" % SITE
    page.insert_text((28, r.height - 9), left, fontname="helv", fontsize=8, color=(1, 1, 1))

    right = "%d / %d" % (shown_index, shown_total)
    page.insert_text((r.width - 28 - fitz.get_text_length(right, "helv", 8), r.height - 9),
                     right, fontname="helv", fontsize=8, color=ACCENT)


def closing_page(doc, book, shown, rect):
    page = doc.new_page(width=rect.width, height=rect.height)
    W, H = rect.width, rect.height
    m = 56

    page.draw_rect(fitz.Rect(0, 0, W, H), color=None, fill=INK)
    draw_logo(page, m, m, 28)

    y = m + 110
    page.insert_text((m, y), "Dit waren %d van de %d pagina's." % (shown, book["pages"]),
                     fontname="hebo", fontsize=24, color=PAPER)
    y += 44

    for line in wrap("In de volledige uitgave staat het complete programma, de "
                     "oefenbibliotheek, de testprotocollen en het logboek.",
                     "helv", 12, W - 2 * m - 60):
        page.insert_text((m, y), line, fontname="helv", fontsize=12, color=MUTED)
        y += 19

    y += 26
    page.insert_text((m, y), "WAT JE ERUIT HAALT", fontname="hebo", fontsize=9, color=ACCENT)
    y += 24
    for point in book["learn"][:4]:
        page.draw_rect(fitz.Rect(m, y - 7, m + 4, y - 1), color=None, fill=ACCENT)
        for i, line in enumerate(wrap(point, "helv", 11, W - 2 * m - 40)):
            page.insert_text((m + 18, y), line, fontname="helv", fontsize=11, color=PAPER)
            y += 17
        y += 8

    y = H - m - 92
    page.draw_line(fitz.Point(m, y), fitz.Point(W - m, y), color=(0.16, 0.20, 0.28), width=0.8)
    y += 26
    page.insert_text((m, y), "EUR %d, incl. btw" % book["price"],
                     fontname="hebo", fontsize=15, color=PAPER)
    page.insert_text((m, y + 22), "%s  ·  direct downloaden na betaling" % SITE,
                     fontname="helv", fontsize=10, color=ACCENT)
    return page


def build_one(book, want_pages, dry=False):
    src = os.path.join(SRC_DIR, book["id"] + ".pdf")
    if not os.path.exists(src):
        return None, "geen bronbestand"

    doc_src = fitz.open(src)
    total = doc_src.page_count
    picks = pick_pages(total, want_pages)
    shown = len(picks)

    if dry:
        doc_src.close()
        return None, "zou %d van %d pagina's nemen: %s" % (
            shown, total, ", ".join(str(p + 1) for p in picks))

    rect = doc_src[0].rect
    out = fitz.open()
    cover_page(out, book, shown, rect)

    for i, p in enumerate(picks, start=1):
        out.insert_pdf(doc_src, from_page=p, to_page=p)
        stamp(out[out.page_count - 1], i, shown)

    closing_page(out, book, shown, rect)

    os.makedirs(OUT_DIR, exist_ok=True)
    dest = os.path.join(OUT_DIR, book["id"] + "-inkijk.pdf")
    out.set_metadata({
        "title": "%s — inkijkexemplaar" % book["title"],
        "author": "N-Force Performance",
        "subject": "Inkijkexemplaar, %d van %d pagina's" % (shown, total),
        "keywords": "N-Force Performance, inkijkexemplaar, %s" % book["id"],
    })
    out.save(dest, deflate=True, garbage=4)
    out.close()
    doc_src.close()

    kb = os.path.getsize(dest) / 1024.0
    return dest, "%d pagina's, %.0f kB" % (shown + 2, kb)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--pages", type=int, default=DEFAULT_PAGES,
                    help="aantal geleende pagina's, exclusief omslag en slot")
    ap.add_argument("--only", action="append", default=[],
                    help="alleen dit handboek-id (mag meerdere keren)")
    ap.add_argument("--list", action="store_true",
                    help="niets schrijven, alleen tonen wat er zou gebeuren")
    args = ap.parse_args()

    if not os.path.isdir(SRC_DIR):
        print("Map ontbreekt: %s" % SRC_DIR)
        print("Maak hem aan en zet er de volledige PDF's in, met de handboek-id als naam.")
        os.makedirs(SRC_DIR, exist_ok=True)

    books = load_books()
    if args.only:
        books = [b for b in books if b["id"] in args.only]
        if not books:
            sys.exit("Geen handboek gevonden met die id.")

    gemaakt, ontbreekt = 0, []
    for b in books:
        dest, note = build_one(b, args.pages, dry=args.list)
        if dest:
            gemaakt += 1
            print("  ok    %-28s %s" % (b["id"], note))
        elif note == "geen bronbestand":
            ontbreekt.append(b["id"])
            print("  mist  %-28s %s.pdf niet in _bron/handboeken/" % (b["id"], b["id"]))
        else:
            print("  ---   %-28s %s" % (b["id"], note))

    print()
    if args.list:
        print("Niets geschreven (--list).")
        return
    print("%d inkijkexemplaar(en) geschreven naar assets/samples/" % gemaakt)
    if ontbreekt:
        print("Nog geen bronbestand voor: %s" % ", ".join(ontbreekt))
    if gemaakt:
        print("Draai nu: python3 tools/make_handbooks.py && python3 tools/build.py")


if __name__ == "__main__":
    main()
