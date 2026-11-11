"""Reproduce Individual Assignment 2 figures and report from the group CSV.

Run with the Codex bundled Python environment. No input file is modified.
"""
from pathlib import Path
import csv
import re
import shutil
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
from docx import Document
from docx.shared import Cm, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.section import WD_SECTION_START
from docx.enum.style import WD_STYLE_TYPE
from docx.oxml import OxmlElement
from docx.oxml.ns import qn

ROOT = Path(__file__).resolve().parents[3]
GROUP = ROOT.parent / "group-assignment-01"
DATA = GROUP / "working/data/merged/co2_wdi_merged.csv"
FIG = ROOT / "working/figures"
DERIVED = ROOT / "working/derived"
SUPP = ROOT / "output/tools/supplementary"
REPORT = ROOT / "output/report"
for p in (FIG, DERIVED, SUPP, REPORT): p.mkdir(parents=True, exist_ok=True)

df = pd.read_csv(DATA)
assert df.shape == (10874, 26) and df.iso3.nunique() == 202
assert not df.duplicated(["iso3", "year"]).any()
assert (df.year.min(), df.year.max()) == (1960, 2024)

R2 = ["co2_pc_wdi_t", "gdp_pc_ppp_int2021", "urban_population_pct"]
R3 = ["renewable_final_energy_pct", "carbon_intensity_energy_g_kwh",
      "energy_pc_owid_kwh", "gdp_pc_ppp_int2021"]

def pair_changes(columns):
    x = df[df.year.isin([2000, 2021])].dropna(subset=columns)
    x = x[x.groupby("iso3").iso3.transform("size") == 2].set_index(["iso3", "year"])
    a, b = x.xs(2000, level="year"), x.xs(2021, level="year")
    out = a[["country", "region_wdi", "population_wdi"]].copy()
    for col in columns:
        out[col + "_2000"] = a[col]
        out[col + "_2021"] = b[col]
        out["change_" + col] = b[col] - a[col]
        out["pct_change_" + col] = np.where(a[col] != 0, 100 * (b[col] / a[col] - 1), np.nan)
    return out.reset_index()

r2, r3 = pair_changes(R2), pair_changes(R3)
assert len(r2) == 190 and len(r3) == 182
r2.to_csv(DERIVED / "rq2_2000_2021_complete_pairs.csv", index=False)
r3.to_csv(DERIVED / "rq3_2000_2021_complete_pairs.csv", index=False)

plt.rcParams.update({"font.family":"DejaVu Sans", "font.size":10,
    "axes.spines.top":False, "axes.spines.right":False,
    "axes.labelcolor":"#28333c", "text.color":"#17232b",
    "axes.edgecolor":"#87949d", "xtick.color":"#42515b", "ytick.color":"#42515b",
    "figure.facecolor":"white", "axes.facecolor":"white", "savefig.facecolor":"white"})
navy, teal, orange = "#24558a", "#008b83", "#d27723"

def save(fig, filename):
    fig.savefig(FIG / filename, dpi=300, bbox_inches="tight", pad_inches=.16)
    plt.close(fig)

# Figure 1: the two peer pairs were chosen from baseline GDP/urban proximity,
# with different observed emissions paths. No selected series is interpolated.
selected = ["EST", "POL", "ROU", "TUR"]
fig, axes = plt.subplots(2, 2, figsize=(11.8, 7.3), sharex=True, sharey=True)
fig.suptitle("Similar starting conditions, different emissions paths", fontsize=17, weight="bold", y=.995)
fig.text(.5, .945, "Four economies | all measures indexed to 2000 = 100 | observed years through 2021", ha="center", fontsize=10)
styles = [("co2_pc_wdi_t", "CO₂ per person", navy),
          ("gdp_pc_ppp_int2021", "PPP GDP per person", teal),
          ("urban_population_pct", "Urban share", orange)]
for ax, code in zip(axes.flat, selected):
    z = df[(df.iso3 == code) & df.year.between(2000, 2021)].set_index("year").reindex(range(2000, 2022))
    base = z.loc[2000]
    assert pd.notna(base[R2]).all() and pd.notna(z.loc[2021, R2]).all()
    assert z[R2].notna().all().all(), f"Unexpected gap in {code}"
    for col, lab, color in styles:
        yy = 100 * z[col] / base[col]
        ax.plot(yy.index, yy.values, color=color, lw=2.3, label=lab)
        ax.scatter([2021], [yy.loc[2021]], color=color, s=20, zorder=3)
    name = z.country.dropna().iloc[0]
    ax.set_title(f"{name}  |  2000: ${base.gdp_pc_ppp_int2021:,.0f}, {base.urban_population_pct:.0f}% urban", loc="left", fontsize=10, weight="bold")
    ax.set_ylim(55, 275); ax.set_xlim(2000, 2021.7)
    ax.set_xticks([2000, 2005, 2010, 2015, 2021])
    ax.grid(axis="y", color="#dce3e8", lw=.7)
for ax in axes[:,0]: ax.set_ylabel("Index (2000 = 100)")
for ax in axes[-1,:]: ax.set_xlabel("Year")
fig.legend(*axes.flat[0].get_legend_handles_labels(), loc="lower center", ncol=3, frameon=False, bbox_to_anchor=(.5, -.01))
fig.text(.5, -.06, "GDP is in constant 2021 international dollars; urban share uses national definitions.", ha="center", fontsize=8.4)
fig.tight_layout(rect=[0,.035,1,.92], h_pad=2.2, w_pad=1.4)
save(fig, "rq2_peer_paths.png")

# Figure 2: global context for the selected peer examples.
fig, ax = plt.subplots(figsize=(11, 7))
x = r2.pct_change_gdp_pc_ppp_int2021
y = r2.pct_change_co2_pc_wdi_t
c = r2.change_urban_population_pct
sc = ax.scatter(x, y, c=c, cmap="PuOr_r", vmin=-20, vmax=40, s=37,
                edgecolor="white", linewidth=.35, alpha=.83)
ax.axhline(0, color="#65727c", lw=.9); ax.axvline(0, color="#65727c", lw=.9)
ax.set_yscale("symlog", linthresh=60)
ax.set_yticks([-70, -40, 0, 40, 100, 300, 1000])
ax.yaxis.set_major_formatter(FuncFormatter(lambda v,p:f"{v:g}"))
ax.set_xlim(-55, 430); ax.set_ylim(-80, 1900)
ax.set_xlabel("Change in PPP GDP per person, 2000–2021 (%)")
ax.set_ylabel("Change in CO₂ per person, 2000–2021 (%)")
ax.grid(color="#e3e8eb", lw=.6); ax.set_axisbelow(True)
for code in selected:
    q = r2[r2.iso3 == code].iloc[0]
    ax.annotate(code, (q.pct_change_gdp_pc_ppp_int2021, q.pct_change_co2_pc_wdi_t),
                xytext=(5,5), textcoords="offset points", fontsize=8, weight="bold")
cb = fig.colorbar(sc, ax=ax, pad=.02, shrink=.85)
cb.set_label("Change in urban share (percentage points)")
fig.suptitle("Income growth often coincided with higher emissions per person", x=.12, ha="left", fontsize=17, weight="bold")
fig.text(.12,.925,"2000–2021 | 190 economies with all three measures at both endpoints | labelled peer examples", fontsize=10)
fig.text(.12,.015,"Vertical scale is linear near zero and compressed beyond ±60%; CO₂ percentage changes can be large from small baselines.", fontsize=8.2)
fig.tight_layout(rect=[.08,.035,1,.89])
save(fig,"rq2_all_economies_changes.png")

# Baseline income and primary-energy tertiles are defined on the exact 182-economy panel.
r3["income_group"] = pd.qcut(r3.gdp_pc_ppp_int2021_2000, 3, labels=["Lower", "Middle", "Higher"])
r3["energy_group"] = pd.qcut(r3.energy_pc_owid_kwh_2000, 3, labels=["Low", "Medium", "High"])
r3.to_csv(DERIVED / "rq3_2000_2021_grouped.csv", index=False)
income_cuts = r3.gdp_pc_ppp_int2021_2000.quantile([1/3, 2/3]).to_numpy()
energy_cuts = r3.energy_pc_owid_kwh_2000.quantile([1/3, 2/3]).to_numpy()

# Figure 3: facet by baseline income, encode baseline energy use by colour.
fig, axes = plt.subplots(1, 3, figsize=(10.6, 6.0), sharey=True)
energy_colors = {"Low":"#487bb1", "Medium":"#d18a25", "High":"#7a4f8c"}
energy_labels = {
    "Low":f"Low: ≤{energy_cuts[0]/1000:.1f}k",
    "Medium":f"Medium: {energy_cuts[0]/1000:.1f}–{energy_cuts[1]/1000:.1f}k",
    "High":f"High: >{energy_cuts[1]/1000:.1f}k",
}
income_labels = {
    "Lower":f"≤ ${income_cuts[0]/1000:.1f}k/person",
    "Middle":f"${income_cuts[0]/1000:.1f}–{income_cuts[1]/1000:.1f}k/person",
    "Higher":f"> ${income_cuts[1]/1000:.1f}k/person",
}
for ax, income in zip(axes, ["Lower", "Middle", "Higher"]):
    z = r3[r3.income_group == income]
    for en in ["Low", "Medium", "High"]:
        q = z[z.energy_group == en]
        ax.scatter(q.change_renewable_final_energy_pct, q.change_carbon_intensity_energy_g_kwh,
                   s=39, c=energy_colors[en], alpha=.8, edgecolors="white", linewidths=.35, label=energy_labels[en])
    ax.axhline(0, color="#64727d", lw=.9); ax.axvline(0,color="#64727d",lw=.9)
    ax.set_title(f"{income} 2000 income | n = {len(z)}\n{income_labels[income]}", fontsize=11.2, weight="bold")
    ax.set_xlim(-45,34); ax.set_xticks([-40,-20,0,20])
    ax.set_yscale("symlog", linthresh=50)
    ax.set_ylim(-1250,210); ax.set_yticks([-1000,-300,-100,-50,0,50,150])
    ax.yaxis.set_major_formatter(FuncFormatter(lambda v,p:f"{v:g}"))
    ax.grid(color="#e5eaed",lw=.6); ax.set_axisbelow(True)
    ax.set_xlabel("Renewable share change (pp)", fontsize=11.2)
    ax.tick_params(labelsize=10.5)
axes[0].set_ylabel("CO₂ intensity change (g/kWh primary energy)", fontsize=11.2)
fig.legend(*axes[0].get_legend_handles_labels(), title="Point colour: 2000 primary energy use (kWh/person; k = 1,000)", ncol=3,
           loc="lower center", bbox_to_anchor=(.5,.03), frameon=False, fontsize=10.5, title_fontsize=10.5)
fig.suptitle("Renewable-share and carbon-intensity changes by starting income", x=.04, ha="left", fontsize=15.2, weight="bold")
fig.text(.04,.91,"Each dot: 2021 value minus 2000 value for one of 182 economies; intervening years are not shown.", fontsize=10.4)
fig.text(.04,.015,"pp = percentage points. Income: 2000 PPP GDP/person in constant 2021 international dollars. Y scale compresses beyond ±50 g/kWh.", fontsize=9.1)
fig.tight_layout(rect=[.005,.13,1,.865], w_pad=.8)
save(fig,"rq3_changes_by_income.png")

# Figure 4: a complementary cross-classification, with one quantity encoded by colour.
cells = r3.groupby(["income_group","energy_group"], observed=True).agg(
    n=("iso3","size"), median_intensity_change=("change_carbon_intensity_energy_g_kwh","median"),
    median_renewable_change=("change_renewable_final_energy_pct","median")).reset_index()
cells.to_csv(DERIVED / "rq3_tertile_medians.csv", index=False)
arr = cells.pivot(index="income_group", columns="energy_group", values="median_intensity_change").loc[["Lower","Middle","Higher"],["Low","Medium","High"]]
fig, ax = plt.subplots(figsize=(8.7,6.5))
im=ax.imshow(arr, cmap="PuOr_r", vmin=-75,vmax=75)
ax.set_xticks(range(3), ["Low","Medium","High"]);ax.set_yticks(range(3),["Lower","Middle","Higher"])
ax.set_xlabel("2000 primary energy use per person (within-sample tertiles)")
ax.set_ylabel("2000 PPP GDP per person (within-sample tertiles)")
for i, income in enumerate(["Lower","Middle","Higher"]):
 for j, energy in enumerate(["Low","Medium","High"]):
    match=cells[(cells.income_group==income)&(cells.energy_group==energy)]
    label = "No economies" if match.empty else f"{match.iloc[0].median_intensity_change:+.0f} g/kWh\nn = {int(match.iloc[0].n)}"
    ax.text(j,i,label,ha="center",va="center",fontsize=11,weight="bold")
cb=fig.colorbar(im,ax=ax,shrink=.8);cb.set_label("Median CO₂ intensity change (g/kWh)")
fig.suptitle("Median intensity changes vary across income and energy-use groups",x=.06,ha="left",fontsize=15,weight="bold")
fig.text(.06,.91,"2000–2021 | 182 economies with all four measures at both endpoints | each cell is a median",fontsize=9.5)
fig.text(.06,.015,"Grouping uses 2000 values; uneven cell sizes are printed. Final-energy renewable-share changes are in the supporting CSV.",fontsize=8.2)
fig.tight_layout(rect=[.04,.04,1,.88])
save(fig,"rq3_income_energy_heatmap.png")

# Compact machine-readable summary used in the accompanying prose.
summary = {
 "r2_n":len(r2), "r3_n":len(r3),
 "r2_median_co2_pct":r2.pct_change_co2_pc_wdi_t.median(),
 "r2_median_gdp_pct":r2.pct_change_gdp_pc_ppp_int2021.median(),
 "r3_increase_renewable_decrease_intensity":int(((r3.change_renewable_final_energy_pct>0)&(r3.change_carbon_intensity_energy_g_kwh<0)).sum()),
 "r3_income_median_intensity":r3.groupby("income_group",observed=True).change_carbon_intensity_energy_g_kwh.median().to_dict(),
}
import json
(DERIVED/"analysis_summary.json").write_text(json.dumps(summary,indent=2)+"\n")

def add_p(doc, text, style=None):
    p=doc.add_paragraph(style=style)
    if text.startswith("Columns used from the dataset:"):
        fields = ("carbon_intensity_energy_g_kwh", "renewable_final_energy_pct",
                  "gdp_pc_ppp_int2021", "energy_pc_owid_kwh",
                  "urban_population_pct", "co2_pc_wdi_t", "population_wdi",
                  "co2_mt", "country", "iso3", "year")
        pattern = re.compile(r"\b(" + "|".join(fields) + r")\b")
        for part in pattern.split(text):
            if part:
                run = p.add_run(part)
                if part in fields:
                    run.italic = True
    else:
        p.add_run(text)
    return p

def accent_block(paragraph, fill=None, color="0F6B70", width="18"):
    """Apply a quiet left rule and optional tint without changing paragraph text."""
    ppr = paragraph._p.get_or_add_pPr()
    if fill:
        shade = OxmlElement("w:shd")
        shade.set(qn("w:fill"), fill)
        ppr.append(shade)
    borders = OxmlElement("w:pBdr")
    left = OxmlElement("w:left")
    left.set(qn("w:val"), "single")
    left.set(qn("w:sz"), width)
    left.set(qn("w:color"), color)
    left.set(qn("w:space"), "8")
    borders.append(left)
    ppr.append(borders)

def paragraph_style(styles, name, font, size, color="000000", *, bold=False, italic=False):
    style = styles.add_style(name, WD_STYLE_TYPE.PARAGRAPH)
    style.base_style = styles["Normal"]
    style.font.name = font
    style.font.size = Pt(size)
    style.font.bold = bold
    style.font.italic = italic
    style.font.color.rgb = RGBColor.from_string(color)
    return style

doc=Document()
sec=doc.sections[0];sec.page_width=Cm(21);sec.page_height=Cm(29.7)
sec.top_margin=Cm(1.45);sec.bottom_margin=Cm(1.45);sec.left_margin=Cm(1.85);sec.right_margin=Cm(1.85)
styles=doc.styles
styles["Normal"].font.name="Arial";styles["Normal"].font.size=Pt(9.25)
styles["Normal"].paragraph_format.space_after=Pt(4.2)
styles["Normal"].paragraph_format.line_spacing=1.08
styles["Title"].font.name="Georgia";styles["Title"].font.size=Pt(20);styles["Title"].font.bold=True;styles["Title"].font.color.rgb=RGBColor(0,0,0)
styles["Title"].paragraph_format.space_after=Pt(3)
title_ppr = styles["Title"]._element.pPr
if title_ppr is not None:
    for border in title_ppr.findall(qn("w:pBdr")):
        title_ppr.remove(border)
for name in ["Heading 1","Heading 2"]:
    styles[name].font.name="Georgia";styles[name].font.color.rgb=RGBColor(0,0,0)
styles["Heading 1"].font.size=Pt(13.5)
styles["Heading 1"].font.bold=True
styles["Heading 1"].paragraph_format.space_before=Pt(10)
styles["Heading 1"].paragraph_format.space_after=Pt(5)
styles["Heading 1"].paragraph_format.keep_with_next=True
subtitle_style = paragraph_style(styles,"Report Subtitle","Arial",8.8,"0F6B70",bold=True)
subtitle_style.font.all_caps = True
subtitle_style.paragraph_format.space_after=Pt(2)
byline_style = paragraph_style(styles,"Report Byline","Arial",8.4,"566872")
byline_style.paragraph_format.space_after=Pt(8)
intro_style = paragraph_style(styles,"Report Intro","Arial",9.5,"34444C")
intro_style.paragraph_format.space_after=Pt(8)
question_style = paragraph_style(styles,"Research Question","Arial",9.2,"173D46")
question_style.paragraph_format.left_indent=Cm(.22)
question_style.paragraph_format.right_indent=Cm(.15)
question_style.paragraph_format.space_before=Pt(3)
question_style.paragraph_format.space_after=Pt(7)
question_style.paragraph_format.keep_with_next=True
figure_style = paragraph_style(styles,"Figure Art","Arial",9)
figure_style.paragraph_format.space_after=Pt(2)
caption_style = paragraph_style(styles,"Figure Caption","Arial",8.6,"566872",italic=True)
caption_style.paragraph_format.space_after=Pt(6)
fields_style = paragraph_style(styles,"Dataset Fields","Arial",8.9,"263B43")
fields_style.paragraph_format.left_indent=Cm(.22)
fields_style.paragraph_format.right_indent=Cm(.15)
fields_style.paragraph_format.space_before=Pt(3)
fields_style.paragraph_format.space_after=Pt(7)
section_style = paragraph_style(styles,"Explanation Section","Arial",9.2,"0F6B70",bold=True)
section_style.paragraph_format.space_before=Pt(5)
section_style.paragraph_format.space_after=Pt(2)
section_style.paragraph_format.keep_with_next=True
doc.add_paragraph("Economic Development and Carbon Dioxide Emissions", style="Title")
add_p(doc,"Individual Assignment 2  Exploratory Data Analysis",style="Report Subtitle")
add_p(doc,"Yazdan ZandiyeVakili  |  12642780  |  Information Visualization VU  |  TU Wien",style="Report Byline")
add_p(doc,"I use the merged OWID and World Bank dataset to compare development paths and energy patterns. The charts use observed values only; I did not fill missing data.",style="Report Intro")

heading=doc.add_heading("Figure 1  Income urbanization and emissions per person",level=1);accent_block(heading,width="15")
question=add_p(doc,"Research question  RQ2  Over the available years, how did CO₂ per person change alongside income and the share of people living in cities, and which economies followed different paths from similar peers?",style="Research Question");accent_block(question,fill="EEF5F4")
doc.add_picture(str(FIG/"rq2_peer_paths.png"),width=Cm(16.25))
doc.paragraphs[-1].style="Figure Art"
add_p(doc,"Figure 1. Annual paths from 2000 to 2021. For each country and measure, its value in 2000 is set to 100.",style="Figure Caption")
fields=add_p(doc,"Columns used from the dataset: co2_pc_wdi_t draws the blue CO₂ line, gdp_pc_ppp_int2021 the teal income line, and urban_population_pct the orange urban-share line. The year column sets the x-axis and country names the panels. CO₂ per person comes from co2_mt and population_wdi.",style="Dataset Fields");accent_block(fields,fill="F3F6F6",color="81A7A7",width="12")
add_p(doc,"Design of the visual",style="Explanation Section")
add_p(doc,"I chose two pairs from the WDI Europe and Central Asia region after reviewing the 190 economies with complete endpoint data. In 2000, Estonia and Poland had PPP incomes of about $20,527 and $18,566 per person and urban shares of 67% and 62%; Romania and Türkiye began near $14,855 per person, at 53% and 59% urban. All four have complete annual data through 2021. Their later CO₂ paths differ, so they are useful examples, though not statistical matches or typical cases. Lines show when the paths changed. The vertical axis indexes each measure to its own 2000 value: 100 × annual value ÷ 2000 value. I use 2000 as the common baseline because these series are complete from then and it matches Figure 2's interval. Thus 150 means a 50% rise and 70 a 30% fall. The common scale makes relative changes comparable but hides starting levels.")
add_p(doc,"What we found",style="Explanation Section")
add_p(doc,"The pairs do not follow one common development path. Estonia and Poland had similar income growth (116% and 121%), yet CO₂ per person fell 30% in Estonia and rose 8% in Poland; their urban shares changed only slightly (+2.8 and −1.9 percentage points). Romania and Türkiye began at almost the same income level, but Romania's CO₂ per person stayed roughly level (−2%) as income rose 153%, while Türkiye's CO₂ per person rose 53% as income rose 116%. Türkiye's urban share also rose far more (+30 points versus about −1 point in Romania). In these examples, income growth or urbanization alone does not describe the emissions path. Other conditions may matter, but this chart cannot identify their effects or show that urbanization caused the difference.")

doc.add_page_break()
heading=doc.add_heading("Figure 2  Renewable energy and carbon intensity",level=1);accent_block(heading,width="15")
question=add_p(doc,"Research question  RQ3  Over years with data for all required measures, how did changes in the renewable share of final energy relate to CO₂ per unit of primary energy, and how did patterns differ by income and energy use per person?",style="Research Question");accent_block(question,fill="EEF5F4")
doc.add_picture(str(FIG/"rq3_changes_by_income.png"),width=Cm(16.25))
doc.paragraphs[-1].style="Figure Art"
add_p(doc,"Figure 2. Each dot is one economy. The two axes show its change from 2000 to 2021, rather than its values in each intervening year. The chart includes 182 economies with all four measures in both years.",style="Figure Caption")
fields=add_p(doc,"Columns used from the dataset: renewable_final_energy_pct gives the x-axis change (2021 minus 2000, in percentage points), and carbon_intensity_energy_g_kwh gives the y-axis change (g CO₂/kWh). The year column selects the two endpoints. The 2000 value of gdp_pc_ppp_int2021 sets the income panel; the 2000 value of energy_pc_owid_kwh, primary energy use per person, sets the dot colour.",style="Dataset Fields");accent_block(fields,fill="F3F6F6",color="81A7A7",width="12")
add_p(doc,"Design of the visual",style="Explanation Section")
add_p(doc,"Each dot is one economy, not one year. A dot right of zero had a higher renewable share in 2021; a dot below zero had lower CO₂ intensity. The lower-right quadrant shows both. The income panels split 2000 PPP GDP per person, in constant 2021 international dollars, at $5,076.23 and $17,674.49. Dot colours split 2000 primary energy use per person at 4,295.50 and 23,377.16 kWh: blue is low, orange middle, and purple high. Here, 'high energy use' means more than 23,377.16 kWh per person. These are thirds of this sample, not universal or official categories. The vertical scale compresses changes beyond ±50 g/kWh to keep outliers visible, making distances there harder to judge.")
add_p(doc,"What we found",style="Explanation Section")
add_p(doc,"In the lower-right quadrant, rising renewable share coincided with falling CO₂ intensity for 1 of 61 lower-income economies, 14 of 60 middle-income economies, and 41 of 61 higher-income economies. Higher income and energy use also overlap: 53 of 61 economies in the highest-income panel have purple dots, so the chart cannot separate their effects. It shows an association between two endpoint changes, not a yearly trend or a causal effect. Renewable share uses final energy and may include biomass; CO₂ intensity uses primary energy. The denominators differ, and the chart does not show what happened between 2000 and 2021.")
for paragraph in doc.paragraphs:
    paragraph.alignment = (WD_ALIGN_PARAGRAPH.CENTER if paragraph._p.xpath('.//a:blip')
                           else WD_ALIGN_PARAGRAPH.JUSTIFY)
doc.save(REPORT/"individual-assignment-02.docx")

supp = """# Supplementary exploration and submission recommendation

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
"""
(SUPP/"supplementary-exploration.md").write_text(supp)
print(json.dumps(summary,indent=2))
