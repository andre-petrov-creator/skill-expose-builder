# Referenz: Seite „Beispielsberechnung" (Cashflow nach Steuer)

Gehört zum **Wohnungs-Teil**, Position: **nach Stammdaten (7a) bzw. Immobilienbewertung (7b, falls
vorhanden), vor den Raum-Folien** (André-fixiert 2026-07-31). Eingeführt 2026-07-31 (Prosperstraße, Essen-Dellwig).

## Bewusste Ausnahme von der Keine-Finanzangaben-Regel

Diese Folie **darf** Kaufpreis, Miete, Hausgeld und Cashflow zeigen — sie ist der
Rechen-Beweis im Sales-Call und der einzige Ort im Exposé, an dem Geld auf dem Blatt steht.
Alle anderen Folien bleiben zahlenfrei (Ausnahmen sonst nur: Stammdaten der Wohnung mit
Miete/Hausgeld, Immobilienbewertungs-Screenshot auf Zuruf).

**Pflicht-Frage vor dem Bauen:** „Beispielsberechnung mit aufnehmen — und mit welchem
Grenzsteuersatz?" Ohne explizites Ja entfällt die Folie.

## Layout

Zwei gleich breite Spalten (`.calcgrid`), gleiche Zeilenfolge, damit der Kunde von links
nach rechts vergleichen kann:

- **links:** „Ohne Eigenkapital · 110-%-Finanzierung"
- **rechts:** „Mit Eigenkapital · Käufer trägt Kaufnebenkosten"

Zeilenfolge (identisch in beiden Spalten):
Kaufpreis · Eigenkapital-Einsatz · Mieteingang · Annuität an die Bank ·
Hausgeld (nicht umlagefähig) · **Zwischensumme** · Steuervorteil · **Cashflow nach Steuer**

CSS: `.calccol__head` (Mono, Oxblood, Rule darunter) · `.calcrow--sum` (fett) ·
`.calcrow--final` (Oberlinie 1,2 pt, Wert 13,5 pt). **Positiver Cashflow in Grün `#1F6B43`**,
Label bleibt Oxblood. Negativer Cashflow in Oxblood.
Unter dem Raster `.calcnote` mit der Berechnungsgrundlage (Mono, 6,6 pt).

Sprache bewusst einfach halten — „Annuität an die Bank", „Hausgeld", „Steuervorteil".
Keine Fachbegriffe wie AfA-Basis, Bewirtschaftungskosten oder Grenzsteuersatz in den
Zeilen selbst; die stehen gesammelt in der Fußnote.

## Kaufnebenkosten (KNK) — der Kern der beiden Varianten

**KNK-Satz je Bundesland erfragen, nie raten.** NRW = **8,5 %** (6,5 % Grunderwerbsteuer
+ ca. 2 % Notar und Grundbuch), provisionsfrei gerechnet. Bei Maklerobjekten Courtage
addieren.

### Rechte Spalte — Käufer trägt die KNK (Normalfall)
- Kaufpreis = Ziel-€/m² × Wohnfläche
- Eigenkapital-Einsatz = KNK = Kaufpreis × KNK-Satz
- Darlehen = Kaufpreis

### Linke Spalte — 110 %, Verkäufer übernimmt die KNK
Der Kaufpreis wird so weit erhöht, dass nach Erstattung der KNK **netto der Zielpreis**
beim Verkäufer bleibt. Entscheidend ist die Division, nicht die Multiplikation:

```
Brutto-Kaufpreis = Ziel-Kaufpreis / (1 − KNK-Satz)
```

Bei 8,5 %: Faktor **1,0929** (nicht 1,085!). Gegenprobe zwingend rechnen:
`Brutto − Brutto × KNK-Satz = Ziel-Kaufpreis`.
Mit 1,085 gerechnet fehlen dem Verkäufer rund 0,8 % — bei 186.000 € sind das ca. 1.350 €.

- Kaufpreis = Zielpreis / (1 − Satz), zusätzlich als €/m² ausweisen
- Eigenkapital-Einsatz = 0 €
- Darlehen = Brutto-Kaufpreis (der Käufer finanziert den Preis, die KNK bekommt er erstattet)

## Rechenweg (beide Spalten identisch)

1. **Annuität** = Darlehen × (Zins + Tilgung) / 12
2. **Zinsanteil** (nur für die Steuer) = Darlehen × Zins / 12
3. **AfA** = AfA-Basis × Gebäudeanteil × AfA-Satz / 12
4. **Hausgeld nicht umlagefähig** = Kaltmiete × 20 % (Standard-Ansatz, sonst echten Wert nehmen)
5. **Steuerlicher Verlust** = Miete − Zins − AfA − Hausgeld
6. **Steuervorteil** = Verlust × Grenzsteuersatz
7. **Cashflow nach Steuer** = Miete − Hausgeld − Annuität + Steuervorteil

### AfA-Basis: der Unterschied zwischen den Spalten
- **Rechte Spalte:** `(Kaufpreis + KNK) × Gebäudeanteil` — die KNK sind Anschaffungs-
  nebenkosten des Käufers und damit abschreibbar.
- **Linke Spalte:** `Kaufpreis × Gebäudeanteil` — die KNK werden dem Käufer erstattet,
  sind für ihn also kein Aufwand. Konservativer Ansatz; die steuerliche Behandlung der
  Erstattung gehört in die Abstimmung mit dem Steuerberater und ist kein Exposé-Thema.

Beide Ansätze in der Fußnote nicht erklären — sie stehen hier für den internen Nachvollzug.

## Werte-Gate (Pflicht vor dem Gießen)

Diese Werte kommen von André, nie aus einer Schätzung:
Ziel-€/m² · Wohnfläche · Nettokaltmiete · Zins · Tilgung · Grenzsteuersatz ·
AfA-Satz · Gebäudeanteil · KNK-Satz · Hausgeld-Ansatz.

Der Text-Entwurf mit allen Zeilen und Beträgen wird im Chat freigegeben, bevor HTML
angefasst wird. Nach dem Gießen einmal gegen die Kalkulations-Excel des Objekts prüfen
(Reiter mit der VK-Rückrechnung) — die rechte Spalte muss die Excel-Zeile treffen.

## Wording-Leitplanken

„Beispielsberechnung" im Titel und in der Fußnote, nie „Rendite" oder „Garantie".
Werte gerundet, mit `ca.` bei abgeleiteten Größen. Fußnote nennt Zins, Tilgung, AfA-Satz,
Gebäudeanteil, Hausgeld-Ansatz und den Hinweis „Beispielsberechnung, Werte gerundet".

## Referenz-Zahlen Prosperstraße 3. OG (Stand 2026-07-31)

95,45 m² · Nettokaltmiete 833 €/Mo · Zins 4,5 % · Tilgung 1,0 % · AfA 5 % ·
Gebäudeanteil 79 % · Steuersatz 42 % · KNK 8,5 % · Hausgeld 20 % der Kaltmiete = 167 €

| | ohne EK (110 %) | mit EK |
|---|---|---|
| Kaufpreis | 203.437 € (2.131 €/m²) | 186.145 € (1.950 €/m²) |
| Eigenkapital | 0 € | ca. 15.800 € |
| Annuität | 932 €/Mo | 853 €/Mo |
| Steuervorteil | 322 €/Mo | 292 €/Mo |
| **Cashflow nach Steuer** | **+56 €/Mo** | **+106 €/Mo** |
