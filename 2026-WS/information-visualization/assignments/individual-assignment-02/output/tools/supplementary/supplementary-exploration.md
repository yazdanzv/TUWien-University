# Supplementary exploration and submission recommendation

**Recommendation.** Submit Figure 1 (`rq2_peer_paths.png`) and Figure 2 (`rq3_changes_by_income.png`) in the individual PDF. Their line and scatter designs are meaningfully different. The first shows paths through time for a transparent peer selection; the second shows the full 182-economy paired comparison and its income/energy context. The two figures below remain supplementary.

## Supplementary Figure A  RQ2 all-economy change scatter

**Research question.** Over the available years, how did CO₂ per person change alongside income and the share of people living in cities, and which economies followed different paths from similar peers?

The scatterplot places each of the 190 economies with complete 2000 and 2021 values by percentage change in PPP GDP per person (horizontal position) and CO₂ per person (vertical position). Colour shows the change in urban population share in percentage points. The four labelled economies are followed up in the selected time-series figure. The zero lines make the signs of the changes easy to compare. The vertical axis uses a linear region near zero and compression at larger values; this retains genuine extreme percentage changes from low emissions baselines but makes distances outside the central region harder to judge. Urban share is encoded with colour because it is context rather than an inferred cause.

Columns: `gdp_pc_ppp_int2021` gives horizontal percentage change, `co2_pc_wdi_t` gives vertical percentage change, and `urban_population_pct` gives colour as a percentage-point change. The two endpoint records are paired for each economy, and `country` labels the selected examples. The CO₂ per-person field is derived from `co2_mt` and `population_wdi`.

Across the 190 economies, the median changes were about +37% for income and +24% for CO₂ per person. The figure reveals substantial spread around that tendency, including countries with rising income and falling emissions. Endpoint differences conceal interim changes and absolute levels. A national urbanization percentage may not mean the same thing in every economy, and neither the scatter nor the selected examples establishes causation [1, 2].

## Supplementary Figure B  RQ3 income and energy heatmap

**Research question.** Over years with data for all required measures, how did changes in the renewable share of final energy relate to CO₂ per unit of primary energy, and how did patterns differ by income and energy use per person?

The heatmap groups the same 182 complete-pair economies by thirds of 2000 PPP GDP per person (rows) and 2000 primary energy use per person (columns). Cell colour encodes the median 2000–2021 change in carbon intensity, and each cell prints the median with its unit and sample size. This aggregation lets readers see the income-by-energy pattern without point overlap. The categories are sorted from low to high on both axes; a diverging palette distinguishes increases from decreases. Exact group membership and the median renewable-share change are saved in the derived CSV.

Columns: `gdp_pc_ppp_int2021` defines income rows, `energy_pc_owid_kwh` defines energy-use columns, and `carbon_intensity_energy_g_kwh` gives each economy's 2000–2021 change before taking the cell median. `renewable_final_energy_pct` is required for the same complete-pair sample and its cell median is saved in the supporting CSV. The two endpoint records are paired for each economy.

The group medians make clear that one overall trend would conceal different baselines and outcomes. Yet a median hides within-cell variation and the renewable-share relationship is not directly visible in colour; the submitted scatter better addresses that part of RQ3. The income and energy tertiles are sample-relative, and some cross-classified cells are much smaller than others. Final and primary energy have different accounting bases; the heatmap does not combine their totals [1, 2].

## References

[1] Our World in Data. CO₂ and Greenhouse Gas Emissions dataset and codebook. Downloaded snapshot used in the group dataset, 7 November 2026. https://github.com/owid/co2-data

[2] World Bank. World Development Indicators and Metadata Glossary. Downloaded WDI extract used in the group dataset; source update 8 October 2026. https://databank.worldbank.org/source/world-development-indicators ; https://databank.worldbank.org/metadataglossary/world-development-indicators
