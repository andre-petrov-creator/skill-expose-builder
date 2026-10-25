---
name: expose-builder
description: Wiederholbarer Prozess, der aus dem Material eines Objekt-Ordners ein schlankes Querformat-Verkaufsexposé (A4 quer, HTML → Headless-Chromium → PDF) für Kapitalanleger erzeugt — Marke HK RuhrInvest, EIN PDF pro Wohnung (Gebäude-Seiten shared, Wohnungs-Seiten individuell). Nur Daten + wenige knackige Sätze, keine Kauf-/Marktpreise; Miete + Hausgeld nur auf der Pflicht-Folie „Stammdaten der Wohnung" (Grundbuch, MEA, Abt. II …), damit dasselbe PDF für Käufer UND Bank reicht. Ablauf: Start-Gates (Einheiten, Datenquelle, Marke, Stadt/Stadtteil-Zuschnitt, Titelmotiv-, Haus-Fotos-, Farbabgleich- und Foto-Fragen) → Recherche-Ausarbeitungen (Makro/Mikro) → Block-für-Block-Fragesparring → objekt.json je Objekt → Kontaktbogen-Gate (passt/passt nicht/anders) → Render pro Wohnung über generische Tools → Abnahme-Check. Trigger: "Exposé bauen", "Verkaufsdossier", "Vertriebsexposé", "Objekt-Dossier", "Kapitalanlage-Exposé", "Exposé für <Objekt>", "Verkaufsunterlage erstellen", Marke HK-RuhrInvest / Petrov Wohnen, oder wenn der User einen Objekt-Ordner mit Fotos, Grundrissen, Unterlagen teilt und daraus eine Verkaufs-Präsentation will. NICHT für: Ankaufsprüfung/Due-Diligence (→ unterlagen-check-ankauf), Aufteiler-Analyse/Kalkulation (→ aufteiler), Bank-Finanzierungsanfragen (→ finanzierungsanfrage-generator) oder Einzelfragen zu einem Dokument.
---

# Exposé-Builder — Querformat-Verkaufsexposé (HK RuhrInvest)

## Mission

Aus dem Objekt-Ordner ein **schlankes, standardisiertes Querformat-Verkaufsexposé** bauen:
**ein PDF pro Wohnung** (Gebäude-Teil identisch, Wohnungs-Teil individuell) — gebaut für
Massenproduktion (z. B. 16 Einheiten eines Hauses) und als **Präsentationsgrundlage im
Sales-Call**. Nur Daten + einzelne knackige Sätze, kein Fließtext, keine Objektbeschreibung.

**Verkaufsdramaturgie (fixiert):** Lage zuerst (Primacy/Halo — starke Lage-Story färbt auf
alles Folgende ab), dann Substanz, dann Wohnung, dann Bilder. Trichter Stadt → Umgebung →
Gebäude → Wohnung.

**Harte Regel: KEINE Finanzangaben im Exposé.** Keine Kaltmiete, kein Hausgeld, kein
Kaufpreis, kein Marktpreis, keine Miet-/Preistrends. Zahlen zu Geld kommen ins Gespräch,
nie auf die Folien. (Nachfrage-Beweis Ø Vermietungsdauer im PLZ-Gebiet ist seit 2026-07
Pflicht-Zeile der Mikro-Folie — Fixwert von André, siehe `references/mikrolage-standort.md`.)
**Ausnahmen:** (1) die **Stammdaten-Folie (7a, Pflicht)** — Nettokaltmiete + Hausgeld (davon nicht
umlagefähig), siehe „Stammdaten der Wohnung". **Instandhaltungsrücklage (Gebäude) auf Gebäude-Eckdaten
nur, wenn vorhanden** (André 2026-10-19: „sofern vorhanden rein, sofern nicht vorhanden raus") —
siehe Start-Gate 11.
(2) die **Immobilienbewertung-Folie (7b)** — nur auf Zuruf (André 2026-10-19: „brauchen wir nicht
unbedingt"); wenn, dann ImmoScout24-Screenshot 1:1 als Bild, nie als eigene Exposé-Zahlen.
(3) die **Beispielsberechnung-Folie (7c)** — optionale Cashflow-Rechnung je Wohnung
(André-fixiert 2026-07-31): der einzige Ort mit Kaufpreis/Cashflow auf dem Blatt,
Details + Rechenweg `references/beispielsberechnung.md`.
(4) die **Stammdaten-Folie** (Pflicht in jedem Exposé, siehe „EIN Exposé je Wohnung") mit
Miete und Hausgeld inkl. Rücklage-Anteil (André-fixiert 2026-10-19).

## Seiten-Taxonomie (fixiert)

**STANDARD-FOLIENFOLGE (v1, André-fixiert 21.10.2026 — Entscheidungsliste v1 Herten, ersetzt die
Folge vom 20.10.; Referenz: `<Herten>/expose/_build/objekt.json` + `tools/build_objekt.py`).
Gilt vor der Nummerierung weiter unten:**
1. Titel (Innenfoto der Einheit; Motiv per Titelmotiv-Gate, Farb-Rezept per Farbabgleich-Gate)
2. Makrolage
3. Mikrolage
4. Gebäude-Eckdaten (Foto rechts)
5. Gebäude-Technik & Zustand (Foto rechts, z. B. Stromkasten)
6. Angaben zur Wohnung (links „Eckdaten“ + „Ausstattung & Zustand“ übereinander, Foto rechts)
7. Grundriss
8. Stammdaten der Wohnung (danach ggf. 7b Immobilienbewertung · 7c Beispielsberechnung)
9. Fenster und Türen
10. Heizung
11. Sanitär
12. Wohnzimmer
13. Zimmer 1
14. Zimmer 2
15. Küche
16. Bad (bei zwei Bad-Folien: erst Gesamtansicht, dann Details)
17. Flur (Wohnungsflur, 1 großes Foto)
18. Haus & Garten — Vorderseite + Hinterhaus + Garten auf EINER Folie, Layout A: 1 Foto groß
    links über beide Zeilen + 2 rechts übereinander (`.hg__grid`); ersetzt die früheren
    Einzelfolien „Ansicht Hinterhaus“ und „Garten“ (FB 3 / S1a / S1b)
19. Treppenhaus
20. Keller
21. Abschluss
→ Seitenzahl-Referenz Herten: 22 / 21 / 21 (v1.1).
→ **Haus-Fotos-Gate (TB5):** „Haus & Garten“ steht per Default HINTEN (direkt vor Treppenhaus/
  Keller). Ist das Haus außen der Hingucker, zieht André sie per Gate nach VORNE (direkt nach
  dem Titel) — gesteuert über `folien.folge` in objekt.json.
→ **Raum-Folien entfallen NIE, weil ihr Foto Titelmotiv ist** (v1.1, André 22.10.2026: „klar
  brauchen wir die Flurfolie“ — die v1-Regel „Flur entfällt bei Flur-Titel“ ist zurückgenommen;
  Dopplung Titelmotiv = Raum-Folie ist ausdrücklich ok, vgl. V1a). Fehlt ein Raum
  (z. B. keine Küche), entfällt die Folie; die Reihenfolge bleibt.
→ Entfallen seit v1: Einzelfolien „Ansicht Hinterhaus“/„Garten“, Sammelfolie „Außenansicht“,
  „Elektrik“-Folie, Steckdosen-Foto.

**Gebäude-Teil (für alle Wohnungen identisch — Ausnahme: Ø Vermietungsdauer auf der Mikrolage,
falls je Einheit abweichend, siehe Start-Gate 10):**
1. Titelseite (Variante A: Logo · „Exposé" · Adresse · Wohnungs-Nr.; Textblock OBEN,
   Logo-Oberkante ~28 mm; Titelfoto-Zone OHNE Umrandung, nur Mini-Marker — Foto wird gesetzt)
2. Makrolage / Stadt (`references/makrolage-stadt.md`)
3. Mikrolage / Standort (`references/mikrolage-standort.md`)
4. Gebäude-Eckdaten
5. Gebäude-Technik & Zustand (`references/gebaeude-technik-zustand.md`)

**Gebäude-Teil, optionale Standard-Folien (Foto-Folien, wohnungsübergreifend — Pflicht-FRAGE
bei jedem Objekt: „Vorhanden? Folie generieren?"):**
5b. Garten · Garagen · Stellplätze · Keller — nur wenn vorhanden UND André sie will;
    Foto zentriert im roomflow-Stil, Bild-Namenskonvention gilt (z. B. `Keller.HEIC`).
    Position: nach Gebäude-Technik & Zustand, vor dem Wohnungs-Teil.

**Wohnungs-Teil (je Einheit):**
6. Grundriss (kleiner Marker, André fügt Grundriss frei ein)
7. Angaben zur Wohnung (`references/wohnungsdaten.md`)
7a. **Stammdaten der Wohnung (Pflicht, jede Wohnung)** — siehe Abschnitt „Stammdaten der Wohnung".
7b. Immobilienbewertung (**nur auf Zuruf**, keine Pflicht-Frage mehr) — ImmoScout24-Bewertungs-Screenshot
    **1:1 im Original** als Bild, zentriert, `1pt`-Rule-Rand. Nur bauen, wenn André von sich aus einen
    Screenshot liefert; Werte NIE selbst recherchieren, NIE als HTML nachbauen. Screenshot ist UI-Bild:
    **KEIN Warm-Cozy**, keine Farbkorrektur, kein Zuschnitt. Namenskonvention:
    `Immobilienbewertung.png` im Objektordner (bzw. `Immobilienbewertung W<N>.png` je Einheit).
7c. Beispielsberechnung (optional) — Cashflow nach Steuer, zwei Spalten „Ohne Eigenkapital ·
    110-%-Finanzierung" / „Mit Eigenkapital · Käufer trägt Kaufnebenkosten"
    (`references/beispielsberechnung.md`). **Pflicht-FRAGE pro Wohnung:** „Beispielsberechnung
    mit aufnehmen — und mit welchem Grenzsteuersatz?" Ohne explizites Ja entfällt die Folie.
    Cashflow-Wert **grün (`#1F6B43`) wenn positiv, Oxblood wenn negativ**; alle Eingangswerte
    kommen von André (Werte-Gate in der Referenz), nie aus Schätzungen.
8. Raum-Folien: Wohnzimmer · Küche · Bad · Flur · Abstellkammer · Schlafzimmer 1–5 · Balkon
   (`references/raum-seiten.md` — leere Folien, KEINE Foto-Markierung; überzählige löscht André)
9. Abschluss (dunkle Schluss-Seite `.closing`, gebaut in der Ringlebstr.-Objektkopie —
   Master-Rückfluss offen, siehe Offene Punkte)

**Haus-&-Garten-Folie (v1, 21.10.2026 — ersetzt die Einzelfolien „Ansicht Hinterhaus“/„Garten“
vom 20.10. und die Sammelfolie „Außenansicht“ von 2026-10-19):** Alle Gebäude-Außenansichten
(Vorderseite, Rückseite, Garten …) kommen auf EINE Folie „Haus & Garten“, Layout A: 1 Foto groß
links über beide Zeilen + 2 rechts übereinander (`.hg__grid`, `object-fit:cover`, 1pt-Rule-Rand);
Position per Haus-Fotos-Gate (TB5). Zwei Fotos desselben Raums (z. B. Keller)
stehen nebeneinander auf EINER Seite (`.roomflow--2`, 8 mm Lücke) statt auf zwei Seiten.
Referenz: `tools/build_objekt.py` (Slot `hausgarten`).

## Stammdaten der Wohnung — EIN Exposé für Käufer und Bank (André-fixiert 2026-10-19)

Es gibt **genau ein Exposé je Wohnung**: `<objekt>/expose/EXPOSE_<Objekt>_<Einheit>.pdf`. Die Folie
**„Stammdaten der Wohnung"** gehört in **jedes** Exposé — keine getrennte Vertriebs-/Bank-Fassung bauen
(André: „Da brauchen wir nicht extra zwei anzufertigen").

- **Aufbau:** Folie **„Stammdaten der Wohnung"** direkt nach „Angaben zur Wohnung". Zweispaltig,
  Datalist-Zeilen, damit der Banker alles auf einen Blick hat:
  - *Grundbuch & Recht:* Grundbuch (AG · Blatt) · Flurstück (Gemarkung · Flur · Nr.) · Grundstück m² ·
    Miteigentumsanteil · Sondereigentum (Wohnung + Keller, Nr. lt. Aufteilungsplan) · Teilungserklärung
    (Datum + Ergänzungen) · Abteilung II · Baulasten (Auskunft-Datum) · Altlasten (Auskunft-Datum) · Erbbaurecht
    — **KEIN Eigentümer und KEINE Hausverwaltung** auf der Folie (André 2026-10-19)
  - *Wohnung & Bewirtschaftung:* Lage (nur Geschoss + Seite; Himmelsrichtung NIE abfragen — André
    2026-10-19) · Wohnfläche + Norm · Zimmer · Garage/Stellplatz · Baujahr · Mietverhältnis (seit ·
    Kündigung; bezugsfrei → „keines · bezugsfrei", keine Mietzeile) · Nettokaltmiete · Hausgeld als ZWEI
    Zeilen: „Hausgeld · 230 € / Monat" + „davon nicht umlagefähig · 137,51 € · davon Rücklage 94,28 €"
    (nicht umlagefähig inkl. Rücklage-Zuführung, André 2026-10-19)
  - **Anzahl Wohneinheiten** aus Hausgeldabrechnung/Wirtschaftsplan („Anz. Einheiten" beim Schlüssel
    Verwaltervergütung) bzw. Teilungserklärung ziehen, nie aus der Projektvorstellung (Herten: 8 → 7)
  - Quellenzeile darunter (mono, klein): Grundbuchabdruck-Datum · Teilungsaufstellung · Wohnflächen-
    berechnung · Wirtschaftsplan · Mietvertrag
- **Finanz-Regel:** Miete und Hausgeld stehen auf der Stammdaten-Folie (die Bank braucht sie).
  **Instandhaltungsrücklage sofern vorhanden IMMER angeben** — Stand auf Gebäude-Eckdaten bleibt drin,
  die monatliche Rücklage-Zuführung der Wohnung steht in der Hausgeld-Zeile (André 2026-10-19).
- **Baustellenfotos sind kein Exposé-Material:** „Renovierung …"-Ordner zeigen oft den Rohbau — Raum-Folien
  dann leer lassen; André liefert Fotos der fertigen Wohnungen (Herten 2026-10-19).
- **Abteilung III nicht aufführen** (die Bank sieht sie im Grundbuchauszug).
- **Quellen-Priorität:** Grundbuch (Bestandsverzeichnis/Abt. II) vor Teilungsaufstellung vor
  Mietvertrag. Garage nur, wenn sie im Grundbuch/der Teilungsaufstellung zur Einheit gehört
  (mitvermietete Garage im Mietvertrag ≠ Sondereigentum).
- **Bau:** HTML der Einheit per String-Replace mit Zähl-Assert aus dem jüngsten fertigen Exposé
  ableiten (`_build/build_<einheit>.py`), Stammdaten-Section im selben Skript erzeugen,
  Rest-Check (keine Fremd-Werte der Basis-Einheit) per Assert. Weitere Einheit eines fertigen Objekts:
  vorhandene Exposés nutzen, NICHT neu recherchieren und keine Fragen-Listen stellen — nur
  Einheitsspezifisches klären, Rest nach Empfehlung setzen und am Ende markieren (André 2026-10-19:
  „es gibt ja schon fertige Exposés").

**Master-Template:** `template/expose.html` + `template/expose.css` (alle Folien-Muster;
Varianten-Anhang am Dateiende = B-Versionen mit Foto, `.vartag`-Label nur in der Master-Vorschau).

## Start-Gates (Phase 0 — VOR dem Bauen abfragen)

**Frage-Format (bewährt Herten 2026-10-14):** Gates als EIN nummerierter Chat-Block, je Frage
Optionen a/b(/c), Empfehlung mit Kurzgrund markiert, Antwortbeispiel am Ende
(„Antwort kurz, z. B. „1a 2a 3: 15 4a 5a""). Kein AskUserQuestion-Fenster (verdeckt den Chat).
Werte, die im Ordner stehen, VORHER selbst ziehen und als Vorschlag zeigen — nicht abfragen.

**Ist-Stand-Checkliste VOR jeder Rückfrage (Pflicht, André 22.10.2026):** erst automatisch prüfen,
dann nur fragen, was danach wirklich fehlt — EINMAL, gebündelt, mit Empfehlung. Nie eine zweite Fragerunde.
1. Fertige Ausgaben im Objektordner: `EXPOSE_*.pdf` (Zeitstempel, Größe), `_build/objekt.json`, `korrekturen.md`.
2. Zielort `~/Downloads`: liegen die PDFs dort, Hash identisch zum Original?
3. Platzhalter im Übergabeprompt (`<VON ANDRÉ EINSETZEN>`): aus Ordner/Stand ableiten statt abfragen.
4. Kurzantwort von André (ein Wort, z. B. „Downloads") als Auftrag gegen den Stand deuten — nicht in
   die eigene Frage zwingen.
5. Auslieferung = PDFs nach `~/Downloads` kopieren + Hash-Vergleich, ohne Rückfrage.
Anlass: 22.10.2026 „Downloads" als Objektort missdeutet und doppelt gefragt, obwohl die fertigen
v1.1-PDFs im Ordner lagen.

1. **Objektordner + Anzahl Einheiten.** Weicht die Adresse vom Bestand ab (Herten: „Bahnhofstr. 3"
   statt Nr. 12 mit 3 Einheiten), mit a/b nachfragen statt raten.
2. **Datenquelle:** Weg 1 = Vertriebspipeline-Excel (Struktur daraus, Lücken aus Ordner) ·
   Weg 2 = autonomer Ordner-Voll-Scan. **Default Weg 2.**
3. **Marke/Firma:** aktuell HK RuhrInvest (Logo `brand/hk-ruhrinvest/`, Footer Leo Kadziela).
   **Kontakt-Mail im Exposé ist ausschließlich `immo@hk-immogroup.de`** (André-fixiert 2026-10-15,
   ersetzt lk@…) — Footer jeder Seite + Abschluss-Seite; Quelle `template/brand/hk-ruhrinvest/brand.json`.
   Multi-Firma über CSS-Variablen vorbereitet.
4. **Makrolage-Zuschnitt:** Stadt als Ganzes ODER Stadt + Stadtteil? (große Städte
   differenzieren, kleine als Ganzes — Details `references/makrolage-stadt.md`).
5. **Mikrolage-Zuschnitt:** Stadt / Stadt + Stadtteil / nur Stadtteil-Viertel-Bezirk?
   (Details `references/mikrolage-standort.md`).
6. **Foto-Fragen (je Datenseite):** „Hast du ein passendes Foto für diese Folie?" für
   Gebäude-Eckdaten, Gebäude-Technik & Zustand, Angaben zur Wohnung.
   Ja → **Variante B** (Daten ~40 % links, Foto-Zone rechts mit Mini-Marker) ·
   Nein → **Variante A** (Datenliste volle Breite). Nie beide.
7. **Titelmotiv-Gate (TB4, André 21.10.2026):** Das Titelbild wird IMMER so bestimmt — Kandidaten
   als Deckblatt-Muster zeigen (im Zuschnitt der Titelzone), André wählt. Faustregel: starke
   Außenaufnahme → Fassade aufs Deckblatt · sonst bestes Innenfoto der Einheit (Herten: Bad je
   Wohnung, zeigt die Renovierungsqualität). Nie selbst festlegen, nie ohne Muster fragen.
7b. **Haus-Fotos-Gate (TB5, André 21.10.2026):** je Objekt fragen, ob die Haus-Außenfotos nach
   VORNE (direkt nach dem Titel) oder nach HINTEN („Haus & Garten“ vor Treppenhaus/Keller)
   gehören: Haus außen stark → vorne · Innenfotos stärker → hinten. Steuert `folien.folge`.
7c. **Farbabgleich-Gate (TB6, André 21.10.2026):** a/b/c/d-Vorschau ÜBER DAS TITELBILD zeigen
   (`tools/titel_vorschau.py <foto> <out.png>`: a Original · b Gamma · c Clean #04 ·
   d Warm-Cozy #08). André wählt; das Rezept gilt für ALLE Titelbilder des Objekts
   (`fotos.titel_rezept` in objekt.json), alle übrigen Fotos bleiben Original.
8. **Stammdaten der Wohnung:** Werte selbst aus Grundbuch, Teilungsaufstellung, Wohnflächenberechnung,
   Wirtschaftsplan und Mietvertrag ziehen und als Vorschlag zeigen — nicht abfragen. Immobilienbewertung
   (7b) wird NICHT abgefragt (nur auf Zuruf).
9. **Beispielsberechnung (je Wohnung):** „Beispielsberechnung mit aufnehmen — und mit welchem
   Grenzsteuersatz?" Ja → Folie 7c nach den Stammdaten · Nein → Folie entfällt.
   Eingangswerte (Ziel-€/m², Zins, Tilgung, AfA, Gebäudeanteil, KNK-Satz, Hausgeld-Ansatz)
   IMMER bei André abfragen (`references/beispielsberechnung.md`).
10. **Ø Vermietungsdauer im PLZ-Gebiet:** mit Suchwerten fragen („PLZ <PLZ>, <N> Zimmer,
    <X> m²" — Zimmer/Wohnfläche aus Ordner/CRM vorher selbst ziehen), Details
    `references/mikrolage-standort.md`.
11. **Instandhaltungsrücklage:** Stand + Stichtag selbst aus der letzten Jahresabrechnung ziehen
    (Abschnitt Erhaltungsrücklage) und als Vorschlag zeigen. **Vorhanden → Zeile auf Gebäude-Eckdaten ·
    nicht vorhanden → Zeile entfällt**, keine Platzhalter, nichts schätzen. Eine bloße Zuführung aus dem
    Wirtschaftsplan ist kein Rücklagen-Stand.
12. **Gesprächsnotizen/Transkript** (Call mit Partner, Note-Taker): Exposé-relevante Fakten
    sofort herausziehen und als `<objekt>/expose/notizen.md` sichern — gegliedert „Alle
    Einheiten" · Tabelle „Je Wohnung" · „Haus/WEG" · „Nicht fürs Exposé" — und von André
    bestätigen lassen. Nicht-Exposé-Themen (Schimmel, Interna) nur nach Rückfrage verwerten.
    Gilt auch mitten im Ablauf: sobald André ein Transkript oder Gesprächsnotizen schickt,
    zuerst `notizen.md` bauen und bestätigen lassen, dann weiter im laufenden Block. Bestätigte
    Fakten fließen in die Feldkataloge (Eckdaten/Technik/Wohnung) mit Quelle „Call <Datum>".

## Kontaktbogen-Gate (TB8, Pflicht VOR JEDEM Render — André 21.10.2026: „unser neuer Skill-Standard“)

VOR jedem Rendern je Exposé einen Kontaktbogen zeigen
(`python tools/contact_plan.py <objekt.json> --out <scratch>`): Folien-Nr. + Titel + Reihenfolge +
zugeordnete Fotos als Thumbnails. Dann EINE Frage: **passt / passt nicht / anders?**
- „passt“ → bauen.
- „passt nicht“ → je beanstandeter Folie gezielt fragen, Andrés Bildwahl in objekt.json einbauen,
  NEUEN Bogen zeigen → Loop, bis „passt“ kommt. Erst dann rendern.
- „anders“ (anderes Vorgehen/Material) → klären, objekt.json anpassen, neuer Bogen.
Gilt auch für Re-Renders nach Korrekturen und für einzelne neue Einheiten. Bei Bildwahl-Fragen
(z. B. Eckdaten-Foto) Kandidaten im Format des Bildfelds zeigen. Ersetzt den früheren losen
Vorschau-Absatz unter „Gelernte Regeln“.

## Objekt-Konfiguration: objekt.json + generische Tools (TB1, 21.10.2026)

Jedes Objekt wird über EINE Datei `<objekt>/expose/_build/objekt.json` beschrieben — ohne Code
änderbar, kein Objekt-Sonderskript mehr. Referenz-Instanz: Herten
`<Herten>/expose/_build/objekt.json`. Inhalt:
- `objekt`: Name, Adresse, Titel-Prefix, Firma, Kontaktzeile
- `fotos`: `orig_dir` (Fotografen-Originale) + Dateimuster, `max_px` (3500), `titel_rezept`
  (aus dem Farbabgleich-Gate), `std` (Name → Foto-Nr. für objektweite Fotos), `extra`
  (Sonderquellen, z. B. Chat-Kopie), `titel` + `units` (Foto-Nrn. je Einheit)
- `folien`: `folge` (Folien-Reihenfolge inkl. Haus-Fotos-Gate-Position), `base_slides`
  (Slot → h2-Titel der base-HTML), `datenfolien_fotos`, `wohnsplit_foto`, `ausstattung`,
  `hausgarten`, `treppenhaus`
- `units`: je Einheit Label, base-HTML, PDF-Name, Soll-Seitenzahl, Grundriss, Räume
  (Titel + Fotonummern + optional Modifikator wie `eng`), Stammdaten (left/right/sources)
- `replace`: objektspezifische Text-Korrekturen (old/new, Zähl-Assert)
- `soll`: Font, Accent, Abschluss-Titel, Firmen-/Kontakt-Marker, Pflicht-/Verbots-Texte,
  verbotene Folientitel, optional Icon-Soll

Generische Tools (`tools/`):
- `prep_objekt_images.py <objekt.json> [--out]` — Bilder aus den Originalen (3500 px, q95,
  subsampling 0, ICC bleibt; NUR das Titelbild mit Rezept, alles andere Original)
- `build_objekt.py <objekt.json> [--out <dir>] [--units a,b]` — ein `expose_<einheit>.html`
  je Einheit aus base-HTML + objekt.json (Calibri-CSS, Fußzeile, Folienfolge, Stammdaten-Folie,
  Haus & Garten, Asserts gegen die Soll-Werte). Der Zielordner braucht `img/`, `brand/` und
  die vom base-`<link>` geladene `expose.css` daneben (Assert prüft das)
- `render_pdf.py` je Einheit (wie gehabt, neuer Dateiname je Iteration)
- `check_objekt.py <objekt.json> [--pdf-dir] [--img-dir] [--ref-dir]` — Abnahme-Tabelle
  PASS/FAIL je PDF (Pflicht nach jedem Lauf; `--ref-dir` = Folientitel-Vergleich gegen
  Referenz-PDFs)
- `contact_plan.py <objekt.json> --out <dir>` — Kontaktbogen fürs TB8-Gate
- `titel_vorschau.py <foto> <out.png>` — a/b/c/d-Montage fürs TB6-Gate
Die base-HTML je Einheit (`units.<e>.base`) trägt die freigegebenen Datenfolien (Titel, Makro,
Mikro, Eckdaten, Technik, Angaben, Grundriss, Keller, Abschluss); alle weiteren Folien baut
`build_objekt.py` aus objekt.json.

## Fragesparring — Standard-Korrekturmodus (André-fixiert 2026-07-31)

**Erst sammeln, dann sparren — nie alles auf einmal in den Chat.**

1. **Sammeln:** die komplette Ausarbeitung ALLER Blöcke erzeugen (Recherche + Feldkataloge),
   ohne zwischendurch Korrekturen einzufordern.
2. **Block für Block:** Block = eine Folie bzw. eine Ausarbeitung (Makrolage, Mikrolage,
   Gebäude-Eckdaten, Technik & Zustand, Wohnungsdaten, Beispielsberechnung …), abgearbeitet
   in Folien-Reihenfolge. Pro Block: kompakt zeigen → **3–5 gezielte Fragen** (Unklarheiten,
   Streichkandidaten, fehlende Werte/`[OFFEN]`) → André antwortet kurz → einarbeiten →
   ggf. weitere Runde → explizite Block-Freigabe durch André.
   Vor JEDEM Frage-Paket drei Teile zeigen: **Entwurf** (so käme es aufs Blatt) ·
   **„Bewusst weggelassen"** (je Punkt mit Grund, z. B. „ohne belegte Zahl", „Werk im Verkauf") ·
   **„Noch unsicher"** (Wert + warum, z. B. „nur Stellenanzeige als Quelle", „Halt nicht in OSM").
   Fragen-Format immer: EIN nummerierter Chat-Block, je Frage Optionen a/b(/c), Empfehlung mit
   Kurzgrund markiert, Antwortbeispiel am Ende („Antwort kurz, z. B. 1b 2a 3a 4a"). Kein
   AskUserQuestion-Fenster.
3. **Feldkatalog immer komplett zeigen (Nachdenkstütze):** bei jeder Datenfolie die VOLLE
   Feldliste der Referenz aufführen (Gebäudetechnik alles, Wohnung alles); Unbefülltes bleibt
   sichtbar als leer/`[OFFEN]`/unverifiziert stehen — nie stillschweigend weglassen, André
   reicht Vergessenes nach.
4. **Speichern:** freigegebenen Block sofort in `<objekt>/expose/ausarbeitung.md`
   fortschreiben (ein Abschnitt pro Block, Status + Datum, Quellen + Stichtag), dann erst
   der nächste Block. Recherche-Rohdaten stehen dort schon vorher je Runde mit Status
   „gesammelt, nicht freigegeben".
5. **Reihenfolge groß:** ALLE Text-Blöcke fertig → Bilderauswahl → zusammenbauen (HTML +
   Render) → Korrektursparring am gebauten Stand, **paketweise** (Korrekturen sammeln →
   alles einarbeiten → neu bauen → nächste Runde).

**Verboten:** die komplette Ausarbeitung als Korrektur-Monolith in den Chat kippen, 17 Seiten
auf einmal zeigen oder von André ein Sammel-Korrekturdokument verlangen.

## Workflow

### Phase 1 — Daten + Ausarbeitungen
- Ordner scannen/lesen: `pdf_text.py` (Text-PDFs), `raster_check.py`+Read (Scans),
  `dump_xlsx.py` (Excel). Read-Tool kann keine PDFs — immer über die Tools.
- **Makro + Mikro parallel per Subagent** recherchieren (Vorlagen
  `references/standort-recherche-prompts.md`), vorher belegte Regionsfakten aus
  `references/standort-fakten-register.md` übernehmen; Rohdaten sofort in `ausarbeitung.md`,
  neu belegte Fakten danach ins Register.
- **Makrolage = Vermietungs-Argumente, nicht Stadtmarketing:** Groß-Arbeitgeber mit belegter
  Beschäftigtenzahl im ~30-Autominuten-Radius, Hochschulen mit Studierendenzahl, Region,
  Routing-Fahrzeiten, News + Negativ-Check — von Anfang an in voller Tiefe
  (`references/makrolage-stadt.md`). Dann Block im Fragesparring → Kurztext → sichern.
- **Mikrolage:** Standortausarbeitung im ~2-km-Radius (POI-Katalog, Nominatim/Overpass/OSRM,
  neue Bahn-Halte prüfen) → Block im Fragesparring → sichern. POI-Darstellung generisch ohne
  Namen (Regeln in der Referenz).
- **Ø Vermietungsdauer** = André-Fixwert, Pflicht-Zeile Mikrolage (Start-Gate 10). Zusätzlich
  Immometrica-/ohne-makler-Screenshot als Call-Material anbieten (nicht ins Exposé).
- Gebäude-/Wohnungsdaten nach Feldkatalogen befüllen; Lücke = `[OFFEN]`, nie raten.

### Phase 2 — Folie für Folie (TEXT zuerst, dann gießen — essenziell)
- Objekt-Kopie des Templates anlegen (`<objekt>/expose/`), Master bleibt sauber.
- **Content-first ist Pflicht:** Pro Folie ZUERST ein **nummerierter Text-Entwurf im Chat**
  (VOLLER Feldkatalog der Referenz + Werte + Quellen, Lücke = `[OFFEN]`). Korrektur läuft im
  **Fragesparring** (Standard-Abschnitt oben): Block zeigen + Frage-Paket, André antwortet
  kurz. Freigabe bleibt Wert für Wert, keine Pauschal-Freigaben, auch nicht bei „mach alles".
  **KEIN HTML anfassen, solange der Text nicht freigegeben ist** — kein HTML-Ping-Pong.
- Beim Text-Durchgang wird gecuttet: alles Vorhandene zeigen, André entscheidet was draufbleibt.
- **Erst nach Text-Freigabe** die Folie in HTML gießen und EINMAL druckgenau rendern
  (`render_pdf.py` → `raster_check.py` → PNG zeigen) → Design-Gate. Layout-Korrekturen
  betreffen dann nur noch Optik, nie Inhalt.
- Live-Preview (`python -m http.server 8791 --directory <template-kopie>` → Browser-Pane)
  nur für Layout-Feinschliff nach dem Gießen.

### Phase 3 — Render pro Wohnung (Zwei-Chat-Workflow seit 2026-07)
- **Chat 1 (Aufbau):** ALLE Folien des Pilot-Exposés zu Ende bauen (Gebäude-Teil inkl.
  Standard-Folien + kompletter Wohnungs-Teil) = grober Entwurf steht. Dann **Übergabeprompt**
  schreiben (Objektpfad, Einheiten-Liste, Datenstand, offene Punkte, Regenerier-Logik) —
  **`<objekt>/expose/ausarbeitung.md` ist Pflicht-Bestandteil** (freigegebene Blöcke = Datenstand).
- **Chat 2 (Massenproduktion):** mit dem Übergabeprompt frisch starten, dann **Wohnung für
  Wohnung** die Einheiten-Liste von oben nach unten durchgenerieren. ALLE fertigen PDFs in
  EINEN Ordner (`<objekt>/expose/`).
- **Globale Änderungen** (betreffen alle Exposés, egal ob in Chat 1 oder nachträglich):
  in die Basis (`expose.html`) einbauen und **einen Agenten spawnen, der parallel läuft**
  und die Änderung in alle bereits generierten Varianten/PDFs einpflegt, während der
  Haupt-Chat weiterarbeitet.
- Loop über Einheiten: Gebäude-Teil (shared) + Wohnungs-Teil (je Einheit) → **ein PDF je
  Wohnung** inkl. Stammdaten-Folie (siehe „Stammdaten der Wohnung"), Dateiname je Wohnung.
- Befehle:
  ```
  python tools/render_pdf.py <objekt>/expose/expose.html -o <objekt>/expose/EXPOSE_<Objekt>_W<N>.pdf
  python tools/raster_check.py <PDF> --out <scratch>/pages --dpi 150
  ```
- Vorschauen nur nach `_scratch/` (gitignored), nie in den OneDrive-Objektordner.

### Phase 4 — Auto-Foto-Test (Pflicht am Ende des ersten Laufs)
Details `references/raum-seiten.md`: André legt Fotos benannt pro Raum ab → Skill setzt sie
testweise automatisch (richtige Folie, ~16 mm Ränder, 8 mm Lücke, 1/2/3-Foto-Raster,
zentriert) → PNGs zeigen → André bewertet. Gut = wird Standard · schlecht = verworfen,
André fügt Fotos weiter manuell ein (PDF-Editor/PowerPoint), Folien bleiben leer.

## Design-Standard (Querformat)

- A4 quer, `.page` = 297×210 mm, `@page{size:A4 landscape}`.
- **Schrift: Calibri als EINZIGE Familie** (TB7/T1, André 21.10.2026: „immer Calibri nutzen“) —
  Headlines „Calibri Light“, Body/Werte/Labels Calibri; KEINE Ersatzschrift (kein Kunstfett
  fürs Fett, kein Courier-Punkt: `.ey::before` ist ein CSS-Kreis, Calibri hat kein ●-Glyph).
  PDF-Abnahme: genau 1 Schriftfamilie. Nur eine belegte Haus-CI-Schrift (offener Punkt X2)
  ersetzt Calibri (`soll.font` in objekt.json).
- Farben: Creme `#F4F1EA` · Anthrazit `#1E1A16` · Oxblood `#7C1D2A` · Muted `#6E6557`.
- Jede Inhaltsseite: Running Head (Logo + Adresse · Wohnung) · Headline + roter Unterstrich
  (`.h2rule`) · Brand-Footer · Wasserzeichen (`.page::before`, 4 % — bleibt auch auf Foto-Folien).
- **Fußzeile Inhaltsseiten: NUR die Kontaktzeile** („Leo Kadziela · immo@hk-immogroup.de“);
  Firmenname + Firmenadresse stehen NUR auf der Abschluss-Seite (F1/FB 4, André 21.10.2026 —
  die Objektadresse in der Kopfzeile ist relevanter). Abnahme: Firmen-Marker genau 1× im PDF.
- Icon-Listen: Line-Icons (inline-SVG, `stroke=currentColor`) in Oxblood, Label (mono) über
  Wert (Serif). Energieausweis: Vollbreiten-Zeile + Mini-Farbskala + Ausstellungsdatum
  direkt unter der Skala (`.energrow__scale` > `.escale--mini` + `.energrow__date`,
  mono 6,5 pt muted) — nur auf der Technik-Seite.

## Feld-Regeln (verbindlich)

- **Adresse** immer `Straße Nr · PLZ Stadt` — Stadtteil raus (Straße ggf. „Str." kürzen nur
  für Portale, nicht hier).
- **Erbbaurecht** immer als Feld, Wert „Nein" (sofern zutreffend).
- **Gewerbeeinheiten** immer sichtbar auf Gebäude-Eckdaten.
- **Aufzug** ist **Pflichtfeld auf Gebäude-Eckdaten** (André-fixiert 2026-08-07) — immer
  sichtbar mit Wert „Ja" / „Nein", auch wenn keiner vorhanden ist. Nicht mehr auf der
  Technik-Seite (kein Duplikat).
- **Instandhaltungsrücklage** auf Gebäude-Eckdaten **nur wenn vorhanden** (Stand + Stichtag belegt,
  Start-Gate 11), sonst Zeile entfernen (Regex-Muster: `build_eg_mitte.py`).
- **Energieausweis nur auf der Technik-Seite** (kein Duplikat auf Eckdaten) — inkl.
  **Ausstellungsdatum als Pflicht-Zeile unter der Farbskala** („Ausgestellt am · TT.MM.JJJJ",
  André-fixiert 2026-08-07). Datum aus dem Energieausweis-PDF ziehen; fehlt es, `[OFFEN]`
  setzen und bei André nachfragen — nie schätzen, nie weglassen.
- Eine Zeile pro Bauteil: WAS + WANN kombiniert („Dach · Satteldach · Ziegel · 2008").
- **Ø Vermietungsdauer im PLZ-Gebiet** — **Pflicht-Zeile auf der Mikrolage-Folie**
  (Folientext „Vermietet in Ø X Tagen · <N>-Zimmer-Wohnungen, PLZ <PLZ>"). Wert ist ein Fixwert von André
  (Quelle: ohne-makler) — **IMMER bei André abfragen**, nie selbst recherchieren, nie
  raten, nie weglassen ohne Rückfrage. (Ausnahme zur Finanz-Regel: das ist keine
  Miet-/Preisangabe, sondern der Nachfrage-Beweis.)

## Wording-Leitplanken

`references/wording-leitplanken.md` ist hart: keine Garantien, kein „sicher"/„steuerfrei",
IST ≠ SOLL, jede Marktzahl in Ausarbeitungen mit Quelle + Stichtag. Auf den Folien selbst
stehen keine Miet-/Preis-Marktzahlen (siehe Finanz-Regel oben; Ausnahme: Ø Vermietungsdauer
im PLZ-Gebiet als Nachfrage-Beweis auf der Mikrolage) — Kennzahlen der Makrolage (Einwohner,
Arbeitsplätze, Studierende) gerundet, in der Ausarbeitung belegt.

## Gelernte Regeln

- **Foto-Freiheit ist André heilig:** Raum-Folien und Grundriss ohne jede Foto-Markierung
  bzw. nur Mini-Marker — er platziert 1–3 Fotos frei im PDF-Editor. Feste Foto-Boxen nur
  in Variante B der Datenseiten, dort Mini-Marker statt großer Platzhalter.
- **`render_pdf.py` überschreibt gesperrte PDFs nicht** (Chrome scheitert leise, alte PDF
  bleibt liegen → stale Render). Wenn die Ziel-PDF offen/gesperrt ist: neuen Dateinamen
  nehmen oder Viewer schließen; Seitenzahl nach jedem Render mit PyMuPDF gegenprüfen.
- **PDFs lesen** über `pdf_text.py` / `raster_check.py` (Read-Tool hat kein pdftoppm).
  **xlsx** über `dump_xlsx.py` (ggf. Kopie ziehen, falls in Excel gesperrt).
- **Fotos: KEIN Warm-Cozy, keine Farbkorrektur** (André 2026-10-19: „nicht warmweiß, kein Cosi" —
  gilt für alle Exposés). Bilder nur exif-transponieren (HEIC → JPG) und unverändert setzen.
  EINZIGE Ausnahme: die Titelbilder — ihr Rezept wählt André am Farbabgleich-Gate (TB6:
  Original / Gamma / Clean #04 / Warm-Cozy #08; Herten 21.10.2026: Clean für alle 3 Bad-Titel);
  `prep_objekt_images.py` wendet es über `warm_cozy_photos.py --profile <rezept>` automatisch an.
  **Stürzende Linien: KEIN Pauschalwert** — Keystone wird PRO BILD
  gesetzt (`--keystone <+/-N>`, Default 0=aus, +unten/−oben verbreitern), nachdem das Bild
  angeschaut wurde; frontale/gerade Motive bleiben bei 0.
  (`prep_image.py`/`enhance_photo.py` = Alt-Weg, nur falls `magick` fehlt.)
- **Pixel-genaue Positionsprüfung** bei Layout-Feinheiten per JS-Messung im Browser-Pane
  (`getBoundingClientRect`) — so wurde die Energieausweis-Zentrierung exakt getroffen.
- **Python-Prints ASCII halten** (Windows cp1252) oder `PYTHONUTF8=1`.
- **Grundriss je Wohnungslage prüfen, nie einen Plan für alle Einheiten übernehmen**
  (Ringlebstr. 2026-10): Ein Muster-Grundriss gilt nur für die Lage, die er zeigt. Gegenüberliegende
  Wohnung (rechts ↔ links) = horizontal gespiegelt, Beschriftung ungespiegelt neu setzen
  (`<objekt>/expose/_build/mirror.py`); anderer Gebäudeflügel = eigener Schnitt (Bauplan +
  Wohnflächenberechnung + Teilungsaufstellung gegenlesen, auch die Zimmerzahl). Lage aus der
  Teilungsaufstellung (Himmelsrichtung) ↔ Vertriebsbezeichnung vor dem Bauen zuordnen.
- **Weitere Einheit eines fertigen Objekts:** HTML aus dem jüngsten Einheiten-Exposé per
  String-Replace mit Zähl-Assert ableiten (`<objekt>/expose/_build/build_<einheit>.py`), nur
  Einheitsspezifisches (Lage, Status, Zustand, Fotos, Garage) tauschen; Folien ohne Foto weglassen.
- **Einzelne Folien in fertigen PDFs tauschen:** `<Ringlebstr.>/expose/_build/splice_pages.py`
  (Zuordnung über die Folien-Überschrift, alle anderen Seiten textgleich geprüft, Inhalts-Check
  per `lower()`, schreibt über `.neu.pdf` + `os.replace`). Vorher Backup-Ordner anlegen.
- **Übergabeprompt ≠ Auftrag ohne Rückfrage:** Nennt ein eingefügter Übergabeprompt mehrere
  Einheiten/Korrekturen, vor dem ersten Schreibschritt in einem Satz bestätigen lassen, welche
  Einheit(en) André wirklich braucht (Ringlebstr. 2026-10-11: Prompt nannte 3 Bestands-Exposés,
  gebraucht wurde 2. OG rechts).
- **Makrolage verkauft die Vermietbarkeit, kein Stadtmarketing** (Herten 2026-10-15):
  Makro-Runde 1 mit Stadtprofil (Einwohner + „Kreis X", Schlösser, Observatorium,
  Wasserstoff-Kompetenzzentrum) fiel komplett durch; erst 30-Min-Radius mit Beschäftigten-/
  Studierendenzahlen, Routing-Fahrzeiten und News traf. Regeln + Muster-Entwurf + Frage-Paket in
  `references/makrolage-stadt.md`, Recherche-Prompts (im Probelauf Gladbeck technisch geprüft)
  in `references/standort-recherche-prompts.md`, belegte Regionsfakten in
  `references/standort-fakten-register.md`. Regionalzahlen nie auf einen Radius umdeuten
  (ehrliche Alternative vorschlagen). Mikrolage: Umfeld/Sehenswürdigkeiten in Gehweite bleiben
  als Lebensqualitäts-POI erlaubt.
- **Fotos, die André in den Chat einfügt, sind Exposé-Material** (nicht nur Info): sie aus dem
  Session-Protokoll `~/.claude/projects/<projekt>/<session>.jsonl` holen — mitten in einer Antwort
  eingefügte Bilder stecken in Zeilen `type: "attachment"` (queued_command) als `image`-Blöcke mit
  base64 → dekodieren, dann wie jedes Foto setzen (ohne Farbänderung). Nie neu anfordern
  (Ringlebstr. EG mitte 2026-10-19). Chat-Bilder kommen nur mit ~2000 px an → das Original des
  Fotografen im Drive suchen (per Bildvergleich zuordnen, Herten: Leos Ordner „Divers“) und das einbauen.
- **Bildqualität = Original** (Herten 2026-10-20, André: „im Original war die Qualität hoch“): Fotografen-
  Originale (Herten 8192 × 5464 px, sRGB) auf max. 3500 px lange Seite, JPEG-Qualität 95, `subsampling=0`,
  ICC-Profil mitgeben — NIE auf 2000 px verkleinern/neu komprimieren. Prüfen: Bild aus dem PDF ziehen
  (PyMuPDF) → Auflösung + Helligkeit gegen das Original messen (muss identisch sein). PDFs werden dadurch
  ~60 MB groß — Qualität geht vor. Referenz: `<Herten>/expose/_build/prep_images.py` + `build.py`.
- **Bildzuordnung läuft über das Kontaktbogen-Gate (TB8)** — siehe eigener Abschnitt oben
  (passt / passt nicht / anders-Loop, Pflicht vor jedem Render).
- **Notizen-Modus:** sagt André „nur Notizen sammeln“, NICHTS bauen — Punkte in `<objekt>/expose/
  korrekturen.md` sammeln, am Ende sortiert (Regeln · Folienfolge · Räume je Wohnung) zeigen und offene
  Fragen gebündelt stellen. Raumfotos ohne klare Raumzuordnung als „Zimmer 1 / Zimmer 2“ beschriften.
- **„Angaben zur Wohnung“ (Herten 2026-10-20):** Spaltenkopf heißt „Eckdaten“ (nie „Die Wohnung“ —
  Fachbegriff); „Eckdaten“ und „Ausstattung & Zustand“ links ÜBEREINANDER, rechts ein Foto über die volle
  Höhe (Herten: Durchlauferhitzer). CSS `.wohnsplit` in `<Herten>/expose/_build/build.py`.
- **Ausstattungs-Folien vor den Raum-Folien** (Herten 2026-10-20, für alle Einheiten gleich): „Fenster und
  Türen“ (beides auf einer Folie) → „Heizung“ → „Sanitär“; Stromkasten-Foto auf „Gebäude-Technik & Zustand“,
  keine eigene Elektrik-Folie, keine Steckdose. Hausflur = eigene Folie „Treppenhaus“, „Flur“ zeigt nur den
  Wohnungsflur (ein großes Bild). Position aller Folien: Standard-Folienfolge oben (Treppenhaus + Keller am Ende).
- **Nach dem Bauen unabhängig prüfen** (Workflow: je Einheit ein Prüfer + ein Layout-Prüfer gegen die
  Vorgabe). Typische Funde Herten: Eckdaten-Liste (13 Zeilen) lief in die Fußlinie → `.splitflow--dicht
  .iconrow` Padding 0,85 mm; verwaiste Einheit „m²“ → `&nbsp;`; Fotopaare 1 pt versetzt → `aspect-ratio:3/2`.
- **Kein persönlicher Kontakt an Dritt-Dienste:** Nominatim/OSRM/Overpass mit User-Agent
  `expose-builder/1.0`, nie mit Andrés Mail-Adresse (Probelauf Gladbeck 2026-10-15 hatte sie
  im User-Agent).

### Layout-Standard seit Ringlebstr. 25 (2026-07, André-fixiert — Referenz-Implementierung: `<Ringlebstr.-Objektordner>/expose/expose.html`)

- **Makrolage-Folie OHNE Kennzahl-Kacheln:** Bild links (~118 mm breit · 127 mm hoch,
  `background:center/cover`), rechts Kurztext (1–2 Sätze, max ~3) + **einzeilige Icon-Liste
  im Mikro-Stil** — KEINE Mono-Überschriften über den Zeilen, Fakt direkt in die Zeile
  („Chemiepark Marl · rund 10.000 Arbeitsplätze"; Inhalt/Auswahl: Vermietungs-Argumente laut
  `references/makrolage-stadt.md`, kein Stadtmarketing). `.macrolist`: cityfact-Zeilen mit
  border-bottom, Schrift 10,5 pt, Icons 6 mm. **Text startet bündig mit der Bildoberkante**
  (`.macrogrid{align-items:start}`).
- **Mikrolage-POIs einzeilig ohne Label-Überbegriffe:** nur „Was · ca. X m" (kein
  ÖPNV/EINKAUF-Label darüber), thematisch gruppiert (Alltag → Kita/Schulen aufsteigend →
  Altstadt/Umfeld → Bahnhof/Autobahn → Klinik), Fahrzeiten einheitlich „Autominuten",
  Distanzen mit `&nbsp;` gebunden (nie „ca. / 200 m" umbrechen).
- **Bild-Rand-Standard:** JEDES vom Skill gesetzte Bild bekommt einen feinen Rand
  `border:1pt solid var(--rule)` (Rule-Ton #D8D0C1) — Titelbild, Makro-Motiv, Mikro-Karte,
  Datenseiten-Fotos (Variante B) und Raum-Fotos. Gilt, sobald ein Bild eingesetzt ist;
  leere Platzhalter/Foto-Zonen bleiben wie gehabt.
- **Foto-Konvention: Bilder heißen wie die Folie.** André legt sie im Objektordner ab
  (z. B. `Titel`, `Makro`, `Mikro`, `Gebäude-Eckdaten`, `Gebäude-Eckdaten Zustand` — auch
  HEIC). Skill sucht nach Folien-Namen und zieht **GENAU diese** ausgewählten Dateien
  unverändert (nur exif-Transpose/HEIC→JPG, KEIN Grade) nach `expose/img/` — **kein
  Ordner-Sweep**. Objektweite Standard-Fotos (gleiche Ausstattung in allen Einheiten) nach
  `expose/img/std/` und per `_build/build_photos.py` in alle Einheiten (Herten 2026-10-19:
  Außenansicht · Keller · Innentüren · Heizung · Elektrik · Fenster · Sanitär vor den Raum-Folien).
  **Stürzende Linien werden PRO BILD beurteilt**
  (jede Aufnahme kippt anders): kippt ein Bild sichtbar, `--keystone <+/-N>` für GENAU dieses
  Bild setzen (Vorzeichen = Richtung, Betrag = Stärke), sonst 0 lassen. Kein fester Keystone
  über alle Bilder. Keine eigene Bildauswahl, wenn benannte Dateien existieren.
- **Foto-Platzierung Datenseiten (Variante B), „symmetrisch bündig":** Bild füllt die
  Foto-Zone absolut (`.splitflow--foto .fotozone{position:relative;overflow:hidden}`,
  `img{position:absolute;inset:0;object-fit:cover}`), Datenzeilen mit
  `justify-content:space-between` über die volle Höhe → Bildober-/-unterkante schließen
  exakt mit erster/letzter Textzeile ab. `.splitflow--foto{margin-bottom:7mm}` + letzte
  Zeile ohne border-bottom, damit nichts über die Footer-Linie läuft. NIE `display:block`
  mit natürlicher Bildhöhe (sprengt die Seite).
- **Titelseite:** Foto-Zone breit — Cover-Grid `82mm/5mm Gap` (Textspalte schmal,
  `.cover__wohn` dann 22 pt), Titelbild als `background:center/cover` über die volle Zone;
  Claim-Zeile klein-kursiv unter dem „Exposé"-Titel (`.cover__claim`).
- **Wohnungsdaten-Block groß:** Variante B mit `.splitflow--wohn` — Datenspalte 120 mm,
  Werte 12,5 pt, Zeilen-Padding 3 mm.
- **Abschluss-Seite (dunkel) steht als `.closing`** in der Ringlebstr.-Objektkopie:
  Eyebrow „Haltung" + Zitat (Serif 24 pt) + Kontakt Leo + „Alle Angaben ohne Gewähr." +
  weißes Logo; Wasserzeichen mit `logo-white.png`.
- **Pro-Wohnung-Varianten per String-Replace** aus der Pilot-HTML (Wohnungs-Nr., Wohnfläche,
  Garage ersetzen → `expose_<einheit>.html`), dann je Datei rendern und Seitenzahl mit
  PyMuPDF gegenprüfen.
- **Scratchpad-Pfadlimit (Windows):** Unterordner-Namen im Session-Scratchpad kurz halten
  (~11 Zeichen), sonst WinError 206 bei `raster_check.py`.

## Offene Punkte (Roadmap)

- **Master-Rückfluss ausstehend:** Die Ringlebstr.-Neuerungen (`.macrolist`-Makro ohne
  Kacheln, einzeilige POIs, `.splitflow--foto`, `.splitflow--wohn`, `.cover__claim`,
  breite Cover-Foto-Zone, `.closing`-Abschluss-Seite) leben bisher nur in der Objekt-Kopie —
  in `template/expose.html` + `expose.css` übernehmen. Zusätzlich Inhalts-Stand Herten
  2026-10-15: Makro-Platzhalter „Stadt-Motiv / Landmark" → „Bildmotiv zur Vermietungs-Story",
  Kacheln + „Bekannt für"-Zeile + Krankenhaus-Betten-Kachel raus, Beispielzeilen auf
  Arbeitgeber/Hochschulen/Anbindung umstellen; Mikro-POI-Raster um Pflicht-Zeile
  „Vermietet in Ø [ wird abgefragt ] Tagen · <N>-Zimmer-Wohnungen, PLZ <PLZ>" ergänzen.
- **Abschluss-Seite** (schwarz): in der Ringlebstr.-Objektkopie gebaut (`.closing`), noch nicht im Master.
- **`build_expose.py`** ist noch Hochformat/`entwurf.json` und damit Alt-Bestand — der
  Querformat-Weg läuft seit TB1 über `objekt.json` + `build_objekt.py` (siehe Abschnitt
  „Objekt-Konfiguration“). Offen bleibt nur der Schritt, auch die base-HTML der Datenfolien
  generisch aus dem Master-Template zu erzeugen (heute: Objekt-Kopie des Templates befüllen).
- Alte Hochformat-References/Docs wurden 2026-07-26 gelöscht (git-Historie hat sie) —
  maßgeblich sind: makrolage-stadt · mikrolage-standort · standort-recherche-prompts ·
  standort-fakten-register ·
  wohnungsdaten · raum-seiten · gebaeude-technik-zustand · wording-leitplanken ·
  beispielsberechnung.

## Constraints

- Kein PowerPoint als Erzeugungsweg, kein WeasyPrint (kaputt) — PDF nur via Headless-Chromium.
- Code Englisch, User-facing Deutsch. Keine Code-Kommentare außer nicht-offensichtlichem WHY.
- Keine Erfindungen — `[OFFEN]` statt raten. Gates ernst nehmen, auch bei „mach alles".
- Master-Template bleibt sauber; Verbesserungen am Objekt fließen ins globale `template/` zurück.

## Stil / Sparring mit André

- Direkt, kurz, Bullet Points. Folie für Folie, Feld für Feld — aber nicht mit unnötigen
  Auswahlfragen nerven. Fragen als Chat-Text mit Optionen a/b/c und markierter Empfehlung
  (auch Start-Gates), kein AskUserQuestion-Fenster.
- Korrekturen IMMER im Block-Fragesparring (Standard-Abschnitt oben): ich stelle die Fragen,
  André gibt kurze Antworten — nie lange Texte am Stück zum Abarbeiten geben.
- „festzurren"/„speichern" = commit + push auf main. Commit-Message Englisch,
  KEINE Co-Authored-By-Zeile.
