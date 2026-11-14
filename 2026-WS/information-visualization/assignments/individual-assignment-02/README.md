# Individual Assignment 2

Yazdan ZandiyeVakili (12642780), Information Visualization VU, TU Wien.

The final submission is `output/report/individual-assignment-02.pdf`; the matching editable file is beside it. It contains RQ2 and RQ3 figures of different chart types. Two further figures and their write-ups are in `working/figures/` and `output/tools/supplementary/`.

The source CSV is `../group-assignment-01/working/data/merged/co2_wdi_merged.csv`. It is read but never changed. The full original assignment brief is kept locally in `instructions/` and omitted from the public repository.

The figure code is also available as `working/notebooks/individual-assignment-02-figures.ipynb`. It contains all four charts, marks the two selected for submission, and regenerates the same PNG files when its cells are run in order. A Markdown copy of the submission text, with links to the selected figures, is in `output/tools/individual-assignment-02.md`.

## Rebuild

Use the Codex bundled Python runtime with `pandas`, `numpy`, `python-docx`, and Matplotlib 3.10.7. Run:

```sh
PYTHONPATH=working/.deps /path/to/bundled/python3 output/tools/scripts/build_assignment.py
```

The script verifies the source panel, writes derived paired-year tables under `working/derived/`, creates four 300 dpi PNG figures under `working/figures/`, and writes the DOCX. Render that DOCX to PDF with the installed Documents skill renderer, then copy the checked PDF to `output/report/`. The local `.deps/` directory is ignored by Git and can be restored with `python3 -m pip install --target working/.deps matplotlib==3.10.7`.

After rebuilding the DOCX, run `output/tools/scripts/export_notebook_and_markdown.py` with the bundled Python to refresh the notebook and Markdown copy.

All endpoint comparisons use only economies with every required measure observed in both 2000 and 2021. Missing values are never set to zero or interpolated. The two selected RQ2 peer pairs are fully observed for 2000–2021. The income and energy-use thirds for RQ3 are formed within the exact 182-economy paired sample using 2000 values.
