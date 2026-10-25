#!/usr/bin/env python3
"""Foto-Veredelung fuer Exposé-Slots — dezenter, hochwertiger Editorial-Look.

Ziel: HD/scharf, sauberer Tonwert, etwas Klarheit + Saettigung — aber SERIOES,
kein knalliger Filter. EXIF-Orientierung wird mitkorrigiert.

    python enhance_photo.py "<src>" "<dst>" [--compare vorher_nachher.png]
    Tuning: --brightness 1.04 --contrast 1.06 --color 1.08 --clarity 20 --sharpen 120
"""
from __future__ import annotations

import argparse
from pathlib import Path

from PIL import Image, ImageDraw, ImageEnhance, ImageFilter, ImageFont, ImageOps


def load_font(size: int):
    for f in (r"C:\Windows\Fonts\arialbd.ttf", r"C:\Windows\Fonts\arial.ttf"):
        try:
            return ImageFont.truetype(f, size)
        except OSError:
            continue
    return ImageFont.load_default()


def orient(im: Image.Image, rotate: int) -> Image.Image:
    im = ImageOps.exif_transpose(im).convert("RGB")
    if rotate:
        im = im.rotate(-rotate, expand=True)  # negativ = im Uhrzeigersinn
    return im


def enhance(im: Image.Image, brightness=1.04, contrast=1.06, color=1.08,
            clarity=20, sharpen=120, autocont=0.4) -> Image.Image:
    if autocont:
        im = ImageOps.autocontrast(im, cutoff=autocont, preserve_tone=True)
    im = ImageEnhance.Brightness(im).enhance(brightness)
    im = ImageEnhance.Contrast(im).enhance(contrast)
    im = ImageEnhance.Color(im).enhance(color)
    if clarity:  # lokaler Kontrast (grossradiger Unsharp) = "Klarheit"
        im = im.filter(ImageFilter.UnsharpMask(radius=28, percent=clarity, threshold=3))
    if sharpen:  # Detail-Schaerfe (HD)
        im = im.filter(ImageFilter.UnsharpMask(radius=2, percent=sharpen, threshold=2))
    return im


def side_by_side(before: Image.Image, after: Image.Image, out: Path) -> None:
    gap, top = 24, 40
    w = before.width + after.width + gap * 3
    h = max(before.height, after.height) + top + gap
    canvas = Image.new("RGB", (w, h), (243, 239, 231))
    canvas.paste(before, (gap, top))
    canvas.paste(after, (before.width + gap * 2, top))
    d = ImageDraw.Draw(canvas)
    font = load_font(22)
    d.text((gap, 10), "ORIGINAL", fill=(107, 101, 91), font=font)
    d.text((before.width + gap * 2, 10), "VEREDELT", fill=(140, 106, 63), font=font)
    canvas.save(out, quality=90)


def main() -> None:
    ap = argparse.ArgumentParser(description="Foto veredeln (Editorial-Look)")
    ap.add_argument("src")
    ap.add_argument("dst")
    ap.add_argument("--max", type=int, default=2000)
    ap.add_argument("--rotate", type=int, default=0, choices=[0, 90, 180, 270])
    ap.add_argument("--brightness", type=float, default=1.04)
    ap.add_argument("--contrast", type=float, default=1.06)
    ap.add_argument("--color", type=float, default=1.08)
    ap.add_argument("--clarity", type=int, default=20)
    ap.add_argument("--sharpen", type=int, default=120)
    ap.add_argument("--compare", help="optional Vorher/Nachher-PNG hier speichern")
    a = ap.parse_args()

    base = orient(Image.open(a.src), a.rotate)
    base.thumbnail((a.max, a.max))
    graded = enhance(base.copy(), a.brightness, a.contrast, a.color, a.clarity, a.sharpen)

    out = Path(a.dst)
    out.parent.mkdir(parents=True, exist_ok=True)
    graded.save(out, quality=92, subsampling=0)
    print(f"{out}  {graded.size}")

    if a.compare:
        side_by_side(base, graded, Path(a.compare))
        print(a.compare)


if __name__ == "__main__":
    main()
