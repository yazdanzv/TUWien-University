"""Build the selected moving-benchmark figures and auditable report inputs."""

import hashlib
import json
import sys
from html import escape
from itertools import product
from pathlib import Path

sys.dont_write_bytecode = True
from svg_helpers import INK, MUTED, TEAL, GRID, text, line, circle

BASE = Path(__file__).resolve().parents[2]
RAW = BASE / "working/data/raw/ilc_lvho07b_20261121T183016Z.json"
OUT = BASE / "working/figures"
EU_COLOR = "#6b687d"
YEARS = list(range(2015, 2026))
QUESTION = 'How differently do national rates and EU-relative measures portray the change in Austria’s housing cost overburden for the lowest-income fifth between 2015 and 2025?'


def canvas(parts, title, description, height):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="1280" height="{height}" '
            f'viewBox="0 0 1280 {height}" role="img" font-family="Arial, sans-serif">'
            f'<title>{escape(title)}</title><desc>{escape(description)}</desc>'
            f'<rect width="1280" height="{height}" fill="white"/>' + ''.join(parts) + '</svg>')


def path(points, color, width=4):
    coordinates = ' '.join(f'{x:.3f},{y:.3f}' for x, y in points)
    return f'<polyline points="{coordinates}" fill="none" stroke="{color}" stroke-width="{width}"/>'


def records():
    provenance = json.loads(RAW.with_suffix('.provenance.json').read_text())
    assert hashlib.sha256(RAW.read_bytes()).hexdigest() == provenance['sha256']
    dataset = json.loads(RAW.read_text())
    categories = [sorted(dataset['dimension'][key]['category']['index'],
                         key=dataset['dimension'][key]['category']['index'].get)
                  for key in dataset['id']]
    selected = []
    for position, combination in enumerate(product(*categories)):
        key = str(position)
        if key not in dataset['value']:
            continue
        row = dict(zip(dataset['id'], combination))
        if row['geo'] in {'AT', 'EU27_2020'} and row['quant_inc'] == 'QU1' and int(row['time']) in YEARS:
            row.update(value=dataset['value'][key], status=dataset.get('status', {}).get(key, ''))
            selected.append(row)
    assert len(selected) == 22 and all(not row['status'] for row in selected)
    assert all(row['freq'] == 'A' and row['unit'] == 'PC' for row in selected)
    return selected, provenance


def white_hat(at, eu):
    x = lambda year: 120 + (year - 2015) * 88
    y = lambda rate: 590 - rate / 40 * 370
    parts = [
        text(55, 65, "Austria’s relative position worsened,", 36, weight=700),
        text(55, 110, "mainly as the EU benchmark fell", 36, weight=700),
        text(55, 158, "Housing cost overburden · Lowest-income fifth · 2015–2025", 23, MUTED),
        text(120, 205, "Share within the lowest-income fifth (%)", 22, MUTED),
        text(760, 205, "● Austria", 22, TEAL, 700),
        text(960, 205, "■ EU-27", 22, EU_COLOR, 700),
    ]
    for tick in [0, 10, 20, 30, 40]:
        parts.extend([line(120, y(tick), 1000, y(tick), GRID, 1),
                      text(100, y(tick) + 7, str(tick), 22, MUTED, anchor="end")])
    for year in YEARS:
        parts.extend([line(x(year), 590, x(year), 598, MUTED, 1),
                      text(x(year), 628, str(year), 22, MUTED, anchor="middle")])
    for series, color, square in [(eu, EU_COLOR, True), (at, TEAL, False)]:
        parts.append(path([(x(year), y(series[year])) for year in YEARS], color))
        for year in YEARS:
            if square:
                parts.append(f'<rect x="{x(year)-5}" y="{y(series[year])-5}" width="10" height="10" fill="{color}"/>')
            else:
                parts.append(circle(x(year), y(series[year]), color, 5))
    parts.extend([
        text(135, y(eu[2015])-18, f"{eu[2015]:.1f}%", 23, EU_COLOR, 700),
        text(135, y(at[2015])+30, f"{at[2015]:.1f}%", 23, TEAL, 700),
        line(1000, y(at[2025]), 1040, 319, TEAL, 1.5),
        text(1050, 310, f"Austria {at[2025]:.1f}%", 23, TEAL, 700),
        text(1050, 338, "Net change +0.5 pp", 22, TEAL),
        line(1000, y(eu[2025]), 1040, 378, EU_COLOR, 1.5),
        text(1050, 390, f"EU-27 {eu[2025]:.1f}%", 23, EU_COLOR, 700),
        text(1050, 418, "Net change −10.4 pp", 22, EU_COLOR),
        text(55, 695, "The Austria–EU gap shifted by 10.9 percentage points", 29, weight=700),
        text(55, 736, "Austria minus EU: −9.5 points in 2015 → +1.4 in 2025", 23, MUTED),
    ])
    austria_change = at[2025] - at[2015]
    benchmark_contribution = eu[2015] - eu[2025]
    width = 1080
    split = width * austria_change / (austria_change + benchmark_contribution)
    parts.extend([
        f'<rect x="100" y="774" width="{split}" height="24" fill="{TEAL}"/>',
        f'<rect x="{100+split}" y="774" width="{width-split}" height="24" fill="{EU_COLOR}"/>',
        text(55, 843, "Austria’s rate rose: +0.5 pp", 23, TEAL, 700),
        text(635, 843, "EU’s fall adds +10.4 pp to the gap", 23, EU_COLOR, 700),
    ])
    return canvas(parts, "Austria and EU-27 lowest-income housing overburden rates, 2015–2025",
                  "Full annual rate paths and a decomposition of the endpoint gap change. Austria rises "
                  "0.5 percentage points; the EU falls 10.4 points. The relative index change is not the domestic rate change.", 880)


def black_hat(indices):
    x = lambda year: 120 + (year - 2015) * 88
    y = lambda value: 750 - (value - 90) / 70 * 420
    change = indices[2025] - 100
    parts = [
        text(55, 65, "Austria’s housing overburden index", 35, weight=700),
        text(55, 140, f"Up {change:.0f}% in a decade", 60, TEAL, 700),
        text(55, 190, "Lowest-income fifth · Austria ÷ EU-27 · 2015–2025", 23, MUTED),
        text(120, 285, "Index (2015 = 100)", 23, weight=700),
    ]
    for tick in range(90, 161, 10):
        parts.extend([line(120, y(tick), 1000, y(tick), MUTED if tick == 100 else GRID, 1.5 if tick == 100 else 1),
                      text(100, y(tick)+7, str(tick), 22, MUTED, anchor="end")])
    for year in YEARS:
        parts.extend([line(x(year), 750, x(year), 758, MUTED, 1),
                      text(x(year), 792, str(year), 22, MUTED, anchor="middle")])
    parts.append(path([(x(year), y(indices[year])) for year in YEARS], TEAL, 5))
    for year in YEARS:
        parts.append(circle(x(year), y(indices[year]), TEAL, 6))
    parts.extend([
        text(140, y(100)-20, "100", 25, TEAL, 700),
        text(1035, y(indices[2025])+10, f"{indices[2025]:.1f}", 34, TEAL, 700),
        text(55, 887, "Index = 100 × (Austria rate ÷ EU rate in year t) ÷ (Austria rate ÷ EU rate in 2015).", 22, MUTED),
    ])
    return canvas(parts, "Austria's EU-relative housing overburden index, 2015–2025",
                  "The Austria/EU rate ratio is indexed to 2015=100 and rises to 142.9. "
                  "This figure suppresses the constituent rate paths and visually foregrounds a 43% increase "
                  "in relative standing, which must not be mistaken for a 43% rise in Austria's domestic rate.", 920)


def main():
    selected, provenance = records()
    values = {(r['geo'], int(r['time'])):r['value'] for r in selected}
    assert len(values) == 22
    at = {year:values['AT',year] for year in YEARS}
    eu = {year:values['EU27_2020',year] for year in YEARS}
    ratios = {year:at[year]/eu[year] for year in YEARS}
    indices = {year:100*ratios[year]/ratios[2015] for year in YEARS}
    assert all(0 <= value <= 40 for value in [*at.values(), *eu.values()])
    assert all(90 <= value <= 160 for value in indices.values())
    assert abs(indices[2015]-100)<1e-10
    assert abs(indices[2025]-142.93760706094125)<1e-8
    gap_change = (at[2025]-eu[2025])-(at[2015]-eu[2015])
    assert abs(gap_change-10.9)<1e-8
    OUT.mkdir(parents=True,exist_ok=True)
    (OUT/'benchmark-white-hat.svg').write_text(white_hat(at,eu))
    (OUT/'benchmark-black-hat.svg').write_text(black_hat(indices))
    findings = {
        'status':'selected moving-benchmark direction; figures prepared for report layout',
        'shared_question':QUESTION,
        'scope':{'geo':['AT','EU27_2020'],'quant_inc':'QU1','years':YEARS,'freq':'A','unit':'PC'},
        'source_retrieved_at_utc':provenance['retrieved_at_utc'],
        'source_updated':json.loads(RAW.read_text())['updated'],
        'source_doi':'https://doi.org/10.2908/ILC_LVHO07B',
        'source_url':provenance['url'],'source_sha256':provenance['sha256'],
        'records':selected,
        'annual_values':[{'year':year,'austria_rate':at[year],'eu_rate':eu[year],
                         'austria_eu_ratio':ratios[year],'relative_index':indices[year],
                         'gap_pp':at[year]-eu[year]} for year in YEARS],
        'summary':{'austria_change_pp':at[2025]-at[2015],
                   'austria_relative_change_percent':100*(at[2025]/at[2015]-1),
                   'eu_change_pp':eu[2025]-eu[2015],
                   'eu_relative_change_percent':100*(eu[2025]/eu[2015]-1),
                   'relative_index_change_percent':indices[2025]-100,
                   'gap_change_pp':gap_change},
        'formulas':{'ratio':'AT_t / EU_t','index':'100 * ratio_t / ratio_2015',
                    'gap_decomposition':'delta(AT - EU) = delta AT - delta EU',
                    'ratio_change_factor':'(AT_2025 / AT_2015) / (EU_2025 / EU_2015)'},
        'figure_paths':{'white':'working/figures/benchmark-white-hat.png',
                        'black':'working/figures/benchmark-black-hat.png'},
        'white_hat_task':'Show both published annual rates and decompose the endpoint gap change.',
        'black_hat_task':'Foreground the indexed ratio, encouraging substitution of relative standing for domestic prevalence.',
        'report_status':'Four-page Word and PDF report with Conclusion on page 4; see submission/ and plan.md.',
        'limitations':['Endpoint decomposition is arithmetic, not causal.',
                       'The additive percentage-point gap decomposition does not decompose the relative ratio change.',
                       'Index 100 denotes the 2015 ratio, not parity with the EU.',
                       'EU aggregate includes Austria; the two series are not independent.',
                       'All annual paths are shown; endpoints do not establish steady change.',
                       'Source has no flags for these 22 observations, but no confidence intervals.',
                       'Constituent-country methodology changes may affect EU comparisons.'],
    }
    (BASE/'working/data/derived/benchmark_findings.json').write_text(json.dumps(findings,indent=2)+'\n')
    print('Built selected benchmark white/black SVG figures and auditable report inputs.')


if __name__ == '__main__':
    main()
