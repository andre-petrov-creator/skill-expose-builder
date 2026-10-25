# Development Guidelines — expose-builder (Querformat)

## Template-Regeln (`template/expose.html` + `expose.css`)
- **EIN Master-Template, wiederverwendbar.** Jede Folie ist `<section class="page …">` =
  genau eine PDF-Seite. Neue Objekte befüllen eine **Kopie** unter `<objekt>/expose/`,
  der Master bleibt unverändert; Verbesserungen fließen zurück.
- **A4 quer fix:** `@page{size:A4 landscape;margin:0}`, `.page` = 297×210 mm.
- **Branding über CSS-Variablen + `template/brand/<firma>/`** (aktiv `hk-ruhrinvest`,
  Logo `logo-ink.png`). Firmenwechsel = Variablen + Brand-Ordner, kein Markup.
- **Seitenrahmen konsistent:** Running Head (Logo + Adresse · Wohnung) · Headline +
  `.h2rule` (roter Unterstrich) · `.brandfoot` · Wasserzeichen `.page::before` (4 %,
  bleibt auch auf Foto-Folien).
- **Icons:** Inline-SVG-Line-Icons, `stroke="currentColor"`, Farbe Oxblood via `.ic`.
  Label (IBM Plex Mono, uppercase) über Wert (Spectral).
- **Foto-Philosophie:** Raum-Folien = leere Fläche OHNE Marker (André platziert 1–3 Fotos
  frei im PDF-Editor). Grundriss = kleiner `.fotomark`-Marker. Datenseiten optional als
  **Variante B** (`.splitflow`: Daten ~40 % links, Foto-Zone rechts mit Mini-Marker).
  Nie große Platzhalter-Kästen, die ein eingefügtes Foto nicht sicher überdeckt.
- **Energieausweis** nur auf „Gebäude-Technik & Zustand": Vollbreiten-Zeile (`.energrow`)
  + Mini-Farbskala (`.escale--mini`, Original-Klassenfarben, aktive Zelle `is-active`).

## PDF-Pipeline (`tools/render_pdf.py`, `raster_check.py`)
- Headless-Chromium: Chrome bevorzugt, Edge als Fallback (Auto-Detection in `render_pdf.py`).
- **Kein WeasyPrint** (GTK auf dieser Maschine kaputt), **kein PowerPoint** als Erzeugungsweg.
- **Stale-Lock-Regel (wiederkehrender Fehler):** Render-Iterationen IMMER auf neuen
  Dateinamen — eine je in einem Viewer geöffnete Ziel-PDF wird still NICHT überschrieben.
  Frische über Inhalt verifizieren: `fitz` → `page.get_text().lower()` auf die geänderte
  Stelle (CSS-`text-transform:uppercase` macht case-sensitive Checks wertlos).
- Umbruch-/Design-Gate: `raster_check.py` (PDF → PNG, 150 dpi) und PNGs visuell prüfen.
- Vorschauen nur nach `_scratch/` (gitignored), nie in OneDrive-Objektordner.

## Workflow-Konvention (Text zuerst)
- Inhalte werden **im Chat als nummerierter Text** entworfen und freigegeben, DANN in
  HTML gegossen (SKILL.md Phase 2). HTML-Änderungen ohne Text-Freigabe sind tabu.

## Wording (hart — rechtlicher Schutz)
- Verbots-/Pflichtliste: `references/wording-leitplanken.md`.
- NIE: Renditegarantie, „sicher", „garantiert", „steuerfrei" als Zusage, „wird mehr wert".
- **Keine Finanzangaben auf Folien** (Ausnahmen laut SKILL.md: Instandhaltungsrücklage auf
  Gebäude-Eckdaten, 7b Immobilienbewertung-Screenshot, 7c Beispielsberechnung; Ø Vermietungsdauer
  = Nachfrage-Beweis, keine Finanzangabe). Kennzahlen in Ausarbeitungen immer mit Quelle + Stichtag.

## Git-Workflow
- Teil des Mono-Repos `C:\meine-projekte\`. Commits nur auf User-Auftrag; „festzurren/speichern"
  = commit + push auf `main` (English Message, keine Co-Authored-By-Zeile).
- Niemals destruktiv ohne Bestätigung, keine Hook-/Signatur-Umgehung.

## Code-Konventionen & Dependencies
- Python `snake_case`, Dateien/CSS `kebab-case`; Code + Commits Englisch, User-facing Deutsch.
- Keine Kommentare außer nicht-offensichtlichem WHY. Keine Schein-Robustheit.
- Windows-Konsole: keine Nicht-ASCII-Prints in `python -c` (cp1252) — ASCII oder `PYTHONUTF8=1`.
- Bevorzugt vorhandene Dependencies: PyMuPDF, Headless-Chromium, Standard-Lib.
