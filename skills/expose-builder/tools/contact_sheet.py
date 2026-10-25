#!/usr/bin/env python3
"""Kontaktbogen-Montage fuer die Foto-Sichtung (Phase 0).

Erzeugt EIN beschriftetes PNG aus vielen Fotos -> token-sparsame Sichtung
(Hauptagent liest 1 Montage statt N Einzelbilder). Label = Kurzname je Foto.

Beispiel:
    python contact_sheet.py --dir "<objekt>/Bilder" --pattern "20250221_*.jpg" \
        --out "<objekt>/expose/_sichtung.png"
"""
from __future__ import annotations

import argparse
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


def load_font(size: int):
    for f in (r"C:\Windows\Fonts\arialbd.ttf", r"C:\Windows\Fonts\arial.ttf"):
        try:
            return ImageFont.truetype(f, size)
        except OSError:
            continue
    return ImageFont.load_default()


def make_sheet(paths: list[Path], out: Path, cols: int = 6, thumb: int = 300,
               label_h: int = 26, pad: int = 10, bg=(243, 239, 231)) -> tuple[Path, int]:
    n = len(paths)
    rows = (n + cols - 1) // cols
    cw, ch = thumb + pad * 2, thumb + label_h + pad * 2
    sheet = Image.new("RGB", (cols * cw, rows * ch), bg)
    draw = ImageDraw.Draw(sheet)
    font = load_font(16)
    for i, p in enumerate(paths):
        r, c = divmod(i, cols)
        x, y = c * cw, r * ch
        try:
            im = Image.open(p)
            im.draft("RGB", (thumb, thumb))
            im = im.convert("RGB")
            im.thumbnail((thumb, thumb))
        except OSError:
            draw.text((x + pad, y + pad), f"ERR {p.name}", fill=(180, 0, 0), font=font)
            continue
        ox = x + pad + (thumb - im.width) // 2
        oy = y + pad + (thumb - im.height) // 2
        sheet.paste(im, (ox, oy))
        label = p.stem.split("_")[-1] or p.stem
        draw.text((x + pad, y + pad + thumb + 4), label, fill=(43, 43, 43), font=font)
    out.parent.mkdir(parents=True, exist_ok=True)
    sheet.save(out, quality=85)
    return out, n


def main() -> None:
    ap = argparse.ArgumentParser(description="Kontaktbogen-Montage")
    ap.add_argument("--dir", required=True, help="Bilder-Ordner")
    ap.add_argument("--pattern", default="*.jpg", help="Glob (Default *.jpg)")
    ap.add_argument("--out", required=True, help="Ziel-PNG")
    ap.add_argument("--cols", type=int, default=6)
    ap.add_argument("--thumb", type=int, default=300)
    args = ap.parse_args()

    paths = sorted(Path(args.dir).glob(args.pattern))
    if not paths:
        raise SystemExit(f"Keine Bilder: {args.dir}\\{args.pattern}")
    out, n = make_sheet(paths, Path(args.out), cols=args.cols, thumb=args.thumb)
    print(f"{out}  ({n} Fotos)")


if __name__ == "__main__":
    main()
