# Exploratory reassessment of housing overburden

Historical research memo. The final selection is Austria’s changing EU comparison,
recorded in `../plan.md`; the alternatives below are not submission content.
The exhaustive `round_02_findings.json` is regenerated with
`working/scripts/explore_round_02.py` and is excluded from Git.

Research memo, 21 November 2026. Proposals only: the recorded question, original brief, raw source and existing figures are unchanged. This is question/design research, not submission prose or finished figures.

**Recommendation: Greece’s unequal recovery, 2015–2025, with the post-2021 reversal visible.** This provides a substantially richer story than Austria’s small one-year benchmark reversal. A second strong option retains Austria but investigates a moving benchmark. Malta offers a distinct, less subtle fallback using complementary percentages. Eight candidates are assessed below; several are deliberately rejected rather than presented as equally promising.

## Evidence and method

The complete original DOCX brief and applicable instructions were read. The existing plan records the student's clarification that the AI paragraph was their own addition. The brief requires the same dataset, two static single-image figures, accurate source values and no explicitly false statements; the black hat must mislead credibly. The supplied rubric emphasises the question, encodings, self-contained labels and reasoned rationale. No grade is predicted.

Source: [Eurostat ilc_lvho07b API](https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/ilc_lvho07b?lang=en). The preserved file was retrieved at 2026-11-21T18:30:16.767717+00:00, reports source update 2026-10-29, and has SHA-256 `954312cf67eb237d778b0f30e3245f53c4c5ea1ad222a896a3516cb00f25ac6f`. The script verifies that hash, all 4,966 observations, unique observation keys and rates within 0–100. There are 46 geographical codes, including nine aggregates; those are not 46 countries. The overall time dimension is 2003–2025; coverage differs by country.

The analysis decodes every observation, retains every source status, scans 5,452 complete windows of at least three elapsed years across individual countries and the fixed EU-27 aggregate, and compares total and quintile changes, Q1 extrema, rankings, pair reversals, and equal-country means/medians against the published EU rate. All eligible windows are saved, including flagged ones. Shortlisted temporal comparisons are checked separately for flags. Rankings use competition ranks (one plus the number of strictly lower rates), not arbitrary tie ordering. No missing rate is filled with zero. Comparisons are exploratory, selected after inspection; they are not preregistered hypotheses or significance tests.

All candidates use `geo`, `quant_inc`, `time`, `value`, `status`, with `freq=A` and `unit=PC`. Q1–Q5 below mean QU1–QU5; TOTAL is kept separate. A rate is the percentage of people **within that group** living in households with housing costs above 40% of disposable income, both net of housing allowances. It is not rent, mean spending, or the share of all overburdened people belonging to that group. See the [official indicator definition](https://ec.europa.eu/eurostat/statistics-explained/index.php?title=Glossary:Housing_cost_overburden_rate).

The [quintile definition](https://ec.europa.eu/eurostat/statistics-explained/index.php?title=Glossary:Income_quintile_group) sorts people by equivalised disposable household income into fifths. National fifths are relative groups, not common euro bands. Annual observations do not follow fixed individuals. The [EU-SILC metadata](https://ec.europa.eu/eurostat/cache/metadata/en/ilc_sieusilc.htm), sections 5, 8.1 and 18.5, distinguish survey/income reference years, explain flags and population weighting. Equal-country averages below describe countries; they never replace the published population-weighted EU rate. No population counts, confidence intervals or causal explanations are inferred.

## Candidate 1 — Did Greece’s housing recovery continue for its lowest-income fifth?

**Scope:** Greece (`EL`), every year 2015–2025, TOTAL and all five quintiles: 66 observations. Compare the decade and the recent 2021–2025 segment within the same figure. No observation flags in this window. The [Greek national metadata](https://ec.europa.eu/eurostat/cache/metadata/EN/ilc_simsilc_el.htm), section 15.2, reports comparability from 2003 and no 2024 break, while noting a 2019 sample redesign. This supports cautious descriptive comparisons, not a guarantee of unchanged measurement in every year; the metadata inspected principally describes 2024, not a detailed 2025 audit.

**Evidence:**

| Group | 2015 | 2019 | 2021 | 2024 | 2025 | Change 2021–2025, pp |
|---|---:|---:|---:|---:|---:|---:|
| Total | 45.5 | 36.2 | 28.8 | 28.9 | 26.4 | −2.4 |
| Q1 | 94.0 | 85.7 | 75.8 | 88.6 | 82.1 | +6.3 |
| Q2 | 65.8 | 45.7 | 31.5 | 35.7 | 31.8 | +0.3 |
| Q3 | 36.1 | 23.2 | 17.2 | 13.4 | 12.8 | −4.4 |
| Q4 | 21.1 | 16.7 | 12.7 | 5.3 | 4.6 | −8.1 |
| Q5 | 10.5 | 9.5 | 6.8 | 1.4 | 0.8 | −6.0 |

**Honest answer:** Every quintile is below its 2015 rate, but the lowest fifth's recovery reversed after 2021. Q1 is above its 2021 rate in all four subsequent years: 83.3, 85.3, 88.6, 82.1. Thus the 2025 decline from 2024 does not erase the reversal. Total fell 42.0% relative to 2015; Q1 fell only 12.7%. The story combines genuine long-term progress, uneven distribution and a persistent recent setback.

**White hat:** One integrated figure: annual trajectories on a common 0–100% scale, Q1 and TOTAL directly labelled, with the other quintiles in compact aligned rows and a right-side 2021→2025 change column. Use a vertical 2021 guide, with the full earlier period visible so the trough is not passed off as a neutral baseline. A small connected-dot strip for each group can preserve annual shape without an unreadable six-line knot. No ribbons implying confidence intervals or individual flows.

**Black hat's specific false inference:** Recovery continued steadily through the recent period for every income group. **Mechanism:** select only 2015, 2019 and 2025, at their correct temporal positions. Every group falls at both displayed intervals. Connect those selected observations with straight lines, use reassuring common colour and the true headline “2025 overburden below 2015 in every income fifth.” Label the subtitle “Selected survey years: 2015, 2019, 2025.” The straight descending connections replace the omitted 2021 trough and subsequent rebound in the reader's visual reconstruction. This is selective temporal sampling plus perceived continuity, not invented intermediate measurements. Do not label interpolated segments as measured annual values or claim uninterrupted improvement in words.

**What careful reading uncovers:** Only three years are plotted; restoring annual observations reverses the recent Q1 conclusion. Merely writing “42% lower” with a total bar would be too weak. The selected-path mechanism is essential. A sophisticated reader may still recognise the omission, so credibility must be tested in the eventual design rather than presumed.

**Verdict:** Strongest. 2015 is a high baseline and 2021 a trough; acknowledge both in the honest figure. The recent difference is 6.3 points and occurs on a large base, not a rounding artefact. Do not call it a policy effect, a cohort experience, or rising rents.

## Candidate 2 — Is Austria falling behind because its rate rose, or because the EU benchmark fell?

**Scope:** `AT`, `EU27_2020`; annual 2015–2025; primarily Q1 (22 observations), TOTAL as optional separate context. Both series are unflagged in the extract.

**Evidence:** Austria Q1 26.7→27.2% (+0.5 pp; +1.87% relative), EU Q1 36.2→25.8% (−10.4 pp; −28.73%). The Austria-minus-EU gap moves from −9.5 to +1.4 pp: a 10.9-point change, arithmetically 0.5 from Austria's change and 10.4 from the falling benchmark. This is a decomposition of a difference, not causal attribution. The ratio Austria/EU rises from 0.737569 to 1.054264, or **42.94%**. Annual Austrian rates fluctuate substantially, including 32.3% in 2022, so the endpoints do not establish flatness in every year.

**Honest answer and white hat:** Relative standing deteriorates mainly because the benchmark improves. Use two directly labelled annual rate tracks plus a small endpoint gap-decomposition strip, separating “Austria +0.5 pp” and “EU decline adds 10.4 pp to the gap.” Include the initial/final rates. A fixed zero and shared units prevent readers confusing the difference with the underlying rate.

**Black hat's specific false inference:** Austria's lowest-income overburden rate itself grew roughly 43%. Plot the annually varying ratio indexed to 2015=100, ending at 142.94, with the true title “Austria’s relative overburden index rises 43%.” Keep the formula `100 × (AT/EU)/(AT2015/EU2015)` and group definition readable but subordinate. Omit the two constituent rate series. This uses denominator movement and an index that visually resembles a domestic trend. No false label such as “43% more Austrians overburdened” is permitted.

**What careful reading uncovers:** The measure is a ratio of rates, not the Austrian rate; a declining denominator accounts for most of its increase. The same annual records let the white figure expose exactly what the black figure suppresses.

**Verdict:** Strong, particularly if Austria is preferred. The misleading effect targets a large discrepancy (43% versus 1.9%), not the statistical importance of the 0.5-point domestic change. More cognitively demanding than Greece, and the formula must remain legible. The EU aggregate has no source flags here, but constituent-country breaks still caution against causal long-term narratives.

## Candidate 3 — Has Malta’s overburden problem remained marginal, and for whom?

**Scope:** Malta (`MT`), all years 2015–2025, all six categories; 66 observations, unflagged. Use the decade as an exploratory window, with all annual values available rather than presenting selected endpoints as a smooth trend.

**Evidence:** TOTAL 1.1→6.0%, +4.9 pp. Q1 4.2→21.5%, +17.3 pp. The complementary percentages not meeting the overburden threshold fall from 98.9 to 94.0% overall and from 95.8 to 78.5% in Q1. The relative increases of 445% and 412% are arithmetically correct, but are not the recommended honest headline.

**Honest answer and white hat:** National prevalence remains below 10%, but the lowest-income group now has more than one person in five above the threshold. Use five equal-width quintile columns, each with a 0–100% prevalence strip, 2015 reference tick and 2025 dot, plus an aligned annual-change row or sparkline. TOTAL is a separate summary, not a sixth population segment. This shows both level and distribution without claiming actual people counts.

**Black hat's specific false inference:** Malta's problem has remained negligible over the decade. Use two nearly full 100% bars for the true complements, 98.9% and 94.0%, with the title “94% of Malta’s population below the housing overburden threshold in 2025.” Fill the complement with strong reassuring colour and leave the 1.1%/6.0% remainder pale. Exclude quintiles. The common upper bound makes the dominant silhouettes look almost unchanged, while the changing adverse remainder attracts little attention. The label must say below the threshold, not “affordable housing,” “financially secure,” or “unaffected.”

**What careful reading uncovers:** Subtracting the displayed values from 100 reveals the more than fivefold rate increase; group detail reveals 21.5% in Q1. The deception combines complement framing, visual dominance and subgroup omission.

**Verdict:** Third, with reservations. The absolute 17.3-point Q1 change is substantial, so this does not depend on a tiny rounding-sensitive rate. However, the graphic device is more familiar and the question less layered than the first two. A reassuring complement chart alone could still read as a truthful prevalence summary; temporal pairing and the intended “little changed” inference must be central.

## Candidate 4 — Who shared in the Netherlands’ latest national improvement?

**Scope:** `NL`, 2017–2025, all groups; 54 observations, unflagged. Start after the 2016 break, rather than citing a pre-break decade decline.

**Evidence:** 2024→2025 TOTAL 6.9→6.5% (−0.4 pp), Q1 20.0→23.0% (+3.0 pp; +15%), Q2 7.9→5.4, Q3 3.7→2.1, Q4 2.2→1.4, Q5 0.5→0.6. Q1 was 34.0% in 2022 and 28.9% in 2023; the latest reversal follows a pronounced decline.

**Honest answer and white hat:** The national improvement coexists with a Q1 setback. Use an annual quintile-by-year dot matrix with a common prevalence scale and a final column of signed 2024→2025 movements; emphasise Q1 and separate TOTAL.

**Black hat:** Show a large national 2024→2025 downward arrow next to Q1's 2022→2025 decline (34→23), each accurately dated, but styled as coordinated recovery panels. Target the mistaken inference that both improved in the latest year. The mismatch of comparison windows produces the distortion; the true title could be “Lower than the displayed starting points.” A careful reader notices different dates and restores the omitted Q1 2024 trough.

**Verdict:** Reserve. This is a specific and credible mixed-window manipulation, but the latest setback is only one year and the total change is small. The longer Greece reversal is more robust and more substantively interesting. Do not overstate Q5's 0.1-point movement.

## Candidate 5 — Are countries converging because everyone is improving?

**Scope:** 15 current EU countries with complete, wholly unflagged 2015–2025 observations: CZ, EE, EL, ES, HR, IT, CY, LV, MT, AT, PT, RO, SI, FI, SE. All six groups screened; focus Q1. This quality-screened subset is not representative of all EU countries.

**Evidence:** Across these countries, Q1 population standard deviation of country rates declines 19.708→17.042 pp and the unweighted mean declines 32.373→26.420%. Yet Estonia increases 27.2→32.5, Malta 4.2→21.5 and Sweden 34.6→41.7. Austria +0.5 and Finland +0.1 are too small to anchor the argument. Removing Greece still gives a dispersion decline (11.202→8.598 pp), so the hypothesised “convergence entirely caused by one outlier” is rejected.

**Honest answer and white hat:** Dispersion shrinks, with both improvement and deterioration. Use two aligned country distributions connected by labelled country trajectories, with the three clear deteriorations highlighted. Separate mean and spread from individual outcomes.

**Black hat:** Show only the narrowing mean±one-country-SD band for 2015 and 2025, accurately labelled “spread of country rates; not a confidence interval.” Use the truthful title “Less variation in lowest-income overburden across 15 countries.” The intended false inference is a broadly shared improvement; omitted trajectories hide the deterioration that also produces convergence. Careful reading identifies an aggregate distribution summary, not universal progress.

**Verdict:** Analytically worthwhile, weaker deception: shrinking dispersion and falling mean are real, so the black version too easily becomes an honest summary. Do not imply the band is uncertainty or that this is all Europe. Not shortlisted.

## Candidate 6 — Does the Sweden–Germany comparison reverse across the income distribution?

**Scope:** `SE`, `DE`, 2025, TOTAL and all quintiles; 12 unflagged records. EU-member ranks provide optional context, with flags on other countries retained.

**Evidence:** Sweden TOTAL 10.8 versus Germany 11.2%; Q1 41.7 versus 31.5%; Q2 9.1 versus 12.1%; Q3 2.8 versus 7.0%; Q4 0.7 versus 3.8%; Q5 0.1 versus 1.5%. Sweden is slightly lower overall but 10.2 points higher in Q1. Sweden's lower-is-better EU ranks are 24th overall and 25th in Q1; Germany's are 25th and 23rd.

**White hat:** An income-ordered pairwise difference profile with original values, showing where the sign changes. Honest answer: national near-equality conceals a large Q1 difference.

**Black hat:** A two-country national leaderboard, enlarged rank badges and the accurate title “Sweden’s total rate below Germany’s,” omitting group differences. Target: Sweden is meaningfully better for vulnerable residents. Close reading reveals only a 0.4-point national gap and no subgroup evidence.

**Verdict:** Reject for this round. Substantive Q1 contrast, but the trick repeats the previous Austria approach; the favourable national ranking rests on a small gap without confidence intervals. Adding a truncated scale would not solve that problem.

## Candidate 7 — Can changing the definition of the European benchmark change Spain’s assessment?

**Scope:** all 27 current EU countries and the separate `EU27_2020` aggregate, 2025 TOTAL. Preserve 2025 break flags for DK/LU/SK and provisional LT. Never count the EU aggregate as a country.

**Evidence:** Published EU 7.6%; equal-country mean 7.174074%; median country 6.1%; Spain 7.2%. Spain is below the published EU rate by 0.4 pp, essentially equal to the equal-country mean (0.025926 pp above it), and above the median by 1.1 pp.

**White hat:** A country dot distribution with separately named benchmark lines and explanation of weighting. Honest answer: “typical country” and “EU population” answer different questions.

**Black hat:** Select the median, call it accurately “median EU-country rate” in the subtitle, and show Spain's 18.0% relative excess over that benchmark. Target: Spain is above the population-wide EU rate. Careful reading uncovers the chosen comparator and different unit of aggregation.

**Verdict:** Reject. Conceptually useful reference-group lesson, but the mean-based reversal is smaller than published one-decimal resolution. Median framing remains a defensible alternative question unless execution actively encourages substitution. Not a strong enough replacement.

## Candidate 8 — Can Greece lead in improvement while remaining worst in level?

**Scope:** 2015 and 2025 TOTAL/Q1 in the same 15-country quality-screened panel as candidate 5; 2025 all 27 EU members only for current ranking. Preserve all 2025 flags in the latter comparison.

**Evidence:** Greece TOTAL −19.1 pp (45.5→26.4) is the largest absolute reduction in the 15-country panel. Greece is nevertheless highest among all 27 in 2025 for TOTAL (26.4%) and Q1 (82.1%). Next-highest total is Denmark 14.7% (break flag); no claim that the latter gap is a confidence interval or causal effect.

**White hat:** A start/end dumbbell ordered by final rate, with change labels. Honest answer: improvement and remaining burden measure different dimensions of performance; a high starting point permits a large absolute fall.

**Black hat:** Rank countries only by absolute decline and award Greece a prominent first-place badge under “Largest fall in the 15-country comparison.” Omit final levels. Target: leader in improvement means best current housing outcome. Careful reading shows that the ranking measures change, not level.

**Verdict:** Reserve/reject as final direction. The facts are striking, but a change-only leaderboard may be a perfectly honest answer to a change question. Candidate 1 goes further by demonstrating a hidden reversal in the omitted path, not simply a different ranking criterion.

## Shortlist and decision

| Rank | Direction | Question depth and substantive interest | Deception strength/subtlety | Static feasibility and rubric fit |
|---|---|---|---|---|
| 1 | Greece: long recovery versus recent Q1 reversal | Combines period choice, distribution and persistence; very large observed burden | Selected descending years suppress an actual intervening reversal; credible continuity illusion with true points | Strong: annual paths plus change column in one image; ample reason to justify marks, dates and hierarchy |
| 2 | Austria: moving EU benchmark | Distinguishes domestic change from relative standing over a decade | Ratio index rises 43% while domestic rate rises 1.9%; denominator hidden in plain sight | Strong but more explanatory work: paired rate paths and gap decomposition versus indexed black figure |
| 3 | Malta: marginal nationally, substantial in Q1 | A large decade change and clear subgroup concentration | Complement bars suppress growing adverse remainder; familiar technique and weaker than first two | Very feasible: quintile prevalence strips versus complementary population bars; avoid “below threshold = secure” |

Greece is the recommendation, not a finalized choice. It is meaningfully richer than the original 12-record comparison: 66 observations reveal two distinct phases, divergent group outcomes, and a 2025 improvement that still leaves Q1 above the 2021 trough. The black hat can create a demonstrably wrong impression of the **path**, using only actual observations and accurate labels. It does not rely on the audience treating a truthful four-of-five summary as a claim of universality.

The dataset is adequate for these descriptive visual arguments. It is limiting for explanations of why burdens change, local housing markets, actual rents, affected population counts, significance, individual mobility or policy success. None is claimed. The deception effects described here are design hypotheses, not tested audience responses. Before final selection, the student should judge whether the proposed misleading inference is convincing; actual layout and prominence will matter.

## Reproduction and saved outputs

Run from any directory:

```sh
/Users/yazdanzandiyevakili/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3 /Users/yazdanzandiyevakili/University/2026-WS/information-visualization/assignments/individual-assignment-01/working/scripts/explore_round_02.py
```

No new dependencies or network access are needed to reproduce the quantitative results. `working/data/derived/round_02_findings.json` stores provenance, all decoded observations, complete-window scans, annual rankings, pair reversals, mean/median comparisons, and candidate-specific evidence. Its `candidate_evidence` object is the fastest entry point. Source flags appear on observations and as keys on scanned windows. Official methodological pages above were consulted on 21 November 2026; they are linked, not silently merged into the dataset.

Executed validation: source hash/count/key/range assertions; full-window completeness checks; explicit assertions for Greece +6.3 pp, Austria gap +10.9 pp and Netherlands +3.0 pp; no-flags checks for the three shortlisted country windows. All passed. This verifies calculations and source consistency, not statistical significance. No final figures, PDF, new repository, or changes to `plan.md` were made.
