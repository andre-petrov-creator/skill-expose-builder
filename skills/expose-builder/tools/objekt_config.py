"""Shared loader for objekt.json - one config file per property (TB1, 21.10.2026).

The config lives in <objekt>/expose/_build/objekt.json and drives the generic tools
prep_objekt_images.py, build_objekt.py, check_objekt.py and contact_plan.py.
Slide order, rooms, photos, master data and acceptance targets all come from here;
no per-property build script is needed any more.
"""
import html
import json
from pathlib import Path

REZEPTE = ('original', 'gamma', 'clean', 'warm-cozy')

DEFAULT_FOLGE = ['titel', 'makro', 'mikro', 'eckdaten', 'technik', 'angaben', 'grundriss',
                 'stammdaten', 'ausstattung', 'raeume', 'hausgarten', 'treppenhaus', 'keller',
                 'abschluss']


class Objekt:
    def __init__(self, path):
        self.path = Path(path).resolve()
        self.cfg = json.loads(self.path.read_text(encoding='utf-8'))
        self.build_dir = self.path.parent
        self.expose_dir = self.build_dir.parent
        assert self.cfg['fotos'].get('titel_rezept', 'original') in REZEPTE

    @property
    def objekt(self):
        return self.cfg['objekt']

    @property
    def fotos(self):
        return self.cfg['fotos']

    @property
    def folien(self):
        return self.cfg['folien']

    @property
    def units(self):
        return self.cfg['units']

    @property
    def soll(self):
        return self.cfg['soll']

    @property
    def folge(self):
        return self.folien.get('folge', DEFAULT_FOLGE)

    @property
    def font(self):
        return self.soll.get('font', 'Calibri')

    def photo_rel(self, unit, ref):
        """A room photo ref is a number (unit folder) or a 'std/...' style string."""
        return f'img/{ref}.jpg' if isinstance(ref, str) else f'img/{unit}/{ref}.jpg'

    def base_slide_title(self, slot):
        return self.folien['base_slides'].get(slot)

    def slot_titles(self, slot, unit):
        u = self.units[unit]
        if slot == 'titel':
            return ['Exposé']
        if slot == 'abschluss':
            return [self.soll['closing_title']]
        if slot == 'stammdaten':
            return ['Stammdaten der Wohnung']
        if slot == 'ausstattung':
            return [t for t, _ in self.folien.get('ausstattung', [])]
        if slot == 'raeume':
            return [r[0] for r in u.get('rooms', [])]
        if slot == 'hausgarten':
            return [self.folien['hausgarten']['titel']] if self.folien.get('hausgarten') else []
        if slot == 'treppenhaus':
            return ['Treppenhaus'] if self.folien.get('treppenhaus') else []
        base = self.base_slide_title(slot)
        return [base] if base else []

    def soll_titles(self, unit):
        out = []
        for slot in self.folge:
            out += self.slot_titles(slot, unit)
        return out

    def soll_pages(self, unit):
        return self.units[unit].get('pages') or len(self.soll_titles(unit))


def esc(text):
    """Plain config text -> the HTML spelling used in <h2> headings."""
    return html.escape(text, quote=False)
