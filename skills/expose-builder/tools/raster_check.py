#!/usr/bin/env python3
"""PDF -> PNG je Seite (PyMuPDF) fuer die visuelle Umbruch-Pruefung (Phase 4/5).

Beispiel:
    python raster_check.py "<objekt>/expose/EXPOSE_x.pdf"            # alle Seiten
    python raster_check.py "<objekt>/expose/EXPOSE_x.pdf" --pages 1-2 # Design-Gate
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

try:
    import fitz  # PyMuPDF
except ImportError:
    sys.exit("PyMuPDF fehlt:  pip install --user pymupdf")


def parse_pages(spec: str | None, total: int) -> list[int]:
    if not spec:
        return list(range(total))
    idxs: list[int] = []
    for part in spec.split(","):
        part = part.strip()
        if "-" in part:
            a, b = part.split("-", 1)
            idxs.extend(range(int(a) - 1, int(b)))
        elif part:
            idxs.append(int(part) - 1)
    return [i for i in idxs if 0 <= i < total]


def raster(pdf_path: Path, out_dir: Path, dpi: int = 130, pages: str | None = None) -> list[Path]:
    doc = fitz.open(pdf_path)
    out_dir.mkdir(parents=True, exist_ok=True)
    mat = fitz.Matrix(dpi / 72, dpi / 72)
    written: list[Path] = []
    for i in parse_pages(pages, len(doc)):
        pix = doc[i].get_pixmap(matrix=mat)
        target = out_dir / f"page_{i + 1:02d}.png"
        pix.save(target)
        written.append(target)
    doc.close()
    return written


def main() -> None:
    ap = argparse.ArgumentParser(description="PDF -> PNG je Seite")
    ap.add_argument("pdf", help="Pfad zum PDF")
    ap.add_argument("--out", help="Zielordner (Default: <pdf>_pages/ daneben)")
    ap.add_argument("--dpi", type=int, default=130)
    ap.add_argument("--pages", help='z.B. "1-2" oder "1,3,5"')
    args = ap.parse_args()

    pdf = Path(args.pdf)
    out = Path(args.out) if args.out else pdf.with_name(pdf.stem + "_pages")
    files = raster(pdf, out, args.dpi, args.pages)
    for f in files:
        print(f)


if __name__ == "__main__":
    main()
