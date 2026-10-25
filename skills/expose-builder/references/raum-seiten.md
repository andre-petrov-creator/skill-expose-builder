# Referenz: Raum-Seiten (Foto-Folien) + Auto-Foto-Test

Gehört zum **Wohnungs-Teil**. Reihenfolge im Exposé (fixiert):
… Gebäude-Technik & Zustand → **Grundriss** → **Angaben zur Wohnung** → **Raum-Seiten** → Abschluss.

## Raum-Set (feste Reihenfolge)

Wohnzimmer · Küche · Bad · Flur · Abstellkammer · Schlafzimmer 1–5 · Balkon.
Überzählige Folien löscht André im PDF-Editor.

## Layout-Regel (verbindlich)

- Jede Raum-Folie = **nur Rahmen**: Running Head, Headline (Raumname) + roter Unterstrich,
  Brand-Footer, Wasserzeichen. **Fläche komplett leer.**
- **KEINE Foto-Markierung, kein Platzhalter-Hinweis** — André platziert 1–3 Fotos frei
  im PDF-Editor (Anzahl variiert pro Raum, er braucht die Freiheit).
- **Wasserzeichen bleibt** (füllt Restfläche bei nur einem Foto, 4 % stört nie).

## Platzier-Spickzettel (für André, manuelle Variante)

- Seitenränder wie Layout: ~16 mm links/rechts; unten über der Footer-Linie enden.
- Bei 2 Fotos: ~8 mm Lücke; an der Headline-Kante ausrichten.
- 2–3 feste Muster verwenden (1 groß / 2 nebeneinander / 1+2), dann wirkt die Serie designed.

## Auto-Foto-Test (am Ende des Skill-Laufs, Pflicht-Schritt)

Nach dem ersten kompletten Exposé-Lauf einen **Test der automatischen Foto-Platzierung** machen:

1. André legt Fotos pro Raum in den Objektordner (Benennung z. B. `wohnzimmer-1.jpg`,
   `bad-1.jpg`, `bad-2.jpg` …).
2. Skill/`build_expose.py` setzt die Bilder **automatisch auf die richtige Raum-Folie**:
   richtige Größe, Ränder ~16 mm, Lücke ~8 mm, zentriert/gemittelt (1 Foto = groß mittig,
   2 Fotos = nebeneinander, 3 = 1+2-Raster).
3. Ergebnis als PNG-Serie zeigen → André bewertet.
4. **Gut** → Auto-Platzierung wird Standard-Weg (PDF-Editor nur noch für Sonderfälle).
   **Zu viel Nacharbeit** → verworfen; André fügt Fotos weiterhin manuell ein
   (PDF-Editor/PowerPoint), Folien bleiben leer wie oben.

## Varianten-Kennzeichnung im Master

Die B-Versionen der Datenseiten (Eckdaten / Technik & Zustand / Angaben zur Wohnung,
Daten 40 % links + Foto rechts) stehen im Master-Template als Anhang und tragen das Label
`.vartag` („Varianten-Muster B · mit Foto"). **Label nur in der Master-Vorschau** — im
echten Exposé wird die gewählte Variante ohne Label gerendert, nie beide Varianten.
