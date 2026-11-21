# Individual Assignment 01 plan and decision record

Updated: 21 November 2026

## Current scope

- **Topic:** housing affordability and inequality.
- **Question:** How differently do national rates and EU-relative measures portray the change in Austria’s housing cost overburden for the lowest-income fifth between 2015 and 2025?
- **Dataset:** Eurostat EU-SILC, Housing cost overburden rate by income quintile (`ilc_lvho07b`). [Original source](https://doi.org/10.2908/ILC_LVHO07B).
- **Selection:** Austria (`AT`), fixed EU-27 (`EU27_2020`), lowest-income fifth (`QU1`), annual percentages, 2015–2025: 22 complete, unflagged observations.
- **Author:** Yazdan Zandiye Vakili, 12642780. The student supplied the name; the number was verified in their Individual Assignment 02 report.

The original brief and raw data are preserved unchanged. The student clarified
that they personally added the brief’s AI-use paragraph and instructed that it
be disregarded. The original handout remains local and excluded from Git.

## Requirements and rubric

The original brief was read in full. Use one dataset for two static,
single-image visualizations: an accurate white hat view and a credible,
subtly deceptive black hat view. Do not fabricate values or assert explicitly
false claims. The PDF must include the dataset and source, selection and
transformations, the question and relationship between the figures, and
200–500 words accompanying each figure. Explain design choices and deception.

| Criterion | Points | Design target |
| --- | ---: | --- |
| Data question | 3 | Explain the difference between changes in a national rate and in its comparison with a changing benchmark. |
| Marks and encodings | 3 | Use readable annual paths, redundant colour and shape, direct labels and a meaningful gap bar. |
| Title and labels | 2 | State the measure, group, period, units and index definition. |
| Design rationale | 2 | Describe both charts and explain the deceptive framing in a separate Conclusion. |

The brief specifies a 20% late penalty per calendar day. It did not provide an
identified deadline, overall page limit or mandated filename. Additional
course-platform rules remain for the student to check; nothing has been
uploaded or submitted through this workflow.

## Analytical facts and calculations

| Measure | 2015 | 2025 | Change |
| --- | ---: | ---: | ---: |
| Austria rate | 26.7% | 27.2% | +0.5 percentage points; +1.9% relative |
| EU-27 rate | 36.2% | 25.8% | −10.4 percentage points; −28.7% relative |
| Austria minus EU gap | −9.5 points | +1.4 points | +10.9 percentage points |
| Austria/EU rate ratio | 0.7376 | 1.0543 | +42.9% relative |
| Ratio index with 2015 = 100 | 100 | 142.9 | +42.9% |

- `ratio_t = AT_t / EU_t`
- `index_t = 100 * ratio_t / ratio_2015`
- `change(AT - EU) = change(AT) - change(EU) = 0.5 + 10.4 = 10.9 pp`

The gap bar is an additive decomposition of the **percentage-point gap**,
not a division of the 42.9% ratio increase. The ratio change is multiplicative:
`(27.2 / 26.7) / (25.8 / 36.2) = 1.429376...`.
Index 100 denotes the starting ratio, not equality with the EU; 142.9 does not
mean Austria was 42.9% above the EU in 2025. It was approximately 5.4% above.

## Final visualizations

**White hat:** Two annual rate paths on a shared 0–40% scale, teal circles for
Austria and muted purple squares for the EU, starting and ending labels and net
changes. A lower bar shows the 0.5- and 10.4-point contributions to the change
in their gap. All years remain visible, including Austria’s 2022 peak.

**Black hat:** A single annual Austria/EU rate-ratio index with 2015 set to 100,
a prominent “Up 43% in a decade” headline, and a smaller subtitle and formula.
The original rates are absent. The intended error is to read a 43% rise in
Austria’s relative index as a 43% rise within Austria; the national rate rose
only about 1.9%. The formula and subtitle use **÷** rather than slashes.
These are intended reading effects; no audience study was conducted.

## Report decisions

The final report has four portrait pages, with no separate cover:

1. Title, identity, shared question, concise dataset description and one source link.
2. White hat figure and 200-word description.
3. Black hat figure and 212-word description.
4. A separate 88-word **Conclusion** explaining why the framing is deceptive.

Use Arial to match the figures, a bold teal title, teal section headings, and
a muted purple black hat heading. Apply Word’s Justify Low alignment to body
prose, with headings and labels left-aligned. Italicize named sources,
institutions and geographical names in prose. Keep page numbers.

The student requested short, natural, professional text. Remove technical
jargon, raw dataset codes, the repeated variables list and duplicated
explanations. Describe the dataset and source once; omit source footers from
the figures and the displayed download date. Keep the simple source statement:
“The original data values were kept unchanged.” The black hat description
supports the title: it highlights Austria, while the subtitle adds EU context.

## Decision history

All decisions below were made on 21 November 2026, in this order.

1. Work step by step, use the supplied 10-point rubric, and maintain this plan.
2. Choose housing affordability and inequality from the proposed topics.
3. Initially ask whether Austria’s below-EU overall rate extended to all income groups in 2025. Develop a difference chart and a selective comparison.
4. Reopen the question because the student found this direction too trivial. At their explicit request, run a separate exploratory analysis with Astra at Medium reasoning. Preserve the research memo and reproducible exploration script.
5. Select the Austria moving-benchmark candidate from that analysis. Replace the one-year question and charts with annual rates and an indexed ratio for 2015–2025.
6. Prepare both figures before writing, then generate Word and PDF using the documents and PDF skills. Replace the initial five-page proposal with a compact layout.
7. Revise typography to Arial and Justify Low, italicize names and colour the headings. Simplify the dataset section and descriptions at the student’s request.
8. Separate descriptive figure text from the explanation of deception. Move the Conclusion to its own fourth page at the student’s request.
9. Approve the current question, focused on how national and EU-relative measures portray change differently. Clarify division notation and describe the title positively.
10. Publish the useful work to the University Git repository and remove redundant files. Retain final reports, final figures, source data, provenance, reproducible scripts and the useful research memo; remove superseded drafts, their unused builders, large regenerable exploration output, placeholders and render previews. Condense this plan without losing the decisions above.

The discarded one-year charts and preview files are superseded, not intended
submission content. The historical research memo still discusses alternatives;
its opening note points to the current selection here.

## Limitations and provenance

The indicator measures people in households with housing costs above 40% of
disposable household income, with costs and income net of housing allowances.
It is not rent, average spending, or a count of overburdened people. National
income fifths have different euro thresholds and annual membership; they are
not fixed cohorts. The EU includes Austria. The extract contains no confidence
intervals, and national methodology changes can affect comparisons. Findings
and gap contributions are descriptive, not causal. The window was selected
exploratorily, not preregistered.

The preserved API extract was retrieved on 21 November 2026 and reports an
update of 29 October 2026. Provenance contains the exact UTC retrieval time,
API URL and SHA-256:
`954312cf67eb237d778b0f30e3245f53c4c5ea1ad222a896a3516cb00f25ac6f`.
No source values were changed or imputed; the published EU aggregate is used
directly. The figures perform the explicit calculations listed above.

## Deliverables and reproduction

- `submission/IA01_ZandiyeVakili_12642780_Report.docx`
- `submission/IA01_ZandiyeVakili_12642780_Report.pdf`
- `working/figures/benchmark-white-hat.svg` and `.png`
- `working/figures/benchmark-black-hat.svg` and `.png`

See README.md for build commands. The final figure builder checks source hash,
record completeness, source flags, units, plotting ranges, index and gap
arithmetic. Word counts are saved in `working/report-word-counts.json`.
The full candidate scan can be regenerated with `explore_round_02.py`; its
large JSON output is ignored. Temporary render QA stays ignored and is removed
after inspection.

## Validation and publication status

The final Word and PDF were rendered and all four page images visually checked
after the last text revision. The report has two figures, a source link and the
Conclusion on page 4. Descriptions meet the 200–500-word range. After cleanup, the complete figure and report build was rerun successfully.
The shared SVG helper extraction produced byte-identical SVGs; source and
arithmetic checks passed. The final PDF has four pages with Conclusion on
page 4; both figure descriptions meet the required length. All final page
images were visually inspected, and temporary QA outputs were then removed.
The commit records the exact version prepared for publication.
