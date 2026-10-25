# Referenz: Recherche-Prompts Makrolage + Mikrolage (Subagent-Vorlagen)

Seit Herten (2026-10-15), technisch geprüft im Probelauf Gladbeck (2026-10-15). Beide Prompts
**parallel** als `general-purpose`-Subagent starten, sobald die Zuschnitt-Gates beantwortet sind.
Platzhalter in `{…}` ersetzen. Ergebnisse roh in `<objekt>/expose/ausarbeitung.md` sichern, erst
dann den Entwurf bauen (`makrolage-stadt.md` / `mikrolage-standort.md`).

## Platzhalter

- `{ADRESSE}` · `{PLZ}` · `{STADT}` · `{STADTTEIL}` — aus dem Objektordner.
- `{REGION}` = **Wirtschaftsregion** (z. B. „Metropole Ruhr"), NICHT Kreis/Regierungsbezirk —
  Verwaltungs-Zuordnung höchstens als Notiz.
- `{NACHBARSTAEDTE}` = alle Städte, deren Zentrum/Hbf per OSRM ≤ ~32 Autominuten vom Objekt
  liegt — nicht aus dem Bauch schätzen; im Zweifel ermittelt der Subagent sie in Schritt 2 selbst.
- `{REGISTER}` = relevante Zeilen aus `references/standort-fakten-register.md` (Stichtag ≤ 12 Monate
  = übernehmen, älter = neu belegen).

## Technik-Bausteine (im Probelauf Gladbeck getestet)

- **Kein persönlicher Kontakt im User-Agent** (keine Mail-Adresse von André an Dritt-Dienste) —
  User-Agent `expose-builder/1.0`. Alle Abrufe per Bash/curl oder Python, max. 1 Anfrage/Sekunde.
- **Koordinaten (Nominatim):** Adresse URL-kodiert (Leerzeichen `%20`, Komma `%2C`):
  `https://nominatim.openstreetmap.org/search?q={ADRESSE_URLKODIERT}&format=json&limit=1&countrycodes=de&addressdetails=1`.
  Treffer nur übernehmen, wenn `address.postcode` = `{PLZ}`, Ort = `{STADT}` und
  `address.house_number` vorhanden; sonst strukturiert wiederholen (`street=…&postalcode=…&city=…`).
- **Ziel-Koordinaten:** Bahnhöfe/Halte NICHT per Nominatim-Freitext (liefert Parkplätze,
  Fahrradständer, Wohnstraßen), sondern per Overpass
  `node["railway"~"station|halt"]["name"~"{NAME}"](around:25000,{LAT},{LON});out;`.
  Firmen, Kliniken, Hochschulen per Nominatim nur bei passender `class`
  (amenity/university, amenity/hospital, landuse/industrial, building); sonst Koordinate aus der
  Wikipedia-Infobox und das in der Ausarbeitung vermerken.
- **Autominuten (OSRM, ohne Verkehr) — EIN Aufruf für alle Ziele:**
  `https://router.project-osrm.org/table/v1/driving/{LON},{LAT};{Z1_LON},{Z1_LAT};…?sources=0&annotations=duration,distance`
  → `durations[0][i]` (s), `distances[0][i]` (m). Vorher `code == "Ok"` prüfen. Reihenfolge
  immer Länge,Breite.
- **Autobahn-Anschlussstellen:** Overpass
  `node["highway"="motorway_junction"](around:10000,{LAT},{LON})->.j; way["highway"="motorway"](bn.j); out tags; .j out body;`
  A-Nummer aus `way.ref`, AS-Nummer aus `node.ref`. Knoten ohne `ref` oder mit „Rast"/„Parkplatz"
  im Namen verwerfen; gleichnamige Knoten (je Fahrtrichtung einer) alle routen, kürzesten Wert
  nehmen. Ausgabe: je Autobahn die schnellste Anschlussstelle (Name, A-Nr., Min, km).
- **Overpass:** alle Fragen eines Laufs in EINE Abfrage bündeln (mehrere Statements mit `out;`),
  als POST mit Feld `data=` an `https://overpass-api.de/api/interpreter`. Bei HTTP 429 einmal auf
  `https://overpass.kumi.systems/api/interpreter` ausweichen, nicht in Schleife wiederholen.
- **Suchanfragen eindeutig machen:** `{STADT} {PLZ}` statt nur `{STADT}` (sonst Treffer zu
  Bergisch Gladbach/Mönchengladbach); News nur mit site-Filter (Stadt-Domain, Regionalzeitung,
  Ratsinformationssystem).

============================================================
## Vorlage „Makrolage" (Vermietungs-Argumente)

```
Recherche auf Deutsch. Zweck: Makrolage-Folie eines Verkaufsexposés für Wohnungen in {ADRESSE}
({STADT}, {REGION}). Gesucht sind NUR harte Argumente, warum sich hier vermieten lässt und warum
sich der Kauf lohnt: große Arbeitgeber, Arbeitsplätze, Hochschulen, Anbindung, Region, aktuelle
Entwicklung. KEIN Tourismus, keine Schlösser/Museen, keine Miet-/Kaufpreise oder Preistrends.
Technik-Bausteine (Nominatim/OSRM-Table/Overpass, User-Agent "expose-builder/1.0", max. 1 Anfrage/s):
<Abschnitt "Technik-Bausteine" aus standort-recherche-prompts.md einfügen>
Budget: rund 40 Tool-Aufrufe, davon mindestens 20 für Arbeitgeber.

Bereits belegt (Register, nicht neu recherchieren, nur übernehmen): {REGISTER}

1. Koordinaten der Adresse per Nominatim verifizieren (Prüfregel PLZ/Ort/Hausnummer).
2. {NACHBARSTAEDTE} per OSRM-Table bestätigen (Hbf/Zentrum ≤ 32 Min).
3. Groß-Arbeitgeber im Radius: ERST Kandidaten finden (IHK-/Wirtschaftsförderungs-Ranglisten,
   Wikipedia-Abschnitt "Wirtschaft" von {STADT} und {NACHBARSTAEDTE}), DANN je Kandidat EINE
   gezielte Suche ("<Name>" Mitarbeiter <Standort> <Jahr> bzw. Geschäftsbericht/Unternehmensprofil).
   Ziel 8–12 Kandidaten, je Name · Beschäftigte AM STANDORT · Stichtag · Autominuten (OSRM).
   Quellen-Rangfolge: Geschäftsbericht > Unternehmens-/Hochschulprofil > Pressemitteilung >
   Wirtschaftsförderung > Stellenanzeige/Drittportal ("(unsicher)"). Wikipedia nur zum Finden,
   nie als Beleg. Konzern-/Deutschland-/Weltzahlen und Stichtage > 3 Jahre → Liste G.
4. Arbeitgeber vor Ort in {STADT}: Gewerbe-/Technologieparks mit Arbeitsplatzzahl, große
   Sitz-Unternehmen. Kleine Initiativen/Kompetenzzentren ehrlich als "klein" kennzeichnen.
5. Hochschulen im Radius: Studierende je Hochschule (Stichtag Semester) + Summe.
6. Einwohner {STADT}: Landesdatenbank (NRW: landesdatenbank.nrw.de, Fortschreibung, letzter
   31.12., Zensus-2022-Basis); Kommunalprofil nur Rückfall, Melderegister nur Notiz, Trend nur
   bei gleicher Zensus-Basis. Region {REGION}: Einwohner + sozialversicherungspflichtig
   Beschäftigte mit Quelle UND Stichtag (Regionalverband, Bundesagentur für Arbeit).
7. Anbindung per OSRM-Table: je Autobahn die schnellste Anschlussstelle (Name, A-Nr., Min, km),
   Hbf von {NACHBARSTAEDTE}. Bahn-Halte in {STADT} inkl. in den letzten 2 Jahren neu eröffneter
   (DB/Verkehrsverbund-Presse): Linien + Takt; Fahrzeit zum nächsten Großstadt-Hbf nur mit
   Fahrplan-Beleg (z. B. zuginfo.nrw), sonst nur den Takt nennen.
8. News der letzten ~2 Jahre (nur eröffnet, beschlossen oder im Bau): neue Bahn-Halte,
   Ansiedlungen, Werkseröffnungen, Einkaufszentren, Neubaugebiete, Innenstadt-/Förder-
   programme, Klinik-Investitionen. Suche mit site-Filter (Stadt-Domain, Regionalzeitung,
   Ratsinformationssystem) und "{STADT} {PLZ}".
9. Negativ-Check für JEDEN Arbeitgeber aus 3/4: Verkauf, Schließung, Stellenabbau am Standort
   (mit Anteil an der Belegschaft) bzw. konzernweite Programme ohne Standortzahl (= Grenzfall).
   Projekte in Planung mit Bauphasen-Belastung ebenfalls hierher, mit Planungsstand.
10. Summe NUR aus Arbeitgebern, die alles bestehen (Standortzahl, Stichtag ≤ 3 Jahre,
    Negativ-Check bestanden, ohne "(unsicher)"); Hochschulen als Arbeitgeber nicht zusätzlich
    zu den Studierenden. Rechenweg als Liste.

Ausgabe: Listen als Tabellen (keine Wortgrenze für Tabellen), Fließtext max. ~150 Wörter:
A Arbeitgeber (stärkstes zuerst) · B Hochschulen · C Einwohner/Region · D Anbindung
(OSRM-Tabelle) · E News positiv · F Negativ/Grenzfälle · G nicht verifiziert (Konzernzahl,
veraltet, ohne Zahl) · H Summe Arbeitsplätze mit Rechenweg. Jede Zeile: Fakt · Zahl ·
Autominuten · [n]. Quellen als nummerierte Liste [1]…[n] am Ende (URL + Stichtag).
Unsicheres "(unsicher)".
```

============================================================
## Vorlage „Mikrolage" (POIs ~2 km)

```
Recherche auf Deutsch. Zweck: Mikrolage-Folie eines Verkaufsexposés für {ADRESSE}
({STADTTEIL}, {STADT}).
Technik-Bausteine (Nominatim/OSRM-Table/Overpass, User-Agent "expose-builder/1.0", max. 1 Anfrage/s):
<Abschnitt "Technik-Bausteine" aus standort-recherche-prompts.md einfügen>

1. Koordinaten per Nominatim verifizieren (Prüfregel PLZ/Ort/Hausnummer; gleiche Straßennamen
   gibt es oft mehrfach in einer Stadt).
2. EINE gebündelte Overpass-Abfrage im Radius 2.000 m, je Kategorie den NÄCHSTGELEGENEN Eintrag
   mit Luftlinie in m: Bushaltestelle, Bahn-/S-Bahn-Halt, Apotheke, Allgemeinmediziner,
   Lebensmittelgeschäft, Bäckerei, Café/Restaurant, Kita, Grundschule, weiterführende Schule
   (Form angeben), Park/Grünfläche/Wald, Ortskern/Zentrum, Krankenhaus (Name + Betten).
3. OSM kann veraltet sein: in den letzten 2 Jahren neu eröffnete Bahn-Halte per
   DB/Verkehrsverbund-Presse prüfen und Distanz zum Haus messen.
4. Per OSRM-Table: Autominuten zur schnellsten Autobahn-Anschlussstelle je Autobahn (Name +
   A-Nummer), zur nächsten Bundesstraßen-Auffahrt und zum nächsten Krankenhaus mit Notaufnahme
   (falls keins im 2-km-Radius).
5. Bahn: Linien + Takt ab dem nächsten Halt; Fahrzeit zu den 2 nächsten Großstadt-Hbf nur mit
   Fahrplan-Beleg, sonst nur Takt.

Ausgabe: eine Zeile je Kategorie: Kategorie · Name (nur intern) · ca. Distanz/Minuten · [n];
Quellen nummeriert am Ende. Hinweis: Luftlinie; Fußweg ca. 20–30 % länger.
Unsicheres "(unsicher)". Max. ~500 Wörter ohne Quellenliste.
```
