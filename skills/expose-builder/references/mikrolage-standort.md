# Referenz: Seite „Mikrolage / Standort" (POI-Katalog + Prozess)

Gehört zum Gebäude-Teil. Position im Verkaufsbogen: **nach Makrolage, vor Gebäude-Eckdaten**
(Trichter Stadt → Umgebung → Gebäude → Wohnung). Layout in `template/expose.html`:
Karten-Platzhalter links (`.mapph`, ~100 mm — Karten-Screenshot mit Pin als
`background:center/cover`), rechts dichte 2-Spalten-POI-Liste (`.poigrid`/`.poirow`,
12 Slots, max. ~14 inkl. Vermietungsdauer-Zeile; bei 13 Zeilen `grid-template-rows:repeat(7,auto)`), Lead-Satz unter
der Headline (`.leadline`).

**POI-Zeilen-Format (André-fixiert seit Ringlebstr. 25, 2026-07):** einzeilig OHNE
Label-Überbegriff — nur „Was · ca. X m" („Zentrum / Fußgängerzone · ca. 550 m"), Icon davor.
Thematisch gruppiert: Alltag (Bus, Apotheke, Einkauf, Zentrum) → Bildung aufsteigend
(Kita → Grundschule → Sekundarschule → Gymnasium) → Umfeld (Altstadt, Naherholung) →
Mobilität (Bahnhof, Autobahn) → Klinik. Fahrzeiten einheitlich „Autominuten";
Distanzen mit `&nbsp;` binden („ca.&nbsp;200&nbsp;m"), damit nichts mitten im Wert umbricht.

## Zuschnitt-Frage (Pflicht, VOR der Recherche)

**„Auf welcher Ebene zeigen wir die Mikrolage?"** (Chat-Frage, Optionen a/b/c, Empfehlung markiert)
- a) **Stadt** (kleine Stadt, POIs stadtweit)
- b) **Stadt + Stadtteil** (POIs im Stadtteil, Bezug zur Stadt — z. B. „Innenstadt" + „Hbf")
- c) **Nur Stadtteil / Viertel / Bezirk** (Großstadt: alles im Viertel, Bezug = Bezirk/Zentrum)

Empfehlung: Ortsteil mit eigener Mitte (Herten-Westerholt) → c als „Viertel ~2 km";
Kleinstadt ohne Ortsteile → a; Großstadt-Viertel → c.

Antwort bestimmt Lead-Satz, Karten-Ausschnitt und worauf sich „Innenstadt"/„Bahnhof" beziehen
(bei Stadtteil-Lage: Fahrzeit bis Hauptbahnhof, siehe Verkehrslogik unten).

## Prozess: Standortausarbeitung zuerst

1. **Immer zuerst eine volle Standortausarbeitung SAMMELN:** alles im **Umkreis von ~2 km**
   recherchieren (kompletter Katalog unten), mit ca.-Distanzen/Fahrzeiten — noch keine
   Korrekturen einfordern. **Per Subagent**, Vorlage „Mikrolage" in
   `references/standort-recherche-prompts.md`, parallel zur Makrolage-Recherche:
   - Koordinaten zuerst per Nominatim verifizieren (Straßennamen gibt es oft mehrfach in einer
     Stadt; Prüfregel + Technik in der Prompt-Referenz).
   - POIs per Overpass = **Luftlinie**; Fußweg ist ~20–30 % länger → auf der Folie „ca." und
     großzügig runden.
   - Autominuten per OSRM-Routing (ohne Verkehr), nicht schätzen.
   - **OSM kann veraltet sein:** neu eröffnete Bahn-Halte der letzten 2 Jahre gezielt prüfen
     (Herten-Westerholt: S 9 seit 14.12.2025, ~450 m vom Haus — fehlte in der ersten Recherche
     als Bahnhof, ist aber das stärkste Mikro-Argument).
   - Krankenhaus im ~2-km-Umkreis (sonst das nächste mit Notaufnahme in Autominuten) gehört als
     POI auf diese Folie (Name + Distanz). Auf der Makrolage erscheint ein Klinikverbund nur als
     Arbeitgeber mit belegter Beschäftigtenzahl, nie als Versorgungs-/Betten-Argument.
   - Rohdaten sofort in `<objekt>/expose/ausarbeitung.md` (Abschnitt Mikrolage, Status
     „gesammelt, nicht freigegeben", jede Runde als eigener Unterabschnitt).
2. Ausarbeitung als **Block im Fragesparring** durcharbeiten (Standard in `SKILL.md`): vor den
   Fragen **Entwurf** (POI-Liste) · **„Bewusst weggelassen"** (mit Grund) · **„Noch unsicher"**
   (z. B. nur Luftlinie, Halt fehlt in OSM) zeigen; Fragen nummeriert mit a/b/c, Empfehlung,
   Antwortform „1b 2a 3a" — Ergebnis: 10–13 POIs + Pflicht-Zeile Ø Vermietungsdauer
   (zusammen max. ~14 Zeilen im Raster).
3. Lead-Satz formulieren (ein knackiger Standort-Satz, positiv, ehrlich).
4. Wert-für-Wert-Gate wie überall; freigegebenen Block in `ausarbeitung.md` sichern.

## POI-Darstellung (André-fixiert 2026-07-31)

- **Generische Kategorie-Begriffe, KEINE Namen/Marken/Linien-Nummern:**
  „Lebensmittelgeschäft · ca. 500 m" (nicht Penny/Lidl/Aldi) · „Bushaltestelle · ca. 100 m"
  (keine Straße, keine Linie) · Apotheke, Allgemeinmediziner, Kita ohne Namen ·
  „Grundschule" reicht · „Gesamtschule" reicht.
- **Pro Kategorie genau EIN Eintrag** — der nächstgelegene (nicht drei Supermärkte).
- **Max. 14 Zeilen (7 je Spalte), jede Zeile kurz (~45 Zeichen, einzeilig).** „Gequetscht" entsteht
  durch lange, umbrechende Sammelzeilen, nicht durch die Zeilenzahl (Herten-Probe 2026-10-15:
  12 lange Zeilen wirkten voller als 14 kurze). Lieber eine Zeile mehr als drei Angaben in einer.
- **Schulen sind Pflicht, nie Streichkandidat** (André-fixiert 2026-10-15, Herten): Kita,
  Grundschule, weiterführende Schule UND Gymnasium stehen immer auf der Folie — auch wenn weit
  weg. Weite Wege nicht verstecken, sondern mit **Bus-Minuten Tür zu Tür** zeigen
  („Grundschule · ca. 6 Min. mit dem Bus", VRR-EFA o. ä.). Beim Kürzen nie Schulen anbieten.
- **Bus/Bahn ab Haustür:** zusätzlich zum Fußweg die direkten Verbindungen ohne Umstieg zeigen
  (S-Bahn mit Zielen + Minuten, „Bus direkt · Zentrum X Min."); Ziele, die nur mit 2+ Umstiegen
  erreichbar sind, nicht auf die Folie (die stehen per Auto auf der Makrolage).
- **Sortierung nach Kategorie** (thematische Gruppen wie oben).
- **Zentrums-Regel:** Ortskern/Stadtteilmitte bzw. Innenstadt nur aufführen, wenn der
  Ort/Stadtteil eine eigene Mitte hat ODER die Innenstadt der Stadt < 2 km entfernt ist.
- Ausnahme von der Namenlos-Regel: identitätsstiftende Einzel-POIs (Schloss, Klinik mit
  Betten, Bahnhof mit Zielangabe) behalten ihren Namen — Alltags-Kategorien nie.

## POI-Katalog (2-km-Prüfung)

### Familie / Alltag
| Feld | Format-Beispiel |
|---|---|
| Kindergarten | Kita · ca. 300 m |
| Schule | Grundschule · ca. 600 m · Gesamtschule · ca. 1,5 km |
| Ärzte / Apotheke | Apotheke · ca. 500 m · Allgemeinmediziner · ca. 600 m |
| Einkauf / Nahversorgung | Lebensmittelgeschäft · ca. 400 m |
| Gastro | Cafés / Restaurants · ca. 350 m |

### Mobilität (Verkehrslogik beachten)
| Feld | Regel |
|---|---|
| ÖPNV | „Bushaltestelle · ca. X m" — ohne Straßenname, ohne Linien-Nr. |
| **Bahnhof / S-Bahn-Halt** | **Distanz zum nächsten Halt + Bahn-Fahrzeit** zur nächsten Großstadt bzw. bei Stadtteil-Lage bis Hauptbahnhof, z. B. „S-Bahn-Halt · ca. 450 m · Essen Hbf ca. X Min (Bahn)". Fahrzeit nur mit Fahrplan-Beleg, sonst Takt („alle 30 Min nach Essen"). In den letzten 2 Jahren neu eröffnete Halte immer gezielt prüfen. Gehört auf diese Folie; auf der Makrolage höchstens als Kurzverweis in der Anbindungs-Zeile |
| **Autobahn** | schnellste Anschlussstelle + A-Nr. in Minuten (OSRM) |
| **Bundesstraße** | Wenn Autobahn weit weg (z. B. 10 Min), aber B-Auffahrt nah (2 Min): **Bundesstraßen-Auffahrt zeigen** („Auffahrt B51 · ca. 3 Min"), Autobahn dann optional dahinter |
| Innenstadt / Zentrum | Entfernung in km |
| **Universität** | **nur wenn Verbindung gut ist** (Bahn/ÖPNV direkt): „Uni / TH Köln · ca. 20 Min (Bahn)" |

### Umfeld / Lebensqualität (nur wenn in der Nähe)
Grünflächen · Park · Wald · Attraktionen/Sehenswürdigkeiten.

Sehenswürdigkeiten in Gehweite bleiben hier als Lebensqualitäts-POI erlaubt (das
Stadtmarketing-Verbot gilt nur für die Makrolage).

**Große Unternehmen → Makrolage** (~30-Autominuten-Radius mit belegter Beschäftigtenzahl,
`references/makrolage-stadt.md`), nicht hier — Ausnahme: direkt im Stadtteil gelegener
Groß-Arbeitgeber als Nachfrage-Argument.

## Pflicht-Zeile: Ø Vermietungsdauer im PLZ-Gebiet (seit 2026-07)

- **Fester Bestandteil der Mikrolage-Folie:** eine Zeile im POI-Raster (Uhr-Icon),
  Folientext (André-fixiert 2026-10-15, Herten): **„Vermietet in Ø X Tagen · <N>-Zimmer-Wohnungen,
  PLZ <PLZ>"** — z. B. „Vermietet in Ø 15 Tagen · 3-Zimmer-Wohnungen, PLZ 45701". Zimmerzahl und
  PLZ gehören in die Zeile, weil der Wert genau für diese Suche gilt (nicht „Ø Vermietungsdauer
  im PLZ-Gebiet").
- **Wert ist ein Fixwert von André** (Quelle: ohne-makler) — **IMMER aktiv abfragen**, nie
  selbst recherchieren, nie raten. **Suchparameter gleich mitliefern** (André sucht bei
  ohne-makler nach Zimmerzahl + Wohnfläche; Herten 2026-10-14 fragte er sonst erst zurück):
  „Wie viele Tage dauert die Vermietung im Schnitt im PLZ-Gebiet <PLZ>? Suchwerte für
  ohne-makler: <N> Zimmer, <X> m²" (bei unterschiedlichen Einheiten: alle Kombinationen nennen).
  Ohne Wert bleibt die Zeile `[OFFEN]` und wird vor dem finalen Render nachgefordert.
- **Abweichende Werte je Einheit:** mit a/b fragen — a) ein gemeinsamer Wert für alle Wohnungen
  (Mikrolage bleibt identischer Gebäude-Teil) · b) Wert je Wohnung (Mikrolage-Folie wird pro
  Einheit per String-Replace variiert, Wert steht in der Einheiten-Liste des Übergabeprompts).
  Wert + Suchwerte + Abfragedatum in `ausarbeitung.md` sichern.
- Zusätzlich fürs Gespräch: Immometrica-/ohne-makler-Screenshot als Call-Material anbieten.

## Wording
ca.-Angaben, keine Garantien; Distanzen/Fahrzeiten plausibel gerundet (m unter 1 km, sonst km/Min).
