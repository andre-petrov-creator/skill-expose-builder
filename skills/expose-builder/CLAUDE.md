# Projekt: expose-builder (Verkaufs-Dossier für Kapitalanlage-Objekte)

Skill-Loader: `~/.claude/skills/expose-builder` (Junction → dieser Ordner).
Master-Code lebt hier im Mono-Repo `C:\meine-projekte\Immobilien\expose-builder-vertrieb\`.

## Vor jeder Aufgabe
1. Lies `SKILL.md` (Orchestrator: Mission, Phasen, Gates).
2. Lies die **für die aktuelle Phase relevanten** Dateien in `references/` — NICHT alle vorab.
3. Lies `DEVELOPMENT_GUIDELINES.md` (Template-, Chart-, PDF-, Wording-Konventionen).
4. Bei Layout/Technik: relevante Dateien in `docs/`.

## Nach jeder Aufgabe
1. Aktualisiere oder erstelle `docs/<feature>.md`.
2. Halte Code-Style und Konventionen aus `DEVELOPMENT_GUIDELINES.md` ein.
3. Template-Verbesserungen am Objekt → ins globale `template/` zurückschreiben.
4. Wiederkehrende Korrekturen Andrés → Abschnitt "Gelernte Regeln" in `SKILL.md`.

## Stack
- **Content:** Text-zuerst — pro Folie nummerierter Text-Entwurf im Chat, Freigabe im Text,
  DANN in HTML gießen (SKILL.md Phase 2). Kein HTML-Ping-Pong.
- **Layout:** EIN HTML/CSS-Print-Template (`template/expose.html` + `expose.css`), **A4 quer**,
  `@page`-Regeln, CSS-Variablen + `template/brand/` fürs Branding (aktiv HK RuhrInvest),
  Section-Klassen als Seitenmodule; Raum-Folien ohne Foto-Marker (freie Platzierung),
  Datenseiten mit A/B-Variante (B = Daten 40 % + Foto-Zone).
- **Keine Finanzangaben im Exposé** — Ausnahmen: Stammdaten der Wohnung (7a, Pflicht: Miete + Hausgeld),
  Immobilienbewertung-Screenshot (7b, nur auf Zuruf), Beispielsberechnung (7c). Instandhaltungsrücklage auf Gebäude-Eckdaten nur, wenn vorhanden.
  Ein Exposé je Wohnung für Käufer und Bank. Die Ø Vermietungsdauer im
  PLZ-Gebiet ist keine Finanzangabe, sondern Pflicht-Zeile der Mikrolage (siehe SKILL.md).
  Keine Chart-/Marktpreis-Seiten mehr (`chart_svg.py` bleibt nur als Import von `build_expose.py`).
- **PDF-Render:** Headless-Chromium (`tools/render_pdf.py`, Chrome ODER Edge `--headless --print-to-pdf`). **Kein WeasyPrint** (GTK-Libs auf dieser Maschine kaputt). **Kein PowerPoint** als Erzeugungsweg.
  Render-Iterationen IMMER auf neuen Dateinamen (gesperrte Ziel-PDF → stiller Stale-Render);
  Frische über `page.get_text().lower()` verifizieren.
- **Umbruch-Prüfung:** PyMuPDF (`tools/raster_check.py`, PDF → PNG je Seite).
- Python 3.14, Node 24 verfügbar.

## Architektur-Prinzipien
- **Content-first / Layout-last.** Text komplett freigegeben, dann gießen.
- **Harte Freigabe-Gates** nach jeder Phase, EIN Arbeitspaket pro Runde (siehe `SKILL.md` → Start-Gates, Fragesparring, Phase 2).
- **References pro Phase laden**, nicht alles vorab (Token-Sparsamkeit).
- **EIN wiederverwendbares Template** — pro Objekt nur Kopie befüllen, Master bleibt sauber.
- **Deploy first:** echtes Objekt durchziehen, dann verfeinern. Keine Schein-Robustheit.

## Konventionen
- Sprache im Code: **Englisch** (Variablen, Funktionen, Commits). User-facing Strings (Exposé, Chat, Logs für User): **Deutsch**.
- Fachbegriffe ohne saubere Übersetzung (Grundbuch, Hausgeld, Teilungserklärung, BRW) bleiben Deutsch.
- Keine Kommentare im Code außer bei nicht-offensichtlichem WHY.
- Naming: `snake_case` (Python), `kebab-case` (Dateien/CSS-Klassen).
- Keine Doku/READMEs ohne Auftrag (diese hier sind der Auftrag).

## Skill-Referenzen
- `unterlagen-check-ankauf` — Struktur-Vorbild (Phasen-Skill mit References + Tools).
- `claude-code-blueprint` — Projekt-Setup-Methodik (FORM dieses Projekts).
