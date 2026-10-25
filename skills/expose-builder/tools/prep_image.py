#!/usr/bin/env python3
"""Bild fuer einen Slot vorbereiten: EXIF-Orientierung anwenden, optional
zusaetzlich drehen, skalieren, als RGB-JPG speichern.

Phone-Fotos sind oft seitlich gespeichert (EXIF-Orientierung). Headless-Chromium
und viele Viewer wenden EXIF NICHT an -> Bild liegt quer. Dieses Tool brennt die
korrekte Orientierung in die Pixel und entfernt das Problem.

    python prep_image.py "<src.jpg>" "<dst.jpg>" [--max 1800] [--rotate 0|90|180|270]
"""
from __future__ import annotations

import argparse
from pathlib import Path

from PIL import Image, ImageOps


def main() -> None:
    ap = argparse.ArgumentParser(description="Bild orientieren + skalieren")
    ap.add_argument("src")
    ap.add_argument("dst")
    ap.add_argument("--max", type=int, default=1800, help="laengste Kante px")
    ap.add_argument("--rotate", type=int, default=0, choices=[0, 90, 180, 270],
                    help="zusaetzliche Drehung im Uhrzeigersinn (falls EXIF fehlt)")
    args = ap.parse_args()

    im = ImageOps.exif_transpose(Image.open(args.src))
    if args.rotate:
        im = im.rotate(-args.rotate, expand=True)  # negativ = im Uhrzeigersinn
    im = im.convert("RGB")
    im.thumbnail((args.max, args.max))
    out = Path(args.dst)
    out.parent.mkdir(parents=True, exist_ok=True)
    im.save(out, quality=88)
    print(f"{out}  {im.size}")


if __name__ == "__main__":
    main()
