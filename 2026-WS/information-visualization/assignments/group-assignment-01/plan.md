# Group Assignment 1 — Dataset Selection Plan

Evaluation date: 7 November 2026. Team size: **4**.

Status: OWID/WDI data preparation completed on 7 November 2026; the merged CSV is
available locally. Topic, audience, and research questions remain proposals for
team discussion. This is not a finished team report. Every member must contribute
to the eventual decisions.

## 1. Assignment requirements

- Explain the topic, motivation, value of interaction, and possible insights.
- Identify a specific audience, its background, information needs, and goals.
- Evaluate at least **4 candidate datasets from different sources**. Each dataset
  description in the report must be no longer than one paragraph and cover its
  contents, collection method, relevance, limitations, and access URL.
- Justify the final selection. Describe cleaning, integration, variable meanings
  and types, missingness, outliers, limitations, and potential biases.
- The final tabular dataset needs at least **10,000 observations and 10 variables**.
- The pasted detailed brief asks for at least 4 initial research questions. The
  attached overview slide asks for at least **n + 1 = 5**. Plan for **5 questions**
  and confirm the authoritative requirement in TUWEL.
- Each member subsequently produces two exploratory visualizations for Individual
  Assignment 2. The slide specifies one combined team PDF, with each A2
  visualization labelled with its author.
- Check the course AI-use/attribution policy before submission; no such policy was
  included in the supplied brief. Do not present this analysis as team consensus.

## 2. Proposed topic and audience

**Proposed topic:** economic development and territorial CO₂ emissions across
countries, with energy use, economic structure, urbanization, and trade as context.
The central analytical direction is whether and how economic growth coincides
with changing emissions. The team has not yet finalized its research questions.

**Proposed audience:** junior climate-policy analysts at European environmental
NGOs who understand basic emissions and GDP concepts and need to compare national
development trajectories. They need to distinguish total emissions from emissions
per person, compare economies with similar characteristics, and inspect changes
over time. These are proposed needs, not findings from audience interviews.

Interaction can support linked country selection, time-window changes, regional
filters, and switching between totals, per-person values, and indexed trends.
It should also expose missing data and the number of economies included in each
comparison. Cross-country associations alone cannot establish policy effects.

## 3. Four genuine candidate datasets

These are real alternatives, not dummy entries. OWID and WDI were downloaded and
profiled. EDGAR and IEA were evaluated through official documentation only; no
empirical missingness or join-quality claims are made for those two alternatives.
Different publishers do not imply independent observations: some candidates share
upstream energy statistics.

### Candidate 1 — Our World in Data CO₂ and Greenhouse Gas Emissions

OWID harmonizes emissions estimates from the Global Carbon Project and other
providers, combining them with energy and population statistics. Its annual
location records include territorial and consumption-based CO₂, fuel-specific
emissions, and energy measures, making it a strong emissions backbone. These are
compiled estimates rather than direct atmospheric measurements. Metric coverage
varies, aggregates must be excluded from country comparisons, and population/GDP
denominators require attention. Select this source for emissions and primary
energy measures. Source/access: [OWID repository](https://github.com/owid/co2-data);
[codebook](https://github.com/owid/co2-data/blob/master/owid-co2-codebook.csv).

### Candidate 2 — World Bank World Development Indicators

WDI compiles national statistics, international agency series, and estimates,
including population, real and PPP GDP, urbanization, economic structure, trade,
and renewable energy. It complements emissions with development context through
documented country and indicator identifiers. Variables come from different
collection systems, so revisions, gaps, and incomplete cross-country comparability
remain important. Select WDI for economic and demographic context rather than
adding a second competing CO₂ series. Source/access:
[WDI DataBank](https://databank.worldbank.org/source/world-development-indicators);
[sources and methods](https://datatopics.worldbank.org/world-development-indicators/sources-and-methods.html).

### Candidate 3 — European Commission JRC EDGAR 2026 GHG

EDGAR provides estimated greenhouse gas emissions by country and sector, with
annual tables covering 1970–2025. It combines activity statistics and emissions
methodologies, including joint IEA–EDGAR fossil CO₂ estimates. It is relevant for
a sector-focused alternative, but supplies little socioeconomic context and needs
careful alignment of gases, units, sectors, and accounting boundaries. The main
dataset excludes LULUCF, which is addressed separately. Prefer OWID for this
proposed country-level development project because its prepared totals,
per-person measures, and consumption-based series reduce integration work;
EDGAR would become more attractive if sector detail became central. Source/access:
[EDGAR 2026 dataset](https://edgar.jrc.ec.europa.eu/dataset_ghg2026).

### Candidate 4 — IEA World Energy Balances

IEA compiles energy balances from national statistics and standardized reporting,
with estimates where necessary. The July 2026 product covers 156 countries plus
regional aggregates and detailed energy products and flows, generally from 1971,
or 1960 for OECD countries, through 2024. It could enrich an energy-system project,
but it requires more reshaping and unit harmonization, and the full product has
subscription and non-CC licensing conditions that complicate a public repository
and visualization. Prefer the selected OWID/WDI indicators for this project's
initial scope; this is an access/scope decision, not a finding that IEA data have
poor quality. Source/access:
[World Energy Balances](https://www.iea.org/data-and-statistics/data-product/world-energy-balances);
[IEA reporting questionnaires](https://www.iea.org/about/data-and-statistics/questionnaires).

## 4. What was actually measured

Downloaded OWID's CSV and codebook and 14 candidate WDI indicator series through
the World Bank API (`source=2`). The WDI API reported an update date of
**8 October 2026**. Download URLs are recorded in
`output/tools/support/dataset-profile.json`.

Evaluation grain: **one economy–year**, retaining only OWID records with observed
territorial CO₂ and a code matching the World Bank's non-aggregate economy list.
“Economies” includes territories; these counts are not counts of sovereign states.
World/regional/income-group aggregates are excluded. No years were generated to
inflate the row count and no missing values were imputed.

| Period | Matched economy–years with CO₂ | With WDI population and real GDP |
| --- | ---: | ---: |
| 1960–2024 | 12,896 | **10,874** |
| 1970–2024 | 11,004 | 9,771 |
| 1990–2023 | 6,923 | 6,632 |
| 2000–2023 | 4,896 | 4,731 |

**Recommended final row filter:** 1960–2024, observed OWID territorial CO₂, WDI
population, and WDI real GDP. This yields **10,874 distinct economy–years from
202 economies**. It is an unbalanced panel: not every economy has every year.

Keeping all 12,896 CO₂ records is a defensible alternative if GDP missingness is
explicitly shown, but the recommended filter makes every retained observation
usable for the main emissions–economy comparison. It excludes some economies and
years systematically, which must be acknowledged as selection bias.

The 10,000-row threshold is met only for the broad historical panel. It is not met
for every analytical subset. Requiring complete WDI population, real GDP, real GDP
per capita, urban share, industry share, and trade leaves only **7,502 rows**.
Do not claim 10,874 fully populated observations across all selected variables.

Key uniqueness was checked in the OWID backbone and the non-null WDI series. The
CO₂ backbone contains no negative total CO₂ values and four reported zeros. Its
available real GDP values are all positive. This is an initial validation, not an
exhaustive outlier investigation.

## 5. Recommended main columns

These **18 columns** are included in the main schema. “Include” does not mean require
a non-missing value in every row. All numeric measurements below are quantitative;
year is a discrete temporal variable. Coverage percentages use the recommended
**10,874-row panel** as their denominator and were measured from the downloaded
snapshots. A full profile for the broader backbone is also saved in the JSON.

### Identifiers and grouping

| Output column | Source | Meaning and type |
| --- | --- | --- |
| `iso3` | OWID `iso_code` matched to WDI economy metadata | Nominal economy identifier; join key with year |
| `country` | WDI economy metadata | Nominal display name; do not join on names |
| `year` | Both sources | Calendar year; discrete temporal |
| `region_wdi` | WDI economy metadata | Nominal regional group from the downloaded classification |

### OWID measures

| Output column | Exact source column | Meaning/unit | Coverage | Use |
| --- | --- | --- | ---: | --- |
| `co2_mt` | `co2` | Territorial annual CO₂, million tonnes; excludes land-use change | 100% | Main emissions total |
| `co2_pc_owid_t` | `co2_per_capita` | Tonnes CO₂ per person, using OWID population | 100% | Compare emissions relative to population |
| `primary_energy_twh` | `primary_energy_consumption` | Annual primary energy consumption, TWh | 83.18% | Energy demand and efficiency context |
| `energy_pc_owid_kwh` | `energy_per_capita` | Primary energy, kWh per person using OWID population | 83.18% | Separate population size from energy use |
| `carbon_intensity_energy_g_kwh` | `co2_per_unit_energy` | Grams CO₂ per kWh of primary energy | 82.73% | Carbon intensity of the energy system |

Use the [OWID codebook](https://github.com/owid/co2-data/blob/master/owid-co2-codebook.csv)
for exact indicator definitions. The repository records a June 2026 unit change
for carbon intensity from kilograms to **grams** per kWh. This measure is not an
electricity-grid emission factor and does not isolate combustion emissions alone.

### WDI measures

| Output column | Indicator code | Meaning/unit | Coverage | Use |
| --- | --- | --- | ---: | --- |
| `population_wdi` | `SP.POP.TOTL` | Total population, people | 100% | Scale and consistent WDI-derived ratios |
| `gdp_real_usd2015` | `NY.GDP.MKTP.KD` | GDP, constant 2015 US$ | 100% | Economic growth within an economy over time |
| `gdp_pc_real_usd2015` | `NY.GDP.PCAP.KD` | GDP per person, constant 2015 US$ | 100% | Longer historical development trajectories |
| `gdp_pc_ppp_int2021` | `NY.GDP.PCAP.PP.KD` | GDP per person, constant 2021 international dollars | 61.28% | Preferred income-level comparison across economies; available from 1990 |
| `urban_population_pct` | `SP.URB.TOTL.IN.ZS` | Urban population, % of population | 100% | Urbanization context |
| `industry_gdp_pct` | `NV.IND.TOTL.ZS` | Industry including construction, value added, % of GDP | 79.07% | Broad economic structure |
| `manufacturing_gdp_pct` | `NV.IND.MANF.ZS` | Manufacturing value added, % of GDP | 72.14% | Distinguish manufacturing from mining/construction |
| `trade_gdp_pct` | `NE.TRD.GNFS.ZS` | Exports plus imports of goods/services, % of GDP | 78.67% | Trade openness |
| `renewable_final_energy_pct` | `EG.FEC.RNEW.ZS` | Renewables, % of total final energy consumption | 57.57% | Energy transition context; downloaded series ends in 2022 |

Definitions: [real GDP](https://databank.worldbank.org/metadataglossary/world-development-indicators/series/NY.GDP.MKTP.KD),
[PPP GDP per person](https://databank.worldbank.org/metadataglossary/world-development-indicators/series/NY.GDP.PCAP.PP.KD),
[industry](https://databank.worldbank.org/metadataglossary/world-development-indicators/series/NV.IND.TOTL.ZS),
[trade](https://databank.worldbank.org/metadataglossary/world-development-indicators/series/NE.TRD.GNFS.ZS),
[urban population](https://databank.worldbank.org/metadataglossary/world-development-indicators/series/SP.URB.TOTL.IN.ZS),
[renewable energy](https://databank.worldbank.org/metadataglossary/world-development-indicators/series/EG.FEC.RNEW.ZS).

Industry includes manufacturing, so the two shares must not be added. Trade can
legitimately exceed 100% of GDP. Urban definitions vary nationally and the series
includes smoothing. Renewable share concerns **final** energy, while OWID energy
measures concern **primary** energy: do not multiply the two to estimate renewable
energy quantities. A renewable share also does not directly measure modern
wind/solar adoption.

## 6. Optional extensions worth retaining

These six OWID fields are also retained, bringing the source-variable schema to
**24 columns**. They support
specific analyses but should not determine inclusion in the main panel.

| Output column | Source column | Unit | Coverage | Value and limitation |
| --- | --- | --- | ---: | --- |
| `consumption_co2_mt` | `consumption_co2` | Million tonnes CO₂ | 37.05% | Trade-adjusted emissions; only 1990–2023 in this snapshot |
| `net_imported_co2_mt` | `trade_co2` | Million tonnes CO₂ | 37.05% | Net emissions embodied in trade; positive means consumption exceeds territorial emissions |
| `coal_co2_mt` | `coal_co2` | Million tonnes CO₂ | 68.25% | Coal-related emissions |
| `oil_co2_mt` | `oil_co2` | Million tonnes CO₂ | 99.67% | Oil-related emissions |
| `gas_co2_mt` | `gas_co2` | Million tonnes CO₂ | 54.57% | Gas-related emissions |
| `cement_co2_mt` | `cement_co2` | Million tonnes CO₂ | 98.48% | Cement-process emissions |

Consumption-based emissions cover **4,029 rows** in the recommended panel. They
are valuable but cannot carry the entire project under the row requirement.
Fuel and cement categories do not necessarily exhaust total CO₂. Missing fuel
values must not automatically become zero or be used to construct misleading
100%-composition charts. The trade sign was verified against
`consumption_co2 - co2`: all available paired records in the downloaded OWID file
agreed within 0.003 million tonnes, allowing for source rounding.

## 7. Derived columns

These two calculated additions bring the merged file to **26 columns**:

| Output column | Calculation | Meaning/type |
| --- | --- | --- |
| `co2_pc_wdi_t` | `co2_mt * 1,000,000 / population_wdi` | Quantitative; tonnes CO₂ per WDI population person |
| `co2_intensity_gdp_kg_usd2015` | `co2_mt * 1,000,000,000 / gdp_real_usd2015` | Quantitative; kg CO₂ per constant 2015 US$ of GDP |

Use positive, observed denominators. OWID per-person columns use OWID population,
while the first derived field uses WDI population. Keep the distinction in names
and metadata; do not silently overwrite OWID's published indicator. Carbon
intensity of GDP can improve even while absolute CO₂ rises.

Calculate indexed GDP/CO₂ trends and multi-year changes for selected windows in
the analysis layer. Require observed endpoints; do not treat adjacent rows as
consecutive years when gaps exist. Define absolute/relative decoupling only after
agreeing on the window and handling recession years and near-zero emissions.

## 8. Columns to leave out initially

- OWID `gdp`, `co2_per_gdp`, and `energy_per_gdp`: OWID's GDP uses Maddison-based
  2011 international dollars, whereas the selected WDI measures use other units
  and vintages. Keep one explicit economic basis instead of mixing them.
- A second WDI CO₂ series: largely duplicates the emissions concept while
  introducing accounting/source differences. It could be a validation comparison.
- WDI `EG.USE.PCAP.KG.OE`: only 47.51% coverage in the recommended panel and
  overlaps the already selected energy-use concept with different units/sources.
- WDI `EG.USE.COMM.FO.ZS`: 45.69% coverage; not needed for the initial scope.
- WDI electricity access: 56.17% coverage; add if energy access becomes a research
  focus, otherwise it broadens the project unnecessarily.
- Life expectancy: excellent coverage, but introduces a health/development theme
  beyond the proposed emissions–economy focus.
- Cumulative emissions, temperature attribution, methane, and total GHG: useful
  for other topics, but add accounting and interpretation complexity here. Do not
  describe a CO₂-only dataset as measuring all greenhouse gases or climate impact.

## 9. Merge, validation, and missing-data rules

1. Preserve downloaded snapshots, codebooks, retrieval details.
2. Reshape WDI indicator records to one row per economy–year. Assert uniqueness
   before joining, rather than silently choosing a record or averaging duplicates.
3. Filter to non-aggregate WDI economies and observed OWID CO₂ for 1960–2024.
4. Join using **ISO/economy code + year**, never display names. Use a validated
   one-to-one join and document unmatched entities. The initial exact-code join
   omits, for example, Taiwan (`TWN`) and OWID-specific Kosovo codes. A manual
   crosswalk would change counts and needs separate validation; do not silently
   map or include historical entities as current countries.
5. Apply the selected population/real-GDP filter to obtain the 10,874-row panel.
   Attach WDI region metadata. Label classifications as snapshot classifications,
   not historical membership. Avoid current income groups unless clearly dated.
6. Keep missing values as empty/NA, distinct from real zeros. Do not interpolate
   across national boundary changes or forward-fill into unavailable recent years.
7. Calculate derived ratios with documented units and denominators. Retain source
   precision; apply display rounding separately.
8. Validate duplicate keys, join counts, year ranges, numeric types, nonpositive
   denominators, percentage bounds where appropriate, and large changes. Flag
   genuine outliers for inspection rather than deleting them automatically.
9. For every visualization, report its actual sample and years. Analyze the
   available cases for its required variables; do not drop rows based on unrelated
   optional columns. Compare exclusions by region and period to assess bias.
10. Keep aggregate totals outside the country panel. Do not add OWID world totals
    to a country sum or assume that this selected panel sums to the full world.

National time series may reflect reconstructed historical boundaries and changing
statistical systems. Inspect source country notes before interpreting structural
breaks. High source coverage is not proof that all values were directly observed;
source estimates and modelling remain part of the data.

## 10. Reproducible work completed

- `output/tools/scripts/profile_datasets.py`: standard-library Python script that
  downloads/caches source data, validates API pagination and key uniqueness, and
  calculates counts and coverage. It evaluates candidates; it does not export a
  final merged file.
- `output/tools/scripts/build_dataset.py`: standard-library Python script that reads
  the preserved snapshots, creates both filtered datasets, merges them, computes
  the two derived variables, and exports the dictionary and quality reports.
- `working/data/raw/`: original downloaded CSV/JSON snapshots and OWID metadata,
  ignored by Git to avoid automatically publishing source data.
- `working/data/raw/wdi_candidate_extract.csv`: convenient long-format CSV of
  all 14 downloaded WDI candidate indicator series, including nulls and aggregates.
  It is a serialization of the original JSON responses, not an untouched publisher
  CSV. The original JSON responses remain the authoritative raw WDI inputs. This
  is a **1960–2024 indicator extract**, not the entire WDI database.
- `working/data/filtered/owid_filtered.csv`: selected OWID fields and eligible
  1960–2024 economy–years with observed CO₂, before matching to eligible WDI rows.
- `working/data/filtered/wdi_filtered.csv`: selected WDI fields and eligible
  economy–years with positive population and real GDP, before matching to OWID.
- `working/data/merged/co2_wdi_merged.csv`: the analysis dataset, 10,874 rows and
  26 columns. UTF-8 CSV, decimal point, comma delimiter, empty cells for missing
  data, sorted by `iso3` then ascending `year`.
- `output/tools/support/dataset-profile.json`: measured profiles, source URLs,
  WDI update metadata, and unmatched code lists.
- `output/tools/support/data_dictionary.csv`: every merged column's source field/code
  or formula, definition, unit, type, selection reason, source link, and missingness.
- `output/tools/support/missing_values.csv`: counts and percentages missing per column.
- `output/tools/support/missing_values_by_group.csv`: missingness by year and region,
  for identifying uneven coverage.
- `output/tools/support/excluded_rows.csv`: in-period source-filter exclusions and
  source-only rows excluded by the join; `stage` distinguishes these categories.
  A row may occur at multiple stages, so this file must not be counted as one
  distinct list of excluded observations. Out-of-period OWID rows are counted in
  the build report rather than listed individually here.
- `output/tools/support/range_flags.csv`: percentage values outside expected bounds
  for manual review; currently header-only because no such flags were found.
- `output/tools/support/build_report.json`: stage counts, validation checks, source update metadata, and build timestamp.
- `instructions/assignment-overview.jpeg`: local copy of the supplied overview,
  ignored by Git. The detailed assignment brief was supplied in the chat.

Run from the assignment directory:

```sh
python3 output/tools/scripts/profile_datasets.py
python3 output/tools/scripts/build_dataset.py
```

The script reuses cached raw files. Removing the cache and rerunning downloads
current releases, so results may change. URLs using `master` are not immutable;
preserve the evaluated cache when reproducing these numbers.

The merged CSV and documentation have been generated and validated locally.
Five initial research questions and matching Word/PDF reports have now been
prepared for team review; this work has not been committed or pushed. Before publishing any source data,
check the indicator-specific upstream licence and attribution requirements;
OWID distinguishes its own material from third-party data.

## 11. Next team decisions

1. Review the four genuine candidates together and record each member's input.
2. Confirm the proposed topic/audience and whether trade-adjusted emissions or
   detailed fuel categories deserve the extra scope.
3. Confirm that the lecturer accepts a historical master panel with smaller
   available-case subsets for specific analyses; never pad a modern subset with
   duplicates, aggregates, or fabricated observations to reach 10,000 rows.
4. Review the implemented schema, merged file, data dictionary, and coverage with
   the team; revise the build script if the analytical scope changes.
5. Review the **five initial research questions** in Section 13 and the report.
   Then allocate the eight individual exploratory visualizations, with each
   student's contribution attributed.

## 12. Implemented preparation decisions and results

### Original inputs and independent source filters

The complete downloaded OWID CSV has **50,411 rows** across all its locations and
years. All original columns are preserved in that file. Restricting it to
1960–2024 leaves **16,456 rows**. Then **3,066 rows** are excluded because their
codes are absent from the WDI non-aggregate economy list, and **494 rows** because
territorial CO₂ is missing. The result is **12,896 rows and 14 columns** in
`owid_filtered.csv`: three source identifiers and eleven selected measures.
`country_owid` preserves OWID's original display name in this source-specific file.

The WDI download contains **242,060 indicator records**: 14 candidate series,
266 economies/aggregates, and 65 years. It includes records whose value is null.
These are not 242,060 independent country–year observations. After removing
aggregates, there are **14,105 distinct economy–years**. Sequentially excluding
**30 rows with missing population** and **2,728 rows with missing real GDP** leaves
**11,347 rows and 13 columns** in `wdi_filtered.csv`: four identifiers/grouping
fields and the nine selected measures. The implementation also requires positive
population and GDP for the ratios; no additional exclusions for nonpositive
values were needed in this source filter.

The two source filters are independent. OWID eligibility does not require WDI
GDP, and WDI eligibility does not require OWID CO₂. This makes the loss at the
subsequent merge explicit rather than hiding it in pre-matched source files.

### Integration

An inner join on `(iso3, year)` produces **10,874 rows** from **202 economies**.
The filtered OWID file has **2,022 rows without an eligible WDI match**, and the
filtered WDI file has **473 rows without an eligible OWID match**. The row counts
reconcile as `12,896 - 2,022 = 11,347 - 473 = 10,874`.

WDI metadata supplies the merged display name and region; names are never merge
keys. The merged table contains four identifier/grouping fields, eleven OWID
measurements, nine WDI measurements, and two derived ratios: **26 columns**. It
exceeds the ten-variable requirement even without counting identifiers.

1960–2024 supports substantive historical comparisons and meets the row minimum
without adding duplicate observations or source aggregates. The shorter modern
panels did not meet the minimum, as the earlier coverage table demonstrates.
Optional fields are retained to support different team analyses, while the main
population/GDP/CO₂ comparison has its required measurements available throughout.

### Missingness and coverage bias

No values were interpolated, forward-filled, mean-filled, or replaced with zero.
Every copied source measurement, including empty values, was checked against its
filtered source after the merged CSV was reopened. Source-reported zeros remain
zeros. Blank cells mean unavailable, not zero emissions or zero economic activity.

Dropping every row with any missing optional field would undermine the historical
coverage and could bias the sample toward better-documented economies. Instead,
the merged table retains missing optional fields, and each visualization should
use the available cases for its own variables and display its sample coverage.
The missingness files quantify these limitations overall, by year, and by region.

The GDP/population eligibility filter itself introduces selection bias. Exact-code
matching also excludes some territories and nonstandard codes. Neither the merged
panel nor its sums should be treated as a complete representation of the world.

### Checks actually executed

The build checked API pagination/record counts, unique source keys, nonnegative territorial CO₂,
positive required denominators, finite numeric values, expected merge counts,
and the assignment's row/column minimum. It checked the trade identity within
0.003 Mt. After writing, it reopened the merged CSV and checked its schema, keys,
row count, copied measurements/missingness, and both derived calculations.

Urbanization, renewables, industry, and manufacturing percentages were checked for
values outside 0–100; **none were flagged**. Trade values were not subjected to a
100% ceiling because that would reject valid observations. This is validation of
structure, accounting, and selected ranges, not a comprehensive investigation of
historical breaks, unusual growth rates, or source estimation uncertainty. Those
remain part of exploratory analysis.


## 13. Report workflow and initial research questions

Report date: 7 November 2026. Team members in the requested order:

1. Yazdan ZandiyeVakili — 12642780
2. Aniruddho Saha — 12551185
3. Amit Bose — 12547293
4. Hani Esreb — 12642251

The work is organized into these steps:

1. **Topic and motivation:** define the relationship between economic development
   and territorial CO2 emissions, and explain the value of interactive comparison.
2. **Audience:** describe junior climate-policy analysts at European environmental
   NGOs, their assumed knowledge, and their briefing/comparison tasks. This is a
   proposed audience rather than evidence from user interviews.
3. **Candidate evaluation:** compare OWID, WDI, EDGAR, and IEA using the genuine
   dataset/documentation review recorded above.
4. **Dataset preparation:** preserve originals, filter sources independently,
   join eligible economy-years, calculate ratios, and document selection bias,
   missingness, and executed validations.
5. **Research questions:** formulate five visually explorable questions and check
   their joint coverage in the actual merged file. The counts below are coverage
   results, not analytical answers to the questions.
6. **Report production:** write the five assignment parts, the complete variable
   descriptions/types, limitations, references, and reproducibility notes in an
   editable DOCX; render the same document to PDF and inspect every page.
7. **Team review and A2:** all members review the topic, audience, selection, and
   questions; confirm the course AI-use/attribution policy and the n versus n+1
   question discrepancy; each member then contributes two exploratory
   visualizations with authorship. This last step remains team work to complete.

The report is generated by `output/tools/scripts/write_report.py` from the preserved
build outputs. Its coverage calculations are saved in
`output/tools/support/research_question_coverage.json`. Deliverables are
`output/report/group-assignment-01-report.docx` and
`output/report/group-assignment-01-report.pdf`.

### RQ1 Growth and territorial emissions

Between 2000 and 2022, which economies combined real GDP growth with falling territorial CO2, and how do their trajectories differ across regions?

Plot percentage changes in real GDP and total CO2 with reference lines at zero, then link selected economies to indexed time series. Among growing economies, distinguish falling CO2 from rising CO2 that grows more slowly than GDP. Show recession cases separately. Compare with 2010 to 2022 to test sensitivity to the chosen baseline.

Joint eligible sample: **193 economies**. Required years: 2000, 2022. Required columns: `co2_mt`, `gdp_real_usd2015`.

### RQ2 Income urbanization and emissions per person

In 2022, how does CO2 per person vary with PPP GDP per person, and which economies have unusually high or low emissions among peers with similar income and urbanization?

Use a scatterplot of PPP GDP per person and CO2 per person, with urban share available as a linked view or filter. A logarithmic income axis can reveal lower-income economies without compressing their differences. Inspect peer groups and labelled exceptions rather than implying a causal income effect.

Joint eligible sample: **194 economies**. Required years: 2022. Required columns: `co2_pc_wdi_t`, `gdp_pc_ppp_int2021`, `urban_population_pct`.

### RQ3 Renewable energy and carbon intensity

In 2021, how does the relationship between renewable final-energy share and CO2 per unit of primary energy differ across economies with different income levels and energy use per person?

Compare renewable share with carbon intensity in a scatterplot, using linked income and energy-use filters. Use 2021 because the joint sample is much larger than in 2022. The two energy concepts have different denominators, so this is an association analysis; it cannot quantify an emissions reduction caused by renewables.

Joint eligible sample: **188 economies**. Required years: 2021. Required columns: `renewable_final_energy_pct`, `carbon_intensity_energy_g_kwh`, `energy_pc_owid_kwh`, `gdp_pc_ppp_int2021`.

### RQ4 Economic structure and emissions

Among economies with comparable PPP GDP per person in 2022, how does CO2 per person differ with the shares of industry and manufacturing in GDP?

Use aligned scatterplots or small multiples for industry and manufacturing, with income filtering and country highlighting shared between them. Manufacturing is included within industry and must not be added to it. Differences may also reflect fuel systems and trade, so they are not estimates of industrial activity causing emissions.

Joint eligible sample: **181 economies**. Required years: 2022. Required columns: `co2_pc_wdi_t`, `gdp_pc_ppp_int2021`, `industry_gdp_pct`, `manufacturing_gdp_pct`.

### RQ5 Territorial and consumption based emissions

Between 2000 and 2022, where do territorial and consumption-based CO2 change in different directions, and how do these differences vary with trade openness and net imported emissions?

Compare changes in the two emissions measures and inspect paired time series with a linked trade view. Positive net imported CO2 means consumption-based emissions exceed territorial emissions. The smaller sample and modelled trade accounting limit generalization; divergent trends alone do not establish deliberate emissions outsourcing.

Joint eligible sample: **110 economies**. Required years: 2000, 2022. Required columns: `co2_mt`, `consumption_co2_mt`, `net_imported_co2_mt`, `trade_gdp_pct`.

The renewable-energy question uses 2021 intentionally. All 197 retained
2021 economy-years have renewable shares, and 188 have all four required fields.
For 2022, only 61 retained economy-years have renewable shares and the complete
question-specific sample would fall to 55. A series ending in 2022 therefore does
not imply broad 2022 coverage.

Report production completed: the matching DOCX and PDF have **8 pages**. Every
page was visually inspected; team names/student numbers, all 26 variable
definitions, the five question samples, page numbers, and source links were
checked. Checks are recorded in `output/tools/support/report-validation.json`.
The report covers G1; the eight A2 exploratory visualizations remain future work.
