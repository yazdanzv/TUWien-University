"""Export a runnable figure notebook and Markdown copy of the submission text."""

from __future__ import annotations

import json
from pathlib import Path
from docx import Document


ROOT = Path(__file__).resolve().parents[3]
SOURCE = ROOT / "output/tools/scripts/build_assignment.py"
DOCX = ROOT / "output/report/individual-assignment-02.docx"
NOTEBOOK = ROOT / "working/notebooks/individual-assignment-02-figures.ipynb"
MARKDOWN = ROOT / "output/tools/individual-assignment-02.md"
NOTEBOOK.parent.mkdir(parents=True, exist_ok=True)
MARKDOWN.parent.mkdir(parents=True, exist_ok=True)

script = SOURCE.read_text(encoding="utf-8")


def section(start: str, end: str) -> str:
    return script[script.index(start):script.index(end)].rstrip() + "\n"


def markdown_cell(cell_id: str, source: str) -> dict:
    return {"cell_type": "markdown", "id": cell_id, "metadata": {},
            "source": source.splitlines(keepends=True)}


def code_cell(cell_id: str, source: str) -> dict:
    return {"cell_type": "code", "id": cell_id, "metadata": {},
            "execution_count": None, "outputs": [],
            "source": source.splitlines(keepends=True)}


setup = '''from pathlib import Path
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

# Run from the notebook folder, assignment folder, or University workspace.
cwd = Path.cwd().resolve()
candidates = (cwd, *cwd.parents,
              cwd / "2026-WS/information-visualization/assignments/individual-assignment-02",
              cwd / "assignments/individual-assignment-02")
ROOT = next((p for p in candidates
             if (p / "instructions/original-assignment-brief.docx").exists()), None)
if ROOT is None:
    raise RuntimeError("Start Jupyter from individual-assignment-02, its subfolders, or University")
DATA = ROOT.parent / "group-assignment-01/working/data/merged/co2_wdi_merged.csv"
FIG = ROOT / "working/figures"
DERIVED = ROOT / "working/derived"
FIG.mkdir(parents=True, exist_ok=True)
DERIVED.mkdir(parents=True, exist_ok=True)
df = pd.read_csv(DATA)
assert df.shape == (10874, 26) and df.iso3.nunique() == 202
assert not df.duplicated(["iso3", "year"]).any()
assert (df.year.min(), df.year.max()) == (1960, 2024)
'''
setup += section('R2 = [', '# Figure 1:')

figure_1 = section('# Figure 1:', '# Figure 2:')
figure_2 = section('# Figure 2:', '# Baseline income')
grouping = section('# Baseline income', '# Figure 3:')
figure_3 = section('# Figure 3:', '# Figure 4:')
figure_4 = section('# Figure 4:', '# Compact machine-readable summary')

cells = [
    markdown_cell('intro', '''# Individual Assignment 2 figure notebook

This notebook regenerates the four standalone 300 dpi figures from the unchanged merged OWID–WDI CSV. Run the cells in order with Python 3 and `pandas`, `numpy` and `matplotlib`. The two selected submission figures are the RQ2 peer paths and the RQ3 change scatter; the other two are supplementary.

The 2000–2021 comparisons require every measure used by that question to be present at **both endpoints**. Missing values are not filled. RQ2 has 190 complete economy pairs; RQ3 has 182. Figures are saved under `working/figures/` and paired data under `working/derived/`.
'''),
    code_cell('setup', setup),
    markdown_cell('rq2-paths', '''## RQ2 selected figure  Peer paths

Estonia and Poland, then Romania and Türkiye, provide two illustrative pairs with fairly similar income and urban shares in 2000 but different later CO₂ paths. Each annual measure is indexed to its **own 2000 value = 100**. All selected series are checked for missing years.
'''),
    code_cell('figure-1', figure_1),
    markdown_cell('figure-1-image', '![RQ2 peer paths](../figures/rq2_peer_paths.png)\n'),
    markdown_cell('rq2-all', '''## RQ2 supplementary figure  All-economy endpoint changes

Each point represents one of the 190 economies with complete 2000 and 2021 values. Horizontal and vertical positions are percentage changes; colour is the urban-share change in percentage points.
'''),
    code_cell('figure-2', figure_2),
    markdown_cell('figure-2-image', '![RQ2 all-economy changes](../figures/rq2_all_economies_changes.png)\n'),
    markdown_cell('rq3-grouping', '''## RQ3 baseline groups

The RQ3 figures use the 182 economies with renewable share, carbon intensity, primary energy use per person and PPP GDP per person at both endpoints. Income and energy-use thirds are calculated from **2000 values within this sample**; they are not World Bank income classes. Both plotted changes equal **2021 value minus 2000 value**.
'''),
    code_cell('grouping', grouping),
    markdown_cell('rq3-scatter', '''## RQ3 selected figure  Endpoint-change scatter

Each dot is an economy, not a year. The x-axis is change in renewable share of **final** energy; the y-axis is change in CO₂ per unit of **primary** energy. Income panels and energy-use colours use 2000 baselines. The original year-by-year paths are not shown.
'''),
    code_cell('figure-3', figure_3),
    markdown_cell('figure-3-image', '![RQ3 endpoint-change scatter](../figures/rq3_changes_by_income.png)\n'),
    markdown_cell('rq3-heatmap', '''## RQ3 supplementary figure  Group median heatmap

Cell colour is the median 2000–2021 carbon-intensity change among economies in each 2000 income-by-energy-use group. Cell counts are printed because group sizes are uneven.
'''),
    code_cell('figure-4', figure_4),
    markdown_cell('figure-4-image', '![RQ3 income and energy heatmap](../figures/rq3_income_energy_heatmap.png)\n'),
]

notebook = {
    "cells": cells,
    "metadata": {"kernelspec": {"display_name": "Python 3", "language": "python", "name": "python3"},
                 "language_info": {"name": "python", "version": "3.12"}},
    "nbformat": 4,
    "nbformat_minor": 5,
}
NOTEBOOK.write_text(json.dumps(notebook, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")


def render_runs(paragraph) -> str:
    rendered = []
    for run in paragraph.runs:
        value = run.text
        if not value:
            continue
        rendered.append(f"*{value}*" if run.italic else value)
    return "".join(rendered)


document = Document(DOCX)
parts = []
figure_number = 0
for paragraph in document.paragraphs:
    if paragraph._p.xpath('.//a:blip'):
        figure_number += 1
        image_name = {1: 'rq2_peer_paths.png', 2: 'rq3_changes_by_income.png'}[figure_number]
        parts.append(f'![Figure {figure_number}](../../working/figures/{image_name})')
        continue
    content = render_runs(paragraph).strip()
    if not content:
        continue
    if paragraph.style.name == 'Title':
        content = '# ' + content
    elif paragraph.style.name.startswith('Heading 1'):
        content = '## ' + content
    elif paragraph.style.name == 'Explanation Section':
        content = '### ' + content
    parts.append(content)

assert figure_number == 2
MARKDOWN.write_text('\n\n'.join(parts) + '\n', encoding='utf-8')
print(f'Wrote {NOTEBOOK}')
print(f'Wrote {MARKDOWN}')
