# expose-builder-vertrieb

Skill **`expose-builder`** — wiederholbarer Prozess, der aus einem Objekt-Ordner ein hochwertiges Verkaufs-Dossier (PDF, Editorial-Stil, 8–14 Seiten) für Kapitalanleger erzeugt. Marke Petrov Wohnen / HK-RuhrInvest.

Master-Code im Mono-Repo, Skill-Loader via Junction.

## Struktur

```
expose-builder-vertrieb/
  SKILL.md                    Orchestrator: Mission, 5-Phasen-Workflow, Freigabe-Gates
  CLAUDE.md                   Steuerungsdatei (Vor/Nach-Aufgabe, Stack, Prinzipien)
  DEVELOPMENT_GUIDELINES.md   Template-, Chart-, PDF-, Wording-Konventionen
  references/                 Wissens-Module (pro Phase geladen)
    mechanik-referenz.md        Warum das Referenz-Dossier funktioniert
    seitenbibliothek.md         Seitenmodule pflicht + optional je Objekttyp
    foto-dramaturgie.md         Spannungsbogen-Reveal + Bild-Slot-System
    faktenblatt-schema.md       Schema für das Faktenblatt (Phase 1)
    preis-anker.md              Marktvergleich-Anker (Wiederverwendung portal-bewertung)
    wording-leitplanken.md      Harte rechtliche Wording-Regeln
    design-system.md            Branding-Variablen, Typografie, Layout
  template/                   EIN wiederverwendbares Print-Template
    expose.html                 A4-Seitenmodule, Bild-Slots, Kopf/Fuß
    expose.css                  @page, CSS-Variablen, Slot-/Chart-Stile, dunkle Schlussseite
    assets/                     Logo-Platzhalter, Schriften-Hinweis
  tools/
    build_expose.py             Freigegebene Content-MDs → HTML einsetzen
    chart_svg.py                Charts als Inline-SVG
    render_pdf.py               HTML → PDF via Headless-Chromium
    raster_check.py             PDF → PNG je Seite (Umbruch-Prüfung)
  docs/                       Pro-Feature-Doku
```

Pro Objekt entsteht ein `/expose`-Ordner **im Objekt-Ordner** (Inventar, Faktenblatt, Content, Layout, fertiges PDF) — der Master bleibt sauber.

## Skill-Junction neu anlegen (nach Recovery / Rechnerwechsel)

```cmd
cmd /c rmdir "%USERPROFILE%\.claude\skills\expose-builder"
cmd /c mklink /J "%USERPROFILE%\.claude\skills\expose-builder" "C:\meine-projekte\Immobilien\expose-builder-vertrieb"
```

## Status

Im Aufbau (2026-06-17). Skelett + References + Template + Tools werden gebaut, dann erster echter Objekt-Durchlauf (Phase 0–5).
