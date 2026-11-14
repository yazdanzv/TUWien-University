# Information Visualization — Group Assignment 01

TU Wien · Winter Semester 2026/27

## Organization

- `working/data/`: raw, filtered, and merged datasets.

The original instructions, other students' submissions, and shared group
deliverables are kept locally and omitted from this public repository pending
publication permission.

See [plan.md](plan.md) for the candidate comparison, recommended merged schema,
measured coverage, assignment requirements, and next steps. The overview slide is
retained locally in `instructions/`; the detailed brief was supplied in the chat.
Follow the applicable course AI-use and attribution requirements.

## Datasets

The step-by-step workflow and team review tasks are recorded in
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
Detailed filtering and selection reasons are in
[plan.md](plan.md#12-implemented-preparation-decisions-and-results). The data
dictionary and generated validation reports are kept locally with the group work.

## Reproduce

The raw and derived data snapshots are included here. The group's preparation
scripts and report are kept locally, so this public copy does not provide a
complete rebuild command. A fresh source download may have a different vintage
and produce different counts.

Only publish course material, datasets, and group work when sharing is permitted.
Keep credentials and personal information out of this public repository.
