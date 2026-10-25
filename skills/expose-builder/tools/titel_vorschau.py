"""Cover colour-grade preview for the TB6 gate: one montage a/b/c/d per candidate photo.

a = original, b = gamma only (brighter, neutral), c = clean #04 (neutral white, wet rooms),
d = warm-cozy #08. Andre picks one letter; the chosen recipe then applies to ALL cover
photos of the property (objekt.json fotos.titel_rezept), every other photo stays original.

    python titel_vorschau.py <foto> <out.png> [--height 700]
"""
import argparse
import tempfile
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont, ImageOps

from warm_cozy_photos import optimize

VARIANTS = [('a Original', None), ('b Gamma', 'gamma'), ('c Clean #04', 'clean'),
            ('d Warm-Cozy #08', 'warm-cozy')]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('src')
    ap.add_argument('out')
    ap.add_argument('--height', type=int, default=700)
    ap.add_argument('--magick', default='magick')
    a = ap.parse_args()
    src = Path(a.src)
    pad, label_h = 10, 44
    try:
        font = ImageFont.truetype('arialbd.ttf', 26)
    except OSError:
        font = ImageFont.load_default()

    tiles = []
    with tempfile.TemporaryDirectory() as td:
        for label, profile in VARIANTS:
            if profile is None:
                im = ImageOps.exif_transpose(Image.open(src)).convert('RGB')
            else:
                tmp = Path(td) / f'{profile}.jpg'
                optimize(src, tmp, profile, a.magick)
                im = Image.open(tmp).convert('RGB')
            im.thumbnail((a.height * 4, a.height))
            tiles.append((label, im))

    w = sum(im.width for _, im in tiles) + pad * (len(tiles) + 1)
    h = label_h + max(im.height for _, im in tiles) + pad * 2
    canvas = Image.new('RGB', (w, h), 'white')
    draw = ImageDraw.Draw(canvas)
    x = pad
    for label, im in tiles:
        draw.text((x, pad), label, fill='black', font=font)
        canvas.paste(im, (x, label_h))
        draw.rectangle([x - 1, label_h - 1, x + im.width, label_h + im.height], outline='#999999')
        x += im.width + pad
    canvas.save(a.out)
    print(a.out)


if __name__ == '__main__':
    main()
