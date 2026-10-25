#!/usr/bin/env python3
"""Charts als Inline-SVG (kein Screenshot). Quellen-Zeile ist Pflicht.

Zwei Typen:
  preisentwicklung  -> Linien-Chart, NUR Vergangenheitsdaten (Wording-Leitplanke)
  marktvergleich    -> horizontale Balken, unser Preis hervorgehoben (Preis-Anker)

Import:  from chart_svg import line_chart, anchor_bars
CLI:     python chart_svg.py --type preisentwicklung \
             --data "2019=1800;2021=2100;2023=2400;2025=2700" \
             --source "Quelle: Homeday/Gutachterausschuss - Stand 06/2026" -o chart.svg
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

ACCENT = "#8C6A3F"
LINE = "#D8CFBF"
MUTED = "#6B655B"
TEXT = "#2B2B2B"
MONO = "IBM Plex Mono, 'Courier New', monospace"


def _src(source: str, x: float, y: float) -> str:
    if not source:
        return ""
    return (f'<text x="{x}" y="{y}" font-family="{MONO}" font-size="6.8" '
            f'fill="{MUTED}">{_esc(source)}</text>')


def _esc(s: str) -> str:
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def line_chart(series: list[tuple[str, float]], source: str = "",
               ylabel: str = "EUR/m2", width: int = 360, height: int = 210) -> str:
    """series: [(jahr, wert), ...] -- aufsteigend sortiert erwartet."""
    pad_l, pad_r, pad_t, pad_b = 38, 14, 14, 40
    ys = [float(v) for _, v in series]
    ymin, ymax = min(ys), max(ys)
    if ymax == ymin:
        ymax = ymin + 1
    x0, x1 = pad_l, width - pad_r
    ybase, ytop = height - pad_b, pad_t
    n = len(series)

    def px(i: int) -> float:
        return x0 + (x1 - x0) * (i / (n - 1) if n > 1 else 0)

    def py(v: float) -> float:
        return ybase + (ytop - ybase) * ((v - ymin) / (ymax - ymin))

    parts = [f'<svg viewBox="0 0 {width} {height}" xmlns="http://www.w3.org/2000/svg">']
    # Achsen
    parts.append(f'<line x1="{x0}" y1="{ytop}" x2="{x0}" y2="{ybase}" stroke="{LINE}"/>')
    parts.append(f'<line x1="{x0}" y1="{ybase}" x2="{x1}" y2="{ybase}" stroke="{LINE}"/>')
    # Y-Labels (min, mitte, max)
    for v in (ymin, (ymin + ymax) / 2, ymax):
        parts.append(f'<text x="4" y="{py(v) + 3:.1f}" font-family="{MONO}" '
                     f'font-size="8" fill="{MUTED}">{v / 1000:.1f}k</text>')
    # Linie + Punkte
    pts = " ".join(f"{px(i):.1f},{py(v):.1f}" for i, v in enumerate(ys))
    parts.append(f'<polyline fill="none" stroke="{ACCENT}" stroke-width="2.5" '
                 f'stroke-linejoin="round" points="{pts}"/>')
    for i, (lbl, v) in enumerate(series):
        parts.append(f'<circle cx="{px(i):.1f}" cy="{py(v):.1f}" r="3" fill="{ACCENT}"/>')
        parts.append(f'<text x="{px(i):.1f}" y="{ybase + 13:.1f}" font-family="{MONO}" '
                     f'font-size="8" fill="{MUTED}" text-anchor="middle">{_esc(lbl)}</text>')
    parts.append(f'<text x="{x0}" y="{ytop - 3}" font-family="{MONO}" font-size="7.5" '
                 f'fill="{MUTED}">{_esc(ylabel)}</text>')
    parts.append(_src(source, x0, height - 6))
    parts.append("</svg>")
    return "".join(parts)


def anchor_bars(rows: list[tuple[str, float]], highlight: str = "",
                source: str = "", width: int = 360) -> str:
    """rows: [(label, wert), ...]. Zeile == highlight wird im Akzent dargestellt."""
    row_h, gap, pad_t, pad_l = 22, 8, 16, 120
    height = pad_t + len(rows) * (row_h + gap) + 26
    vmax = max(float(v) for _, v in rows) or 1
    bar_max = width - pad_l - 46

    parts = [f'<svg viewBox="0 0 {width} {height}" xmlns="http://www.w3.org/2000/svg">']
    y = pad_t
    for lbl, v in rows:
        v = float(v)
        is_hi = lbl.strip().lower() == highlight.strip().lower()
        col = ACCENT if is_hi else LINE
        txtcol = TEXT if is_hi else MUTED
        w = bar_max * (v / vmax)
        weight = "600" if is_hi else "400"
        parts.append(f'<text x="{pad_l - 6}" y="{y + row_h * 0.7:.1f}" font-family="{MONO}" '
                     f'font-size="8.5" fill="{txtcol}" font-weight="{weight}" '
                     f'text-anchor="end">{_esc(lbl)}</text>')
        parts.append(f'<rect x="{pad_l}" y="{y:.1f}" width="{w:.1f}" height="{row_h}" '
                     f'rx="1.5" fill="{col}"/>')
        parts.append(f'<text x="{pad_l + w + 5:.1f}" y="{y + row_h * 0.7:.1f}" '
                     f'font-family="{MONO}" font-size="8.5" fill="{txtcol}" '
                     f'font-weight="{weight}">{v:,.0f}</text>'.replace(",", "."))
        y += row_h + gap
    parts.append(_src(source, pad_l, height - 8))
    parts.append("</svg>")
    return "".join(parts)


def _parse_data(spec: str) -> list[tuple[str, float]]:
    out: list[tuple[str, float]] = []
    for pair in spec.split(";"):
        pair = pair.strip()
        if not pair:
            continue
        k, v = pair.split("=", 1)
        out.append((k.strip(), float(v.replace(".", "").replace(",", "."))))
    return out


def main() -> None:
    ap = argparse.ArgumentParser(description="Chart als Inline-SVG")
    ap.add_argument("--type", required=True, choices=["preisentwicklung", "marktvergleich"])
    ap.add_argument("--data", required=True, help='"Label=Wert;Label=Wert;..."')
    ap.add_argument("--source", default="", help="Quelle + Stichtag (Pflicht im Exposé)")
    ap.add_argument("--highlight", default="Unser Preis", help="hervorgehobene Zeile (marktvergleich)")
    ap.add_argument("-o", "--out", help="Ziel-SVG (Default: stdout)")
    args = ap.parse_args()

    data = _parse_data(args.data)
    if args.type == "preisentwicklung":
        svg = line_chart(data, source=args.source)
    else:
        svg = anchor_bars(data, highlight=args.highlight, source=args.source)

    if args.out:
        Path(args.out).write_text(svg, encoding="utf-8")
        print(args.out)
    else:
        sys.stdout.write(svg)


if __name__ == "__main__":
    main()
