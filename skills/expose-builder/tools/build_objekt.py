"""Build one expose HTML per unit from objekt.json + the unit's base HTML (TB1).

Generic successor of the Herten part-A build script (reference: <Herten>/expose/_build/
build.py, decision list v1 21.10.2026). Encoded standards: Calibri as the only font
family (TB7), contact-only footer with the company address on the closing page only (F1),
slide order per objekt.json 'folge' (STD-expose-folienfolge-bildzuordnung), Stammdaten
slide per unit, 'Haus & Garten' layout A, assertions against the acceptance targets.

    python build_objekt.py <objekt.json> [--out <dir>] [--units eg-links,eg-rechts]
"""
import argparse
import html
import re
from pathlib import Path

from PIL import Image

from objekt_config import Objekt, esc

V1_CSS = '''
/* v1 (21.10.2026): __FONT__ as the only family (T1/TB7); artificial-bold footer and the
   Courier bullet on the closing page are gone with it (.ey dot drawn in CSS, no glyph) */
.page{--serif:"__FONT__ Light",__FONT__,sans-serif;--body:__FONT__,sans-serif;--mono:__FONT__,sans-serif}
.ey::before{content:"";display:inline-block;width:1.6mm;height:1.6mm;border-radius:50%;
  background:var(--accent);margin-right:2mm;vertical-align:1pt}
/* v1 (S1b): "Haus & Garten" layout A - front elevation large, back + garden stacked right */
.hg{flex:1;min-height:0;display:flex;align-items:center;justify-content:center;margin:4mm 0 8mm}
.hg__grid{display:grid;gap:6mm;grid-template-columns:175mm 84mm;grid-template-rows:55.5mm 55.5mm}
.hg__grid img{width:100%;height:100%;object-fit:cover;display:block;border:1pt solid var(--rule)}
.hg__grid img:first-child{grid-row:1/3}
.roomflow--2{gap:8mm}
.roomflow--2 img{height:100%;width:auto;max-width:calc(50% - 4mm);object-fit:cover}
.roomflow--2q{gap:8mm}
.roomflow--2q img{width:calc(50% - 4mm);height:auto;max-height:100%;aspect-ratio:3/2;object-fit:cover}
.roomflow--eng{gap:3mm}
.roomflow--eng img{max-width:calc(50% - 1.5mm)}
.wohnsplit{flex:1;min-height:0;display:grid;grid-template-columns:1.25fr 1fr;column-gap:10mm;margin:4mm 0 9mm}
.wohnsplit__data{display:flex;flex-direction:column;justify-content:center}
.wohnsplit .colhead{align-self:flex-start;margin-bottom:2.5mm}
.wohnsplit .colhead--2{margin-top:7mm}
.wohnsplit .datalist__row{padding:1.5mm 0;gap:6mm}
.wohnsplit .datalist__label{flex:none}
.wohnsplit__foto{position:relative;overflow:hidden;border:1pt solid var(--rule)}
.wohnsplit__foto img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover}
.splitflow--dicht .iconrow{padding-top:.85mm;padding-bottom:.85mm}
.stamm{flex:1;display:grid;grid-template-columns:1fr 1fr;column-gap:14mm;margin:5mm 0 9mm}
.stamm .colhead{margin-bottom:1.5mm}
.stamm .datalist__row{padding:2.1mm 0;gap:6mm}
.stamm .datalist__label{flex:none;max-width:42mm}
.stamm .datalist__val{font-size:9.8pt}
.stamm__note{font-family:var(--mono);font-size:6.4pt;letter-spacing:.08em;color:var(--muted);margin-top:3mm}
</style>'''

WOHNSPLIT_OLD_HEAD = '''  <div class="wohnflow">
    <div class="datacols">
      <div class="eckpanel">
        <div class="colhead">Die Wohnung</div>'''
WOHNSPLIT_NEW_HEAD = '''  <div class="wohnsplit">
    <div class="wohnsplit__data">
        <div class="colhead">Eckdaten</div>'''
WOHNSPLIT_OLD_MID = '''      </div>

      <div class="eckpanel">
        <div class="colhead">Ausstattung &amp; Zustand</div>'''
WOHNSPLIT_NEW_MID = '''        <div class="colhead colhead--2">Ausstattung &amp; Zustand</div>'''
WOHNSPLIT_OLD_TAIL = '''      </div>
    </div>
  </div>
'''
WOHNSPLIT_NEW_TAIL = '''    </div>
    <div class="wohnsplit__foto"><img src="{src}" alt="{alt}"></div>
  </div>
'''

MARKER_RX = re.compile(r'(<!-- ={5} .*? ={5} -->\n?)')


def rep(s, old, new, count=1):
    n = s.count(old)
    assert n == count, f'{old[:60]!r}: expected {count}, found {n}'
    return s.replace(old, new)


class Builder:
    def __init__(self, obj, out_dir):
        self.obj = obj
        self.out = out_dir

    def foot(self):
        return ('  <div class="brandfoot">\n    <span></span>\n'
                f'    <span>{self.obj.objekt["kontakt"]}</span>\n  </div>')

    def photos(self, unit, refs, alt, mod=None):
        rels = [self.obj.photo_rel(unit, r) for r in refs]
        ims = [Image.open(self.out / r) for r in rels]
        if len(rels) == 1:
            cls = 'roomflow'
        else:
            cls = 'roomflow roomflow--2q' if all(i.width > i.height for i in ims) else 'roomflow roomflow--2'
        if mod:
            cls += f' roomflow--{mod}'
        return (f'<div class="{cls}">'
                + ''.join(f'<img src="{r}" alt="{alt}">' for r in rels) + '</div>')

    def slide(self, meta, logo, title, inner, comment):
        return f'''<!-- ===== {comment} ===== -->
<section class="page section">
  <div class="runhead">
    {logo}
    <div class="runhead__meta">{meta}</div>
  </div>
  <div class="section__head"><h2>{title}</h2><div class="h2rule"></div></div>
  {inner}
{self.foot()}
</section>

'''

    def stammdaten_slide(self, meta, logo, unit):
        u = self.obj.units[unit]['stammdaten']

        def row(label, value):
            return (f'      <div class="datalist__row"><span class="datalist__label">{label}</span>'
                    f'<span class="datalist__val">{value}</span></div>')

        inner = f'''<div class="stamm">
    <div>
      <div class="colhead">Grundbuch &amp; Recht</div>
{chr(10).join(row(*r) for r in u['left'])}
    </div>
    <div>
      <div class="colhead">Wohnung &amp; Bewirtschaftung</div>
{chr(10).join(row(*r) for r in u['right'])}
      <div class="stamm__note">Quellen: {u['sources']}</div>
    </div>
  </div>'''
        return self.slide(meta, logo, 'Stammdaten der Wohnung', inner,
                          'SEITE 7a · STAMMDATEN DER WOHNUNG')

    def split_base(self, s):
        tokens = MARKER_RX.split(s)
        prefix, chunks = tokens[0], []
        for i in range(1, len(tokens) - 1, 2):
            chunks.append([tokens[i], tokens[i + 1]])
        body_end = chunks[-1][1].rfind('</body>')
        suffix = chunks[-1][1][body_end:]
        chunks[-1][1] = chunks[-1][1][:body_end]
        slots, dropped = {}, 0
        rev = {v: k for k, v in self.obj.folien['base_slides'].items()}
        for marker, content in chunks:
            if 'roomflow--leer' in content:
                dropped += content.count('<section')
                continue
            m = re.search(r'<h2>(.*?)</h2>', content)
            if m:
                plain = html.unescape(m.group(1))
                assert plain in rev, f'unknown base slide {plain!r} ({marker.strip()})'
                slots[rev[plain]] = marker + content
            elif 'cover' in content:
                slots['titel'] = marker + content
            elif 'closing' in content:
                slots['abschluss'] = marker + content
            else:
                raise AssertionError(f'unclassified base slide: {marker.strip()}')
        return prefix, slots, suffix, dropped

    def build_unit(self, unit):
        obj = self.obj
        u = obj.units[unit]
        s = (obj.build_dir / u['base']).read_text(encoding='utf-8')
        assert 'img/std/' not in s and 'Stammdaten der Wohnung' not in s
        meta = re.search(r'<div class="runhead__meta">([^<]+)</div>', s).group(1)
        logo = re.search(r'<img src="brand/[^"]+" alt="[^"]*">', s).group(0)
        base_sections = s.count('<section class="page')

        s = rep(s, '</style>', V1_CSS.replace('__FONT__', obj.font))
        s = rep(s, '<meta charset="utf-8">',
                f'<meta charset="utf-8">\n<title>{obj.objekt["titel_prefix"]} – {u["label"]}</title>')
        s, n = re.subn(r'(class="cover__foto" style="background:url\()img/[^)]+(\))',
                       rf'\g<1>img/{unit}/titel.jpg\g<2>', s)
        assert n == 1, n
        firma, kontakt = obj.objekt['firma'], obj.objekt['kontakt']
        s, n_foot = re.subn(
            rf'<div class="brandfoot">\s*<span><b>{re.escape(firma)}</b>[^<]*</span>\s*'
            rf'<span>{re.escape(kontakt)}</span>\s*</div>',
            self.foot().strip(), s)
        assert n_foot == base_sections - 1, (n_foot, base_sections)
        for old, new, *c in obj.cfg.get('replace', []) + u.get('replace', []):
            s = rep(s, old, new, c[0] if c else 1)

        prefix, slots, suffix, dropped = self.split_base(s)

        wf = obj.folien.get('wohnsplit_foto')
        if wf and 'angaben' in slots and 'wohnsplit' not in slots['angaben']:
            w = slots['angaben']
            w = rep(w, WOHNSPLIT_OLD_HEAD, WOHNSPLIT_NEW_HEAD)
            w = rep(w, WOHNSPLIT_OLD_MID, WOHNSPLIT_NEW_MID)
            w = rep(w, WOHNSPLIT_OLD_TAIL, WOHNSPLIT_NEW_TAIL.format(src=wf[0], alt=wf[1]))
            slots['angaben'] = w
        if u.get('grundriss'):
            slots['grundriss'], n = re.subn(r'src="img/[^"]+"', f'src="{u["grundriss"]}"',
                                            slots['grundriss'])
            assert n == 1, n
        for title, (src, alt) in obj.folien.get('datenfolien_fotos', {}).items():
            slot = {v: k for k, v in obj.folien['base_slides'].items()}[title]
            slots[slot], n = re.subn(r'<img src="img/[^"]+" alt="[^"]*">',
                                     f'<img src="{src}" alt="{alt}">', slots[slot])
            assert n == 1, (title, n)

        parts = [prefix]
        for slot in obj.folge:
            if slot in slots:
                parts.append(slots.pop(slot))
            elif slot == 'stammdaten':
                parts.append(self.stammdaten_slide(meta, logo, unit))
            elif slot == 'ausstattung':
                for title, refs in obj.folien.get('ausstattung', []):
                    parts.append(self.slide(meta, logo, esc(title),
                                            self.photos(unit, refs, title),
                                            f'AUSSTATTUNG · {title.upper()}'))
            elif slot == 'raeume':
                for r in u.get('rooms', []):
                    parts.append(self.slide(meta, logo, r[0],
                                            self.photos(unit, r[1], r[0],
                                                        r[2] if len(r) > 2 else None),
                                            f'RAUM · {r[0].upper()}'))
            elif slot == 'hausgarten':
                hg = obj.folien['hausgarten']
                assert hg.get('layout', 'a') == 'a', hg
                imgs = ''.join(f'<img src="{self.obj.photo_rel(unit, p)}" alt="{hg["titel"]}">'
                               for p in hg['fotos'])
                parts.append(self.slide(meta, logo, esc(hg['titel']),
                                        f'<div class="hg"><div class="hg__grid">{imgs}</div></div>',
                                        f'GEBÄUDE-FOLIE · {hg["titel"].upper()}'))
            elif slot == 'treppenhaus':
                refs = obj.folien.get('treppenhaus')
                if refs:
                    parts.append(self.slide(meta, logo, 'Treppenhaus',
                                            self.photos(unit, refs, 'Treppenhaus'),
                                            'GEBÄUDE-FOLIE · TREPPENHAUS'))
            else:
                raise AssertionError(f'folge slot {slot!r} missing in base and not buildable')
        assert not slots, f'unused base slides: {list(slots)}'
        parts.append(suffix)
        s = ''.join(parts)

        self.check_unit(unit, s)
        out = self.out / f'expose_{unit}.html'
        out.write_text(s, encoding='utf-8')
        titles = re.findall(r'<h2>(.*?)</h2>', s)
        print(unit, s.count('<section class="page'), 'pages:',
              ' | '.join(html.unescape(t) for t in titles))
        return out

    def check_unit(self, unit, s):
        obj = self.obj
        for f in set(re.findall(r'(?:src="|url\()(img/[^")]+)', s)):
            assert (self.out / f).exists(), f
        # a missing linked stylesheet still renders - as a many-page overflow PDF
        for f in re.findall(r'<link rel="stylesheet" href="([^"]+)"', s):
            assert (self.out / f).exists(), f'missing stylesheet {f}'
        titles = [html.unescape(t) for t in re.findall(r'<h2>(.*?)</h2>', s)]
        want = [t for slot in obj.folge if slot not in ('titel', 'abschluss')
                for t in obj.slot_titles(slot, unit)]
        assert titles == want, (titles, want)
        for t in obj.soll.get('verbotene_titel', []):
            assert t not in titles, t
        assert 'roomflow--leer"' not in s
        for needle in obj.soll.get('pflicht_text', []):
            assert needle in s, needle
        for needle in obj.soll.get('verboten_text', []):
            assert needle not in s, needle
        for needle in obj.soll.get('firmen_marker', []):
            assert s.count(needle) == 1, (needle, s.count(needle))
        sections = s.count('<section class="page')
        assert s.count(obj.objekt['kontakt']) == sections - 1
        assert sections == obj.soll_pages(unit), (sections, obj.soll_pages(unit))
        for other, v in obj.units.items():
            if other != unit:
                assert f'· {v["label"]}</div>' not in s, f'foreign unit label {v["label"]} in {unit}'


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('config')
    ap.add_argument('--out', help='output dir with img/ + brand/ (default: <objekt>/expose)')
    ap.add_argument('--units', help='comma-separated subset')
    a = ap.parse_args()
    obj = Objekt(a.config)
    out = Path(a.out) if a.out else obj.expose_dir
    b = Builder(obj, out)
    for unit in (a.units.split(',') if a.units else obj.units):
        b.build_unit(unit)


if __name__ == '__main__':
    main()
