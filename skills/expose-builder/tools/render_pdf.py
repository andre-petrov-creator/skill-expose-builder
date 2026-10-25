#!/usr/bin/env python3
"""HTML -> PDF via Headless-Chromium (Chrome bevorzugt, Edge als Fallback).

Beispiel:
    python render_pdf.py "<objekt>/expose/04_layout/expose.html" \
        -o "<objekt>/expose/EXPOSE_Musterstrasse-12.pdf"
"""
from __future__ import annotations

import argparse
import os
import subprocess
import sys
import tempfile
from pathlib import Path

BROWSER_CANDIDATES = [
    r"C:\Program Files\Google\Chrome\Application\chrome.exe",
    r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
    os.path.expandvars(r"%LOCALAPPDATA%\Google\Chrome\Application\chrome.exe"),
    r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
    r"C:\Program Files\Microsoft\Edge\Application\msedge.exe",
]


def find_browser(explicit: str | None = None) -> str:
    if explicit:
        if Path(explicit).exists():
            return explicit
        sys.exit(f"Browser nicht gefunden: {explicit}")
    for cand in BROWSER_CANDIDATES:
        if cand and Path(cand).exists():
            return cand
    sys.exit("Kein Chrome/Edge gefunden. Mit --browser <pfad> angeben.")


def render(html_path: Path, pdf_path: Path, browser: str, timeout: int = 180) -> Path:
    html_path = html_path.resolve()
    pdf_path = pdf_path.resolve()
    if not html_path.exists():
        sys.exit(f"HTML nicht gefunden: {html_path}")
    pdf_path.parent.mkdir(parents=True, exist_ok=True)

    # eigenes Profil -> kein Konflikt mit laufendem Browser
    with tempfile.TemporaryDirectory() as profile:
        cmd = [
            browser,
            "--headless",
            "--disable-gpu",
            "--no-sandbox",
            f"--user-data-dir={profile}",
            "--allow-file-access-from-files",
            "--no-pdf-header-footer",
            "--virtual-time-budget=6000",  # Zeit fuer Web-Fonts/@import
            f"--print-to-pdf={pdf_path}",
            html_path.as_uri(),
        ]
        proc = subprocess.run(cmd, capture_output=True, text=True, timeout=timeout)

    if not pdf_path.exists():
        sys.stderr.write((proc.stdout or "") + "\n" + (proc.stderr or "") + "\n")
        sys.exit(f"PDF wurde nicht erzeugt (Exit {proc.returncode}).")
    return pdf_path


def main() -> None:
    ap = argparse.ArgumentParser(description="HTML -> PDF (Headless-Chromium)")
    ap.add_argument("html", help="Pfad zur expose.html")
    ap.add_argument("-o", "--out", help="Ziel-PDF (Default: neben der HTML)")
    ap.add_argument("--browser", help="Pfad zu chrome.exe / msedge.exe")
    args = ap.parse_args()

    html = Path(args.html)
    out = Path(args.out) if args.out else html.with_suffix(".pdf")
    pdf = render(html, out, find_browser(args.browser))
    print(pdf)


if __name__ == "__main__":
    main()
