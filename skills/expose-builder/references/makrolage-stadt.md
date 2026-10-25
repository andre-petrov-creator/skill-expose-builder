# Referenz: Seite „Makrolage / Stadt" (Vermietungs-Argumente + Prozess)

Gehört zum Gebäude-Teil. Position im Verkaufsbogen: **direkt nach dem Titel** — Lage zuerst
(Primacy/Halo: starke Lage-Story färbt auf alles Folgende ab).

**Leitfrage der Folie (André-fixiert 2026-10-15, Herten):** *Warum vermietet sich eine Wohnung
hier — und warum lohnt sich der Kauf?* Jede Zeile zahlt darauf ein: Arbeitsplätze, Studierende,
Anbindung, Region. Stadtmarketing (Schlösser, Observatorien, Museen, Fachwerk, Tourismus) hat auf
der Folie nichts verloren. Kleine Initiativen ohne belegte Größe (Herten: Wasserstoff-
Kompetenzzentrum h2herten) fallen über die Arbeitgeber-Regel raus (Auswahl-Regeln unten).

**Layout (André-fixiert seit Ringlebstr. 25, 2026-07 — Referenz `<objekt>/expose/expose.html`):**
Bild links (`.cityimg` ~118×127 mm, `background:center/cover`), rechts Kurztext (`.macrotext`,
1–2 Sätze) + **einzeilige Icon-Liste** (`.macrolist` mit cityfact-Zeilen, 10,5 pt, Icons 6 mm) —
**KEINE Kennzahl-Kacheln, KEINE Mono-Überschriften** über den Zeilen; der Fakt steht direkt in
der Zeile („Chemiepark Marl · rund 10.000 Arbeitsplätze"). Kurztext startet bündig mit der
Bildoberkante (`.macrogrid{align-items:start}`). Bildmotiv passend zur Vermietungs-Story
(Groß-Arbeitgeber, Ortsbild am Objekt oder Region) — wird im Fragesparring entschieden.

## Zuschnitt-Frage (Pflicht, VOR der Recherche)

Als Chat-Frage mit Optionen a/b und markierter Empfehlung (kein AskUserQuestion-Fenster):
**„Bilden wir die Stadt als Ganzes ab oder Stadt + Stadtteil?"**
- a) **Kleine/mittlere Stadt** (z. B. Herten, Wesseling) → Stadt als Ganzes. **Recherche-Radius
  trotzdem ~30 Autominuten ums Objekt** — die Kleinstadt allein trägt die Vermietungs-Story
  nicht, die Arbeitgeber und Hochschulen der Nachbarstädte schon.
- b) **Große Stadt** (z. B. Essen, Köln, Dortmund) → Stadt + Stadtteil differenzieren:
  Headline z. B. „Makrolage Essen" oder „Essen – Stadtteil X", Zeilen zweistufig
  (Stadt-Ebene: Arbeitgeber/Hochschulen/Anbindung · Stadtteil-Ebene: Charakter/Lage in der Stadt).
- Antwort bestimmt Headline, Recherche-Ebene und Bildmotiv.

## Prozess: sofort in voller Tiefe recherchieren

**Lehre Herten (2026-10-14/15):** Runde 1 (Stadtprofil: Einwohner + „Kreis X", Sehenswürdigkeiten,
Wasserstoff-Kompetenzzentrum) wurde komplett verworfen; erst Runde 3 (30-Min-Radius,
Beschäftigtenzahlen, Studierende, Routing-Fahrzeiten, aktuelle News) traf. → Diese Tiefe ist ab
jetzt der **erste** Durchgang.

1. **Fakten-Register lesen** (`references/standort-fakten-register.md`): dort belegte Zahlen der
   Region mit Stichtag ≤ 12 Monate übernehmen („übernommen aus Register, Quelle …"), Älteres
   neu belegen lassen.
2. **Sammeln per Subagent** (general-purpose, Vorlage „Makrolage" in
   `references/standort-recherche-prompts.md`), parallel zur Mikrolage-Recherche. Quellen +
   Stichtag zu jeder Zahl, Unsicheres als `(unsicher)` markiert.
3. Ergebnis + Rohdaten sofort in `<objekt>/expose/ausarbeitung.md` (Abschnitt Makrolage, Status
   „gesammelt, nicht freigegeben", jede Runde als eigener Unterabschnitt).
4. **Entwurf** nach den Auswahl-Regeln unten (Kurztext + bis 8 Zeilen) → **Block im
   Fragesparring** mit dem Frage-Paket unten.
5. Freigabe Wert für Wert → Block in `ausarbeitung.md` auf „freigegeben" setzen, dann ins Layout.
6. **Register pflegen:** neu belegte Fakten (Arbeitgeber, Hochschulen, Region, Negativ-Funde)
   mit Quelle + Stichtag ins Fakten-Register übernehmen.

## Recherche-Katalog (Reihenfolge = Gewicht)

| # | Kategorie | Was genau | Quelle bevorzugt |
|---|---|---|---|
| 1 | **Groß-Arbeitgeber im ~30-Autominuten-Radius** | Name · **Beschäftigte am Standort** · Autominuten (Routing). Chemieparks/Werke, Konzernzentralen, Unis als Arbeitgeber, Stadtverwaltungen der Nachbar-Großstädte, Klinikverbünde, Versorger, ÖPNV-Betriebe, Logistikzentren. **Ziel: 8–12 belegte Kandidaten** — erst Kandidaten finden, dann je Kandidat gezielt belegen | Geschäftsbericht > Unternehmens-/Hochschulprofil > Pressemitteilung > Wirtschaftsförderung > Stellenanzeige/Drittportal (= `(unsicher)`). Wikipedia nur zum Finden, nie als Beleg |
| 2 | **Hochschulen im ~30-Min-Radius** | Studierende je Hochschule + **Summe** | Hochschulstatistik/Destatis, Stichtag Semester |
| 3 | **Arbeitgeber vor Ort** | Gewerbe-/Technologieparks (Arbeitsplätze), große Sitz-Unternehmen mit Zahl | Wirtschaftsförderung der Stadt |
| 4 | **Einwohner + Region** | Stadt: Landesdatenbank (NRW: landesdatenbank.nrw.de, Fortschreibung, letzter 31.12., Zensus-2022-Basis; Kommunalprofil nur Rückfall, Melderegister nur Notiz; Trend nur bei gleicher Basis) · Region: Einwohner + sozialversicherungspflichtig Beschäftigte mit Quelle + Stichtag | Landesamt, Regionalverband, Bundesagentur für Arbeit |
| 5 | **Anbindung** | Autominuten per Routing (OSRM) zu den schnellsten Autobahn-Anschlussstellen je Autobahn und den Hbf der Nachbar-Großstädte; Bahn-Halte inkl. **neu eröffneter**, Linien + Takt (Fahrzeit nur mit Fahrplan-Beleg) | OSRM, DB/Verkehrsverbund-Presse |
| 6 | **News der letzten ~2 Jahre** | eröffnet/beschlossen/im Bau: neue Bahn-Halte/Linien, Ansiedlungen, Werkseröffnungen, Einkaufszentren, Neubaugebiete, Innenstadt-/Förderprogramme, Klinik-Investitionen | Stadt-Pressemitteilungen, Regionalpresse, Ratsinformationssystem |
| 7 | **Negativ-Check (Pflicht)** | Stellenabbau, Werksverkauf, Schließungen — gezielt für jeden Arbeitgeber aus #1/#3; Projekte in Planung mit Bauphasen-Belastung | Presse |
| 8 | Profil/Tourismus | **nicht recherchieren** (Subagent-Prompt schließt es aus); nur notieren, wenn nebenbei gefunden | — |

## Auswahl-Regeln (was aufs Blatt darf)

- **Nur Arbeitgeber mit belegter Beschäftigtenzahl am Standort** im Radius. Konzern-,
  Deutschland- oder Weltzahlen (E.ON, RWE …) zählen nie — weder als Zeile noch in der Summe.
- **Stichtag ≤ 3 Jahre.** Ältere Zahlen (Herten: Ewald 1.300+ aus 2021) nicht still übernehmen,
  sondern unter „Noch unsicher" zeigen und fragen.
- **Negativ-Check schlägt Größe, mit Schwelle:** weglassen, wenn (a) der Standort im Radius
  verkauft wird, schließt oder ein Werk dort stillgelegt wird, oder (b) am Standort ein Abbau
  von ≥ 10 % der Belegschaft angekündigt ist (Herten: Raffinerie Gelsenkirchen im Verkauf,
  Herta-Stellenabbau) — André unter „Bewusst weggelassen" zeigen. **Konzernweite Programme
  ohne Standortzahl** (Probelauf Gladbeck: Evonik-Abbau, Chemiepark Marl) = **Grenzfall**:
  weder still weglassen noch still behalten → „Noch unsicher" + Grenzfall-Frage im Frage-Paket.
- **Regionalzahlen ehrlich zuordnen:** eine Region-Kennzahl nie auf einen Radius umdeuten
  („1,8 Mio. Arbeitsplätze im 30-km-Umkreis" ist falsch, wenn die Zahl für die ganze Metropole
  Ruhr gilt) → „mitten in der Metropole Ruhr: 5,1 Mio. Einwohner, 1,8 Mio. Arbeitsplätze".
  Für den Radius stattdessen die **Summe der belegten Groß-Arbeitgeber**.
- **Summen-Regel:** Summe nur aus Arbeitgebern, die alle Regeln bestehen (Standortzahl,
  Stichtag ≤ 3 Jahre, Negativ-Check bestanden, ohne `(unsicher)`); Hochschulen als Arbeitgeber
  nicht zusätzlich zu den Studierenden zählen. Steht im Kurztext „bei den großen Arbeitgebern
  unten", dürfen nur die auf der Folie genannten Arbeitgeber einfließen; sonst „im Umkreis".
  Rechenweg mit Einzelwerten in die Ausarbeitung. Summe < 10.000 oder < 3 Arbeitgeber →
  Kurztext ohne Arbeitsplatz-Summe (Anbindung, Studierende, Region) und als „Noch unsicher" melden.
- **Keine Verwaltungs-Zuordnung, die der Story widerspricht** („mitten im Ruhrgebiet … Kreis
  Recklinghausen" verwässert die Lage).
- **Verdichten statt auflisten:** höchstens 8 Zeilen. Zeile 1 darf Stadt + Region als Rahmen
  setzen (Einwohner + Wirtschaftsregion, ohne Kreis), danach stärkstes Vermietungsargument
  zuerst. Bündeln: „Vier Hochschulen · über 100.000 Studierende (…)", „Sechs weitere Arbeitgeber
  mit je über 1.000 Beschäftigten (…)". **Keine Füllzeilen:** bestehen weniger als 6 Zeilen die
  Regeln, die Lücke melden und fragen (a mit n Zeilen gehen · b gezielt nachrecherchieren).
- **Bahn-Halt am Haus** gehört mit Distanz auf die Mikrolage-Folie; auf der Makrolage höchstens
  als Kurzverweis in der Anbindungs-Zeile.
- **Fahrzeiten** nur aus Routing (OSRM, ohne Verkehr), nie geschätzt. Runden: unter 10 Min ganze
  Minuten („A2 in 8 Min"), ab 10 Min auf volle 5 („in rund 30 Min"; 32,9 → 35). Ein Ziel zählt
  zum Radius, wenn OSRM ≤ 32 Min liefert; 33–40 Min nur als Notiz, nie in Summen.

## Muster-Entwurf (Herten, Runde 4 vom 2026-10-15 — Tiefe/Ton als Vorlage, Wortlaut nicht freigegeben)

> Herten liegt mitten im Ruhrgebiet. In rund 30 Autominuten: über 30.000 Arbeitsplätze allein bei
> den großen Arbeitgebern unten und über 100.000 Studierende.

1. Herten · rund 61.000 Einwohner — mitten in der Metropole Ruhr: 5,1 Mio. Einwohner, 1,8 Mio. Arbeitsplätze
2. Chemiepark Marl · rund 10.000 Arbeitsplätze *(Grenzfall Evonik-Abbau — vor Wiederverwendung prüfen)*
3. Neuer VW-Standort Bochum · über 1.000 Entwickler (VW Infotainment, MARK 51°7)
4. Vier Hochschulen · über 100.000 Studierende (RUB, UDE, TU Dortmund, Westfälische Hochschule)
5. Sechs weitere Arbeitgeber mit je über 1.000 Beschäftigten (RUB, Stadt Gelsenkirchen,
   Knappschaft Kliniken Vest, Gelsenwasser, Vestische Straßenbahnen, Zukunftsstandort Ewald)
6. A2/A52 in 8 Min · Essen, Bochum, Dortmund in rund 30 Min · neuer S-Bahn-Halt (S 9, 12/2025)

Quellen + Stichtage aller Muster-Zahlen: `references/standort-fakten-register.md`.
**Achtung:** Die „über 30.000" im Muster-Kurztext entstand vor der Summen-Regel (enthält
unsichere/alte Werte, Chemiepark-Grenzfall und die RUB doppelt als Arbeitgeber + Studierende) —
nach der Regel neu rechnen, bevor der Satz verwendet wird.

## Frage-Paket Makrolage (Fragesparring-Muster)

Vor den Fragen kurz zeigen: **Entwurf** · **„Bewusst weggelassen"** (mit Grund) · **„Noch unsicher"**
(Zahl + warum). Dann 3–6 Fragen im Chat, Optionen a/b/c, Empfehlung markiert, Antwortform
„1b 2a 3a 4a". Die Fragen sind Auswahl — die Werte werden danach einzeln bestätigt.
1. Zeilen-Auswahl: a) alle Zeilen behalten · b) auf 6 kürzen/bündeln (Empfehlung + Grund)
2. Unsichere/alte Zahl (nur Stellenanzeige/Drittportal, Stichtag > 3 Jahre): a) Quellwert ·
   b) vorsichtigerer Wert · c) streichen
3. Kurztext: a) passt · b) ändern — wie?
4. Bild: a) Groß-Arbeitgeber · b) Ortsbild am Objekt · c) Region/Luftbild
5. Fahrzeiten: a) Einzelwerte (Routing, gerundet) · b) Sammelangabe („Essen, Bochum, Dortmund in
   rund 30 Min")
6. Nur wenn vorhanden — Grenzfall Negativ-Check: <Arbeitgeber> · <Abbau/Verkauf, Quelle>:
   a) weglassen · b) mit vorsichtiger Zahl behalten · c) ohne Namen in eine Bündelzeile —
   Empfehlung a bei Verkauf/Schließung des Standorts oder Abbau ≥ 10 %, sonst b.

Fragt André nach einer griffigen Radius-Zahl, die es nicht belegt gibt: ehrlich sagen, warum sie
angreifbar ist, und die belegbare Alternative (Region-Zahl oder Summe der Groß-Arbeitgeber)
vorschlagen.

## Harte Regel: keine Marktdaten im Exposé

**Bewusst NICHT aufs Blatt:** Mietpreise, Kaufpreise, Miet-/Preistrends, Marktvergleiche.
Das Exposé ist Präsentationsgrundlage — Zahlen zu Miete/Preis kommen im Gespräch.
Die **Ø Vermietungsdauer im PLZ-Gebiet** steht nicht hier, sondern als Pflicht-Zeile auf der
Mikrolage-Folie (André-Fixwert, `references/mikrolage-standort.md`).

## Wording
Nur belastbare, positive Zahlen mit Quelle/Stichtag in der Ausarbeitung; auf der Folie
gerundet („rund 10.000", „über 1.000"). Bei schwacher Lage: stärksten ehrlichen Winkel spielen
(Anbindung, Arbeitsplätze im Radius), nie Rohschwäche zeigen, nie erfinden.
