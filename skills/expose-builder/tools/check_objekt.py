"""Acceptance check driven by objekt.json - one PASS/FAIL table per unit PDF (TB1/TB2).

Generic successor of the Herten check_v1.py. Verifies slide titles/order, page count,
single font family (TB7), company address only on the closing page (F1), contact footer
everywhere, cover + room photo resolution and brightness against the prepared images,
GEG lines on the Technik slide, forbidden strings, optional icon census, and - with
--ref-dir - identical slide titles against a reference set of PDFs.

    python check_objekt.py <objekt.json> [--pdf-dir <dir>] [--img-dir <dir>] [--ref-dir <dir>]
"""
import argparse
import io
import sys
from pathlib import Path

import fitz
from PIL import Image

from objekt_config import Objekt


def titles(page):
    best = []
    for b in page.get_text('dict')['blocks']:
        for line in b.get('lines', []):
            spans = [s for s in line['spans'] if s['size'] >= 18 and s['text'].strip()]
            if spans:
                best.append((''.join(s['text'] for s in spans).strip(), line['bbox'][1]))
    best.sort(key=lambda t: t[1])
    return best[0][0] if best else ''


def accent_icons(page, accent):
    rects = [d['rect'] for d in page.get_drawings()
             if d.get('color') and len(d['color']) == 3
             and all(abs(a - b) <= 0.06 for a, b in zip(d['color'], accent))
             and d['rect'].width <= 45 and d['rect'].height <= 45
             and not (min(d['rect'].width, d['rect'].height) < 1.2 and max(d['rect'].width, d['rect'].height) > 20)]
    parent = list(range(len(rects)))

    def find(i):
        while parent[i] != i:
            parent[i] = parent[parent[i]]
            i = parent[i]
        return i

    grown = [fitz.Rect(r.x0 - 1, r.y0 - 1, r.x1 + 1, r.y1 + 1) for r in rects]
    for i in range(len(rects)):
        for j in range(i + 1, len(rects)):
            if grown[i].intersects(grown[j]):
                parent[find(i)] = find(j)
    out = {}
    for i, r in enumerate(rects):
        k = find(i)
        out.setdefault(k, fitz.Rect(r)).include_rect(r)
    return sum(1 for c in out.values() if 6 <= max(c.width, c.height) <= 45)


def biggest_image(page, doc):
    best = None
    for img in page.get_images(full=True):
        xref, w, h = img[0], img[2], img[3]
        if best is None or w * h > best[1] * best[2]:
            best = (xref, w, h)
    pix = Image.open(io.BytesIO(doc.extract_image(best[0])['image']))
    return best[1], best[2], pix


def brightness(im):
    return sum(im.convert('L').resize((64, 64)).getdata()) / 4096


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('config')
    ap.add_argument('--pdf-dir', help='dir with the rendered PDFs (default: <objekt>/expose)')
    ap.add_argument('--img-dir', help='dir with the prepared images (default: <pdf-dir>/img)')
    ap.add_argument('--ref-dir', help='reference PDFs: slide titles must match 1:1')
    a = ap.parse_args()

    obj = Objekt(a.config)
    soll = obj.soll
    pdf_dir = Path(a.pdf_dir) if a.pdf_dir else obj.expose_dir
    img_dir = Path(a.img_dir) if a.img_dir else pdf_dir / 'img'
    max_px = obj.fotos.get('max_px', 3500)
    font = obj.font
    accent = tuple(int(soll.get('accent', '#7C1D2A').lstrip('#')[i:i + 2], 16) / 255
                   for i in (0, 2, 4))
    company = [m.lower() for m in soll['firmen_marker']]
    kontakt_marker = soll['kontakt_marker'].lower()

    fail = 0
    for unit, u in obj.units.items():
        doc = fitz.open(pdf_dir / u['pdf'])
        want_titles = obj.soll_titles(unit)
        got_titles = [titles(p) for p in doc]
        rows = []

        def check(name, ok, detail=''):
            rows.append((name, bool(ok), detail))

        check('Seitenzahl', len(doc) == obj.soll_pages(unit), f'{len(doc)} (soll {obj.soll_pages(unit)})')
        tmatch = (len(got_titles) == len(want_titles)
                  and all(g == w or g.startswith(w) for g, w in zip(got_titles, want_titles)))
        check('Folientitel-Reihenfolge', tmatch,
              '; '.join(f'S{i + 1}:{g!r} (soll {w!r})' for i, (g, w) in
                        enumerate(zip(got_titles, want_titles)) if not (g == w or g.startswith(w))) or 'ok')
        fonts = {f[3].split('+')[-1] for p in doc for f in p.get_fonts(full=True)}
        check(f'Nur {font}', all(f.startswith(font) for f in fonts), ', '.join(sorted(fonts)))
        comp_pages = [i + 1 for i, p in enumerate(doc)
                      if any(k in p.get_text('text').lower() for k in company)]
        check('Firmenadresse nur letzte Seite', comp_pages == [len(doc)], str(comp_pages))
        foot_pages = [i + 1 for i, p in enumerate(doc)
                      if kontakt_marker in p.get_text('text').lower()]
        check('Kontakt-Fusszeile ueberall', foot_pages == list(range(1, len(doc) + 1)),
              f'{len(foot_pages)} Seiten')
        bad = [t for t in soll.get('verboten_text', [])
               if any(t in p.get_text('text') for p in doc)]
        check('Verbotene Texte fehlen', not bad, ', '.join(bad) or 'ok')
        bad_t = [t for t in soll.get('verbotene_titel', []) if t in got_titles]
        check('Verbotene Folientitel fehlen', not bad_t, ', '.join(bad_t) or 'ok')

        if soll.get('icons'):
            icons = {i + 1: accent_icons(p, accent) for i, p in enumerate(doc)}
            icons = {k: v for k, v in icons.items() if v}
            ok = (sum(icons.values()) == soll['icons']['count']
                  and set(icons) == set(soll['icons']['pages']))
            check(f'Icons unveraendert ({soll["icons"]["count"]})', ok, str(icons))

        w, h, pix = biggest_image(doc[0], doc)
        ref = Image.open(img_dir / unit / 'titel.jpg')
        check(f'Titelbild {max_px} px', max(w, h) == max_px, f'{w}x{h}')
        check('Titelbild = Rezept-Datei', abs(brightness(pix) - brightness(ref)) < 0.6,
              f'pdf {brightness(pix):.1f} vs datei {brightness(ref):.1f}')
        rooms = u.get('rooms', [])
        if rooms:
            rp = got_titles.index(rooms[0][0])
            w2, h2, pix2 = biggest_image(doc[rp], doc)
            ref2 = Image.open(img_dir / obj.photo_rel(unit, rooms[0][1][0]).removeprefix('img/'))
            check(f'Raumfoto {max_px} px, Helligkeit = Original',
                  max(w2, h2) == max_px and abs(brightness(pix2) - brightness(ref2)) < 0.6,
                  f'{w2}x{h2}, pdf {brightness(pix2):.1f} vs datei {brightness(ref2):.1f}')
        if obj.folien['base_slides'].get('technik'):
            tech = doc[got_titles.index(next(t for t in got_titles
                                             if t.startswith(obj.folien['base_slides']['technik'].split(' &')[0])))]
            low = tech.get_text('text').lower()
            check('Energieausweis-Angaben (GEG)', 'energie' in low and 'ausgestellt am' in low)

        if a.ref_dir:
            ref_doc = fitz.open(Path(a.ref_dir) / u['pdf'])
            ref_titles = [titles(p) for p in ref_doc]
            check('Folientitel = Referenz-PDF', got_titles == ref_titles,
                  '; '.join(f'S{i + 1}:{g!r} (ref {r!r})' for i, (g, r) in
                            enumerate(zip(got_titles, ref_titles)) if g != r)
                  or f'{len(got_titles)} vs {len(ref_titles)} Seiten' if got_titles != ref_titles else 'ok')

        print(f'== {unit}')
        for name, ok, detail in rows:
            print(f'  {"PASS" if ok else "FAIL"}  {name:44s} {detail}')
            if not ok:
                fail += 1
    print('RESULT', 'GREEN' if fail == 0 else f'RED ({fail} failures)')
    sys.exit(0 if fail == 0 else 1)


if __name__ == '__main__':
    main()
