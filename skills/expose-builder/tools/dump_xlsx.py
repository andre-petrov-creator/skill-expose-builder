#!/usr/bin/env python3
"""Nicht-leere Zellen einer Excel-Datei ausgeben — fuer Deal-Sheets /
Mietaufstellungen / Kalkulationen aus dem Objekt-Ordner.

    python dump_xlsx.py "<datei.xlsx>"
"""
from __future__ import annotations

import sys

import openpyxl


def main() -> None:
    if len(sys.argv) < 2:
        raise SystemExit("usage: dump_xlsx.py <datei.xlsx>")
    wb = openpyxl.load_workbook(sys.argv[1], data_only=True)
    for ws in wb.worksheets:
        print(f"== SHEET: {ws.title}  ({ws.dimensions}) ==")
        n = 0
        for row in ws.iter_rows(values_only=True):
            cells = [str(c).strip() for c in row if c is not None and str(c).strip()]
            if cells:
                print(" | ".join(cells))
                n += 1
            if n > 250:
                print("... (gekuerzt)")
                break


if __name__ == "__main__":
    main()
