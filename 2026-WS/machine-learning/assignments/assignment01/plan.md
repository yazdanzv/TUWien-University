# Exercise 0 implementation plan

Updated: 25 October 2026. Notebook explanations and report wording simplified;
code reviewed for readability while retaining the data checks and all eight figures.

## Agreed result

Two polished, executed Jupyter notebooks, one per dataset, and one concise report
based on their results. The report is editable in Word and exported to PDF.
Every code cell must have a useful Markdown explanation immediately before it.
All acquisition, analysis, validation, and plotting code belongs in the notebooks.

Group 56: Yazdan ZandiyeVakili, Amir Saadati, and Hani Esreb.

Selected datasets:

- MembershipWoes, OpenML 44225, version 2.
- Dermatology, UCI 33.

Keep the original assignment brief unchanged. The group manages registration,
deadline tracking, and submission. This plan replaces the earlier broader design.

## Minimal structure

```text
assignment01/
├── MachineLearning-2026W-exercise_dataset.pdf
├── plan.md
├── work/
│   ├── membershipwoes.ipynb
│   └── dermatology.ipynb
└── report/
    ├── Exercise0_Report.docx
    └── 56_ZandiyeVakili_Saadati_Esreb_Exercise0_Report.pdf
```

No helper classes, separate scripts, README, requirements file, exported tables,
figure folders, nested repository, or submission ZIP are part of this revision.
The notebooks download official source bytes into memory; they do not alter raw
data or leave downloaded files behind. Running them requires internet access.
Sources, checksums, dependencies, and setup instructions are recorded inside each
notebook. Temporary build, execution, and document-review files stay outside the
assignment folder. The assignment's final ZIP packaging remains a group task.

## Assignment requirements checklist

- [x] Identify all three contributors and group 56.
- [x] Explain why two classification datasets with contrasting characteristics
      were selected; diversity matters for grading.
- [x] Give sample, input, and target counts; distinguish identifiers from inputs.
- [x] Describe nominal, ordinal, quantitative, and temporal measurement types.
- [x] Show selected input distributions and target distributions.
- [x] Describe numeric ranges, missingness, and preprocessing implications.
- [x] Keep plotting code reproducible and exclude code from the written report.
- [x] Produce an approximately two-page report and correctly named PDF.
- [x] Verify results by executing both notebooks from fresh kernels.

No model training or performance comparison is required. Describe future
preprocessing without fitting imputers, scalers, or classifiers in this exercise.
Do not invent undocumented code meanings, currency units, or observation times.

## Notebook presentation standard

Each notebook has five short sections: setup, official data loading, attribute
types, missing values, and selected distributions. MembershipWoes includes an
end-date check within the analysis. Repeated final modelling advice is removed;
the report retains the required discussion of preprocessing.
Source references appear at the end. MembershipWoes has eleven code cells and
five figures; Dermatology has eight code cells and three figures. Repeated validation blocks, full category-code dumps,
manual Dermatology column definitions, and overlapping explanations are removed.

Before every code cell, explain what it computes and why. Use short, focused
cells with meaningful variable names. Display selected tables and figures rather
than logs, entire datasets, raw source documentation, or giant metadata dumps.
Follow important outputs with interpretations supported by computed values.
Figures need clear titles, units where documented, ordered categories, explicit
bins, and readable labels. Retain missingness and unusual values in the original
view; disclose any plotting transformation or omission of unavailable values.

## Implementation stages

### 1. Set up the notebooks

**Objective:** Establish the minimal structure and a consistent notebook style.

**Tools:** Python 3.12, pandas, NumPy, Matplotlib, liac-arff, Jupyter/ipykernel;
nbformat and nbclient for authoring and execution. Use a simple installation
command without version pins and record NumPy/pandas versions in notebook output.
The verification environment uses NumPy 2.3.5, pandas 2.2.3, Matplotlib 3.11.2,
ipykernel 7.4.0, and liac-arff 2.5.0 on Python 3.12. No dedicated notebook skill
is exposed in this session.

**Outputs:** Two `.ipynb` files. Dependencies are explained in introductory
Markdown, including a copyable installation command. No separate environment
files are delivered.

**Validation:** Valid notebook schema, Python kernel metadata, Markdown before
every code cell, and no external helper-code dependency.

**Issues:** ARFF contains strings, so use liac-arff instead of SciPy's parser.

### 2. Acquire and validate official sources

**Objective:** Read unchanged source bytes and establish dataset identity.

**Tools:** urllib, hashlib, io, liac-arff, and pandas.

**Outputs:** In-memory dataframes plus visible source identity/checksum output.
MembershipWoes comes from OpenML download 22106810. Dermatology uses UCI
33's header-labelled CSV, verified to contain exactly the same ordered values
and missingness as the original archive. Its documentation defines measurement
types and class labels.

**Dependencies:** Stage 1 and working internet access.

**Validation:** Expected source fingerprint, 10,362 by 15 MembershipWoes shape,
366 by 35 Dermatology shape, correct target labels, documented missing markers,
and correct attribute order. Stop on a changed source instead of silently
accepting a different snapshot.

**Issues:** Repository outages and missing code definitions; report uncertainty
rather than guess. Network access is required for a fresh run.

### 3. Inspect attributes and data quality

**Objective:** Establish dimensions, roles, measurement scales, numeric ranges,
missingness, unique identifiers, and duplicate profiles.

**Outputs:** Compact attribute/type tables, numeric summaries, missingness tables,
and relevant assertions in each notebook.

**Dependencies:** Validated source loading.

**Validation:** Counts and percentages reconcile; nominal codes are not treated
as measurements. Dermatology has 32 ordinal scores, binary family history, and
age. MembershipWoes separates quantities, nominal fields, dates, and identifier.

**Issues:** Unknown monetary units, high agent cardinality, unusual zero/extreme
values, date interpretation, and duplicates after identifier removal. Preserve
observations and explain concerns rather than deleting them automatically.

### 4. Explore distributions and preprocessing needs

**Objective:** Show class balance and selected informative features.

**Tools:** pandas, NumPy, and Matplotlib; static scientific figures need no
interactive visualization skill.

**Outputs:** Embedded target/age figures, MembershipWoes fee and payment-frequency
plots, and four approved diagrams: missing values by field, cancellation rate by
membership package, age distributions by disease, and 100% stacked distributions
for five ordinal clinical findings. The stacked chart replaces the earlier
single-finding/family-history chart; family-history counts remain in the output.
Overall age histograms and target plots remain available in both notebooks.
Explain package associations descriptively, without causal claims; label the
observed-age sample size for each disease and disclose missing ages. Use the
first five documented ordinal findings rather than selecting by association.

**Dependencies:** Stage 3.

**Validation:** Class counts sum to all rows; percentages sum to 100%; histogram
bins account for all observed values. State missing-value exclusions and log
transformations. Check date validity and end-date availability versus status.

**Issues:** MembershipWoes end-date availability may reveal outcome information;
exclude it in prospective modelling unless timing justifies its use. Dermatology
scores are ordered but equal intervals are not established; biopsy variables may
not be available in a clinical-only setting. Fit future learned preprocessing
only on training folds. Do not claim causal effects or missingness mechanisms.

### 5. Compare findings and write the report

**Objective:** Explain selection, contrast the datasets, and present the main
results in approximately two pages without code.

**Skills:** `documents:documents` for Word creation and render review;
`pdf:pdf` for PDF verification. These are installed and available. No skill
installation is needed; no spreadsheet or interactive artifact is required.

**Outputs:** Word report and matching PDF in `report/`. Reuse figures embedded in
the executed notebooks; do not recalculate analysis separately for the report.
The report includes all four approved diagrams, copied directly from notebook
PNG outputs. Dataset comparison is concise prose to preserve the two-page layout.

**Dependencies:** Both notebooks executed and inspected.

**Report content:** Group identification; selection rationale and comparison of
size/types; MembershipWoes characteristics, balance, distributions and leakage
concern; Dermatology characteristics, balance, distributions and preprocessing;
brief comparison and verified official source references.

**Validation:** Every number and interpretation traces to notebook output or
primary documentation. Both datasets receive meaningful coverage. Contributor
names are accurate; no invented division of work is added. Inspect every rendered
page for readable plots, complete tables, clipping, and page count.

**Issues:** Two-page limit requires selecting informative plots and concise prose.
Keep fuller analysis in the notebooks.

### 6. Final verification

**Objective:** Deliver only the agreed files in a reproducible, readable state.

**Tools:** Fresh-kernel notebook execution, nbformat validation, targeted data
assertions, and Word/PDF rendering with the bundled document runtime.

**Validation:** No error outputs or missing execution counts; every code cell has
a preceding explanation; all figures are embedded; checksums and actual versions
are recorded; report facts match outputs; PDF is two readable pages; original
brief remains unchanged. Inspect the final folder for unnecessary artifacts.

**Completion:** Both simplified notebooks were executed successfully, each code
cell has a preceding Markdown explanation, and the matching Word/PDF report was
rendered and checked on both pages. Registration, deadline, final ZIP packaging, and
TUWEL upload remain with the group.

### 7. Publish the assignment repository

**Objective:** Publish the approved deliverables in an assignment-only public
GitHub repository, as explicitly requested by the group.

**Tools:** Git and the installed GitHub CLI, using the authenticated `yazdanzv`
account and existing Git author identity. No new skill or dependency is required.

**Outputs:** Public repository `yazdanzv/machine-learning-exercise0`,
containing this plan, both executed notebooks, and the Word/PDF report. Maintain
its checkout outside University to avoid a redundant nested repository. The
original course brief stays in University and is excluded from publication.

**Dependencies:** Completed notebook and report validation.

**Validation:** Verify public visibility, remote commit and file list, matching
local/remote revisions, and a clean publishing checkout. Publish no University
history, temporary files, credentials, or unrelated course material.

**Issues:** Fresh notebook execution requires internet access to official data
sources; no raw datasets are redistributed. Registration and TUWEL submission
remain separate group tasks.
