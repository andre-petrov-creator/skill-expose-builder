"""Contact sheet per unit from objekt.json - the TB8 gate artefact (nothing is built).

Shows the planned slide order with photo thumbnails + photo numbers so Andre can approve
or correct the mapping BEFORE any render. Loop: show sheet -> passt / passt nicht /
anders -> adjust objekt.json -> new sheet -> build only after "passt".

    python contact_plan.py <objekt.json> --out <dir> [--img-dir <dir>]
"""
import argparse
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont, ImageOps

from objekt_config import Objekt

TW, RH, PAD, TEXTW = 260, 150, 10, 520


def rows_for(obj, unit):
    u = obj.units[unit]
    rezept = obj.fotos.get('titel_rezept', 'original')
    bilder = obj.folien.get('kontaktbogen_bilder', {})
    rows, n = [], 1
    for slot in obj.folge:
        if slot == 'titel':
            rows.append((f'{n} Titel', [f'img/{unit}/titel.jpg'],
                         f'{obj.fotos["titel"][unit]} · {rezept}'))
        elif slot == 'abschluss':
            rows.append((f'{n} Abschluss', [], 'dunkle Schlussseite'))
        elif slot == 'stammdaten':
            rows.append((f'{n} Stammdaten', [], 'Datenfolie'))
        elif slot == 'ausstattung':
            for title, refs in obj.folien.get('ausstattung', []):
                rows.append((f'{n} {title}', [obj.photo_rel(unit, r) for r in refs],
                             ' + '.join(str(r).split('/')[-1] for r in refs)))
                n += 1
            continue
        elif slot == 'raeume':
            for r in u.get('rooms', []):
                rows.append((f'{n} {r[0]}', [obj.photo_rel(unit, x) for x in r[1]],
                             ' + '.join(str(x) for x in r[1])))
                n += 1
            continue
        elif slot == 'hausgarten':
            hg = obj.folien['hausgarten']
            rows.append((f'{n} {hg["titel"]}', [obj.photo_rel(unit, p) for p in hg['fotos']],
                         ' + '.join(str(p).split('/')[-1] for p in hg['fotos'])))
        elif slot == 'treppenhaus':
            refs = obj.folien.get('treppenhaus', [])
            rows.append((f'{n} Treppenhaus', [obj.photo_rel(unit, r) for r in refs],
                         ' + '.join(str(r).split('/')[-1] for r in refs)))
        else:
            title = obj.folien['base_slides'][slot]
            foto = obj.folien.get('datenfolien_fotos', {}).get(title)
            img = [foto[0]] if foto else ([bilder[slot]] if slot in bilder else [])
            note = foto[0].split('/')[-1] if foto else ('Datenfolie' if not img else img[0])
            if slot == 'grundriss' and u.get('grundriss'):
                img, note = [u['grundriss']], u['grundriss'].split('/')[-1]
            rows.append((f'{n} {title}', img, note))
        n += 1
    return rows


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('config')
    ap.add_argument('--out', required=True)
    ap.add_argument('--img-dir', help='dir that img/ paths are relative to (default: <objekt>/expose)')
    a = ap.parse_args()
    obj = Objekt(a.config)
    base = Path(a.img_dir) if a.img_dir else obj.expose_dir
    out_dir = Path(a.out)
    out_dir.mkdir(parents=True, exist_ok=True)
    try:
        font = ImageFont.truetype('arialbd.ttf', 20)
        font2 = ImageFont.truetype('arial.ttf', 18)
    except OSError:
        font = font2 = ImageFont.load_default()

    for unit, u in obj.units.items():
        rows = rows_for(obj, unit)
        canvas = Image.new('RGB', (TEXTW + 3 * (TW + PAD) + 2 * PAD, len(rows) * (RH + PAD) + PAD + 50),
                           'white')
        draw = ImageDraw.Draw(canvas)
        draw.text((PAD, PAD), f'Kontaktbogen · {u["label"]} · {len(rows)} Folien', fill='black', font=font)
        y = 50
        for title, imgs, note in rows:
            draw.text((PAD, y + 8), title, fill='black', font=font)
            draw.text((PAD, y + 38), note, fill='#666666', font=font2)
            x = TEXTW
            for p in imgs:
                fp = Path(p) if Path(p).is_absolute() else base / p
                if not fp.exists():
                    draw.text((x, y + 8), f'FEHLT: {p}', fill='red', font=font2)
                    x += TW + PAD
                    continue
                im = Image.open(fp)
                im.draft('RGB', (TW * 2, TW * 2))
                im = ImageOps.exif_transpose(im).convert('RGB')
                im.thumbnail((TW, RH))
                canvas.paste(im, (x, y))
                draw.rectangle([x - 1, y - 1, x + im.width, y + im.height], outline='#999999')
                x += TW + PAD
            draw.line([(PAD, y + RH + PAD // 2), (canvas.width - PAD, y + RH + PAD // 2)], fill='#DDDDDD')
            y += RH + PAD
        out = out_dir / f'KONTAKTBOGEN_{unit}.png'
        canvas.save(out)
        print(out, len(rows), 'Folien')


if __name__ == '__main__':
    main()
