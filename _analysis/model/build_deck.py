"""Build the 10-slide deck + 2 AI-appendix slides. Run: python -I model/build_deck.py <deliverables dir>"""
import sys, os
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.chart.data import CategoryChartData
from pptx.enum.chart import XL_CHART_TYPE, XL_LEGEND_POSITION
from pptx.enum.text import PP_ALIGN

OUT = os.path.join(sys.argv[1], 'ORRI_Bid_or_Walk_Away.pptx')
NAVY = RGBColor(0x1F, 0x38, 0x64); GREY = RGBColor(0x59, 0x59, 0x59); RED = RGBColor(0xC0, 0x00, 0x00)
GREEN = RGBColor(0x37, 0x86, 0x3C); LIGHT = RGBColor(0xD9, 0xE1, 0xF2); WHITE = RGBColor(0xFF, 0xFF, 0xFF)
prs = Presentation(); prs.slide_width = Inches(13.333); prs.slide_height = Inches(7.5)
BL = prs.slide_layouts[6]

def slide(title, sub=None, num=None):
    s = prs.slides.add_slide(BL)
    bar = s.shapes.add_shape(1, 0, 0, prs.slide_width, Inches(1.05)); bar.fill.solid(); bar.fill.fore_color.rgb = NAVY; bar.line.fill.background()
    tb = s.shapes.add_textbox(Inches(0.4), Inches(0.12), Inches(12.5), Inches(0.85)); tf = tb.text_frame; tf.word_wrap = True
    p = tf.paragraphs[0]; p.text = title; p.font.size = Pt(26); p.font.bold = True; p.font.color.rgb = WHITE; p.font.name = 'Arial'
    if sub:
        t2 = s.shapes.add_textbox(Inches(0.4), Inches(1.12), Inches(12.5), Inches(0.5)); q = t2.text_frame.paragraphs[0]
        q.text = sub; q.font.size = Pt(15); q.font.italic = True; q.font.color.rgb = GREY; q.font.name = 'Arial'
    if num:
        t3 = s.shapes.add_textbox(Inches(12.4), Inches(7.05), Inches(0.8), Inches(0.35)); r = t3.text_frame.paragraphs[0]
        r.text = str(num); r.font.size = Pt(10); r.font.color.rgb = GREY; r.alignment = PP_ALIGN.RIGHT
    return s

def bullets(s, items, x=0.5, y=1.7, w=12.3, h=5.3, size=17):
    tb = s.shapes.add_textbox(Inches(x), Inches(y), Inches(w), Inches(h)); tf = tb.text_frame; tf.word_wrap = True
    first = True
    for it in items:
        lvl = 0; bold = False; color = None
        if isinstance(it, tuple): it, lvl = it[0], it[1]
        if it.startswith('**'): it = it.strip('*'); bold = True
        if it.startswith('!!'): it = it[2:]; color = RED
        p = tf.paragraphs[0] if first else tf.add_paragraph(); first = False
        p.text = ('• ' if lvl == 0 else '– ') + it; p.level = lvl
        p.font.size = Pt(size - 2 * lvl); p.font.bold = bold; p.font.name = 'Arial'; p.space_after = Pt(6)
        if color: p.font.color.rgb = color
    return tb

def table(s, data, x, y, w, h, size=13, widths=None, hl_rows=()):
    rows, cols = len(data), len(data[0])
    t = s.shapes.add_table(rows, cols, Inches(x), Inches(y), Inches(w), Inches(h)).table
    for i, row in enumerate(data):
        for j, v in enumerate(row):
            c = t.cell(i, j); c.text = str(v)
            for p in c.text_frame.paragraphs:
                p.font.size = Pt(size); p.font.name = 'Arial'
                if i == 0: p.font.bold = True; p.font.color.rgb = WHITE
                if i in hl_rows: p.font.bold = True
            if i == 0: c.fill.solid(); c.fill.fore_color.rgb = NAVY
            elif i in hl_rows: c.fill.solid(); c.fill.fore_color.rgb = RGBColor(0xFF, 0xF2, 0xCC)
    if widths:
        for j, wd in enumerate(widths): t.columns[j].width = Inches(wd)
    return t

def note(s, text, y=6.85):
    tb = s.shapes.add_textbox(Inches(0.5), Inches(y), Inches(11.8), Inches(0.5)); tf = tb.text_frame; tf.word_wrap = True
    p = tf.paragraphs[0]; p.text = text; p.font.size = Pt(10); p.font.italic = True; p.font.color.rgb = GREY; p.font.name = 'Arial'

# 1 -------------------------------------------------------------- decision
s = slide('BID: $98M cash + up to $24M paid only if public data proves the upside',
          'Decision as of Aug 15, 2018 for the 19-interest Gulf of Mexico ORRI package (seller BP)  |  [Team name & members]', 1)
table(s, [['', 'Our answer'],
          ['Cash at closing price', '$98M for the whole package (allocated across all 19 interests)'],
          ['Performance payments', 'Up to $24M more, triggered only by BOEM public production reports (Kodiak volumes, new wells)'],
          ['If BP requires a fixed price', '$105M all-cash = our ceiling (base value $102M + a quarter of the $13M risked drilling). Above that we walk away.'],
          ['Value of producing wells', '~$102M (base case, PV @12%); ~$134M if output follows the operator trend'],
          ['Return to us', '~15% base case; ~26% if output follows the operator trend (BP then collects ~$15M of the $24M)'],
          ['Funding', '~$84M cash at closing after BP credits Jan-Jun 2018 royalties; equity from an existing royalty fund'],
          ['Go / no-go gate', 'Signed equity commitment by Aug 8. No signature = we walk away (no unfunded bid).']],
      0.5, 1.75, 12.3, 4.6, size=15, widths=[3.4, 8.9])
note(s, 'Why it wins: BP sees up to $122M; we pay $98M unless BP\'s own production story comes true. "We can\'t assume when drilling happens, so we pay for it when BOEM shows it happened."')

# 2 -------------------------------------------------------------- what we are buying
s = slide('19 royalties on 9 platforms - but 3 fields carry ~95% of the value', 'An overriding royalty = a % of gross sales, with no operating costs and no plugging liability', 2)
cd = CategoryChartData(); cd.categories = ['Kodiak', 'Lucius', 'Stones', 'S. Santa Cruz', 'Ship Shoal', 'Main Pass', 'Grand Isle', 'Orion', 'Pompano']
cd.add_series('PV @12%, base case ($M)', (52.8, 26.4, 16.9, 2.0, 2.0, 1.0, 0.9, 0.3, 0.0))
ch = s.shapes.add_chart(XL_CHART_TYPE.BAR_CLUSTERED, Inches(0.5), Inches(1.7), Inches(6.6), Inches(5.0), cd).chart
ch.has_legend = False; ch.plots[0].has_data_labels = True; ch.plots[0].data_labels.font.size = Pt(11); ch.plots[0].data_labels.number_format = '$0.0"M"'
ch.plots[0].data_labels.number_format_is_linked = False; ch.category_axis.reverse_order = True; ch.value_axis.visible = False
ch.category_axis.tick_labels.font.size = Pt(12); ch.has_title = True; ch.chart_title.text_frame.text = 'Value of producing wells by field, $M (PV @12%)'
ch.chart_title.text_frame.paragraphs[0].font.size = Pt(13)
bullets(s, ['**Kodiak (~half the value): one deepwater well, 6.375% royalty',
            'Lucius: 1.43% of the whole unit (not 4%)',
            'Stones: 1.5%, only 1 of 8 blocks produces',
            'Six small interests: ~$6M combined',
            'Royalty owners carry no decommissioning liability (30 CFR 250.1701) and pay no OCS severance tax',
            '!!Concentration risk: one Kodiak well drives our decision'], x=7.3, y=1.8, w=5.6, size=16)

# 3 -------------------------------------------------------------- fine print
s = slide('The fine print shrinks the package', 'We read every assignment and unit agreement. Five traps that inflate rival bids:', 3)
table(s, [['Interest', 'Looks like', 'Actually is', 'Why (source document)', 'Value effect'],
          ['Lucius KC 874/875', '2% + 2% = 4%', '1.43% of unit output', 'Each 2% burdens only its tract: 24.77% + 46.67% (unit Exhibit C)', '~2.8x lower'],
          ['Pompano MC 72', '5.625% of WoodMac "Pompano" (~$71M)', '~$0', 'Covers only LLOG/Nexen-assignee wells to 13,405 ft; none since Oct-2014. WoodMac field is on other blocks', '-$71M vs naive'],
          ['Ship Shoal 219', '8%', '4% (fact: 8% listed)', 'Amoco reserved 8% from its own 50% interest - we value 4%, ask BP', '-$2M'],
          ['Stones (8 blocks)', '1.5% x 8 leases', '1.5% of WR 508 only', 'Other 7 leases not producing; royalty-relief lease may delay payment', 'risk -$2M'],
          ['Kodiak', '6.375% x 2 lines', '6.375% once', 'Already net (10% x 63.75%); 17,500 ft+ only; 260-day outage 2017-18', 'avoid double count']],
      0.4, 1.7, 12.5, 4.4, size=13, widths=[1.9, 2.2, 1.9, 4.8, 1.7])
note(s, 'Facts = Attachment A decimals and recorded documents. Our readings (Ship Shoal 4%, Lucius paid on unit basis) are labelled assumptions; if Lucius pays on the old lease basis, value falls ~$7M.')

# 4 -------------------------------------------------------------- 2017 rebuild
s = slide("We rebuilt the seller's 2017 revenue from public government data", 'Independent cross-check: BOEM monthly production x royalty shares x 2017 prices', 4)
table(s, [['Field', '2017 royalty revenue ($M)'], ['Kodiak', '6.6'], ['Lucius (pre-unit, lease basis)', '7.5'], ['Stones', '5.7'], ['Ship Shoal (8%)', '1.2'],
          ['Others', '1.1'], ['Our rebuild, before deductions', '22.0'], ['Our rebuild, after $3/bbl & $0.40/mcf deductions', '20.6'], ["Seller's listing", '20.4']],
      0.5, 1.75, 6.3, 4.4, size=14, widths=[4.3, 2.0], hl_rows=(7, 8))
bullets(s, ['**Within 1% after deductions (8% before): the seller\'s number is real',
            'Deductions are our assumption - we show both',
            '**But 2017 is NOT the run-rate:',
            ('Kodiak was offline Jun-2017 to Feb-2018 (~$8M lost)', 1),
            ('Lucius unitised 1/1/2018: royalty share of the field roughly doubles', 1),
            ('Stones shut in Mar-May 2018 - cause unknown', 1),
            'That is why we forecast from 2018 monthly data, not from 2017'], x=7.1, y=1.8, w=5.9, size=16)

# 5 -------------------------------------------------------------- forecast running hot
s = slide("The seller's 2018 forecast is running hot", 'WoodMac 2018 forecast vs BOEM actual production, Jan-May 2018 (gross field oil, thousand bbl/day)', 5)
cd = CategoryChartData(); cd.categories = ['Lucius', 'Stones', 'Kodiak', 'S. Santa Cruz']
cd.add_series('WoodMac 2018 forecast', (50.3, 60.3, 17.0, 13.7)); cd.add_series('BOEM actual 2018 (Jan-May)', (36.8, 10.3, 16.9, 3.5))
ch = s.shapes.add_chart(XL_CHART_TYPE.COLUMN_CLUSTERED, Inches(0.5), Inches(1.7), Inches(7.2), Inches(5.0), cd).chart
ch.has_legend = True; ch.legend.position = XL_LEGEND_POSITION.BOTTOM; ch.legend.include_in_layout = False; ch.legend.font.size = Pt(12)
ch.plots[0].has_data_labels = True; ch.plots[0].data_labels.font.size = Pt(11); ch.value_axis.visible = False; ch.category_axis.tick_labels.font.size = Pt(13)
bullets(s, ['Lucius: down ~1/3 since Dec-17 (incl. part shutdowns); we model 35%/yr',
            'Stones: zero output Mar-May 2018 (all wells shut in)',
            'S. Santa Cruz: one well; forecast needs wells not drilled',
            'Kodiak: on track, but its earlier zones fell 40-60%/yr and it ran only ~2/3 of the time',
            '**The gap is mostly future drilling - the case says we cannot assume when drilling happens',
            'So: value producing wells; pay for drilling only when it shows up'], x=7.9, y=1.8, w=5.1, size=15)
note(s, 'Only BOEM months public by Aug 15, 2018 are used (Jan-2015 to May-2018). Kodiak Mar-May shown for the Kodiak bar (restart Feb-22).')

# 6 -------------------------------------------------------------- value
s = slide('Value: ~$102M today; ~$134M if the operator trend holds', 'PV at Sept 14 close (~$101M / ~$133M at Aug 15); NYMEX strip of Aug 15, 2018; 2%/yr hurricane haircut', 6)
table(s, [['Present value ($M)', 'Base case (from public monthly data)', 'Operator-trend case'],
          ['@ 10%', '106', '140'], ['@ 12%  (our rate)', '102', '134'], ['@ 15%', '98', '127'], ['@ 20%', '91', '116'],
          ['Risked drilling upside @12% (not in price)', '+13', '+13'], ['Our estimate from WoodMac volumes (risked)', '~$220M+', '']],
      0.5, 1.75, 7.6, 4.0, size=15, widths=[3.6, 2.2, 1.8], hl_rows=(2,))
bullets(s, ['**Base case: Kodiak 35% first-year decline, 90% uptime; Lucius 35%; Stones restarts Sep-2018',
            'Operator trend: Kodiak 22%, Lucius 25%, no downtime',
            'Why 12%: offshore producing royalty with single-well risk, inside the case\'s 10-20% range',
            'Life: cash to ~2035, but most value is earned in years 1-5 (inside the 10-15 yr horizon)',
            'Our price ($98M) sits below the base-case value at 12%'], x=8.4, y=1.8, w=4.6, size=15)
note(s, 'Model: ORRI_Bid_Model.xlsx (Engine + Valuation tabs). Every input is labelled fact or assumption; change any blue cell and all values recalculate.')

# 7 -------------------------------------------------------------- sensitivities
s = slide('What would change our mind: Kodiak, oil price, Lucius payment basis', 'Change in base-case value (PV @12%, $M) vs $102M', 7)
cd = CategoryChartData()
cats = ['Kodiak fails in 2020', 'Oil $45 from 2019', 'Lucius paid on lease basis', 'Discount rate 15%', 'Stones restart slips to 2019',
        'Kodiak declines 25% (not 35%)', 'Oil $75 +2%/yr', 'Operator-trend case']
vals = (-21.4, -17.8, -6.8, -4.6, -2.4, 13.3, 19.3, 31.9)
cd.categories = cats
cd.add_series('Lower value', tuple(v if v < 0 else 0 for v in vals)); cd.add_series('Higher value', tuple(v if v > 0 else 0 for v in vals))
ch = s.shapes.add_chart(XL_CHART_TYPE.BAR_STACKED, Inches(0.5), Inches(1.6), Inches(8.0), Inches(5.2), cd).chart
from pptx.enum.chart import XL_TICK_LABEL_POSITION
ch.has_title = False; ch.has_legend = False; ch.plots[0].overlap = 100; ch.plots[0].gap_width = 60
ch.category_axis.reverse_order = True; ch.category_axis.tick_labels.font.size = Pt(12); ch.value_axis.visible = False
ch.category_axis.tick_label_position = XL_TICK_LABEL_POSITION.LOW
for ser, col in zip(ch.plots[0].series, (RED, GREEN)):
    ser.invert_if_negative = False; ser.format.fill.solid(); ser.format.fill.fore_color.rgb = col
for i, v in enumerate(vals):
    ser = ch.plots[0].series[0 if v < 0 else 1]
    tf = ser.points[i].data_label.text_frame; tf.text = f'{v:+.1f}'; tf.paragraphs[0].font.size = Pt(11)
bullets(s, ['**Biggest risk: the single Kodiak well',
            ('Fails in 2020 -> lose ~$21M of value', 1),
            ('Our answer: Kodiak upside is paid only if BOEM shows it', 1),
            '**Oil price: hedge 2019-20 oil at the Aug-15 strip (~$60-64)',
            '**Weather: a 3-6 month host outage costs the royalty; owners cannot insure it -> 2%/yr haircut',
            '6,000 simulated outcomes (incl. Kodiak failure): middle ~$98M; 1-in-10 below ~$79M (value @12%)'], x=8.7, y=1.7, w=4.4, size=14)

# 8 -------------------------------------------------------------- returns
s = slide('Returns: ~15% base case, ~26% if output follows the operator trend', 'Unlevered IRR before $3.1M costs/reserve and before any loan, on cash paid at closing (BP credits Jan-Jun 2018 royalties at closing)', 8)
table(s, [['Scenario', '$98M + performance payments', '$105M fixed (ceiling)', 'Payments made'],
          ['Base case, strip prices', '15%', '11%', '$0'],
          ['Operator-trend, strip', '26%', '27%', '$15M'],
          ['Base case, $45 oil', '3%', '0%', '$0'],
          ['Operator-trend, $45 oil', '18%', '14%', '$0 (price test)'],
          ['Kodiak fails in 2020', '-2%', '-5%', '$0']],
      0.5, 1.75, 8.3, 3.4, size=15, widths=[3.0, 2.3, 1.8, 1.2], hl_rows=(1,))
table(s, [['Performance payment (cash)', 'Trigger (BOEM public data)', 'Amount'],
          ['Kodiak 2019 / 2020 / 2021', 'Royalty-burdened Kodiak oil (17,500 ft+) >= 11.0 / 8.5 / 6.5 kb/d per BOEM, and WTI >= $55; paid 30 days after Dec data posts', '$5M each'],
          ['Kodiak 2nd well', 'New completion below 17,500 ft producing 90 days by end-2021', '$5M'],
          ['Stones Phase 2', 'New royalty-paying well on any of the 8 WR blocks by end-2021', '$4M']],
      0.5, 5.3, 8.3, 1.5, size=12, widths=[2.4, 4.6, 1.3])
bullets(s, ['**$98M + payments: base-case NPV @12% ~ +$4M (IRR ~15%) even if BP is wrong', '$105M fixed is a ceiling, not a target: base-case NPV ~ -$3M; justified only by blended view', 'At $98M (base): profit ~$31M, 1.3x, payback 2022; ~$70M if the operator trend holds, after paying BP $15M',
            'Blended view (60% base / 40% operator trend): ~16-17% at $105M',
            'Payments secured by reversion of part of the Kodiak royalty if we miss one',
            'Earn-outs / contingent payments are common in upstream deals'], x=9.0, y=1.8, w=4.1, size=14)

# 9 -------------------------------------------------------------- funding
s = slide('Funding in 5 weeks: the bottleneck was diligence speed, not money', 'The bank is not on the critical path; prime rate 5.00% (Aug 15, 2018)', 9)
table(s, [['Sources & uses at closing (Sept 14)', '$M'], ['Price', '98.0'], ['Less: Jan-Jun 2018 royalties credited by BP', '(17.5)'],
          ['Transaction costs + hurricane reserve', '3.1'], ['Cash needed at closing', '83.6'], ['Anchor royalty fund equity (95%)', '79.4'],
          ['Team co-invest / promote (5%)', '4.2'], ['10% deposit at award (Aug 30)', '9.8']],
      0.5, 1.75, 6.2, 3.9, size=14, widths=[4.8, 1.4], hl_rows=(4,))
table(s, [['Date (2018)', 'Step'], ['Jul 16', 'NDA consent to share data room with funders'], ['Jul 20', 'Our title + BOEM diligence pack and model to fund'],
          ['Jul 27', 'Term sheet; fund engineer starts reserve letter'], ['Aug 3 / Aug 8', 'Investment committee 1 / 2 -> signed commitment = GATE'],
          ['Aug 15', 'Submit bid + 19-line allocation + title terms'], ['Aug 30 / Sep 14', 'Award + deposit / close'],
          ['Q1 2019', 'Optional royalty-backed loan $25-30M at prime + 2.25% = 7.25%; hedge oil']],
      6.9, 1.75, 6.1, 3.9, size=12, widths=[1.4, 4.7])
bullets(s, ['Fund can say yes in weeks: no capex, title + BOEM diligence done (4 missing instruments covered by title-defect terms), price rises only on BOEM proof',
            'Loan sized at <50% of base-case value (sponsor rule); we are not counting on it to close', 'Anchor test: ~15% base case clears a 12-15% hurdle; the $45-oil downside is covered by hedging 50-75% of 2019-20 oil at the Aug 15 strip', 'Cost of money: fund equity ~12% (our discount rate); optional loan 7.25% (prime 5.00% + 2.25%); returns shown before any borrowing',
            '!!No signed commitment by Aug 8 -> we walk away. No unfunded bids.'], x=0.5, y=5.62, w=12.4, size=12)

# 10 -------------------------------------------------------------- bidders + questions
s = slide('What other bidders see - and what we ask BP before award', None, 10)
table(s, [['Bidder type', 'What they see', 'Likely outcome'],
          ['Brochure-driven', 'WoodMac volumes, Pompano at $71M, Lucius at 4%', 'Overpay or fail to fund'],
          ['Revenue-multiple screeners', '5-7x $20.4M = $100-140M', 'Miss 2018 changes'],
          ['Disciplined royalty funds', 'Producing wells, 12-15% hurdle', 'Our real competition'],
          ['Us', 'Verified title + public data + pay-on-proof price', 'Credible, fundable, flexible']],
      0.4, 1.3, 6.4, 3.3, size=12, widths=[1.8, 2.8, 1.8])
bullets(s, ['Overlooked value we claim in the bid letter:',
            ('Lucius Jan-May 2018 unit true-up (~$2-3M) belongs to the buyer', 1),
            ('Assignment of all payor claims and audit rights (e.g. KC 875 is "free of all costs")', 1)], x=0.4, y=4.75, w=6.4, size=14)
bullets(s, ['**Documents we require from BP:',
            'Payor remittances + division orders 2016-18 (all 22 payors)',
            'Is Lucius paying on the 1.43% unit basis, or holding funds in suspense?',
            'Why Stones shut in Mar-May 2018; Shell remittances during royalty relief',
            'Kodiak: current rate, lease-continuity approval for the 2017-18 gap',
            'Ship Shoal: 8% of all production, or of Amoco\'s 50%?',
            'Missing: KC 874 instrument, Amoco->BP vesting, WR 551 page, MP 1979 letter',
            'Why is the WR 199 royalty excluded from the sale?'], x=7.0, y=1.3, w=6.1, size=14)
note(s, 'Data note: the case\'s "production workbook" was not in our folder; we used BOEM public production (to May-2018) and the WoodMac PDFs provided.')

# A1 -------------------------------------------------------------- AI use
s = slide('AI appendix (1/2): how we used AI and how we checked it', None, 'A1')
table(s, [['Task', 'AI role', 'How the team verified'],
          ['Read 60+ title PDFs', 'Extract decimals, depth limits, parties', 'Re-read key pages: Lucius Exhibit C, Kodiak ABOS p3, SS 219 p3'],
          ['Production data', 'Pull BOEM monthly data by lease', 'Kept only months public by Aug 15, 2018; flagged the rest'],
          ['Valuation model', 'Draft Python engine, then Excel', 'Rebuilt 2017 revenue vs listing; Excel and Python reconcile'],
          ['Red-team review', 'AI agents role-played reserve engineer, title lawyer, banker, auction strategist, judges', 'Team weighed each challenge; we rejected the AI strategist\'s $132M bid'],
          ['Writing', 'Draft slides and Q&A', 'Every number traced to a model cell or source page']],
      0.4, 1.4, 12.5, 4.6, size=13, widths=[2.3, 4.6, 5.6])
note(s, 'Example prompts: "Extract the ORRI decimal, depth limit and burdened lease from this assignment, with page"; "Compare WoodMac 2018 volumes with BOEM Jan-May 2018 by lease"; "Attack our bid as a title attorney". The expert panel was AI-simulated roles; all decisions were made by the team.', y=6.3)

# A2 -------------------------------------------------------------- AI corrections
s = slide('AI appendix (2/2): where AI was wrong - and how we caught it', None, 'A2')
table(s, [['AI said', 'How we caught it', 'Correction', 'Impact'],
          ['Lucius royalty is 4% (2% + 2%)', 'Unit agreement Exhibit C tract factors', '1.43% of unit output', 'Value ~2.8x lower'],
          ["Pompano = WoodMac's Pompano field (~$71M)", 'Read MC 72 assignment; BOEM by lease', 'Different field -> ~$0', '-$71M'],
          ['Value off the seller forecast (~$220M+)', 'BOEM Jan-May 2018 actuals', 'Forecast running hot; value producing wells', 'Bid: $98M cash + up to $24M on proof'],
          ['Closing credit $29M, loan $45M', 'Payment lag (~60 days); loan sized on gone revenue', '$17.5M credit; $25-30M loan', 'Cash at close +$11.5M'],
          ['Kodiak declines 22%/yr', 'Plotted 2016-18 monthly data', '35% base case, 22% shown as upside', 'About -$13M (25% vs 35% decline)'],
          ['Bid $132M to win the auction (AI strategist)', 'Fails funding + hurdle tests', 'Rejected; pay-on-proof structure', 'Avoided overpaying']],
      0.4, 1.4, 12.5, 5.0, size=13, widths=[3.4, 3.6, 3.3, 2.2])

prs.save(OUT); print('wrote', OUT)
