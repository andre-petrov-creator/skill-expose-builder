# Referenz: Seite „Angaben zur Wohnung" (Feldkatalog + Prozess)

Gehört zum **Wohnungs-Teil** (je Einheit, ein PDF pro Wohnung). Reihenfolge im Exposé:
… Gebäude-Technik & Zustand → **Grundriss** (eigene Seite, großer Platzhalter + Lead-Zeile
„Wohnung X · Zimmer · m² · Lage") → **Angaben zur Wohnung** → Raum-/Foto-Seiten.

## Harte Regel: keine Finanzangaben auf dieser Folie

**Bewusst NICHT auf „Angaben zur Wohnung":** Kaltmiete, Jahresmiete, Hausgeld, nicht
umlagefähige Kosten, Rücklagen-Anteil der Einheit, Kaufpreis, €/m², Marktpreis, Faktor. Das
Exposé ist Präsentationsgrundlage — Zahlen zu Miete/Preis kommen im Gespräch bzw. in der
Kalkulation. Geldzahlen stehen im Exposé nur auf den Ausnahmen laut SKILL.md
(7a Stammdaten der Wohnung mit Miete/Hausgeld/MEA/Grundbuch — direkt nach dieser Folie,
7b Immobilienbewertung-Screenshot nur auf Zuruf, 7c Beispielsberechnung).

## Layout: zwei Varianten (Foto-Frage vorab)

Im Skill-Lauf **vor** dem Bauen dieser Folie fragen (gilt genauso für Gebäude-Eckdaten und
Gebäude-Technik & Zustand): **„Hast du ein passendes Foto für diese Folie?"**

- **Variante A (ohne Foto):** 2-Spalten-Datenliste (`.datacols`/`.datalist__row`), vertikal
  zentriert, volle Breite.
- **Variante B (mit Foto):** Daten kompakt in **~40 % links** (`.splitflow`/`.splitdata`),
  rechts **~60 % Foto-Zone** (`.fotozone`) mit **bewusst winzigem** gestricheltem Marker
  (`.fotomark`) — das im PDF-Editor eingefügte Foto überdeckt ihn sicher. Bei Technik-Seite
  wandert die Energieausweis-Zeile inkl. Mini-Skala mit in die linke Spalte (gestapelt).
  Für „Angaben zur Wohnung" den Datenblock groß setzen (`.splitflow--wohn`: Spalte 120 mm,
  Werte 12,5 pt, Zeilen-Padding 3 mm).
- **Setzt der Skill das Foto selbst** (Bild nach Folien-Name vorhanden, siehe SKILL.md
  Foto-Konvention): `.splitflow--foto` — Bild absolut in der Foto-Zone
  (`position:absolute; inset:0; object-fit:cover`), Datenzeilen `justify-content:space-between`,
  `margin-bottom:7mm` + letzte Zeile ohne border → Bild schließt oben/unten bündig mit dem
  Textblock ab und bleibt über der Footer-Linie. Nie das Bild mit natürlicher Höhe in den
  Flow legen (sprengt die Seite).
- Muster beider Varianten stehen in `template/expose.html` (B-Versionen im Varianten-Anhang
  am Dateiende); im echten Exposé ersetzt B die A-Seite — nie beide.

## Feldkatalog

### Essentiell — immer aufs Blatt (auto-befüllen, sonst `[OFFEN]`)

| Feld | Beispiel-Wert |
|---|---|
| Lage im Haus (Etage + li/re/Mitte) | 2. OG · links |
| Wohnfläche | 68 m² |
| Zimmer | 3 Zimmer |
| Status (vermietet / Eigennutzung / leer) | vermietet |
| Miteigentumsanteil (MEA) — **bei WEG** | 112 / 1.000 |
| Sondereigentum / Sondernutzungsrecht — **bei WEG** | SE Whg. 4 · SNR TG-Platz 4 |

### Pflicht-Frage bei jeder Wohnung (seit 2026-07)

| Feld | Regel |
|---|---|
| Elektrik (Wohnung) · FI-Schalter | **IMMER fragen: „Aufnehmen?"** — Auswahloptionen anbieten (z. B. „FI-Schalter vorhanden", „Elektrik erneuert <Jahr>", „FI-Schalter + erneuerte Elektrik"). Nur bei Ja + Datenlage aufs Blatt. |

### Nice-to-have — nachfragen bzw. aus Ordner ziehen

| Feld | Beispiel-Wert |
|---|---|
| Aufteilung (Küche, Bad, WC-Anzahl) | Wohnküche · 1 Bad · Gäste-WC |
| Bad (Fenster / Wanne / Dusche) | Fensterbad · Wanne + Dusche |
| Balkon / Terrasse / Loggia (+ m²) | Balkon · ca. 6 m² |
| Bodenbelag | Parkett / Vinyl |
| Ausrichtung | Südwest |
| Stellplatz / Garage / TG (Nr.) | TG-Platz Nr. 4 |
| Keller- / Abstellraum | Kellerabteil vorhanden |
| Ausstattung (EBK, Einbauten) | EBK verbleibt |
| Zustand der Wohnung | teilrenoviert |

### Konditional
| Feld | Bedingung |
|---|---|
| bezugsfrei ab | nur bei leer / Eigennutzung |

## Prozess

1. Essentiell automatisch aus Objektdaten/Excel befüllen, Lücke = `[OFFEN]`.
2. Foto-Frage stellen → Variante A/B wählen.
3. Auto-Entwurf → **Angabe für Angabe** mit André festzurren (Wert-Gate).
4. Alles Vorhandene in den Entwurf aufnehmen; beim Durchgang wird gecuttet.
