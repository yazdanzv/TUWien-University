"""Create the compact assignment report; render separately for visual QA."""
from pathlib import Path
import json
import re
from docx import Document
from docx.shared import Inches, Pt, RGBColor
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.enum.text import WD_ALIGN_PARAGRAPH

BASE = Path(__file__).resolve().parents[2]
OUT = BASE / 'submission'
OUT.mkdir(exist_ok=True)
NAME = 'IA01_ZandiyeVakili_12642780_Report'
WHITE = [
    "The white hat figure shows Austria’s housing overburden rate alongside the EU rate for the lowest-income fifth. Between 2015 and 2025, Austria’s rate rose from 26.7% to 27.2%, while the EU rate fell from 36.2% to 25.8%. Austria ended slightly above the EU, although its own rate changed little.",
    "I used the same percentage scale for both lines so their levels can be compared directly. The vertical axis runs from zero to 40%. Light gridlines help readers estimate values, while labels show the starting and ending rates and the net changes. Every year is included, making Austria’s fluctuations and its 2022 peak visible. Teal circles identify Austria and purple squares identify the EU, so readers can distinguish them by shape as well as colour.",
    "The lower bar shows how Austria’s increase and the EU’s decrease widened the gap. Austria’s rise contributed 0.5 percentage points (pp), and the EU’s fall contributed 10.4, giving a total shift of 10.9 points. The bar lengths show these amounts. The labels also record the gap at each endpoint: Austria was 9.5 points below the EU in 2015 and 1.4 points above it in 2025. This calculation describes the change; it does not explain its causes."
]
BLACK = [
    "The black hat figure divides Austria’s housing overburden rate by the EU rate each year, then sets the 2015 comparison to 100. The index reaches 142.9 in 2025, a rise of about 43%. Both the large headline and the final value label refer to this index. The group and period are the same as in the first figure.",
    "A teal line connects the annual values, with a circular marker for every year. The line rises and falls during the decade, including a drop in 2021 and a rebound in 2022. The horizontal axis labels every year from 2015 to 2025. The vertical axis runs from 90 to 160, with gridlines at intervals of ten and a stronger line at 100. Labels mark the first and last index values.",
    "The title highlights Austria as the focus, and the subtitle adds context by specifying the comparison with the EU. The formula below the plot gives the calculation: divide each year’s Austria/EU rate ratio by its 2015 value, then multiply by 100. The two original rates are not drawn separately. Here, 100 represents the starting comparison in 2015; it does not mean the two rates were equal. The 2025 index of 142.9 corresponds to an Austrian rate about 5.4% above the EU rate that year."
]
CONCLUSION = [
    "The white hat chart keeps both rates visible, so readers can see that Austria’s worsening position mainly reflects the EU’s falling rate. The black hat chart is deceptive because its large “Up 43%” headline can be mistaken for an increase within Austria, whose rate actually rose by only 1.9%. The smaller subtitle and formula explain the comparison, but receive less attention, while the original rates are absent. The calculation is correct; its framing encourages the wrong interpretation. These are intended reading effects, not results from an audience study."
]

def count(paras):
    return len(re.findall(r"\S+", ' '.join(paras)))
for label, paras in [('white', WHITE), ('black', BLACK)]:
    assert 200 <= count(paras) <= 500
    print(label, count(paras), 'words')

D = Document()
s = D.sections[0]
s.page_width, s.page_height = Inches(8.5), Inches(11)
s.top_margin, s.bottom_margin = Inches(.65), Inches(.6)
s.left_margin, s.right_margin = Inches(.65), Inches(.65)
s.footer_distance = Inches(.27)
styles = D.styles
for name in ['Normal', 'Title', 'Subtitle', 'Heading 1', 'Heading 2', 'Caption']:
    styles[name].font.name = 'Arial'
    styles[name].font.color.rgb = RGBColor(0, 0, 0)
    for border in styles[name].element.xpath('./w:pPr/w:pBdr'):
        border.getparent().remove(border)
    for fonts in styles[name].element.xpath('./w:rPr/w:rFonts'):
        for attribute in list(fonts.attrib):
            if 'theme' in attribute.lower():
                del fonts.attrib[attribute]
normal = styles['Normal']
normal.font.size = Pt(11)
normal.paragraph_format.line_spacing = 1.12
normal.paragraph_format.space_after = Pt(7)
normal.paragraph_format.widow_control = True
styles['Title'].font.name = 'Arial'
styles['Title'].font.bold = True
styles['Title'].font.size = Pt(30)
styles['Title'].font.color.rgb = RGBColor.from_string('087F84')
styles['Heading 1'].font.color.rgb = RGBColor.from_string('087F84')
styles['Heading 2'].font.color.rgb = RGBColor.from_string('087F84')
styles['Title'].paragraph_format.space_after = Pt(12)
styles['Subtitle'].font.size = Pt(11)
styles['Subtitle'].font.italic = False
styles['Subtitle'].paragraph_format.space_after = Pt(8)
for name, size in [('Heading 1', 18), ('Heading 2', 14)]:
    styles[name].font.size = Pt(size)
    styles[name].font.bold = True
    styles[name].paragraph_format.space_before = Pt(14)
    styles[name].paragraph_format.space_after = Pt(8)
    styles[name].paragraph_format.keep_with_next = True
# A small page number provides navigation without a running title.
f = s.footer.paragraphs[0]
f.alignment = WD_ALIGN_PARAGRAPH.RIGHT
r = f.add_run()
r.font.name = 'Arial'; r.font.size = Pt(9)
fld = OxmlElement('w:fldSimple'); fld.set(qn('w:instr'), 'PAGE'); r._r.addnext(fld)

D.core_properties.title = 'Housing overburden in Austria and the changing EU rate'
D.core_properties.subject = 'Information Visualization Individual Assignment 1'
D.core_properties.author = 'Yazdan Zandiye Vakili'
D.core_properties.keywords = 'housing overburden, white hat, black hat, benchmark'
D.add_paragraph('Housing overburden in Austria\nand the changing EU rate', 'Title')
D.add_paragraph('Individual Assignment 1  |  White Hat and Black Hat Visualization', 'Subtitle')
p = D.add_paragraph('Yazdan Zandiye Vakili  |  12642780\nInformation Visualization VU  |  TU Wien  |  Winter semester 2026')
p.paragraph_format.space_after = Pt(19)
p.runs[0].font.size = Pt(10)
D.add_paragraph('Austria’s position relative to the EU worsened mainly because the EU rate fell. These two figures show how presenting the same data differently can change the message.')
D.add_paragraph('Shared data question', 'Heading 2')
p = D.add_paragraph('How differently do national rates and EU-relative measures portray the change in Austria’s housing cost overburden for the lowest-income fifth between 2015 and 2025?')
p.runs[0].font.size = Pt(14)
p.paragraph_format.line_spacing = 1.12
p.paragraph_format.space_after = Pt(10)
D.add_paragraph('Dataset and scope', 'Heading 2')
D.add_paragraph('Both figures use Eurostat’s Housing cost overburden rate by income quintile dataset, based on EU-SILC. I selected 22 annual observations for Austria and the EU-27, covering the lowest-income fifth from 2015 to 2025. The rate measures the percentage of people whose household housing costs exceed 40% of disposable household income. Housing allowances are deducted from both costs and income.')
D.add_paragraph('Dataset source', 'Heading 2')
D.add_paragraph('The original data values were kept unchanged.')
p = D.add_paragraph()
p.paragraph_format.space_before = Pt(10)
p.paragraph_format.space_after = Pt(0)
r=p.add_run('Source  '); r.bold=True
link=OxmlElement('w:hyperlink')
link.set(qn('r:id'), D.part.relate_to('https://doi.org/10.2908/ILC_LVHO07B', 'http://schemas.openxmlformats.org/officeDocument/2006/relationships/hyperlink', is_external=True))
lr=OxmlElement('w:r'); prop=OxmlElement('w:rPr'); col=OxmlElement('w:color'); col.set(qn('w:val'),'146B70'); prop.append(col); lr.append(prop)
t=OxmlElement('w:t'); t.text='doi.org/10.2908/ILC_LVHO07B'; lr.append(t); link.append(lr); p._p.append(link)
for r in p.runs: r.font.size=Pt(9)

for label, filename, paragraphs in [
    ('White hat visualization', 'benchmark-white-hat.png', WHITE),
    ('Black hat visualization', 'benchmark-black-hat.png', BLACK),
]:
    D.add_page_break()
    h = D.add_paragraph(label, 'Heading 1')
    if label.startswith('Black'):
        h.runs[0].font.color.rgb = RGBColor.from_string('6B687D')
    h.paragraph_format.space_before=Pt(0)
    h.paragraph_format.space_after=Pt(7)
    p=D.add_paragraph()
    p.paragraph_format.space_after=Pt(10)
    p.paragraph_format.line_spacing=1
    if label.startswith('Black'):
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    pic=p.add_run().add_picture(str(BASE/'working/figures'/filename), width=Inches(6.5 if label.startswith('Black') else 7.2))
    pic._inline.docPr.set('descr', 'Annual Austria and EU-27 rates and a bar explaining the change in their gap.' if 'white' in filename else 'Austria to EU-27 rate ratio indexed to 100 in 2015, reaching 142.9 in 2025.')
    for text in paragraphs:
        body = D.add_paragraph(text)
        if label.startswith('Black'):
            body.paragraph_format.space_after = Pt(6)
D.add_page_break()
conclusion_heading = D.add_paragraph('Conclusion', 'Heading 1')
conclusion_heading.paragraph_format.space_before = Pt(0)
for text in CONCLUSION:
    D.add_paragraph(text)
# Apply Word's Justify Low to prose while preserving title and figure alignment.
for paragraph in D.paragraphs:
    if paragraph.style.name == 'Normal' and len(paragraph.text.split()) > 20:
        paragraph.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY_LOW
# Italicize named sources, institutions, places and dataset identifiers in prose.
# Match within each existing run to preserve paragraph layout and other formatting.
from copy import deepcopy
special_names = [
    'Housing cost overburden rate by income quintile',
    'Yazdan Zandiye Vakili', 'Information Visualization VU', 'TU Wien',
    'Eurostat', 'EU-SILC', 'ilc_lvho07b', 'EU27_2020', 'EU-27',
    'Austria', 'EU', 'QU1', 'AT',
]
pattern = re.compile(r'(?<![A-Za-z0-9_])(' + '|'.join(re.escape(t) for t in sorted(special_names, key=len, reverse=True)) + r')(?![A-Za-z0-9_])')
for paragraph in D.paragraphs:
    if paragraph.style.name not in {'Normal', 'Subtitle'}:
        continue
    for run in list(paragraph.runs):
        if not pattern.search(run.text):
            continue
        original_properties = deepcopy(run._r.rPr)
        source = run.text
        anchor = run._r
        for segment in pattern.split(source):
            if not segment:
                continue
            from docx.text.run import Run
            element = OxmlElement('w:r')
            if original_properties is not None:
                element.append(deepcopy(original_properties))
            anchor.addnext(element)
            new_run = Run(element, paragraph)
            new_run.text = segment
            if pattern.fullmatch(segment):
                new_run.italic = True
            anchor = element
        run._r.getparent().remove(run._r)
D.save(OUT/f'{NAME}.docx')
(BASE/'working/report-word-counts.json').write_text(json.dumps({'white_hat_rationale':count(WHITE),'black_hat_rationale':count(BLACK),'conclusion':count(CONCLUSION),'body_without_figures':count([p.text for p in D.paragraphs])},indent=2)+'\n')
print(OUT/f'{NAME}.docx')
