#!/usr/bin/env python3
r"""Foto-Optimierung fuer Exposé-Fotos via ImageMagick — Look "Warm-Cozy #08".

Heller, warmer, sauberer Editorial-Look mit Weissabgleich (Gruen-/Kuehl-Stich raus),
Schatten geoeffnet ueber Gamma, dezente Waerme + Saettigung, geschuetzten Highlights
(Fenster fressen NICHT aus). Liest auch HEIC (iPhone). EXIF-Orientierung wird korrigiert.

Setzt eine installierte ImageMagick 7 voraus (Befehl `magick` im PATH).

    # Einzelbild:
    python warm_cozy_photos.py "<src.heic>" "<dst.jpg>"
    # Ganzer Ordner -> Unterordner \optimiert\ (resumable):
    python warm_cozy_photos.py "<ordner>" --folder --resume
    # Nassraum-clean statt warm:
    python warm_cozy_photos.py "<src>" "<dst>" --profile clean
    # Mit Aufrichten (PRO BILD einzeln setzen!):
    python warm_cozy_photos.py "<src>" "<dst>" --keystone 3     # unten verbreitern (Aufsicht/Drohne)
    python warm_cozy_photos.py "<src>" "<dst>" --keystone -3    # oben verbreitern (Kamera nach oben gekippt)

Keystone ist NICHT pauschal: jede Aufnahme kippt anders. Default = 0 (aus). Der Wert wird PRO
BILD gesetzt, nachdem man das Bild angeschaut hat (Vorzeichen = Richtung, Betrag = Staerke).
Farbe #08 ist dagegen ein echter Standard fuer alle Bilder.

WICHTIG — kein Helligkeits-Boost ueber -modulate: ein +10% (modulate 110) frisst auf
Fotos mit hellen Klarglas-Fenstern die Fenster aus (buntes Clipping-Rauschen). Helligkeit
kommt aus dem Gamma. Fuer "heller" das Gamma leicht erhoehen (max ~1.30), NICHT modulate.
"""
from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path

SRC_EXTS = {".heic", ".jpg", ".jpeg", ".png"}

# Look-Profile: Liste der magick-Operatoren zwischen <src> und <dst>.
# "warm-cozy" = Standard (#08), "clean" = neutral-hell fuer Nassraeume (#04).
PROFILES: dict[str, list[str]] = {
    "warm-cozy": [
        "-auto-orient", "-colorspace", "sRGB",
        "-channel", "RGB", "-contrast-stretch", "0.15%x0.06%", "+channel",
        "-gamma", "1.24",
        "-channel", "R", "-evaluate", "multiply", "1.06", "+channel",
        "-channel", "B", "-evaluate", "multiply", "0.945", "+channel",
        "-modulate", "100,128",
        "-sigmoidal-contrast", "2.2x50%",
        "-unsharp", "0x1.2",
        "-quality", "92",
    ],
    "clean": [
        "-auto-orient", "-colorspace", "sRGB",
        "-channel", "RGB", "-contrast-stretch", "0.15%x0.05%", "+channel",
        "-gamma", "1.28",
        "-channel", "R", "-evaluate", "multiply", "1.03", "+channel",
        "-channel", "B", "-evaluate", "multiply", "0.965", "+channel",
        "-modulate", "100,120",
        "-sigmoidal-contrast", "2.0x50%",
        "-unsharp", "0x1.2",
        "-quality", "92",
    ],
    # brighter but colour-neutral (option b at the TB6 cover gate) - gamma only, no grade
    "gamma": [
        "-auto-orient", "-colorspace", "sRGB",
        "-gamma", "1.24",
        "-quality", "92",
    ],
}


def _dims(src: Path, magick: str) -> tuple[int, int]:
    r = subprocess.run([magick, str(src), "-auto-orient", "-format", "%w %h", "info:"],
                       capture_output=True, text=True, check=True)
    w, h = r.stdout.split()
    return int(w), int(h)


def optimize(src: Path, dst: Path, profile: str, magick: str, keystone: float = 0.0) -> None:
    dst.parent.mkdir(parents=True, exist_ok=True)
    args = list(PROFILES[profile])
    if keystone:  # stuerzende Linien PRO BILD aufrichten (Vorzeichen = Richtung), Bildgroesse bleibt
        w, h = _dims(src, magick)
        dx = round(w * abs(keystone) / 100.0)
        if keystone > 0:  # unten verbreitern (Aufsicht/Drohne: Vertikalen laufen nach unten zusammen)
            pts = f"0,0 0,0  {w},0 {w},0  0,{h} {-dx},{h}  {w},{h} {w + dx},{h}"
        else:             # oben verbreitern (klassische stuerzende Linien: Kamera nach oben gekippt)
            pts = f"0,0 {-dx},0  {w},0 {w + dx},0  0,{h} 0,{h}  {w},{h} {w},{h}"
        distort = ["-set", "option:distort:viewport", f"{w}x{h}+0+0",
                   "-virtual-pixel", "edge", "-distort", "Perspective", pts]
        qi = args.index("-quality")
        args[qi:qi] = distort
    subprocess.run([magick, str(src), *args, str(dst)], check=True)


def run_folder(folder: Path, profile: str, magick: str, resume: bool, keystone: float) -> None:
    out = folder / "optimiert"
    srcs = sorted(p for p in folder.iterdir() if p.is_file() and p.suffix.lower() in SRC_EXTS)
    done = skipped = 0
    for s in srcs:
        target = out / (s.stem + ".jpg")
        if resume and target.exists():
            skipped += 1
            continue
        optimize(s, target, profile, magick, keystone)
        done += 1
        print(f"  ok  {s.name} -> optimiert/{target.name}")
    print(f"Fertig: {done} neu, {skipped} uebersprungen, {len(srcs)} Quelle -> {out}")


def main() -> None:
    ap = argparse.ArgumentParser(description="Exposé-Fotos optimieren (Warm-Cozy #08)")
    ap.add_argument("src", help="Einzeldatei ODER Ordner (mit --folder)")
    ap.add_argument("dst", nargs="?", help="Zieldatei (nur ohne --folder)")
    ap.add_argument("--folder", action="store_true", help="src ist ein Ordner -> \\optimiert\\")
    ap.add_argument("--profile", choices=list(PROFILES), default="warm-cozy")
    ap.add_argument("--resume", action="store_true", help="vorhandene Ziele ueberspringen")
    ap.add_argument("--magick", default="magick", help="Pfad zum magick-Binary")
    ap.add_argument("--keystone", type=float, default=0.0,
                    help="stuerzende Linien PRO BILD aufrichten (Prozent): >0 unten, <0 oben verbreitern, 0 = aus. KEIN Pauschalwert!")
    a = ap.parse_args()

    src = Path(a.src)
    if a.folder:
        run_folder(src, a.profile, a.magick, a.resume, a.keystone)
    else:
        if not a.dst:
            ap.error("dst fehlt (oder --folder benutzen)")
        optimize(src, Path(a.dst), a.profile, a.magick, a.keystone)
        print(Path(a.dst))


if __name__ == "__main__":
    try:
        main()
    except subprocess.CalledProcessError as e:
        print(f"magick-Fehler (Exitcode {e.returncode}): {e.cmd}", file=sys.stderr)
        sys.exit(e.returncode)
