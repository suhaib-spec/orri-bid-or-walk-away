"""Build the SIMPLE 15-minute deck: 10 main slides + 2 AI-appendix slides + 1 references slide.
Order follows the case: recommendation, financial model, funding plan, risk analysis, AI record, references.
Same numbers as build_deck.py (the full deck); fewer words, one visual per slide, bigger type.
Run: python -I model/build_deck_simple.py <deliverables dir>"""
import sys, os
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.chart.data import CategoryChartData
from pptx.enum.chart import XL_CHART_TYPE, XL_LEGEND_POSITION, XL_TICK_LABEL_POSITION, XL_LABEL_POSITION
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.enum.shapes import MSO_SHAPE
from pptx.enum.dml import MSO_LINE_DASH_STYLE

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import ANALYSIS_DIR
# Output folder: first argument, else _analysis/deliverables
OUT = os.path.join(sys.argv[1] if len(sys.argv) > 1 else os.path.join(ANALYSIS_DIR, 'deliverables'), 'ORRI_Bid_or_Walk_Away_SIMPLE.pptx')
NAVY = RGBColor(0x1F, 0x38, 0x64); GREY = RGBColor(0x59, 0x59, 0x59); RED = RGBColor(0xC0, 0x00, 0x00)
GREEN = RGBColor(0x37, 0x86, 0x3C); LIGHT = RGBColor(0xD9, 0xE1, 0xF2); WHITE = RGBColor(0xFF, 0xFF, 0xFF)
PALE = RGBColor(0xF2, 0xF2, 0xF2); MID = RGBColor(0xA6, 0xA6, 0xA6); YELLOW = RGBColor(0xFF, 0xF2, 0xCC)
LGREEN = RGBColor(0x9B, 0xC8, 0x8E); BLACK = RGBColor(0x26, 0x26, 0x26)
FONT = 'Arial'
prs = Presentation(); prs.slide_width = Inches(13.333); prs.slide_height = Inches(7.5)
BL = prs.slide_layouts[6]


def slide(title, num=None, sub=None):
    s = prs.slides.add_slide(BL)
    bar = s.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, prs.slide_width, Inches(1.05))
    bar.fill.solid(); bar.fill.fore_color.rgb = NAVY; bar.line.fill.background(); bar.shadow.inherit = False
    tb = s.shapes.add_textbox(Inches(0.4), Inches(0.1), Inches(12.5), Inches(0.85)); tf = tb.text_frame; tf.word_wrap = True
    tf.vertical_anchor = MSO_ANCHOR.MIDDLE
    p = tf.paragraphs[0]; p.text = title; p.font.size = Pt(28); p.font.bold = True; p.font.color.rgb = WHITE; p.font.name = FONT
    if sub:
        text(s, sub, 0.45, 1.12, 12.4, 0.45, size=16, italic=True, color=GREY)
    if num:
        t3 = s.shapes.add_textbox(Inches(12.4), Inches(7.05), Inches(0.8), Inches(0.35)); r = t3.text_frame.paragraphs[0]
        r.text = str(num); r.font.size = Pt(11); r.font.color.rgb = GREY; r.alignment = PP_ALIGN.RIGHT; r.font.name = FONT
    return s


def text(s, lines, x, y, w, h, size=18, bold=False, italic=False, color=BLACK, align=PP_ALIGN.LEFT,
         anchor=MSO_ANCHOR.TOP, space=6):
    """lines: str or list of str / (str, dict) pairs. dict keys: size, bold, color, italic."""
    tb = s.shapes.add_textbox(Inches(x), Inches(y), Inches(w), Inches(h)); tf = tb.text_frame; tf.word_wrap = True
    tf.vertical_anchor = anchor
    if isinstance(lines, str): lines = [lines]
    for i, ln in enumerate(lines):
        opt = {}
        if isinstance(ln, tuple): ln, opt = ln
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        p.text = ln; p.alignment = align; p.space_after = Pt(opt.get('space', space))
        f = p.font; f.name = FONT; f.size = Pt(opt.get('size', size)); f.bold = opt.get('bold', bold)
        f.italic = opt.get('italic', italic); f.color.rgb = opt.get('color', color)
    return tb


def box(s, x, y, w, h, fill=LIGHT, line=None, dash=False, shape=MSO_SHAPE.ROUNDED_RECTANGLE):
    b = s.shapes.add_shape(shape, Inches(x), Inches(y), Inches(w), Inches(h))
    b.shadow.inherit = False
    if fill is None: b.fill.background()
    else: b.fill.solid(); b.fill.fore_color.rgb = fill
    if line is None: b.line.fill.background()
    else:
        b.line.color.rgb = line; b.line.width = Pt(2.25)
        if dash: b.line.dash_style = MSO_LINE_DASH_STYLE.DASH
    if shape == MSO_SHAPE.ROUNDED_RECTANGLE: b.adjustments[0] = 0.08
    return b


def card(s, x, y, w, h, big, small, fill=LIGHT, big_color=NAVY, small_color=BLACK, big_size=40, small_size=15, line=None):
    box(s, x, y, w, h, fill=fill, line=line)
    text(s, [(big, {'size': big_size, 'bold': True, 'color': big_color, 'space': 4}),
             (small, {'size': small_size, 'color': small_color, 'space': 0})],
         x + 0.15, y + 0.1, w - 0.3, h - 0.2, align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)


def table(s, data, x, y, w, h, size=16, widths=None, hl_rows=(), bold_col0=False):
    rows, cols = len(data), len(data[0])
    t = s.shapes.add_table(rows, cols, Inches(x), Inches(y), Inches(w), Inches(h)).table
    for i, row in enumerate(data):
        for j, v in enumerate(row):
            c = t.cell(i, j); c.text = str(v); c.vertical_anchor = MSO_ANCHOR.MIDDLE
            c.margin_top = Inches(0.05); c.margin_bottom = Inches(0.05)
            for p in c.text_frame.paragraphs:
                p.font.size = Pt(size); p.font.name = FONT
                if i == 0: p.font.bold = True; p.font.color.rgb = WHITE
                if i in hl_rows or (bold_col0 and j == 0 and i > 0): p.font.bold = True
            if i == 0: c.fill.solid(); c.fill.fore_color.rgb = NAVY
            elif i in hl_rows: c.fill.solid(); c.fill.fore_color.rgb = YELLOW
    if widths:
        for j, wd in enumerate(widths): t.columns[j].width = Inches(wd)
    return t


def note(s, txt, y=6.95, size=11):
    text(s, txt, 0.5, y, 11.8, 0.45, size=size, italic=True, color=GREY)


def chart_font(ch, size=14):
    ch.font.name = FONT; ch.font.size = Pt(size)


# 1 ---------------------------------------------------------------- the answer (title slide)
s = prs.slides.add_slide(BL)
band = box(s, 0, 0, 13.333, 1.95, fill=NAVY, shape=MSO_SHAPE.RECTANGLE)
text(s, [('Bid or Walk Away?   Our answer: BID', {'size': 38, 'bold': True, 'color': WHITE, 'space': 6}),
         ('19 Gulf of Mexico royalty interests offered by BP  |  decision as of Aug 15, 2018',
          {'size': 18, 'color': LIGHT, 'space': 0})], 0.45, 0.25, 12.4, 1.5)
box(s, 0.5, 2.1, 12.33, 0.6, fill=YELLOW, line=RED, dash=True)
text(s, '[FILL IN]  Team name: ______________    Members: ______________, ______________, ______________',
     0.65, 2.13, 12.0, 0.55, size=16, bold=True, color=RED, anchor=MSO_ANCHOR.MIDDLE)
card(s, 0.5, 2.9, 3.95, 2.2, '$98M', 'cash at closing for all 19 royalties', fill=NAVY, big_color=WHITE,
     small_color=WHITE, big_size=54, small_size=17)
card(s, 4.69, 2.9, 3.95, 2.2, '+ up to $24M', 'paid later ONLY if government production data proves the extra oil',
     fill=GREEN, big_color=WHITE, small_color=WHITE, big_size=40, small_size=17)
card(s, 8.88, 2.9, 3.95, 2.2, '$105M max', 'if BP insists on one fixed price. Above that, we walk away.',
     fill=PALE, big_color=RED, big_size=40, small_size=17, line=RED)
facts = [('~$102M', 'value of the producing wells today (base case)'),
         ('~15%', 'yearly return (~26% in our optimistic case)'),
         ('~$84M', 'cash at closing; 95% from an assumed royalty fund'),
         ('Aug 8', 'no signed money by then = we walk away')]
for i, (b, sm) in enumerate(facts):
    card(s, 0.5 + i * 3.11, 5.3, 2.95, 1.3, b, sm, fill=LIGHT, big_size=28, small_size=13)
text(s, '"We can\'t assume when drilling happens, so we pay for it when the government data shows it happened."',
     0.5, 6.72, 12.3, 0.45, size=15, italic=True, color=NAVY, align=PP_ALIGN.CENTER)

# 2 ---------------------------------------------------------------- what we are buying
s = slide('19 royalty slices, but 3 fields hold ~95% of the value', 2)
cd = CategoryChartData()
cd.categories = ['Kodiak', 'Lucius', 'Stones', 'S. Santa Cruz', 'Ship Shoal', 'Main Pass', 'Grand Isle', 'Orion', 'Pompano']
cd.add_series('Value today ($M)', (52.8, 26.4, 16.9, 2.0, 2.0, 1.0, 0.9, 0.3, 0.0))
ch = s.shapes.add_chart(XL_CHART_TYPE.BAR_CLUSTERED, Inches(0.4), Inches(1.25), Inches(7.4), Inches(5.65), cd).chart
chart_font(ch, 14)
ch.has_legend = False; pl = ch.plots[0]; pl.gap_width = 45; pl.vary_by_categories = False
pl.has_data_labels = True; pl.data_labels.font.size = Pt(14); pl.data_labels.font.bold = True
pl.data_labels.number_format = '$0.0"M"'; pl.data_labels.number_format_is_linked = False
pl.data_labels.position = XL_LABEL_POSITION.OUTSIDE_END
ch.category_axis.reverse_order = True; ch.value_axis.visible = False; ch.value_axis.has_major_gridlines = False
ch.value_axis.maximum_scale = 62
ch.category_axis.tick_labels.font.size = Pt(14); ch.category_axis.format.line.fill.background()
ch.has_title = True; ch.chart_title.text_frame.text = "Value of each field's producing wells today ($M)"
ch.chart_title.text_frame.paragraphs[0].font.size = Pt(15); ch.chart_title.text_frame.paragraphs[0].font.bold = True
ser = pl.series[0]; ser.format.fill.solid(); ser.format.fill.fore_color.rgb = MID
for i, col in ((0, RED), (1, NAVY), (2, NAVY)):
    pt = ser.points[i]; pt.format.fill.solid(); pt.format.fill.fore_color.rgb = col
box(s, 8.05, 1.35, 4.85, 1.55, fill=LIGHT)
text(s, [('What is a royalty (ORRI)?', {'size': 16, 'bold': True, 'color': NAVY, 'space': 4}),
         ('A fixed % of the money from all oil and gas sold. The owner pays no drilling, operating or clean-up costs, but has no control.',
          {'size': 15, 'space': 0})], 8.2, 1.42, 4.6, 1.45)
text(s, [('~95%', {'size': 44, 'bold': True, 'color': NAVY, 'space': 0}),
         ('of the value is in Kodiak, Lucius and Stones', {'size': 16, 'space': 0})], 8.05, 3.4, 4.85, 1.4, align=PP_ALIGN.CENTER)
box(s, 8.05, 4.95, 4.85, 1.2, fill=PALE, line=RED)
text(s, [('Kodiak = about half the value,', {'size': 17, 'bold': True, 'color': RED, 'space': 0}),
         ('from ONE well. Our biggest risk.', {'size': 17, 'bold': True, 'color': RED, 'space': 0})],
     8.15, 5.0, 4.65, 1.1, align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
text(s, 'The other six fields together: ~$6M', 8.05, 6.3, 4.85, 0.4, size=15, color=GREY, align=PP_ALIGN.CENTER)
note(s, 'Base case, 12% discount rate ("PV @12%" = all future royalty checks converted to today\'s dollars).', size=12)

# 3 ---------------------------------------------------------------- fine print
s = slide('The fine print makes the package smaller than it looks', 3,
          'We read every legal document. Five places where the seller\'s list looks bigger than reality:')
table(s, [['Royalty', 'Looks like', 'Our reading of the documents', 'Effect on value'],
          ['Lucius', '2% + 2% = 4%', '1.43% of the field', '~2.8x lower'],
          ['Pompano', '~$71M (same name as a big field)', '~$0: different area, nothing since 2014', '-$71M vs a naive buyer'],
          ['Ship Shoal', '8%', '4%: our assumption (creator owned only half); BP to confirm', 'about -$2M'],
          ['Stones', '1.5% on 8 blocks', 'only 1 block produces', 'risk of about -$2M'],
          ['Kodiak', 'listed twice', 'one royalty: count it once', 'avoids double counting']],
      0.5, 1.7, 12.33, 4.6, size=18, widths=[1.9, 3.5, 4.33, 2.6], bold_col0=True)
note(s, 'The seller\'s percentages are facts. Our readings (Ship Shoal 4%, Lucius paid on its 1.43% share of the whole field) are labelled assumptions. '
        'If Lucius still pays the old way, value falls ~$7M.', y=6.6, size=12)

# 4 ---------------------------------------------------------------- checking BP's numbers
s = slide("BP's past numbers are real; its 2018 forecast is too high", 4)
box(s, 0.45, 1.3, 4.35, 5.55, fill=LIGHT)
text(s, [('Check 1: 2017 revenue', {'size': 18, 'bold': True, 'color': NAVY, 'space': 8}),
         ('BP says', {'size': 15, 'space': 0}), ('$20.4M', {'size': 38, 'bold': True, 'color': GREY, 'space': 6}),
         ('We rebuilt it from government data', {'size': 15, 'space': 0}),
         ('$20.6M', {'size': 38, 'bold': True, 'color': GREEN, 'space': 6}),
         ('Within 1%: the past number is real.', {'size': 16, 'bold': True, 'color': GREEN, 'space': 2}),
         ('($22.0M before transport deductions, within 8%)', {'size': 12, 'italic': True, 'color': GREY, 'space': 14}),
         ('But 2017 is not the future:', {'size': 15, 'bold': True, 'space': 2}),
         ('Kodiak was offline ~8 months', {'size': 14, 'space': 1}),
         ("Lucius's share changed Jan 2018", {'size': 14, 'space': 1}),
         ('Stones shut in Mar-May 2018', {'size': 14, 'space': 0})], 0.6, 1.4, 4.05, 5.4, align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
text(s, 'Check 2: 2018 oil output, forecast vs actual', 5.1, 1.25, 7.9, 0.45, size=18, bold=True, color=NAVY)
cd = CategoryChartData(); cd.categories = ['Lucius', 'Stones', 'Kodiak', 'S. Santa Cruz']
cd.add_series("Seller's forecast (WoodMac)", (50.3, 60.3, 17.0, 13.7)); cd.add_series('Actual, government data (Jan-May)', (36.8, 10.3, 16.9, 3.5))
ch = s.shapes.add_chart(XL_CHART_TYPE.COLUMN_CLUSTERED, Inches(5.0), Inches(1.7), Inches(8.0), Inches(4.3), cd).chart
chart_font(ch, 14)
ch.has_legend = True; ch.legend.position = XL_LEGEND_POSITION.TOP; ch.legend.include_in_layout = False; ch.legend.font.size = Pt(14)
pl = ch.plots[0]; pl.gap_width = 60; pl.overlap = 0
pl.has_data_labels = True; pl.data_labels.font.size = Pt(14); pl.data_labels.font.bold = True
pl.data_labels.position = XL_LABEL_POSITION.OUTSIDE_END
pl.data_labels.number_format = '0.0'; pl.data_labels.number_format_is_linked = False
ch.value_axis.visible = False; ch.value_axis.has_major_gridlines = False; ch.value_axis.maximum_scale = 70
ch.category_axis.tick_labels.font.size = Pt(15)
for ser, col in zip(pl.series, (MID, NAVY)):
    ser.format.fill.solid(); ser.format.fill.fore_color.rgb = col
text(s, [('Thousand barrels of oil a day, whole field. Kodiak actual = Mar-May (restarted Feb 22).', {'size': 13, 'italic': True, 'color': GREY, 'space': 4}),
         ('The gap is mostly future drilling. We can\'t assume when drilling happens, so we value only wells producing today.',
          {'size': 16, 'bold': True, 'color': BLACK, 'space': 0})], 5.1, 6.0, 7.9, 0.95)

# 5 ---------------------------------------------------------------- value
s = slide('The producing wells are worth ~$102M; we bid $98M', 5)
cd = CategoryChartData()
cd.categories = ['Our cash bid', 'Base-case value (our view)', 'Fixed-price ceiling', 'Our optimistic case',
                 "Seller's forecast volumes (our estimate)"]
cd.add_series('$M', (98, 102, 105, 134, 220))
ch = s.shapes.add_chart(XL_CHART_TYPE.BAR_CLUSTERED, Inches(0.4), Inches(1.25), Inches(7.6), Inches(5.0), cd).chart
chart_font(ch, 14)
ch.has_legend = False; ch.has_title = False; pl = ch.plots[0]; pl.gap_width = 40; pl.vary_by_categories = False
ch.category_axis.reverse_order = True; ch.value_axis.visible = False; ch.value_axis.has_major_gridlines = False
ch.value_axis.minimum_scale = 0; ch.value_axis.maximum_scale = 265
ch.category_axis.tick_labels.font.size = Pt(14); ch.category_axis.format.line.fill.background()
ser = pl.series[0]
for i, (col, lab) in enumerate(((NAVY, '$98M'), (GREEN, '$102M'), (MID, '$105M'), (LGREEN, '$134M'), (PALE, '~$220M+'))):
    pt = ser.points[i]; pt.format.fill.solid(); pt.format.fill.fore_color.rgb = col
    if i == 4: pt.format.line.color.rgb = MID
    tf = pt.data_label.text_frame; tf.text = lab
    tf.paragraphs[0].font.size = Pt(16); tf.paragraphs[0].font.bold = True; tf.paragraphs[0].font.name = FONT
    pt.data_label.position = XL_LABEL_POSITION.OUTSIDE_END
text(s, [('How we value it', {'size': 18, 'bold': True, 'color': NAVY, 'space': 5}),
         ('Only wells producing today.', {'size': 16, 'space': 6}),
         ('12% discount rate (case range: 10-20%).', {'size': 16, 'space': 6}),
         ('Kodiak and Lucius drop 35% in year 1 (base),', {'size': 16, 'space': 0}),
         ('or 22% / 25% in our optimistic case.', {'size': 16, 'space': 6}),
         ('Cash to ~2035; most value in years 1-5.', {'size': 16, 'space': 0})], 8.3, 1.3, 4.7, 2.8)
table(s, [['Discount rate', 'Base case', 'Optimistic'], ['10%', '$106M', '$140M'], ['12% (ours)', '$102M', '$134M'],
          ['15%', '$98M', '$127M'], ['20%', '$91M', '$116M']], 8.3, 4.2, 4.6, 2.2, size=14, widths=[1.6, 1.4, 1.6], hl_rows=(2,))
note(s, 'Value at the Sept 14 closing (at Aug 15: ~$101M / ~$133M). Not in our price: ~$13M of possible new drilling; '
        'ceiling = $102M + a quarter of it. Oil = Aug 15, 2018 futures; output cut 2%/yr for hurricanes.', y=6.45, size=12)

# 6 ---------------------------------------------------------------- how the $24M works
s = slide('The extra $24M is paid only if public data proves it', 6)
card(s, 0.5, 1.35, 3.6, 1.35, '$98M', 'cash at closing', fill=NAVY, big_color=WHITE, small_color=WHITE, big_size=36, small_size=15)
text(s, '+', 4.1, 1.5, 0.6, 1.0, size=44, bold=True, color=NAVY, align=PP_ALIGN.CENTER)
card(s, 4.7, 1.35, 3.6, 1.35, 'up to $24M', 'only on proof', fill=GREEN, big_color=WHITE, small_color=WHITE, big_size=36, small_size=15)
text(s, '=', 8.3, 1.5, 0.6, 1.0, size=44, bold=True, color=NAVY, align=PP_ALIGN.CENTER)
card(s, 8.9, 1.35, 3.93, 1.35, 'up to $122M', 'headline BP sees', fill=PALE, big_size=36, small_size=15, line=NAVY)
text(s, 'Three triggers, checked in free government (BOEM) production reports (plus the US oil price, WTI, for Kodiak):', 0.5, 2.9, 12.3, 0.45,
     size=16, bold=True, color=NAVY)
trig = [('$15M', 'Kodiak keeps producing', '$5M a year for 2019-21, if output targets are met and oil is at least $55'),
        ('$5M', 'A 2nd Kodiak well', 'producing for 90 days by end-2021'),
        ('$4M', 'A new Stones well', 'paying royalties by end-2021')]
for i, (b, h, sm) in enumerate(trig):
    x = 0.5 + i * 4.18
    box(s, x, 3.45, 3.97, 2.35, fill=LIGHT)
    text(s, [(b, {'size': 40, 'bold': True, 'color': GREEN, 'space': 2}), (h, {'size': 18, 'bold': True, 'color': NAVY, 'space': 6}),
             (sm, {'size': 16, 'space': 0})], x + 0.15, 3.5, 3.67, 2.25, align=PP_ALIGN.CENTER)
text(s, [('If BP is right, BP collects most of it. If BP is wrong, we paid $98M and still earn ~15%.', {'size': 16, 'bold': True, 'space': 4}),
         ('If we miss a payment, part of the Kodiak royalty goes back to BP. Pay-later deals ("earn-outs") are common in oil.', {'size': 15, 'color': GREY, 'space': 0})],
     0.5, 5.95, 12.3, 0.95)

# 7 ---------------------------------------------------------------- returns
s = slide("Pay-on-proof earns ~15% even if BP's forecast is wrong", 7)
cd = CategoryChartData()
cd.categories = ['Base case', 'Optimistic case', 'Base case, $45 oil', 'Optimistic, $45 oil', 'Kodiak fails 2020']
cd.add_series('$98M + pay-on-proof (our bid)', (0.15, 0.26, 0.03, 0.18, -0.02))
cd.add_series('$105M fixed price (ceiling)', (0.11, 0.27, 0.00, 0.14, -0.05))
gf = s.shapes.add_chart(XL_CHART_TYPE.COLUMN_CLUSTERED, Inches(0.4), Inches(1.2), Inches(8.3), Inches(5.3), cd)
ch = gf.chart; chart_font(ch, 13)
ch.has_title = True; ch.chart_title.text_frame.text = 'Yearly return (IRR) by scenario'
ch.chart_title.text_frame.paragraphs[0].font.size = Pt(15); ch.chart_title.text_frame.paragraphs[0].font.bold = True
ch.has_legend = True; ch.legend.position = XL_LEGEND_POSITION.BOTTOM; ch.legend.include_in_layout = False; ch.legend.font.size = Pt(14)
pl = ch.plots[0]; pl.gap_width = 70; pl.overlap = 0
pl.has_data_labels = True; pl.data_labels.font.size = Pt(14); pl.data_labels.font.bold = True
pl.data_labels.number_format = '0%'; pl.data_labels.number_format_is_linked = False
pl.data_labels.position = XL_LABEL_POSITION.OUTSIDE_END
ch.value_axis.visible = False; ch.value_axis.has_major_gridlines = False
ch.value_axis.minimum_scale = -0.08; ch.value_axis.maximum_scale = 0.32
ch.category_axis.tick_labels.font.size = Pt(13); ch.category_axis.tick_label_position = XL_TICK_LABEL_POSITION.LOW
for ser, col in zip(pl.series, (NAVY, MID)):
    ser.invert_if_negative = False; ser.format.fill.solid(); ser.format.fill.fore_color.rgb = col
card(s, 8.95, 1.3, 3.9, 1.55, '~15%', "base case at $98M: above our 12% cost of money, even if BP's forecast is wrong", big_size=36, small_size=14)
card(s, 8.95, 3.0, 3.9, 1.55, '~26%', 'in our optimistic case (slower declines), even after paying BP ~$15M of the $24M', big_size=36, small_size=14)
card(s, 8.95, 4.7, 3.9, 1.55, '~11%', 'a fixed $105M in the base case. $105M is a ceiling, not a target.', fill=PALE, big_color=GREY, big_size=36, small_size=14)
note(s, 'IRR = yearly return on cash paid at closing, before any loan and before $3.1M costs/reserve. '
        'Base case at $98M: profit ~$31M, 1.3x money back, paid back by 2022.', y=6.6, size=12)

# 8 ---------------------------------------------------------------- funding
s = slide('Funding: ~$84M at closing, from an assumed royalty fund', 8)
eq = [('$98.0M', 'price', NAVY, WHITE), ('- $17.5M', 'Jan-Jun 2018 royalties BP credits us', LIGHT, NAVY),
      ('+ $3.1M', 'costs + hurricane reserve', LIGHT, NAVY), ('= $83.6M', 'cash needed at closing (Sept 14)', YELLOW, NAVY)]
for i, (b, sm, f, c) in enumerate(eq):
    card(s, 0.5 + i * 3.11, 1.3, 2.95, 1.45, b, sm, fill=f, big_color=c, small_color=(WHITE if f == NAVY else BLACK), big_size=30, small_size=14)
text(s, 'Who pays it:', 0.5, 2.95, 2.4, 0.5, size=18, bold=True, color=NAVY, anchor=MSO_ANCHOR.MIDDLE)
card(s, 2.6, 2.9, 6.6, 0.95, '95% = $79.4M', 'ASSUMED: an existing royalty fund with committed capital; must sign by Aug 8', fill=GREEN, big_color=WHITE,
     small_color=WHITE, big_size=22, small_size=13)
card(s, 9.35, 2.9, 3.48, 0.95, '5% = $4.2M', 'our team', fill=LGREEN, big_size=22, small_size=13)
# timeline
text(s, 'Timeline, 2018 (5 weeks to the bid):', 0.5, 4.05, 6.0, 0.4, size=16, bold=True, color=NAVY)
line = s.shapes.add_connector(1, Inches(1.1), Inches(4.85), Inches(12.3), Inches(4.85)); line.line.color.rgb = NAVY; line.line.width = Pt(3)
steps = [('Jul 20', 'our research pack to the fund'), ('Jul 27', 'term sheet'), ('Aug 8', 'GATE: signed money commitment'),
         ('Aug 15', 'submit bid'), ('Aug 30', 'award + 10% deposit'), ('Sep 14', 'close')]
for i, (d, w) in enumerate(steps):
    cx = 1.2 + i * 2.2
    gate = d == 'Aug 8'
    dot = s.shapes.add_shape(MSO_SHAPE.OVAL, Inches(cx - 0.14), Inches(4.71), Inches(0.28), Inches(0.28))
    dot.fill.solid(); dot.fill.fore_color.rgb = RED if gate else NAVY; dot.line.fill.background(); dot.shadow.inherit = False
    text(s, [(d, {'size': 17, 'bold': True, 'color': RED if gate else NAVY, 'space': 0}),
             (w, {'size': 13, 'bold': gate, 'color': RED if gate else BLACK, 'space': 0})], cx - 1.05, 5.05, 2.1, 0.95, align=PP_ALIGN.CENTER)
box(s, 0.5, 6.1, 12.33, 0.75, fill=PALE, line=RED)
text(s, [('No signed commitment by Aug 8 = we walk away. No unfunded bids.', {'size': 17, 'bold': True, 'color': RED, 'space': 0}),
         ('A bank is not needed to close. Optional loan after closing: $25-30M at 7.25% (5.00% prime rate + 2.25%).', {'size': 13, 'color': BLACK, 'space': 0})],
     0.6, 6.1, 12.1, 0.75, align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)

# 9 ---------------------------------------------------------------- what could change our mind
s = slide('What could change our mind: Kodiak and the oil price', 9,
          'How much our ~$102M base-case value moves if one thing changes ($M)')
cats = ['Kodiak well fails in 2020', 'Oil falls to $45 from 2019', 'Lucius paid the old way', 'Discount rate 15%',
        'Stones restart slips to 2019', 'Kodiak declines 25% (not 35%)', 'Oil $75, rising 2%/yr', 'Our optimistic case']
vals = (-21.4, -17.8, -6.8, -4.6, -2.4, 13.3, 19.3, 31.9)
cd = CategoryChartData(); cd.categories = cats
cd.add_series('Lower value', tuple(v if v < 0 else None for v in vals)); cd.add_series('Higher value', tuple(v if v > 0 else None for v in vals))
ch = s.shapes.add_chart(XL_CHART_TYPE.BAR_CLUSTERED, Inches(0.3), Inches(1.6), Inches(8.3), Inches(5.3), cd).chart
chart_font(ch, 14)
ch.has_legend = False; pl = ch.plots[0]; pl.overlap = 100; pl.gap_width = 45
ch.category_axis.reverse_order = True; ch.category_axis.tick_labels.font.size = Pt(14); ch.value_axis.visible = False
ch.value_axis.has_major_gridlines = False; ch.value_axis.minimum_scale = -32; ch.value_axis.maximum_scale = 42
ch.category_axis.tick_label_position = XL_TICK_LABEL_POSITION.LOW
for ser, col in zip(pl.series, (RED, GREEN)):
    ser.invert_if_negative = False; ser.format.fill.solid(); ser.format.fill.fore_color.rgb = col
for i, v in enumerate(vals):
    ser = pl.series[0 if v < 0 else 1]; dl = ser.points[i].data_label
    tf = dl.text_frame; tf.text = f'{v:+.1f}'; tf.paragraphs[0].font.size = Pt(14); tf.paragraphs[0].font.bold = True
    dl.position = XL_LABEL_POSITION.OUTSIDE_END
risks = [('Kodiak fails: -$21M', 'Answer: the Kodiak upside is paid only on proof.'),
         ('Oil at $45: -$18M', 'Answer: lock in (hedge) 2019-20 oil at ~$60-64.'),
         ('Hurricanes', "A 3-6 month platform outage can't be insured by royalty owners, so we cut output 2% a year.")]
for i, (h, b) in enumerate(risks):
    y = 1.65 + i * 1.32
    box(s, 8.85, y, 4.1, 1.18, fill=LIGHT)
    text(s, [(h, {'size': 17, 'bold': True, 'color': RED if i < 2 else NAVY, 'space': 2}), (b, {'size': 14, 'space': 0})],
         9.0, y + 0.06, 3.85, 1.1, anchor=MSO_ANCHOR.MIDDLE)
card(s, 8.85, 5.65, 4.1, 1.25, '6,000 simulations', 'middle ~$98M; 1 in 10 below ~$79M. Oil price held fixed.', fill=PALE, big_size=18, small_size=14)

# 10 ---------------------------------------------------------------- other bidders + questions for BP
s = slide('What other bidders will miss, and what we ask BP', 10)
table(s, [['Bidder type', 'What they will likely do'],
          ['Believes the brochure', 'Pompano $71M, Lucius 4%: overpays or can\'t fund'],
          ['Multiplies 2017 revenue', '5-7 x $20.4M = $100-140M: misses 2018'],
          ['Disciplined royalty funds', 'Need 12-15% a year: our real competition'],
          ['Us', 'Checked title + public data + pay-on-proof']],
      0.45, 1.3, 6.6, 4.1, size=16, widths=[2.4, 4.2], hl_rows=(4,), bold_col0=True)
box(s, 0.45, 5.65, 6.6, 1.15, fill=LIGHT)
text(s, [('Value others may miss', {'size': 16, 'bold': True, 'color': NAVY, 'space': 3}),
         ('~$2-3M of Lucius catch-up payments (Jan-May 2018) + audit rights', {'size': 15, 'space': 0})], 0.6, 5.7, 6.3, 1.05,
     anchor=MSO_ANCHOR.MIDDLE)
text(s, [('Before we commit, we ask BP:', {'size': 20, 'bold': True, 'color': NAVY, 'space': 14}),
         ('1.  Payment records 2016-18 from all 22 companies that pay the royalties', {'size': 17}),
         ('2.  Is Lucius paid on our 1.43% share of the whole field, or is money held back?', {'size': 17}),
         ('3.  Why did Stones shut in from March to May 2018?', {'size': 17}),
         ("4.  Kodiak: current output, and proof its lease survived the 2017-18 shutdown", {'size': 17}),
         ("5.  Ship Shoal: is it 8% or 4%?", {'size': 17}),
         ('6.  Four missing documents, and why a related royalty (WR 199) is left out of the sale', {'size': 17})], 7.35, 1.3, 5.6, 5.0)

# A1 ---------------------------------------------------------------- AI use
s = slide('AI appendix (1/2): how we used AI, and how we checked it', 'A1')
table(s, [['Task', 'What AI did', 'How we checked it'],
          ['Read 60+ legal PDFs', 'Pulled out royalty %, depth limits, parties', 'Re-read the key pages ourselves (Lucius, Kodiak, Ship Shoal)'],
          ['Production data', 'Pulled government (BOEM) monthly data', 'Used data to May 2018 only (May is borderline; conclusions hold without it)'],
          ['Valuation model', 'Drafted the Python engine, then the Excel', 'Rebuilt 2017 revenue vs BP; Excel and Python agree'],
          ['Red team', 'Role-played engineer, title lawyer, banker, auction strategist, judges', 'We weighed each challenge; rejected its $132M bid'],
          ['Writing', 'Drafted slides and Q&A', 'Every number traced to a model cell or source page']],
      0.45, 1.3, 12.4, 3.9, size=15, widths=[2.3, 4.6, 5.5], bold_col0=True)
box(s, 0.45, 5.35, 12.4, 1.2, fill=LIGHT)
text(s, [('Example prompts', {'size': 15, 'bold': True, 'color': NAVY, 'space': 3}),
         ('"Extract the ORRI decimal, depth limit and burdened lease from this assignment, with page"', {'size': 13, 'italic': True, 'space': 1}),
         ('"Compare WoodMac 2018 volumes with BOEM Jan-May 2018 by lease"   |   "Attack our bid as a title attorney"', {'size': 13, 'italic': True, 'space': 3}),
         ('The "expert panel" was AI role-play. All decisions were made by the team.', {'size': 13, 'bold': True, 'space': 0})],
     0.6, 5.38, 12.1, 1.15)
box(s, 0.45, 6.62, 12.4, 0.4, fill=YELLOW, line=RED, dash=True)
text(s, '[FILL IN]  AI tools we used: ______________________   (plus Python and Excel)', 0.6, 6.62, 12.1, 0.4, size=14, bold=True, color=RED, anchor=MSO_ANCHOR.MIDDLE)

# A2 ---------------------------------------------------------------- AI corrections
s = slide('AI appendix (2/2): where AI was wrong, and how we caught it', 'A2')
table(s, [['AI said', 'How we caught it', 'What we did / impact'],
          ['Lucius royalty is 4% (2% + 2%)', 'Read the unit agreement (Exhibit C)', '1.43%: value ~2.8x lower'],
          ["Pompano = WoodMac's Pompano field (~$71M)", 'Read the MC 72 deed; checked BOEM by lease', 'Different field: ~$0 (-$71M)'],
          ["Value it off the seller's forecast (~$220M+)", 'BOEM Jan-May 2018 actuals', 'Value producing wells: $98M + up to $24M on proof'],
          ['Closing credit $29M, loan $45M', 'Royalties arrive ~60 days late', '$17.5M credit; $25-30M loan (+$11.5M cash at close)'],
          ['Kodiak declines 22% a year', 'Plotted 2016-18 monthly data', '35% in our base case; 22% shown only as upside'],
          ['Bid $132M to win (AI strategist)', 'Failed our funding and return tests', 'Rejected: pay-on-proof instead']],
      0.45, 1.3, 12.4, 5.4, size=15, widths=[4.4, 3.9, 4.1], hl_rows=(1,))

# R ---------------------------------------------------------------- references
s = slide('References', 'R')
text(s, [('Case materials (data room)', {'size': 17, 'bold': True, 'color': NAVY, 'space': 6}),
         ('UNT Hackathon 2026 case, "Bid or Walk Away?"', {'size': 14, 'space': 4}),
         ('Bid Instructions (Jul 15, 2018) and Attachment A: the 19 interests and their decimals', {'size': 14, 'space': 4}),
         ('Location map; purchase price allocation file', {'size': 14, 'space': 4}),
         ('Recorded title documents: assignments, unit agreements (e.g. Lucius unit Exhibit C, Kodiak ABOS, Ship Shoal 219 assignment)', {'size': 14, 'space': 4}),
         ('Wood Mackenzie (WoodMac) field reports and 2018 forecasts provided by the seller', {'size': 14, 'space': 14}),
         ('Our analysis files', {'size': 17, 'bold': True, 'color': NAVY, 'space': 6}),
         ('ORRI_Bid_Model.xlsx: Dashboard, Valuation, Returns, Funding, Allocation, Facts_vs_Assumptions, AI_Log tabs', {'size': 14, 'space': 4}),
         ('Python valuation engine and 6,000-run simulation (values pasted into Excel)', {'size': 14, 'space': 4}),
         ('Every input is labelled fact or assumption; change any blue input cell and all values recalculate', {'size': 14, 'space': 0})],
     0.5, 1.3, 6.1, 5.5)
text(s, [('Public sources (only information available by Aug 15, 2018)', {'size': 17, 'bold': True, 'color': NAVY, 'space': 6}),
         ('BOEM OGOR-A monthly production by lease, Jan 2015 to May 2018 (data.boem.gov)', {'size': 14, 'space': 4}),
         ('NYMEX (CME) WTI oil and Henry Hub gas futures, settlements of Aug 15, 2018', {'size': 14, 'space': 4}),
         ('EIA: WTI spot prices to Aug 15, 2018; Gulf of Mexico hurricane shut-in history', {'size': 14, 'space': 4}),
         ('WSJ US prime rate: 5.00%, effective Jun 14, 2018, unchanged on Aug 15, 2018', {'size': 14, 'space': 4}),
         ('30 CFR 250.1701: who must pay for decommissioning (lessees and operators, not royalty owners)', {'size': 14, 'space': 14}),
         ('Not available to us', {'size': 17, 'bold': True, 'color': NAVY, 'space': 6}),
         ("The case's production workbook was not in our folder; BOEM public data was used instead.", {'size': 14, 'space': 0})],
     6.9, 1.3, 6.1, 5.5)

prs.save(OUT); print('wrote', OUT)
