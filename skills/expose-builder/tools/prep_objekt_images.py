"""Prepare expose images from the photographer's originals, driven by objekt.json (TB1).

Standard (STD-expose-foto-optimierung): no colour changes - the only exception is the
cover photo per unit, graded with the recipe chosen at the Farbabgleich gate (TB6:
original / gamma / clean / warm-cozy). Long side capped (default 3500 px = 300 dpi
across A4 landscape), JPEG quality 95, subsampling 0, ICC profile kept.

    python prep_objekt_images.py <objekt.json> [--out <img-dir>]
"""
import argparse
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

from PIL import Image, ImageOps

from objekt_config import Objekt

WARM_TOOL = Path(__file__).resolve().parent / 'warm_cozy_photos.py'


def find_src(orig_dir, pattern, nr):
    hits = sorted(orig_dir.glob(pattern.format(nr=nr)))
    assert len(hits) == 1, (nr, hits)
    return hits[0]


def save(source, dst, max_px):
    im = Image.open(source)
    icc = im.info.get('icc_profile')
    im = ImageOps.exif_transpose(im).convert('RGB')
    if max(im.size) > max_px:
        im.thumbnail((max_px, max_px), Image.LANCZOS)
    dst.parent.mkdir(parents=True, exist_ok=True)
    im.save(dst, quality=95, subsampling=0, icc_profile=icc)
    return im.size


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('config')
    ap.add_argument('--out', help='image output dir (default: <objekt>/expose/img)')
    a = ap.parse_args()

    obj = Objekt(a.config)
    f = obj.fotos
    orig = Path(f['orig_dir'])
    pattern = f.get('pattern', '{nr}*.jpg')
    max_px = f.get('max_px', 3500)
    rezept = f.get('titel_rezept', 'original')
    img = Path(a.out) if a.out else obj.expose_dir / 'img'

    for d in ['std', *f['units']]:
        shutil.rmtree(img / d, ignore_errors=True)

    for name, nr in f.get('std', {}).items():
        print(name, save(find_src(orig, pattern, nr), img / 'std' / f'{name}.jpg', max_px))
    for name, spec in f.get('extra', {}).items():
        print(name, save(Path(spec['src']), img / 'std' / f'{name}.jpg', max_px),
              spec.get('note', ''))

    for unit, nrs in f['units'].items():
        for nr in nrs:
            save(find_src(orig, pattern, nr), img / unit / f'{nr}.jpg', max_px)
        titel_src = find_src(orig, pattern, f['titel'][unit])
        if rezept == 'original':
            print(unit, 'titel original', save(titel_src, img / unit / 'titel.jpg', max_px))
        else:
            # grade the full-size original first, then cap like all others
            with tempfile.TemporaryDirectory() as td:
                tmp = Path(td) / 'titel_full.jpg'
                subprocess.run([sys.executable, str(WARM_TOOL), str(titel_src), str(tmp),
                                '--profile', rezept], check=True)
                print(unit, f'titel {rezept}', save(tmp, img / unit / 'titel.jpg', max_px))
        print(unit, len(nrs))


if __name__ == '__main__':
    main()
