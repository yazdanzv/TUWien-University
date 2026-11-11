# Information Visualization — Group Assignment 01

TU Wien · Winter Semester 2026/27

## Organization

- `instructions/`: original assignment brief and supporting instructions.
- `working/data/`: raw, filtered, and merged datasets.
- `output/tools/`: preparation and report scripts, supporting tables, and render checks.
- `output/report/`: final deliverables, kept separate from working files.

See [plan.md](plan.md) for the candidate comparison, recommended merged schema,
measured coverage, assignment requirements, and next steps. The overview slide is
retained locally in `instructions/`; the detailed brief was supplied in the chat.
Follow the applicable course AI-use and attribution requirements.

## Datasets

The G1 report is available as an editable [Word document](output/report/group-assignment-01-report.docx)
and matching [PDF](output/report/group-assignment-01-report.pdf). It covers the topic,
audience, four candidates, selected dataset, and five initial research questions.
The step-by-step workflow and remaining team review tasks are in
[plan.md](plan.md#13-report-workflow-and-initial-research-questions).

| Stage | File | Rows | Columns |
| --- | --- | ---: | ---: |
| Raw OWID | [Original CSV](working/data/raw/owid-co2-data.csv) | 50,411 | Original schema |
| Raw WDI extract | [Consolidated CSV](working/data/raw/wdi_candidate_extract.csv) | 242,060 indicator records | 11 |
| Filtered OWID | [Selected economy–years](working/data/filtered/owid_filtered.csv) | 12,896 | 14 |
| Filtered WDI | [Selected economy–years](working/data/filtered/wdi_filtered.csv) | 11,347 | 13 |
| Merged | [CO₂ and WDI analysis dataset](working/data/merged/co2_wdi_merged.csv) | **10,874** | **26** |

The WDI extract contains 14 candidate indicators for 1960–2024, including nulls
and aggregates. It is not the complete WDI database. Original API JSON responses
and country metadata are preserved in `working/data/raw/`; the consolidated CSV
is a convenience export. Raw source snapshots are included in the repository alongside the filtered and merged datasets.

The merged data cover 202 economies during 1960–2024. Each row is an economy–year;
empty cells mean missing. Optional missing values are retained without imputation.
See the [data dictionary](output/tools/support/data_dictionary.csv),
[missingness table](output/tools/support/missing_values.csv), and
[build report](output/tools/support/build_report.json). Detailed filtering and selection
reasons are in [plan.md](plan.md#12-implemented-preparation-decisions-and-results).

## Reproduce

Python 3.9+; standard library only. From this assignment directory:

```sh
python3 output/tools/scripts/profile_datasets.py
python3 output/tools/scripts/build_dataset.py
```

The profiling script downloads missing original inputs and reuses existing raw
snapshots. The build produces filtered
data, the merge, and reports. Rebuilding replaces generated outputs, never the
original downloads. A fresh download may have a different source vintage and
different counts; retain the evaluated snapshots for exact reproduction.

Only publish course material, datasets, and group work when sharing is permitted.
Keep credentials and personal information out of this public repository.
