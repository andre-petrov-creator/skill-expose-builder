#!/usr/bin/env python3
"""Text aus einem PDF je Seite extrahieren (PyMuPDF) — fuer text-basierte
Objekt-Dokumente (Wohnflaeche, Mietvertrag, Energieausweis, Protokolle).

Scan-PDFs ohne Text-Layer werden gemeldet -> dann via raster_check.py rendern
und multimodal lesen.

    python pdf_text.py "<datei.pdf>" [seiten z.B. 1-3]
"""
from __future__ import annotations

import sys

import fitz  # PyMuPDF


def parse_pages(spec: str | None, total: int) -> list[int]:
    if not spec:
        return list(range(total))
    out: list[int] = []
    for part in spec.split(","):
        part = part.strip()
        if "-" in part:
            a, b = part.split("-", 1)
            out.extend(range(int(a) - 1, int(b)))
        elif part:
            out.append(int(part) - 1)
    return [i for i in out if 0 <= i < total]


def main() -> None:
    if len(sys.argv) < 2:
        raise SystemExit("usage: pdf_text.py <datei.pdf> [seiten]")
    doc = fitz.open(sys.argv[1])
    spec = sys.argv[2] if len(sys.argv) > 2 else None
    for i in parse_pages(spec, len(doc)):
        text = doc[i].get_text().strip()
        print(f"\n===== Seite {i + 1} / {len(doc)} =====")
        print(text if text else "[kein Text-Layer — Scan, rendern noetig]")
    doc.close()


if __name__ == "__main__":
    main()
