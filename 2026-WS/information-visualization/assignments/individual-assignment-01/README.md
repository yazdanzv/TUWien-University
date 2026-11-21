# Information Visualization — Individual Assignment 01

TU Wien · Winter Semester 2026/27 · Yazdan Zandiye Vakili · 12642780

Two static visualizations use the same Eurostat housing cost overburden data to
compare Austria with the EU-27 for the lowest-income fifth, 2015–2025. The white
hat figure shows both annual rates and the change in their gap. The black hat
figure presents an indexed comparison. The report explains the deceptive
framing separately in its Conclusion.

## Final reports

- [PDF report](submission/IA01_ZandiyeVakili_12642780_Report.pdf)
- [Editable Word report](submission/IA01_ZandiyeVakili_12642780_Report.docx)

The report has four pages: question and dataset, white hat visualization,
black hat visualization, and Conclusion. This folder contains prepared
submission files; it does not establish that they have been uploaded.

## Project files

- [Plan and decision record](plan.md): agreed scope, design, revision history and checks.
- `working/data/raw/`: unchanged Eurostat JSON extract and URL, retrieval time and SHA-256 provenance.
- `working/data/derived/benchmark_findings.json`: selected observations, calculations and limitations.
- `working/figures/`: the final SVG masters and high-resolution PNGs.
- `working/scripts/`: data inspection, figure generation, PNG rendering and Word authoring.
- `working/analysis-round-02.md`: historical candidate analysis; its exploration script is retained.
- `instructions/`: original course brief, kept locally and excluded from Git.

Source: [Eurostat Housing cost overburden rate by income quintile](https://doi.org/10.2908/ILC_LVHO07B).

## Reproduction

Run from this assignment directory. Python 3 is required; Word generation also
requires `python-docx`. PNG rendering requires Node.js and `sharp`. No network
access is needed to rebuild from the preserved extract.

```sh
python3 working/scripts/build_benchmark_figures.py
node working/scripts/render_figures.cjs /absolute/path/to/node_modules/sharp
python3 working/scripts/build_report.py
```

The figure builder verifies the source hash, completeness, flags, units, plot
ranges, relative index and gap arithmetic. The report builder checks the
200–500-word range for each figure description and writes the word-count record.

Export the Word file to PDF with Word or LibreOffice. During authoring, the
Codex documents skill’s `render_docx.py --emit_pdf` produced the matching PDF
and page images for visual inspection. Keep such temporary output under
`working/report-qa/` (ignored); copy only the reviewed final PDF to `submission/`.

Optional source inspection and exploratory reassessment:

```sh
python3 working/scripts/inspect_dataset.py working/data/raw/ilc_lvho07b_20261121T183016Z.json
python3 working/scripts/explore_round_02.py
```

The large exploration JSON is reproducible and excluded from Git. Superseded
one-year charts, their unused builders and temporary render previews have been
removed. Original course instructions and source data remain preserved.
