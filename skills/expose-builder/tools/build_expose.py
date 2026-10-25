#!/usr/bin/env python3
"""Assembler v2: entwurf.json  ->  04_layout/expose.html (v2-Editorial-Template).

Liest die freigegebene entwurf.json (Single Source of Truth), rendert jede Seite
ins v2-Layout (Libre Caslon + Spectral + Oxblood, Haarlinien-Bänder, freie Zahlen),
löst Bilder auf (EXIF-Korrektur + Veredelung) und Charts (chart_svg), kopiert
expose.css + Assets. Format der entwurf.json: references/entwurf-format.md.

    python build_expose.py --object-dir "<objekt>" [--only 1-2]
"""
from __future__ import annotations

import argparse
import json
import shutil
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from chart_svg import anchor_bars, line_chart  # noqa: E402

try:
    from PIL import Image, ImageOps
    from enhance_photo import enhance
    _PIL = True
except ImportError:
    _PIL = False

IMG_EXT = {".jpg", ".jpeg", ".png", ".webp", ".gif"}


def esc(s) -> str:
    return str(s).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


# ---------- Bilder ----------
class Images:
    def __init__(self, object_dir: Path, layout_dir: Path, veredeln: bool = True):
        self.imgdir = layout_dir / "assets" / "img"
        self.veredeln = veredeln
        self.index: dict[str, Path] = {}
        for p in object_dir.rglob("*"):
            if p.is_file() and p.suffix.lower() in IMG_EXT and "04_layout" not in p.parts:
                self.index.setdefault(p.name.lower(), p)

    def ref(self, name: str | None):
        if not name:
            return None
        src = self.index.get(str(name).strip().lower())
        if not src:
            return None
        self.imgdir.mkdir(parents=True, exist_ok=True)
        dst = self.imgdir / (Path(src).stem + ".jpg")
        if not dst.exists():
            if _PIL:
                im = ImageOps.exif_transpose(Image.open(src)).convert("RGB")
                if self.veredeln:
                    im = enhance(im)
                im.thumbnail((2000, 2000))
                im.save(dst, quality=90)
            else:
                shutil.copy2(src, dst)
        return f"assets/img/{dst.name}"


def img_or_box(R: "Images", name, label, h="80mm"):
    ref = R.ref(name)
    if ref:
        return f'<img src="{esc(ref)}" style="width:100%;height:{h};object-fit:cover" alt="">'
    return f'<div class="ph-box" style="height:{h}">{esc(label or "BILD")}</div>'


# ---------- Kopf / Fuß ----------
def head(obj, eyebrow, nr, total):
    sec = (eyebrow or "").upper()
    return (f'<div class="head"><div class="head__left"><span class="mono-mark">'
            f'{esc(obj.get("marke","P")[0])}</span><span class="head__name"><b>'
            f'{esc(obj.get("marke","PETROV WOHNEN"))}</b> &nbsp;·&nbsp; {esc(obj.get("claim","Kapitalanlage"))}'
            f'</span></div><div>{esc(sec)} · S. {nr:02d}</div></div>')


def foot(obj, nr, total):
    return (f'<div class="foot"><span>{esc(obj.get("name",""))}</span>'
            f'<span>{nr:02d} / {total}</span></div>')


def head_block(f):
    h = ""
    if f.get("eyebrow"):
        h += f'<p class="ey">{esc(f["eyebrow"])}</p>'
    if f.get("headline"):
        h += f'<h1>{esc(f["headline"])}</h1>'
    if f.get("subline"):
        h += f'<p class="subline">{esc(f["subline"])}</p>'
    return h


def chart_html(c):
    pairs = []
    for pair in str(c.get("daten", "")).split(";"):
        if "=" in pair:
            k, v = pair.split("=", 1)
            try:
                pairs.append((k.strip(), float(v.replace(".", "").replace(",", "."))))
            except ValueError:
                pass
    if not pairs:  # Draft mit [OFFEN]-Daten -> Platzhalter statt Crash
        src = f'<p class="chart-source">{esc(c.get("quelle",""))}</p>' if c.get("quelle") else ""
        return f'<div class="ph-box" style="height:78mm">CHART · [OFFEN]</div>{src}'
    if c.get("typ") == "marktvergleich":
        svg = anchor_bars(pairs, highlight=c.get("highlight", "Unser Preis"), source=c.get("quelle", ""))
    else:
        svg = line_chart(pairs, source="")
    src = f'<p class="chart-source">{esc(c.get("quelle",""))}</p>' if c.get("quelle") else ""
    return f'<div class="chart">{svg}</div>{src}'


def mean_block(f):
    if not f.get("insight"):
        return ""
    body = f'<p class="mean__body">{esc(f.get("insight_body",""))}</p>' if f.get("insight_body") else "<div></div>"
    return (f'<div class="mean"><p class="ey">Was das bedeutet</p>'
            f'<p class="quote">{esc(f["insight"])}</p>{body}</div>')


# ---------- Modul-Renderer ----------
def render_cover(s, obj, nr, total, R):
    f = s["felder"]
    hero = img_or_box(R, f.get("hero"), "HERO / AUSSENANSICHT", h="100%")
    return (f'<section class="page page--cover"><div class="cover__hero">{hero}</div>'
            f'<div class="cover__panel"><div class="cover__mark">{esc(obj.get("marke","P")[0])}</div>'
            f'<h1 class="cover__title">{esc(f.get("titel",""))}</h1>'
            f'<p class="cover__addr">{esc(f.get("adresse",""))}</p>'
            f'<p class="cover__tag">{esc(f.get("tagline",""))}</p></div></section>')


def render_facts(s, obj, nr, total, R):
    f = s["felder"]
    stats = ""
    for st in f.get("stats", []):
        unit = f' <small>{esc(st.get("unit",""))}</small>' if st.get("unit") else ""
        stats += (f'<div><div class="stat__num">{esc(st.get("num",""))}{unit}</div>'
                  f'<div class="stat__label">{esc(st.get("label",""))}</div>'
                  f'<div class="stat__sub">{esc(st.get("sub",""))}</div></div>')
    cols = ""
    for c in f.get("concept", []):
        cols += (f'<div class="col"><p class="ey">{esc(c.get("label",""))}</p>'
                 f'<h2>{esc(c.get("head",""))}</h2><p>{esc(c.get("body",""))}</p></div>')
    body = f'<p class="body" style="margin-top:1mm">{esc(f["body"])}</p>' if f.get("body") else ""
    parts = [head(obj, f.get("eyebrow"), nr, total), '<div class="thesis">', head_block(f), body, '</div>']
    if stats:
        parts += ['<div class="rule"></div>', '<p class="ey">Die Eckdaten</p>',
                  f'<div class="stats" style="margin-top:5mm">{stats}</div>']
    if cols:
        parts += ['<div class="rule"></div>', f'<div class="cols">{cols}</div>']
    if f.get("insight"):
        parts += ['<div class="rule"></div>', mean_block(f)]
    parts.append(foot(obj, nr, total))
    return f'<section class="page">{"".join(parts)}</section>'


def render_data(s, obj, nr, total, R):
    f = s["felder"]
    if f.get("chart"):
        left = chart_html(f["chart"])
    elif f.get("bild"):
        left = img_or_box(R, f["bild"], f.get("bild_label", "KARTE"))
        if f.get("bild_quelle"):
            left += f'<p class="chart-source">{esc(f["bild_quelle"])}</p>'
    else:
        left = ""
    right = ""
    if f.get("fakten"):
        for row in f["fakten"]:
            right += (f'<div class="datalist__row"><div class="datalist__label">{esc(row.get("label",""))}</div>'
                      f'<div class="datalist__val">{esc(row.get("wert",""))}</div></div>')
    elif f.get("markttabelle"):
        rows = ""
        for row in f["markttabelle"]:
            cls = ' class="is-ours"' if row.get("highlight") else ""
            rows += f'<tr{cls}><td>{esc(row.get("label",""))}</td><td>{esc(row.get("wert",""))}</td></tr>'
        right = f'<table class="markt-table">{rows}</table>'
        if f.get("quelle"):
            right += f'<p class="source">{esc(f["quelle"])}</p>'
    elif f.get("body"):
        right = f'<p class="body">{esc(f["body"])}</p>'
    return (f'<section class="page">{head(obj, f.get("eyebrow"), nr, total)}{head_block(f)}'
            f'<div class="data__cols"><div>{left}</div><div>{right}</div></div>'
            f'{mean_block(f)}{foot(obj, nr, total)}</section>')


def render_photo(s, obj, nr, total, R):
    f = s["felder"]
    bilder = f.get("bilder", [])
    slot = f.get("slot", "single")
    if slot == "hero" and bilder:
        b = bilder[0]
        cap = f'<figcaption>{esc(b.get("caption",""))}</figcaption>' if b.get("caption") else ""
        return f'<section class="page page--photo"><figure class="slotfig slot--hero">{img_or_box(R,b.get("datei"),"FOTO",h="100%")}{cap}</figure></section>'
    if slot == "duo":
        cells = ""
        for b in bilder[:2]:
            tag = f'<span class="tag-ba">{esc(b.get("tag",""))}</span>' if b.get("tag") else ""
            cells += f'<figure>{img_or_box(R,b.get("datei"),"FOTO",h="148.5mm")}{tag}</figure>'
        return f'<section class="page page--photo"><div class="slot--duo">{cells}</div></section>'
    if slot == "grid":
        cells = "".join(img_or_box(R, b.get("datei"), "FOTO", h="118mm") for b in bilder)
        return f'<section class="page page--photo"><div class="slot--grid">{cells}</div></section>'
    b = bilder[0] if bilder else {}
    cap = f'<figcaption>{esc(b.get("caption",""))}</figcaption>' if b.get("caption") else ""
    return (f'<section class="page page--photo"><figure class="slotfig slot--single" style="padding:0">'
            f'{img_or_box(R,b.get("datei"),"FOTO",h="235mm")}{cap}</figure></section>')


def render_plan(s, obj, nr, total, R):
    f = s["felder"]
    ref = R.ref(f.get("bild"))
    plan = (f'<img src="{esc(ref)}" class="plan-img" alt="Grundriss">' if ref
            else '<div class="plan-img ph-box" style="height:210mm">GRUNDRISS</div>')
    cap = f'<p class="chart-source">{esc(f.get("caption",""))}</p>' if f.get("caption") else ""
    return (f'<section class="page">{head(obj, f.get("eyebrow"), nr, total)}{head_block(f)}'
            f'{plan}{cap}{foot(obj, nr, total)}</section>')


def render_close(s, obj, nr, total, R):
    f = s["felder"]
    person = ""
    if f.get("person"):
        person = (f'<div class="close__person">{esc(f["person"])}<br>'
                  f'<span class="close__role">{esc(f.get("rolle",""))}</span></div>')
    return (f'<section class="page page--close"><p class="ey">{esc(f.get("eyebrow","Haltung"))}</p>'
            f'<p class="close__quote">{esc(f.get("quote",""))}</p>{person}'
            f'<div class="close__mark">{esc(obj.get("marke","P")[0])}</div>'
            f'{foot(obj, nr, total)}</section>')


RENDER = {"cover": render_cover, "facts": render_facts, "data": render_data,
          "photo": render_photo, "plan": render_plan, "close": render_close}


def in_range(nr, only):
    if not only:
        return True
    for part in str(only).split(","):
        if "-" in part:
            a, b = part.split("-", 1)
            if int(a) <= nr <= int(b):
                return True
        elif part.strip().isdigit() and int(part) == nr:
            return True
    return False


def main():
    ap = argparse.ArgumentParser(description="entwurf.json -> v2 expose.html")
    ap.add_argument("--object-dir", required=True)
    ap.add_argument("--entwurf", help="Default: <object>/expose/entwurf.json")
    ap.add_argument("--out", help="Default: <object>/expose/04_layout/expose.html")
    ap.add_argument("--only", help='nur diese Seiten, z.B. "1-2"')
    ap.add_argument("--template-dir", default=str(Path(__file__).resolve().parent.parent / "template"))
    args = ap.parse_args()

    object_dir = Path(args.object_dir).resolve()
    entwurf = Path(args.entwurf) if args.entwurf else object_dir / "expose" / "entwurf.json"
    out = Path(args.out) if args.out else object_dir / "expose" / "04_layout" / "expose.html"
    template_dir = Path(args.template_dir)
    layout = out.parent
    layout.mkdir(parents=True, exist_ok=True)

    data = json.loads(entwurf.read_text(encoding="utf-8"))
    obj = data.get("objekt", {})
    seiten = data.get("seiten", [])
    total = len(seiten)

    shutil.copy2(template_dir / "expose.css", layout / "expose.css")
    R = Images(object_dir, layout)

    sections = []
    for s in seiten:
        nr = s.get("nr", 0)
        if not in_range(nr, args.only):
            continue
        fn = RENDER.get(s.get("modul"))
        if not fn:
            sys.stderr.write(f"WARN Seite {nr}: unbekanntes modul '{s.get('modul')}'\n")
            continue
        sections.append(fn(s, obj, nr, total, R))

    html = ('<!DOCTYPE html><html lang="de"><head><meta charset="utf-8"><title>Exposé</title>'
            '<link rel="stylesheet" href="expose.css"></head><body>' + "".join(sections) + "</body></html>")
    out.write_text(html, encoding="utf-8")
    print(out)


if __name__ == "__main__":
    main()
