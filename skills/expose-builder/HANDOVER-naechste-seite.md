# Übergabe: expose-builder Querformat — Stand nach SKILL-Umbau

**Stand 2026-07-26 (historisch).** Aktueller Stand, Regeln und offene Punkte stehen in
`SKILL.md` (Gelernte Regeln, Offene Punkte/Roadmap). Bei Widerspruch gilt SKILL.md.

## Wo alles steht

- **Workflow/Regeln:** `SKILL.md` (Start-Gates, Taxonomie, Wert-Gate, Auto-Foto-Test, Feld-Regeln).
- **Master:** `template/expose.html` + `expose.css` — Seiten: Titel · Makrolage · Mikrolage ·
  Eckdaten · Technik & Zustand · Grundriss · Angaben zur Wohnung · 11 Raum-Folien ·
  Varianten-Anhang B (3 Datenseiten mit Foto, `.vartag`-Label nur Master-Vorschau).
- **References (maßgeblich):** führende Liste in SKILL.md → Offene Punkte.
- **Render:** `python tools/render_pdf.py template/expose.html -o _scratch/wireframes/<name>.pdf`
  → `python tools/raster_check.py <pdf> --out _scratch/wireframes/pages --dpi 150 [--pages N]`.
  Achtung: gesperrte Ziel-PDF wird NICHT überschrieben (stale) — neuer Name oder Viewer zu.

## Kern-Entscheidungen (nicht wieder aufmachen)

- **Keine Finanzangaben im Exposé** (keine Miete/Hausgeld/Preise) — Exposé = Präsentationsgrundlage.
- **Lage zuerst:** Titel → Makro → Mikro → Gebäude → Wohnung → Bilder.
- **Raum-Folien + Grundriss ohne Foto-Markierung** (nur Mini-Marker beim Grundriss) — André
  platziert Fotos frei im PDF-Editor.
- **Foto-Frage pro Datenseite** → Variante A (volle Breite) oder B (Daten 40 % + Foto).
- **Stadt/Stadtteil-Zuschnitt** wird bei Makro + Mikro abgefragt (Start-Gates 4+5).
- **Ø Vermietungsdauer im PLZ-Gebiet** = Pflicht-Zeile auf der Mikrolage-Folie (Fixwert von
  André, Quelle ohne-makler, mit Suchwerten PLZ · Zimmer · m² abfragen — Start-Gate 10).
  Immometrica-/ohne-makler-Screenshot zusätzlich nur als Call-Material.

## Offen

- Abschluss-Seite: als `.closing` in der Ringlebstr.-Objektkopie gebaut, Rückfluss in den Master offen.
- `build_expose.py`: Querformat + Pro-Wohnung-Loop + Auto-Foto-Platzierung (Test-Protokoll
  in `references/raum-seiten.md`).
- ~~Alte Hochformat-References~~ → 2026-07-26 gelöscht (seitenbibliothek, design-system,
  foto-dramaturgie, entwurf-format, faktenblatt-schema, mechanik-referenz, preis-anker,
  docs/content-format, docs/pipeline, template/beispiel-uebersicht + MUSTER.pdf + assets).
  Wiederherstellbar über git-Historie.
