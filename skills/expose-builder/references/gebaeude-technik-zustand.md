# Referenz: Seite „Gebäude-Technik & Zustand" (Feldkatalog + Prozess)

Gehört zum Gebäude-Teil (für alle Wohnungen eines Hauses identisch). Layout = Icon-Liste
im Standard von Seite 2 (`template/expose.html`, Klasse `.iconcols` / `.iconrow`), zwei
Spalten ohne Spalten-Köpfe, Inhalt vertikal zentriert. Energieausweis als Vollbreiten-Zeile
unten (Absatzlinie statt Symbol, Mini-Farbskala rechts).

## Darstellungsregel

- **Eine Zeile pro Bauteil, WAS + WANN kombiniert** (z. B. „Dach · Satteldach · Ziegel · 2008",
  „Heizung · Gas-Zentralheizung · Bj. 2015"). Technik-Fakt und Sanierungsjahr NICHT auf zwei
  Zeilen aufteilen.
- **Icon links** (Line-Icon in Oxblood), **Label (mono) über Wert (Serif)**.
- **Energieausweis** immer die letzte, volle Zeile: kein Icon/Chip davor, nur die Absatzlinie
  darüber; Text links (Typ · kWh/(m²·a) · Gültigkeit), **Mini-Farbskala A+…G rechts** mit
  markierter Klasse (`.escale--mini`, aktive Zelle `is-active`). Klasse steht in der Skala,
  daher nicht zusätzlich im Text.
- **Ausstellungsdatum ist Pflicht** und steht **direkt unter der Farbskala** — eigene Zeile
  `.energrow__date` im Wrapper `.energrow__scale` („Ausgestellt am · TT.MM.JJJJ", mono 6,5 pt,
  muted). Wert kommt aus dem Energieausweis-PDF; fehlt er, `[OFFEN]` setzen und nachfragen.
- Jede Angabe mit Quelle aus den Objektdaten oder `[OFFEN]` — nie raten.

## Feldkatalog

### Essentiell — immer aufs Exposé (automatisch befüllen, sonst `[OFFEN]`)

| Feld | Beispiel-Wert |
|---|---|
| Dachform + Dacheindeckung (+ Sanierungsjahr) | Satteldach · Ziegel · 2008 |
| Heizungsart + Energieträger (+ Baujahr Heizung) | Gas-Zentralheizung · Bj. 2015 |
| Fensterart (Isolier-/Doppelverglasung) (+ Jahr) | Isolierverglasung · 2021 |
| Elektrik (Zustand / Sanierungsjahr) | Erneuert 2016 |
| Leitungen / Stränge (Wasser/Elektro/Gas Zustand) | Wasser/Elektro 2016 · Gas Bestand |
| Fassade (Sanierungsjahr) | 2019 |
| Energieausweis (Typ, Wert kWh, Klasse, Gültigkeit) — **gesetzl. Pflicht** | Verbrauchsausweis · 132 kWh/(m²·a) · Klasse E · gültig bis 05/2032 |
| Ausstellungsdatum Energieausweis — **Pflicht, Zeile unter der Skala** | Ausgestellt am · 12.05.2022 |

Die „Durchgeführten Sanierungen + Jahr" (Dach, Fassade, Fenster, Elektrik, Strang) sind in
die jeweiligen Bauteil-Zeilen eingerechnet, nicht als separater Block.

### Nice-to-have — nachfragen, ob Info vorhanden

| Feld | Beispiel-Wert |
|---|---|
| Zustand (Modernisierungsstau / saniert) | Gepflegt · teilsaniert |

### Nur wenn ja — nachfragen, nur einblenden wenn zutreffend

| Feld | Wert / Regel |
|---|---|
| Fassade / Dämmung (WDVS ja/nein) | nur wenn ja → „WDVS gedämmt" an die Fassade-Zeile hängen |
| Keller (unterkellert / Teilkeller) | nur wenn zutreffend → „Voll unterkellert" / „Teilkeller" |

**Aufzug steht NICHT mehr hier** — seit 2026-08-07 Pflichtfeld auf der Folie
„Gebäude-Eckdaten" (immer sichtbar, Wert „Ja" / „Nein"), siehe SKILL.md → Feld-Regeln.

## Prozess (Ablauf beim echten Objekt)

1. **Essentielle Felder automatisch füllen** aus Objektordner / Vertriebspipeline; fehlt eine
   Angabe → `[OFFEN]` (nicht raten).
2. **Nice-to-have + „nur wenn ja" abfragen:** „Haben wir dazu Infos?" bzw. „Trifft das zu?"
   Nur bei Ja/Datenlage einblenden.
3. **Auto-Entwurf zeigen, dann Angabe für Angabe durchgehen** — André korrigiert/bestätigt je
   Feld, dann festzurren.
4. **Variabel-Felder ohne Datenlage weglassen** (keine leeren Platzhalter im finalen Objekt-PDF;
   im Master bleiben sie als löschbare Beispielzeilen).
