# Roadmap / offene To-dos — expose-builder

## 1. Foto-Aufwertung per KI (priorisiert)
**Status:** offen. **Interim:** `tools/enhance_photo.py` (Pillow — Tonwert, Klarheit, HD-Schärfe; dezent/seriös). Für aktuelle Objekte akzeptiert.

**Ziel (André, 2026-06-17):** Eigener Schritt nach der Foto-Sichtung — *„wie wir die Bilder auswählen, werden sie durch eine vernünftig angebundene KI aufgewertet"*. Qualität deutlich über reiner Pillow-Korrektur: echtes HD/Super-Resolution, Belichtung, Perspektive geradeziehen, Entstörung, ggf. Himmel.

**Kandidaten (zu evaluieren):**
- Super-Resolution/Restoration via Replicate-API: Real-ESRGAN, GFPGAN, SwinIR.
- Real-Estate-Foto-Enhancer-APIs: z. B. autoenhance.ai, BoxBrownie.
- Topaz Photo AI (Desktop/Batch, keine API — als lokaler Schritt denkbar).

**Auswahlkriterien:** Ergebnisqualität (seriös, nicht „AI-fake"), Kosten je Bild, API-Stabilität, DSGVO/AVV (Objektfotos = ggf. personenbezogen, Mieter).

**Integration:** API-Key in `.env` (nicht committen). Schritt zwischen Foto-Sichtung (Auswahl) und Slot-Einbau. Original behalten, veredelte Fassung in `assets/img/`. Fallback = `enhance_photo.py`.

## 2. Veredelung auf ALLE Slot-Bilder
`build_expose.py` + `contact_sheet.py`: EXIF-Orientierung + `enhance_photo`-Grade automatisch auf jedes eingebundene Bild anwenden (aktuell nur Hero manuell veredelt).

## 3. Mockup-Modus im Assembler
`build_expose.py --mockup`: fehlende Inhalte als Akzent-Badges/Platzhalter rendern (statt manuell pro Seite HTML zu bauen), damit das „Blatt für Blatt mit sichtbarem Input"-Sparring aus einem Tool kommt.

## 4. Design-System v2 ins Master-Template ziehen
Der Reference-Grade-Stil (Libre Caslon + Spectral + Oxblood, Haarlinien-Bänder, freie Zahlen ohne Kästchen) liegt aktuell self-contained in `template/beispiel-uebersicht.html`. To-do: Design-Tokens + Klassen nach `template/expose.css` extrahieren, `template/expose.html` + `build_expose.py`-Renderer auf v2 umstellen, Cover (Seite 1) im neuen Stil nachziehen.
