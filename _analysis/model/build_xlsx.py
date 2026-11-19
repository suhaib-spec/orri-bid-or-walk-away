"""Build the live Excel decision model (formula-driven) for the ORRI bid case.
Run: python -I model/build_xlsx.py "<_analysis dir>"   -> writes deliverables/ORRI_Bid_Model.xlsx
Mechanics mirror panel/scripts/reserves_rebuttal.py (auditor-corrected timing, Arps decline, uptime,
economic limit, Kodiak failure, Stones restart month) so Python and Excel reconcile."""
import csv, sys, os, datetime
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter as CL
from openpyxl.workbook.defined_name import DefinedName
from openpyxl.comments import Comment
from openpyxl.chart import LineChart, BarChart, Reference
from openpyxl.worksheet.datavalidation import DataValidation

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import analysis_dir
S = analysis_dir()
OUT = os.path.join(S, 'deliverables', 'ORRI_Bid_Model.xlsx')
os.makedirs(os.path.dirname(OUT), exist_ok=True)

F = 'Arial'
f_norm = Font(name=F, size=10)
f_in = Font(name=F, size=10, color='0000FF')
f_link = Font(name=F, size=10, color='008000')
f_b = Font(name=F, size=10, bold=True)
f_h = Font(name=F, size=10, bold=True, color='FFFFFF')
f_t = Font(name=F, size=14, bold=True)
f_note = Font(name=F, size=9, italic=True, color='595959')
fill_h = PatternFill('solid', fgColor='1F3864')
fill_key = PatternFill('solid', fgColor='FFFF00')
fill_sub = PatternFill('solid', fgColor='D9E1F2')
fill_fact = PatternFill('solid', fgColor='DDEBF7')
fill_ass = PatternFill('solid', fgColor='FCE4D6')
thin = Side(style='thin', color='BFBFBF')
box = Border(top=thin, bottom=thin, left=thin, right=thin)
M0 = '$#,##0.0;($#,##0.0);-'
M2 = '$#,##0.00;($#,##0.00);-'
P1 = '0.0%;(0.0%);-'
N0 = '#,##0;(#,##0);-'

wb = Workbook()
def sheet(name, first=False):
    ws = wb.active if first else wb.create_sheet()
    ws.title = name
    ws.sheet_view.showGridLines = False
    return ws
def name(nm, ref):
    wb.defined_names[nm] = DefinedName(nm, attr_text=ref)
def put(ws, cell, v, font=f_norm, fmt=None, fill=None, bold=False):
    c = ws[cell]; c.value = v; c.font = Font(name=F, size=10, bold=True, color=font.color) if bold else font
    if fmt: c.number_format = fmt
    if fill: c.fill = fill
    return c
def hdr(ws, row, col, labels):
    for i, l in enumerate(labels):
        c = ws.cell(row=row, column=col + i, value=l); c.font = f_h; c.fill = fill_h
        c.alignment = Alignment(horizontal='center', vertical='center', wrap_text=True)

PROPS = [('Kodiak', 'Kodiak'), ('Lucius', 'Lucius'), ('Stones', 'Stones'), ('South Santa Cruz', 'South Santa Cruz'),
         ('Grand Isle 116 unit', 'Grand Isle 116'), ('Main Pass 59', 'Main Pass 59'), ('Ship Shoal 219', 'Ship Shoal 219'),
         ('Orion', 'Orion')]
SHARE = [0.06375, 0.014288, 0.015, 0.0093, 0.005, 0.02604167, 0.04, 0.013125]
SHARE_NOTE = ['10% x 63.75% of unit production (ABOS Kodiak p3)', '2% x (24.77%+46.67%) unit tract factors (Exh. C)',
              '1.26725%+0.23275% on WR 508 (only producing Stones lease)', '2% x 46.5% (MC 563 assignment)',
              '0.5% below 13,000 ft (GI ORRI assignment p3)', '5/192 of lease production (MP 59 assignment)',
              '8% of Amoco 50% = 4% (SS 219 assignment p3); 8% = upside', '1.3125% (Orion ABOS)']
# production views: rate from Jun-2018 (kb/d), gas (mmcf/d), first-yr decline, Arps b, end yr, uptime, econ limit kb/d
CAUT = [(15.0, 12.3, .35, .5, 2035, .90, 1.5), (29.0, 27.0, .35, .5, 2040, .97, 3.0), (23.0, 3.3, .30, .5, 2040, .95, 5.0),
        (3.3, 1.75, .25, .3, 2035, .95, .8), (1.5, 18.3, .20, .3, 2030, .97, 0), (.35, 1.6, .12, 0, 2030, .97, 0),
        (.6, 2.7, .20, 0, 2025, .97, 0), (.35, 0, .20, 0, 2022, .97, 0)]
OPER = [(16.0, 13.0, .22, 0, 2035, 1, 0), (30.0, 29.0, .25, 0, 2040, 1, 0), (20.0, 3.0, .20, 0, 2040, 1, 0),
        (3.4, 1.8, .15, 0, 2035, 1, 0), (1.5, 18.5, .18, 0, 2030, 1, 0), (.35, 1.6, .10, 0, 2032, 1, 0),
        (.6, 2.8, .20, 0, 2025, 1, 0), (.4, 0, .20, 0, 2022, 1, 0)]

# ---------------------------------------------------------------- Dashboard (filled last)
dash = sheet('Dashboard', first=True)

# ---------------------------------------------------------------- Inputs
inp = sheet('Inputs')
inp.column_dimensions['A'].width = 2; inp.column_dimensions['B'].width = 38
for c in 'CDEFGHIJ': inp.column_dimensions[c].width = 13
inp.column_dimensions['K'].width = 60
put(inp, 'B1', 'INPUTS  (blue = hard-coded input; yellow = key judgement; every input carries its source)', f_t)
put(inp, 'B2', 'Facts come from documents or public data available by Aug 15, 2018. Assumptions are our judgement and are labelled.', f_note)
hdr(inp, 4, 2, ['General input', 'Value', 'Type', '', '', '', '', '', '', 'Source / rationale'])
GEN = [
 ('Effective date', datetime.date(2018, 1, 1), 'Fact', 'EffDate', 'yyyy-mm-dd', 'Bid Instruction: effective date 1/1/2018'),
 ('Bid due / valuation reference date', datetime.date(2018, 8, 15), 'Fact', 'BidDate', 'yyyy-mm-dd', 'Bid Instruction: bids due Aug 15, 2018 4pm CST'),
 ('Closing date (t = 0 for returns)', datetime.date(2018, 9, 14), 'Fact', 'CloseDate', 'yyyy-mm-dd', 'Bid Instruction: closing Sept 14, 2018'),
 ('Cash price at closing ($M)', 98.0, 'Decision', 'Bid', M0, 'Plus up to $24M performance payments triggered by BOEM data (see Returns notes)'),
 ('Fixed-price ceiling / walk-away ($M)', 105.0, 'Decision', 'WalkAway', M0, 'If BP requires a fixed price only'),
 ('Base discount rate', 0.12, 'Assumption', 'BaseRate', P1, 'Case range 10-20%; 12% = royalty buyer hurdle; 15% shown for offshore single-well risk'),
 ('Oil realisation vs WTI ($/bbl)', 0.70, 'Assumption', 'OilAdj', M2, 'Mars sour vs WTI 2017 avg (+$0.70); Mars was WTI -$1.90 on Aug 15, 2018'),
 ('Oil transport/processing deduction ($/bbl)', 3.00, 'Assumption', 'OilDed', M2, 'Typical deepwater deduction; makes 2017 rebuild = $20.4M (gross $21.8M w/o)'),
 ('Gas heat content (MMBtu/mcf)', 1.10, 'Assumption', 'GasMult', '0.00', 'Wet associated gas'),
 ('Gas deduction ($/mcf)', 0.40, 'Assumption', 'GasDed', M2, 'Typical gathering/processing'),
 ('Hurricane downtime haircut (per yr)', 0.02, 'Assumption', 'Hurricane', P1, 'EIA mean GoM shut-in history ~2%/yr; 3% costs ~$0.6M'),
 ('ORRI payment lag (months)', 2, 'Fact (industry)', 'LagM', '0', 'Operators remit ~60 days after production month'),
 ('Decline anchor (yrs from Jan-1 to rate start)', 0.21, 'Assumption', 'Anchor', '0.00', 'Jun-Dec 2018 average is centred ~Sep 15 (model-auditor fix)'),
 ('Prime rate (Aug 15, 2018)', 0.05, 'Fact', 'Prime', '0.00%', 'WSJ prime 5.00% since Jun 14, 2018'),
 ('Post-close loan spread over prime', 0.0225, 'Assumption', 'LoanSpread', '0.00%', 'Royalty-backed term loan; bank deck, Kodiak given little loan credit'),
 ('Post-close loan size ($M)', 27.5, 'Assumption', 'LoanSize', M0, 'Capital-markets panel: $25-30M (40% of low-deck PV10 of 2019+ cash flow)'),
 ('Transaction costs ($M)', 1.6, 'Assumption', 'TxnCost', M0, 'Legal, title, engineering, fees'),
 ('Liquidity reserve ($M)', 1.5, 'Assumption', 'LiqRes', M0, 'Hurricane-season reserve'),
 ('Anchor fund share of equity', 0.95, 'Assumption', 'AnchorPct', P1, 'Committed-capital royalty fund; team/sponsor co-invest 5%'),
 ('Deposit at award (% of price)', 0.10, 'Assumption', 'DepositPct', P1, 'Market standard for A&D auctions'),
 ('Lucius lease-basis factor (if payors ignore unit)', 0.7405, 'Assumption', 'LucLease', '0.0000', '52.9% of Jan-May 2018 Lucius volumes on KC 874/875 x 2% / 1.4288%'),
]
r = 5
for lbl, v, typ, nm, fmt, src in GEN:
    put(inp, f'B{r}', lbl); c = put(inp, f'C{r}', v, f_in, fmt)
    if nm in ('Bid', 'WalkAway', 'BaseRate'): c.fill = fill_key
    put(inp, f'D{r}', typ, fill=fill_fact if typ.startswith('Fact') else fill_ass)
    put(inp, f'K{r}', src, f_note)
    name(nm, f"Inputs!$C${r}"); r += 1

# Price decks
r += 1; PD0 = r
put(inp, f'B{r}', 'PRICE DECKS ($/bbl WTI, $/MMBtu Henry Hub)', f_b); r += 1
hdr(inp, r, 2, ['Year', 'Strip WTI', 'Strip HH', 'Low WTI', 'Low HH', 'High WTI', 'High HH', '', '', 'Source'])
r += 1; DK0 = r
STRIP_W = {2018: 66.5, 2019: 64.5, 2020: 61.0, 2021: 58.5}; STRIP_H = {2018: 2.95, 2019: 2.82, 2020: 2.66}
for y in range(2018, 2041):
    put(inp, f'B{r}', y, f_norm, '0')
    put(inp, f'C{r}', STRIP_W.get(y, 57.0), f_in, M2); put(inp, f'D{r}', STRIP_H.get(y, 2.65), f_in, M2)
    if y == 2018:
        put(inp, f'E{r}', f'=C{r}', f_norm, M2); put(inp, f'F{r}', f'=D{r}', f_norm, M2)
        put(inp, f'G{r}', f'=C{r}', f_norm, M2); put(inp, f'H{r}', f'=D{r}', f_norm, M2)
    else:
        put(inp, f'E{r}', 45.0, f_in, M2); put(inp, f'F{r}', 2.25, f_in, M2)
        put(inp, f'G{r}', 75.0 if y == 2019 else f'=G{r-1}*1.02', f_in if y == 2019 else f_norm, M2)
        put(inp, f'H{r}', 3.25, f_in, M2)
    r += 1
DK1 = r - 1
put(inp, f'K{DK0}', 'Strip: NYMEX settlements Aug 15, 2018 (cal-year averages; 2022+ held flat at $57 / $2.65)', f_note)
put(inp, f'K{DK0+1}', 'Low: $45 / $2.25 flat from 2019 (2015-17 trough); High: $75 +2%/yr, $3.25', f_note)
name('DeckYears', f'Inputs!$B${DK0}:$B${DK1}')
name('DeckTable', f'Inputs!$C${DK0}:$H${DK1}')

# Shares
r += 1; put(inp, f'B{r}', 'EFFECTIVE ORRI SHARE OF GROSS PRODUCTION (detail: Title_Shares tab)', f_b); r += 1
hdr(inp, r, 2, ['Property', 'Share used', 'Type', '', '', '', '', '', '', 'Basis'])
r += 1; SH0 = r
for (k, d), s, n in zip(PROPS, SHARE, SHARE_NOTE):
    put(inp, f'B{r}', d); put(inp, f'C{r}', s, f_in, '0.0000%'); put(inp, f'D{r}', 'Fact (document)' if d != 'Ship Shoal 219' else 'Assumption (conservative)',
        fill=fill_fact if d != 'Ship Shoal 219' else fill_ass)
    put(inp, f'K{r}', n, f_note); r += 1

# Production views
def view_table(r, title, rows, typ):
    put(inp, f'B{r}', title, f_b); r += 1
    hdr(inp, r, 2, ['Property', 'Oil rate from Jun-18 (kb/d gross)', 'Gas rate (mmcf/d)', 'First-yr decline', 'Arps b',
                    'Last year', 'Uptime', 'Econ limit (kb/d)', '', 'Basis'])
    r += 1; r0 = r
    for (k, d), v in zip(PROPS, rows):
        put(inp, f'B{r}', d)
        for j, (val, fmt) in enumerate(zip(v, ['0.00', '0.00', P1, '0.0', '0', '0%', '0.0'])):
            put(inp, f'{CL(3+j)}{r}', val, f_in, fmt)
        put(inp, f'D{r}' if False else f'J{r}', typ, fill=fill_ass); r += 1
    return r, r0
r += 1
r, CV0 = view_table(r, 'PRODUCTION VIEW 1 - BASE CASE (set from public BOEM monthly data to May-2018; judgement, not a regression fit)', CAUT, 'Assumption')
put(inp, f'K{CV0}', 'Kodiak: 1st zone fell 11.7->7.3 kb/d Jun-Dec 2016 (~60%/yr); 2017 zone ~37%/yr; ran ~66% of time since first oil', f_note)
put(inp, f'K{CV0+1}', 'Lucius: Dec-17 52 kb/d -> Apr-18 35 kb/d; May-18 19.4 = planned tie-in downtime (all leases -45-50% together)', f_note)
put(inp, f'K{CV0+2}', 'Stones: shut in Mar-May 2018 (cause unknown at Aug 15) -> restart month is a case lever; 23 kb/d = Jan-Feb 2018 level', f_note)
r += 1
r, OV0 = view_table(r, 'PRODUCTION VIEW 2 - OPERATOR-TREND (our v1 inputs: Mar-May 2018 run-rate, exponential decline)', OPER, 'Assumption')
put(inp, f'K{OV0}', 'Kodiak 22%/yr exponential = WoodMac-like single-well profile; no failure, 100% uptime', f_note)

# ---------------------------------------------------------------- Cases
cs = sheet('Cases')
cs.column_dimensions['A'].width = 2; cs.column_dimensions['B'].width = 34
CASES = [
 ('Live case (edit blue cells)', 1, 1, 1.0, 0, 9, 1.0, None, 0.12),
 ('Base case - strip', 1, 1, 1.0, 0, 9, 1.0, None, 0.12),
 ('Operator-trend - strip', 2, 1, 1.0, 0, 7, 1.0, None, 0.12),
 ('Cautious - $45 oil', 1, 2, 1.0, 0, 9, 1.0, None, 0.12),
 ('Operator-trend - $45 oil', 2, 2, 1.0, 0, 7, 1.0, None, 0.12),
 ('Cautious - Kodiak well fails 2020', 1, 1, 1.0, 2020, 9, 1.0, None, 0.12),
 ('Cautious - Stones restart slips to 2019', 1, 1, 1.0, 0, 13, 1.0, None, 0.12),
 ('Cautious - Lucius paid on lease basis', 1, 1, 1.0, 0, 9, '=LucLease', None, 0.12),
 ('Cautious - Kodiak declines 25% not 35%', 1, 1, 1.0, 0, 9, 1.0, 0.25, 0.12),
 ('Cautious - high price ($75 +2%)', 1, 3, 1.0, 0, 9, 1.0, None, 0.12),
]
NC = len(CASES)
put(cs, 'B1', 'SCENARIO CASES  (each column runs the full model in the Engine tab)', f_t)
put(cs, 'B2', 'Case 1 is the live case shown on the Dashboard - change its blue cells. Cases 2-10 are fixed presets used for the IRR grid and tornado.', f_note)
PARAMS = ['Case name', 'Production view (1 = Cautious, 2 = Operator-trend)', 'Price deck (1 = Strip, 2 = Low, 3 = High)',
          'Oil price multiplier (2019+)', 'Kodiak well fails from year (0 = never)', 'Stones restart month in 2018 (13 = 2019)',
          'Lucius share factor (1 = unit basis)', 'Kodiak first-yr decline override (blank = view)', 'Discount rate']
for i, p in enumerate(PARAMS):
    put(cs, f'B{4+i}', p, f_b if i == 0 else f_norm)
for j, cse in enumerate(CASES):
    col = CL(3 + j); cs.column_dimensions[col].width = 17
    for i, v in enumerate(cse):
        fmt = [None, '0', '0', '0.00', '0', '0', '0.0000', P1, P1][i]
        c = put(cs, f'{col}{4+i}', v, f_in if (j == 0 or i == 0) and not (isinstance(v, str) and v.startswith('=')) else (f_norm if isinstance(v, str) and v.startswith('=') else f_in), fmt)
        if i == 0: c.font = f_h; c.fill = fill_h; c.alignment = Alignment(wrap_text=True, horizontal='center')
cs.row_dimensions[4].height = 42
dv = DataValidation(type='list', formula1='"1,2"', allow_blank=False); cs.add_data_validation(dv); dv.add('C5')
dv2 = DataValidation(type='list', formula1='"1,2,3"', allow_blank=False); cs.add_data_validation(dv2); dv2.add('C6')

# ---------------------------------------------------------------- BOEM data
bd = sheet('BOEM_Data')
rows = [x for x in csv.DictReader(open(os.path.join(S, 'boem', 'monthly_by_lease.csv'))) if x['public_by_2018_08_15'].startswith('Y')]
put(bd, 'A1', 'BOEM OGOR-A monthly production by lease - ONLY months public by Aug 15, 2018 (Jun-2018+ rows excluded as hindsight)', f_b)
put(bd, 'A2', 'Source: BOEM Data Center, OGOR-A production by lease (data.boem.gov). Oil = oil + condensate.', f_note)
hdr(bd, 3, 1, ['Property', 'Lease', 'YYYYMM', 'Oil+cond (bbl)', 'Gas (mcf)', 'Water (bbl)', 'Producing completions', 'Oil (bopd)', 'Public by 8/15/18'])
for i, x in enumerate(rows):
    rr_ = 4 + i
    vals = [x['property'], x['lease'], int(x['yyyymm']), float(x['oil_bbl'] or 0) + float(x['condensate_bbl'] or 0),
            float(x['gas_mcf'] or 0), float(x['water_bbl'] or 0), x['producing_completions'], f'=IFERROR(D{rr_}/DAY(EOMONTH(DATE(INT(C{rr_}/100),MOD(C{rr_},100),1),0)),0)', 'Y']
    for j, v in enumerate(vals):
        c = bd.cell(row=rr_, column=1 + j, value=v); c.font = f_norm
        if j in (3, 4, 5, 7): c.number_format = N0
BD1 = 3 + len(rows)
for c, w in zip('ABCDEFGHI', [26, 9, 9, 13, 13, 12, 11, 10, 10]): bd.column_dimensions[c].width = w
name('BD_Prop', f'BOEM_Data!$A$4:$A${BD1}'); name('BD_Lease', f'BOEM_Data!$B$4:$B${BD1}')
name('BD_Ym', f'BOEM_Data!$C$4:$C${BD1}'); name('BD_Oil', f'BOEM_Data!$D$4:$D${BD1}'); name('BD_Gas', f'BOEM_Data!$E$4:$E${BD1}')
bd.freeze_panes = 'A4'

# ---------------------------------------------------------------- Engine
en = sheet('Engine')
en.column_dimensions['A'].width = 30; en.column_dimensions['B'].width = 18
for c in range(3, 13): en.column_dimensions[CL(c)].width = 9
PER = [('M', 2018, m) for m in range(1, 13)] + [('Y', y, None) for y in range(2019, 2041)]
C0 = 13  # first period column (M)
PC = [CL(C0 + i) for i in range(len(PER))]
LASTC = PC[-1]
for c in PC: en.column_dimensions[c].width = 9
put(en, 'A1', 'ENGINE - revenue to the ORRI package by case, property and period ($M)', f_t)
put(en, 'A2', 'Jan-May 2018 = BOEM actuals. Jun-2018 on = forecast. Rate(t) = start rate x Arps factor; zero after last year, below economic limit, or after Kodiak failure.', f_note)
R_LBL, R_TYPE, R_YEAR, R_MON, R_DAYS, R_PAY, R_EXP, R_T, R_HUR, R_YM = 4, 5, 6, 7, 8, 9, 10, 11, 12, 13
labels = {R_LBL: 'Period', R_TYPE: 'Type (M = month, Y = year)', R_YEAR: 'Year', R_MON: 'Month', R_DAYS: 'Days',
          R_PAY: 'Cash receipt date', R_EXP: 'Years from closing', R_T: 'Decline time t (yrs)', R_HUR: 'Hurricane factor', R_YM: 'YYYYMM'}
for rr_, l in labels.items(): put(en, f'A{rr_}', l, f_b)
for i, (t, y, m) in enumerate(PER):
    c = PC[i]
    put(en, f'{c}{R_LBL}', datetime.date(y, m, 1).strftime('%b-%y') if t == 'M' else str(y), f_h, fill=fill_h)
    put(en, f'{c}{R_TYPE}', t); put(en, f'{c}{R_YEAR}', y, f_norm, '0'); put(en, f'{c}{R_MON}', m if m else '')
    if t == 'M':
        put(en, f'{c}{R_DAYS}', f'=DAY(EOMONTH(DATE({c}{R_YEAR},{c}{R_MON},1),0))', fmt='0')
        put(en, f'{c}{R_PAY}', f'=IF({c}{R_MON}<=6,CloseDate,IF({c}{R_MON}<=9,DATE(2019,1,16),EffDate+ROUND(({c}{R_MON}+1)/12*365+25,0)))', fmt='yyyy-mm-dd')
        put(en, f'{c}{R_T}', '')
        put(en, f'{c}{R_HUR}', f'=IF({c}{R_MON}<8,1,IF({c}{R_MON}=8,1-Hurricane*17/31,1-Hurricane))', fmt='0.000')
        put(en, f'{c}{R_YM}', y * 100 + m, f_norm, '0')
    else:
        put(en, f'{c}{R_DAYS}', f'=DATE({c}{R_YEAR}+1,1,1)-DATE({c}{R_YEAR},1,1)', fmt='0')
        put(en, f'{c}{R_PAY}', f'=EffDate+({c}{R_YEAR}-2018+0.5+LagM/12)*365', fmt='yyyy-mm-dd')
        put(en, f'{c}{R_T}', f'={c}{R_YEAR}-2018-Anchor', fmt='0.00')
        put(en, f'{c}{R_HUR}', '=1-Hurricane', fmt='0.000')
    put(en, f'{c}{R_EXP}', f'=MAX(0,({c}{R_PAY}-CloseDate)/365)', fmt='0.000')
name('PayDates', f'Engine!${PC[0]}${R_PAY}:${LASTC}${R_PAY}')
name('YrsFromClose', f'Engine!${PC[0]}${R_EXP}:${LASTC}${R_EXP}')

BLOCK = 4 + 4 * len(PROPS) + 3
case_total_row = []; case_rate_cell = []; prop_rev_rows = []
start = 16
for j in range(NC):
    b0 = start + j * (BLOCK + 2)
    ccol = CL(3 + j)
    put(en, f'A{b0}', f'=Cases!{ccol}4', f_h, fill=fill_h)
    for c in ['B'] + [CL(x) for x in range(3, 13)] + PC: en[f'{c}{b0}'].fill = fill_h
    # case parameter pulls (row b0+1)
    pr = b0 + 1
    pnames = ['View', 'Deck', 'Price mult', 'Kodiak fails', 'Stones restart', 'Lucius factor', 'Kodiak De ovr', 'Rate']
    for i, pn in enumerate(pnames):
        put(en, f'{CL(3+i)}{pr-0}', pn, f_note) if False else None
    put(en, f'A{pr}', 'Case parameters  ->', f_b)
    put(en, f'B{pr}', 'view/deck/mult/fail/restart/Lucius/KodDe/rate', f_note)
    for i in range(8):
        put(en, f'{CL(3+i)}{pr}', f'=IF(Cases!{ccol}{5+i}="","",Cases!{ccol}{5+i})', f_link, ['0', '0', '0.00', '0', '0', '0.0000', P1, P1][i])
    V, D, PM, KF, SR, LF, KD, RT = [f'${CL(3+i)}${pr}' for i in range(8)]
    case_rate_cell.append(f'Engine!{RT}')
    # prices
    ro, rg = b0 + 2, b0 + 3
    put(en, f'A{ro}', 'Net oil price ($/bbl)', f_b); put(en, f'A{rg}', 'Net gas price ($/mcf)', f_b)
    for c in PC:
        put(en, f'{c}{ro}', f'=INDEX(DeckTable,MATCH({c}${R_YEAR},DeckYears,0),2*{D}-1)*IF({c}${R_YEAR}>2018,{PM},1)+OilAdj-OilDed', fmt=M2)
        put(en, f'{c}{rg}', f'=INDEX(DeckTable,MATCH({c}${R_YEAR},DeckYears,0),2*{D})*GasMult-GasDed', fmt=M2)
    hdr(en, b0 + 4, 1, ['Line', 'Property', 'Share', 'Start rate', 'Gas rate', 'Decl.', 'b', 'Last yr', 'Uptime', 'Econ lim', 'Di', 'Spare'])
    rr_ = b0 + 5; revrows = []
    for pi, (key, disp) in enumerate(PROPS):
        rf, rO, rG, rR = rr_, rr_ + 1, rr_ + 2, rr_ + 3
        put(en, f'A{rf}', f'{disp}: decline factor'); put(en, f'A{rO}', f'{disp}: gross oil (bbl)')
        put(en, f'A{rG}', f'{disp}: gross gas (mcf)'); put(en, f'A{rR}', f'{disp}: ORRI revenue ($M)', f_b)
        for x in (rf, rO, rG, rR): put(en, f'B{x}', key)
        sh = f'Inputs!$C${SH0+pi}'
        put(en, f'C{rf}', f'={sh}*IF($B{rf}="Lucius",{LF},1)', f_link, '0.0000%')
        for k, col in enumerate('DEFGHIJ'):
            src_c = CL(3 + k)
            fml = f'=IF({V}=1,Inputs!${src_c}${CV0+pi},Inputs!${src_c}${OV0+pi})'
            if col == 'F' and key == 'Kodiak': fml = f'=IF({KD}<>"",{KD},IF({V}=1,Inputs!${src_c}${CV0+pi},Inputs!${src_c}${OV0+pi}))'
            put(en, f'{col}{rf}', fml, f_link, ['0.00', '0.00', P1, '0.0', '0', '0%', '0.0'][k])
        put(en, f'K{rf}', f'=IF(G{rf}=0,0,((1-F{rf})^(-G{rf})-1)/G{rf})', fmt='0.000')
        for i, (t, y, m) in enumerate(PER):
            c = PC[i]
            if t == 'M':
                if m <= 5:
                    put(en, f'{c}{rf}', 'actual')
                    put(en, f'{c}{rO}', f'=SUMIFS(BD_Oil,BD_Prop,$B{rO},BD_Ym,{c}${R_YM})', fmt=N0)
                    put(en, f'{c}{rG}', f'=SUMIFS(BD_Gas,BD_Prop,$B{rG},BD_Ym,{c}${R_YM})', fmt=N0)
                else:
                    put(en, f'{c}{rf}', f'=IF($B{rf}="Stones",IF({c}${R_MON}>={SR},1,0),1)', fmt='0.000')
                    put(en, f'{c}{rO}', f'=$D{rf}*{c}{rf}*1000*{c}${R_DAYS}*$I{rf}', fmt=N0)
                    put(en, f'{c}{rG}', f'=$E{rf}*{c}{rf}*1000*{c}${R_DAYS}*$I{rf}', fmt=N0)
            else:
                arps = f'IF($G{rf}=0,(1-$F{rf})^{c}${R_T},(1+$G{rf}*$K{rf}*{c}${R_T})^(-1/$G{rf}))'
                put(en, f'{c}{rf}', f'=IF(OR({c}${R_YEAR}>$H{rf},AND($B{rf}="Kodiak",{KF}>0,{c}${R_YEAR}>={KF})),0,IF($D{rf}*{arps}<$J{rf},0,{arps}))', fmt='0.000')
                put(en, f'{c}{rO}', f'=$D{rf}*{c}{rf}*1000*{c}${R_DAYS}*$I{rf}', fmt=N0)
                put(en, f'{c}{rG}', f'=$E{rf}*{c}{rf}*1000*{c}${R_DAYS}*$I{rf}', fmt=N0)
            put(en, f'{c}{rR}', f'=({c}{rO}*$C{rf}*{c}${ro}+{c}{rG}*$C{rf}*{c}${rg})/1000000*{c}${R_HUR}', fmt=M2)
        revrows.append(rR); rr_ += 4
    rt = rr_
    put(en, f'A{rt}', 'TOTAL ORRI CASH FLOW ($M)', f_b)
    for c in PC:
        put(en, f'{c}{rt}', '=' + '+'.join(f'{c}{x}' for x in revrows), fmt=M2).font = f_b
        en[f'{c}{rt}'].fill = fill_sub
    en[f'A{rt}'].fill = fill_sub
    put(en, f'A{rt+1}', 'PV at case rate, at closing ($M)', f_b)
    put(en, f'B{rt+1}', f'=SUMPRODUCT({PC[0]}{rt}:{LASTC}{rt},1/(1+{RT})^YrsFromClose)', fmt=M0).font = f_b
    put(en, f'C{rt+1}', 'Closing credit (Jan-Jun receipts) $M', f_note)
    put(en, f'H{rt+1}', f'=SUM({PC[0]}{rt}:{PC[5]}{rt})', fmt=M0)
    case_total_row.append(rt); prop_rev_rows.append(revrows)
en.freeze_panes = f'{PC[0]}{R_YM+1}'

def tot_ref(j): return f'Engine!${PC[0]}${case_total_row[j]}:${LASTC}${case_total_row[j]}'
def pv_ref(j): return f'Engine!$B${case_total_row[j]+1}'
def credit_ref(j): return f'Engine!$H${case_total_row[j]+1}'

# ---------------------------------------------------------------- Valuation
va = sheet('Valuation')
va.column_dimensions['A'].width = 2; va.column_dimensions['B'].width = 40
for c in 'CDEFGH': va.column_dimensions[c].width = 14
put(va, 'B1', 'VALUATION - PV of ORRI cash flow at closing (Sept 14, 2018), $M', f_t)
put(va, 'B2', 'PV includes Jan-Jun 2018 receipts that the seller credits at closing (a reduction of cash paid). Existing wells only - no new drilling.', f_note)
hdr(va, 4, 2, ['Case', 'PV @10%', 'PV @12%', 'PV @15%', 'PV @20%', 'Closing credit', 'PV @ case rate'])
RATES = [0.10, 0.12, 0.15, 0.20]
for j in range(NC):
    r_ = 5 + j
    put(va, f'B{r_}', f'=Cases!{CL(3+j)}4', f_link)
    for k, rt_ in enumerate(RATES):
        put(va, f'{CL(3+k)}{r_}', f'=SUMPRODUCT({tot_ref(j)},1/(1+{rt_})^YrsFromClose)', fmt=M0)
    put(va, f'G{r_}', f'={credit_ref(j)}', f_link, M0); put(va, f'H{r_}', f'={pv_ref(j)}', f_link, M0)
VROW = {j: 5 + j for j in range(NC)}
r_ = 5 + NC + 2
put(va, f'B{r_}', 'PV BY PROPERTY @ base rate ($M)', f_b); r_ += 1
hdr(va, r_, 2, ['Property', 'Cautious (base)', 'Operator-trend', 'Cautious share', 'Operator share']); r_ += 1
PP0 = r_
for pi, (key, disp) in enumerate(PROPS):
    put(va, f'B{r_}', disp)
    for k, j in enumerate((1, 2)):
        rr0 = prop_rev_rows[j][pi]
        put(va, f'{CL(3+k)}{r_}', f'=SUMPRODUCT(Engine!${PC[0]}${rr0}:${LASTC}${rr0},1/(1+BaseRate)^YrsFromClose)', fmt=M0)
    put(va, f'E{r_}', f'=C{r_}/SUM($C${PP0}:$C${PP0+7})', fmt=P1); put(va, f'F{r_}', f'=D{r_}/SUM($D${PP0}:$D${PP0+7})', fmt=P1)
    r_ += 1
put(va, f'B{r_}', 'Total', f_b); put(va, f'C{r_}', f'=SUM(C{PP0}:C{r_-1})', fmt=M0, bold=True); put(va, f'D{r_}', f'=SUM(D{PP0}:D{r_-1})', fmt=M0, bold=True)
PPT = r_
r_ += 2
put(va, f'B{r_}', 'TORNADO - change in PV @12% vs Cautious base ($M)', f_b); r_ += 1
hdr(va, r_, 2, ['Driver', 'PV @12%', 'Change vs base']); r_ += 1
TOR0 = r_
for j in [2, 9, 8, 3, 6, 7, 5]:
    put(va, f'B{r_}', f'=Cases!{CL(3+j)}4', f_link); put(va, f'C{r_}', f'=D{VROW[j]}', f_norm, M0)
    put(va, f'D{r_}', f'=C{r_}-$D${VROW[1]}', f_norm, M0); r_ += 1
for lbl, fml in (('Discount rate 10% (vs 12%)', f'=C{VROW[1]}'), ('Discount rate 15% (vs 12%)', f'=E{VROW[1]}'), ('Discount rate 20% (vs 12%)', f'=F{VROW[1]}')):
    put(va, f'B{r_}', lbl); put(va, f'C{r_}', fml, f_norm, M0); put(va, f'D{r_}', f'=C{r_}-$D${VROW[1]}', f_norm, M0); r_ += 1
TOR1 = r_ - 1
r_ += 1
put(va, f'B{r_}', 'Monte Carlo (6,000 runs; Python panel/scripts/reserves_rebuttal.py) - cautious mechanics incl. Kodiak failure risk 6%/yr', f_b); r_ += 1
hdr(va, r_, 2, ['Package value', 'P90 (low)', 'P50', 'P10 (high)']); r_ += 1
for lbl, a, b_, c_ in (('PV @12% ($M)', 79.0, 98.3, 116.0), ('PV @15% ($M)', 76.0, 94.2, 111.0)):
    put(va, f'B{r_}', lbl); put(va, f'C{r_}', a, f_in, M0); put(va, f'D{r_}', b_, f_in, M0); put(va, f'E{r_}', c_, f_in, M0)
    put(va, f'F{r_}', 'Values pasted from Python run (Excel cannot run 6,000 simulations without macros)', f_note); r_ += 1
MCROW = r_ - 2

# ---------------------------------------------------------------- Upside (risked development)
up = sheet('Upside')
up.column_dimensions['A'].width = 2; up.column_dimensions['B'].width = 44
for c in 'CDEFGHIJKLM': up.column_dimensions[c].width = 11
put(up, 'B1', 'DRILLING UPSIDE - risked, NOT included in the base value or the bid math unless stated', f_t)
put(up, 'B2', 'Case rule: "you cannot assume when drilling will happen or how much it will add". We therefore pay at most a risked fraction, one well at a time.', f_note)
hdr(up, 4, 2, ['Item (status at Aug 15, 2018)', 'ORRI share', 'First-yr rate (kb/d)', 'Decline', 'b', 'First year', 'Chance of success',
               'Other haircut', 'Unrisked PV12', 'Risked PV12'])
ITEMS = [('Hadrian North into Lucius unit (sanctioned, spud Q2-18)', '=Inputs!$C$' + str(SH0 + 1), 15.0, .30, .5, 2020, .80, .40, 'x40% = chance volumes are allocated through the unit'),
         ('Lucius 9th well / KC 919 rework (planned)', '=Inputs!$C$' + str(SH0 + 1), 10.0, .30, .5, 2019, .30, 1.0, ''),
         ('Stones Phase 2 - 2 wells + subsea pumps (planned)', '=Inputs!$C$' + str(SH0 + 2), 20.0, .30, .5, 2020, .30, .80, 'x0.8 for WR 464 allocation and royalty-relief risk'),
         ('Kodiak 2nd well (planned, operator mid-sale)', '=Inputs!$C$' + str(SH0), 10.0, .35, .5, 2020, .15, 1.0, '')]
YR = list(range(2019, 2033))
for k, y in enumerate(YR): put(up, f'{CL(14+k)}4', str(y), f_h, fill=fill_h)
for i, it in enumerate(ITEMS):
    r_ = 5 + i
    put(up, f'B{r_}', it[0])
    for k, v in enumerate(it[1:8]):
        put(up, f'{CL(3+k)}{r_}', v, f_link if k == 0 else f_in, ['0.0000%', '0.0', P1, '0.0', '0', '0%', '0%'][k])
    for k, y in enumerate(YR):
        c = CL(14 + k)
        t = f'({y}-$G{r_})'
        arps = f'(1+$F{r_}*((1-$E{r_})^(-$F{r_})-1)/$F{r_}*{t})^(-1/$F{r_})'
        put(up, f'{c}{r_}', f'=IF({y}<$G{r_},0,$D{r_}*{arps}*1000*365*$C{r_}*(INDEX(DeckTable,MATCH({y},DeckYears,0),1)+OilAdj-OilDed)*0.98*0.95/1000000/(1+BaseRate)^({y}-2018+0.5+LagM/12-256/365))', fmt=M2)
    put(up, f'J{r_}', f'=SUM({CL(14)}{r_}:{CL(14+len(YR)-1)}{r_})', fmt=M0)
    put(up, f'K{r_}', f'=J{r_}*H{r_}*I{r_}', fmt=M0)
    put(up, f'L{r_}', it[8], f_note)
put(up, 'B9', 'Total risked development upside', f_b); put(up, 'K9', '=SUM(K5:K8)', fmt=M0, bold=True); put(up, 'J9', '=SUM(J5:J8)', fmt=M0, bold=True)
name('UpsideRisked', 'Upside!$K$9')
put(up, 'B11', 'Excluded on purpose: Pompano ORRI (covers only LLOG/Nexen-assignee production in a limited area to 13,405 ft; none since Oct-2014), Orion lease lapse.', f_note)

# ---------------------------------------------------------------- Returns
rtn = sheet('Returns')
rtn.column_dimensions['A'].width = 2; rtn.column_dimensions['B'].width = 40
put(rtn, 'B1', 'RETURNS - unlevered IRR on cash paid at closing (seller credits Jan-Jun 2018 receipts at closing)', f_t)
put(rtn, 'B2', 'IRR = XIRR of [-bid + closing credit at Sept 14, 2018] and every later ORRI receipt. Existing wells only.', f_note)
BIDS = [95, 98, 100, 105, 110, 115, 120]
hdr(rtn, 4, 2, ['Case \\ Bid ($M)'] + [f'${b}M' for b in BIDS])
for k in range(len(BIDS)): rtn.column_dimensions[CL(3+k)].width = 11
# cash flow rows below
CFR0 = 30
put(rtn, f'B{CFR0-2}', 'Cash-flow rows feeding XIRR (bid at t=0, then receipts by date)', f_b)
put(rtn, f'B{CFR0-1}', 'Date', f_b)
put(rtn, f'C{CFR0-1}', '=CloseDate', fmt='yyyy-mm-dd')
for i, c in enumerate(PC):
    put(rtn, f'{CL(4+i)}{CFR0-1}', f'=INT(Engine!{c}{R_PAY})', f_link, 'yyyy-mm-dd')
DCOLS = f'$C${CFR0-1}:${CL(3+len(PC))}${CFR0-1}'
cfrow = {}
rr_ = CFR0
for j in range(NC):
    for b in BIDS + ['Bid']:
        put(rtn, f'B{rr_}', f'=Cases!{CL(3+j)}4&" @ {b}"', f_note)
        put(rtn, f'C{rr_}', f'=-{b}' if b != 'Bid' else '=-Bid', fmt=M2)
        for i, c in enumerate(PC):
            put(rtn, f'{CL(4+i)}{rr_}', f'=Engine!{c}{case_total_row[j]}', f_link, M2)
        cfrow[(j, b)] = rr_; rr_ += 1
def xirr(j, b):
    r0 = cfrow[(j, b)]
    return f'=XIRR($C${r0}:${CL(3+len(PC))}${r0},{DCOLS})'
for j in range(NC):
    r_ = 5 + j
    put(rtn, f'B{r_}', f'=Cases!{CL(3+j)}4', f_link)
    for k, b in enumerate(BIDS):
        c = put(rtn, f'{CL(3+k)}{r_}', xirr(j, b), fmt=P1)
        if b == 98: c.fill = fill_key
put(rtn, f'B{6+NC}', 'MOIC (undiscounted cash / bid) at the recommended bid', f_b)
hdr(rtn, 7 + NC, 2, ['Case', 'IRR @ Bid', 'MOIC', 'Profit $M (undisc.)', 'Payback year'])
for j in range(NC):
    r_ = 8 + NC + j; r0 = cfrow[(j, 'Bid')]
    put(rtn, f'B{r_}', f'=Cases!{CL(3+j)}4', f_link)
    put(rtn, f'C{r_}', xirr(j, 'Bid'), fmt=P1)
    put(rtn, f'D{r_}', f'=SUM($D${r0}:${CL(3+len(PC))}${r0})/Bid', fmt='0.00x')
    put(rtn, f'E{r_}', f'=SUM($C${r0}:${CL(3+len(PC))}${r0})', fmt=M0)
    # payback: first period where cumulative >= 0 -> use helper: count of periods with cumulative<0
    put(rtn, f'F{r_}', f'=IFERROR(INDEX(Engine!${PC[0]}${R_YEAR}:${LASTC}${R_YEAR},MATCH(TRUE,INDEX(SUBTOTAL(9,OFFSET($C${r0},0,0,1,COLUMN($D${r0}:${CL(3+len(PC))}${r0})-COLUMN($C${r0})+1))>=0,0),0)),"Not repaid")', fmt='0')
IRR_ROW = {j: 5 + j for j in range(NC)}
MOIC_ROW = {j: 8 + NC + j for j in range(NC)}

# ---------------------------------------------------------------- Funding
fu = sheet('Funding')
fu.column_dimensions['A'].width = 2; fu.column_dimensions['B'].width = 46; fu.column_dimensions['C'].width = 14; fu.column_dimensions['D'].width = 70
put(fu, 'B1', 'FUNDING - sources & uses at closing (Sept 14, 2018) and timeline', f_t)
put(fu, 'B2', 'All financing items are ASSUMPTIONS (no commitment exists in the case). The bank is NOT on the critical path.', f_note)
hdr(fu, 4, 2, ['Uses', '$M', 'Note'])
U = [('Purchase price (bid)', '=Bid', 'Whole package, all cash'),
     ('Less: closing credit (Jan-Jun 2018 receipts held by seller)', f'=-{credit_ref(0)}', 'Only proceeds actually received by closing (~60-day lag)'),
     ('Transaction costs', '=TxnCost', 'Legal, title, engineering'),
     ('Liquidity reserve', '=LiqRes', 'Hurricane season'),
     ]
for i, (a, b_, c_) in enumerate(U):
    put(fu, f'B{5+i}', a); put(fu, f'C{5+i}', b_, f_link, M0); put(fu, f'D{5+i}', c_, f_note)
put(fu, 'B9', 'Cash needed at closing', f_b); put(fu, 'C9', '=SUM(C5:C8)', fmt=M0, bold=True); fu['C9'].fill = fill_sub
name('CashAtClose', 'Funding!$C$9')
hdr(fu, 11, 2, ['Sources', '$M', 'Note'])
put(fu, 'B12', 'Anchor royalty fund equity (committed, already-raised capital)'); put(fu, 'C12', '=C9*AnchorPct', fmt=M0)
put(fu, 'D12', 'Signed unconditional commitment required by Aug 8, 2018 (our go/no-go gate)', f_note)
put(fu, 'B13', 'Team / sponsor co-invest'); put(fu, 'C13', '=C9*(1-AnchorPct)', fmt=M0)
put(fu, 'B14', 'Total sources', f_b); put(fu, 'C14', '=C12+C13', fmt=M0, bold=True)
put(fu, 'B15', 'Check: sources - uses (must be 0)', f_note); put(fu, 'C15', '=C14-C9', fmt=M0)
put(fu, 'B17', 'Deposit wired at award, Aug 30 (10% of price)'); put(fu, 'C17', '=Bid*DepositPct', fmt=M0)
put(fu, 'B18', 'Commitment headroom for Lucius suspense risk'); put(fu, 'C18', 5.0, f_in, M0)
put(fu, 'B19', 'Equity commitment letter size', f_b); put(fu, 'C19', '=C9+C18', fmt=M0, bold=True)
hdr(fu, 21, 2, ['After closing (optional - not in bid math)', '$M', 'Note'])
put(fu, 'B22', 'Final settlement receipts for Jul-Sep 14 production (Jan 2019)'); put(fu, 'C22', f"=SUMPRODUCT(Engine!{PC[6]}{case_total_row[0]}:{PC[8]}{case_total_row[0]})+Engine!{PC[8]}{case_total_row[0]}*0+0", fmt=M0)
put(fu, 'D22', 'Jul-Sep 2018 production, paid to seller after closing, passed to us at final settlement', f_note)
put(fu, 'B23', 'Royalty-backed term loan (Q1 2019)'); put(fu, 'C23', '=LoanSize', f_link, M0)
put(fu, 'B24', 'Loan rate (prime + spread)'); put(fu, 'C24', '=Prime+LoanSpread', fmt='0.00%')
put(fu, 'D24', 'Prime 5.00% (Aug 15, 2018) + 2.25%; 50-75% of oil hedged ~$60-64 as lender condition', f_note)
put(fu, 'B25', 'Loan as % of cautious PV of 2019+ cash flow @10%'); put(fu, 'C25', f'=C23/SUMPRODUCT(Engine!{PC[12]}{case_total_row[1]}:{LASTC}{case_total_row[1]},1/(1+0.1)^Engine!{PC[12]}{R_EXP}:{LASTC}{R_EXP})', fmt=P1)
put(fu, 'D25', "Must stay under the sponsor's 'loan up to 50%'", f_note)
put(fu, 'B26', 'Net equity at risk after settlement + loan', f_b); put(fu, 'C26', '=C9-C22-C23', fmt=M0, bold=True)
hdr(fu, 28, 2, ['Timeline (2018)', 'Date', 'Action'])
TL = [('Jul 9', 'Bid package issued; sign NDA incl. consent to share with financing sources'), ('Jul 15-31', 'Title + BOEM production diligence (done - this model)'),
      ('Aug 1-10', 'Anchor fund IC #1/#2 on our diligence pack; reserve audit by fund engineer'), ('Aug 8', 'GO/NO-GO: signed unconditional equity commitment'),
      ('Aug 15 4pm', 'Submit $98M + performance payments (fixed alternate $105M) + 19-line allocation + title terms'), ('Aug 30', 'Award; wire 10% deposit'),
      ('Sep 14', 'Close; seller credits Jan-Jun receipts'), ('Jan 2019', 'Final settlement; royalty-backed loan funds; hedges placed')]
for i, (a, b_) in enumerate(TL):
    put(fu, f'B{29+i}', a); put(fu, f'D{29+i}', b_)

# ---------------------------------------------------------------- Allocation
al = sheet('Allocation')
al.column_dimensions['A'].width = 2; al.column_dimensions['B'].width = 20; al.column_dimensions['C'].width = 30
for c in 'DEFG': al.column_dimensions[c].width = 15
al.column_dimensions['H'].width = 60
put(al, 'B1', 'BID ALLOCATION BY INTEREST (Bid Instruction requires allocation by individual interest - 19 lines)', f_t)
put(al, 'B2', 'Producing value allocated by cautious PV share; token values on non-producing interests. Allocated values double as the title-defect remedy schedule.', f_note)
put(al, 'B4', 'Token allocations ($M)', f_b)
put(al, 'B5', 'Pompano MC 72'); put(al, 'D5', 0.1, f_in, M2)
put(al, 'B6', 'Each non-producing Stones block'); put(al, 'D6', 0.1, f_in, M2)
put(al, 'B7', 'Pool allocated by PV share'); put(al, 'D7', '=Bid-D5-7*D6', fmt=M2)
hdr(al, 9, 2, ['Property', 'Interest', 'Attachment A net ORRI', 'Split within property', 'Allocated $M', 'Fact/Assump.', 'Basis'])
ALLOC = [('Kodiak', 'MC 727 NE/4 & S/2', 0.06375, 0, .84, 'Producing well bottomed on MC 727; MC 771 could contract out of unit ~2019'),
         ('Kodiak', 'MC 771', 0.06375, 0, .16, ''),
         ('Lucius', 'KC 875', 0.02, 1, 46.67 / (46.67 + 24.77), 'Unit tract factor 46.67% (Exhibit C)'),
         ('Lucius', 'KC 874', 0.02, 1, 24.77 / (46.67 + 24.77), 'Unit tract factor 24.77%; creating instrument missing'),
         ('Stones', 'WR 508', 0.015, 2, 1.0, 'Only producing Stones lease'),
         ] + [('Stones', f'WR {b}', 0.015, None, None, 'Non-producing; risk of contraction ~2021') for b in (507, 509, 551, 552, 553, 596, 597)] + [
         ('South Santa Cruz', 'MC 563', 0.0093, 3, 1.0, ''),
         ('Grand Isle 116 unit', 'GI 116', 0.005, 4, .8073, 'True tract factor 80.73% (unit agreement)'),
         ('Grand Isle 116 unit', 'GI 110', 0.005, 4, .1927, 'Tract factor 19.27%'),
         ('Main Pass 59', 'MP 59 S/2 & NE/4', 0.02604167, 5, 1.0, '$750k production payment payout unverified'),
         ('Ship Shoal 219', 'SS 219', 0.08, 6, 1.0, 'Valued at 4% (8% of Amoco 50%); 8% = upside'),
         ('Orion', 'MC 110', 0.013125, 7, 1.0, 'Lease likely lapses ~2019'),
         ('Pompano', 'MC 72 S/2 & S/2 S/2 N/2', 0.05625, None, None, 'No ORRI-area production since Oct-2014; WoodMac "Pompano" is a different field')]
for i, (p, it, dec, pi, split, note) in enumerate(ALLOC):
    r_ = 10 + i
    put(al, f'B{r_}', p); put(al, f'C{r_}', it); put(al, f'D{r_}', dec, f_in, '0.00000000')
    if pi is None:
        put(al, f'E{r_}', '-'); put(al, f'F{r_}', '=$D$5' if p == 'Pompano' else '=$D$6', fmt=M2)
    else:
        put(al, f'E{r_}', split, f_in, P1)
        put(al, f'F{r_}', f'=$D$7*Valuation!$E${PP0+pi}*E{r_}', fmt=M2)
    put(al, f'G{r_}', 'Fact (decimal)'); put(al, f'H{r_}', note, f_note)
AL1 = 10 + len(ALLOC) - 1
put(al, f'B{AL1+1}', 'TOTAL (must equal bid)', f_b); put(al, f'F{AL1+1}', f'=SUM(F10:F{AL1})', fmt=M2, bold=True)
put(al, f'B{AL1+2}', 'Check', f_note); put(al, f'F{AL1+2}', f'=F{AL1+1}-Bid', fmt=M2)

# ---------------------------------------------------------------- 2017 check
ck = sheet('Check_2017')
ck.column_dimensions['A'].width = 2; ck.column_dimensions['B'].width = 26; ck.column_dimensions['C'].width = 22
for c in 'DEFGHIJ': ck.column_dimensions[c].width = 13
put(ck, 'B1', "2017 CROSS-CHECK - rebuild the seller's '$20.4M 2017 net revenue' from public BOEM volumes", f_t)
put(ck, 'B2', "2017 basis: Lucius was NOT yet unitised, so the ORRI applied to production located on KC 874/875 only. Independent check, not a calibration proof.", f_note)
put(ck, 'B4', 'Deepwater oil 2017 ($/bbl, Mars)'); put(ck, 'C4', 51.5, f_in, M2)
put(ck, 'B5', 'Shelf oil 2017 ($/bbl, LLS)'); put(ck, 'C5', 54.0, f_in, M2)
put(ck, 'B6', 'Henry Hub 2017 ($/MMBtu)'); put(ck, 'C6', 2.99, f_in, M2)
hdr(ck, 8, 2, ['Property', 'Leases (2017 basis)', '2017 oil (bbl)', '2017 gas (mcf)', 'ORRI share', 'Oil price', 'Gross ORRI $M', 'Net of deductions $M'])
CK = [('Kodiak', ['G24102', 'G24107'], 0.06375, 'D'), ('Lucius (lease basis)', ['G26771', 'G21444'], 0.02, 'D'), ('Stones', ['G17001'], 0.015, 'D'),
      ('South Santa Cruz', ['G21176'], 0.0093, 'D'), ('Orion', ['G18192'], 0.013125, 'D'), ('Grand Isle 116', ['G13943', 'G13944'], 0.005, 'S'),
      ('Main Pass 59', ['G03194'], 0.02604167, 'S'), ('Ship Shoal 219 (at 8%)', ['00829'], 0.08, 'S')]
for i, (p, ls, s, kind) in enumerate(CK):
    r_ = 9 + i
    put(ck, f'B{r_}', p); put(ck, f'C{r_}', ', '.join(ls))
    put(ck, f'D{r_}', '=' + '+'.join(f'SUMIFS(BD_Oil,BD_Lease,"{l}",BD_Ym,">=201701",BD_Ym,"<=201712")' for l in ls), fmt=N0)
    put(ck, f'E{r_}', '=' + '+'.join(f'SUMIFS(BD_Gas,BD_Lease,"{l}",BD_Ym,">=201701",BD_Ym,"<=201712")' for l in ls), fmt=N0)
    put(ck, f'F{r_}', s, f_in, '0.0000%'); put(ck, f'G{r_}', '=$C$4' if kind == 'D' else '=$C$5', fmt=M2)
    put(ck, f'H{r_}', f'=(D{r_}*F{r_}*G{r_}+E{r_}*F{r_}*$C$6*GasMult)/1000000', fmt=M2)
    put(ck, f'I{r_}', f'=(D{r_}*F{r_}*(G{r_}-OilDed)+E{r_}*F{r_}*($C$6*GasMult-GasDed))/1000000', fmt=M2)
r_ = 9 + len(CK)
put(ck, f'B{r_}', 'Pompano'); put(ck, f'C{r_}', 'G08483 (outside ORRI area)'); put(ck, f'H{r_}', 0, fmt=M2); put(ck, f'I{r_}', 0, fmt=M2)
r_ += 1
put(ck, f'B{r_}', 'TOTAL', f_b); put(ck, f'H{r_}', f'=SUM(H9:H{r_-1})', fmt=M2, bold=True); put(ck, f'I{r_}', f'=SUM(I9:I{r_-1})', fmt=M2, bold=True)
CKT = r_
put(ck, f'B{r_+1}', "Seller's listing: 2017 net revenue (Hart Energy listing)"); put(ck, f'H{r_+1}', 20.4, f_in, M2); put(ck, f'I{r_+1}', 20.4, f_in, M2)
put(ck, f'B{r_+2}', 'Difference vs listing', f_b); put(ck, f'H{r_+2}', f'=H{r_}/H{r_+1}-1', fmt=P1); put(ck, f'I{r_+2}', f'=I{r_}/I{r_+1}-1', fmt=P1)
put(ck, f'B{r_+4}', 'Reading: gross (no deductions) lands ~7% above the listing; deductions are our assumption and close the gap. 2017 is NOT the run-rate:', f_note)
put(ck, f'B{r_+5}', 'Kodiak was offline Jun-17 to Feb-18 (~$8M lost) and Lucius unitisation from Jan-18 roughly doubles the ORRI share of Lucius output.', f_note)

# ---------------------------------------------------------------- Title_Shares
ti = sheet('Title_Shares')
ti.column_dimensions['A'].width = 2
for c, w in zip('BCDEFGHI', [18, 24, 12, 16, 46, 18, 44, 10]): ti.column_dimensions[c].width = w
put(ti, 'B1', 'TITLE & SHARES - what each interest really pays (verified against source documents)', f_t)
hdr(ti, 3, 2, ['Property', 'Interest', 'Attachment A', 'Share of gross production used', 'Basis / trap', 'Depth limit', 'Source (case folder)', 'Confidence'])
TI = [('Kodiak', 'MC 727 + MC 771', '0.06375 each', '6.375% of unit', 'Already net (10% x 63.75%). Do NOT add the two lines. 260-day outage Jun-17 to Feb-18 -> lease-continuity question', '17,500-99,999 ft', 'Kodiak/SourceDocs/5. ABOS KODIAK.pdf p3, p10', 'High'),
      ('Lucius', 'KC 874 + KC 875', '0.02 each', '1.4288% of unit', 'Trap: 2%+2% = 4% is wrong. Each 2% burdens only its tract: 2% x (24.77%+46.67%). Unit effective 1/1/2018 -> Jan-May true-up owed to buyer', 'None', 'Lucius/SourceDocs/BSEE-Approved-UnitAgreement.pdf p25 (Exh. C)', 'High (875) / Med (874)'),
      ('Stones', 'WR 507-597 (8 blocks)', '0.015', '1.5% of WR 508', 'Only WR 508 produces. Royalty-relief lease and ORRI "calculated in same manner as Lessor royalty" -> payment risk', 'None', 'Stones/SourceDocs WR 508 assignment p5-6', 'High / Med'),
      ('South Santa Cruz', 'MC 563', '0.0093', '0.93%', '2% x 46.5%. No BOEM filing stamp seen', 'Surface-19,000 ft', 'SoSantaCruz/SourceDocs/3. MC 563 ASSIGNMENT.pdf', 'High / Med'),
      ('Grand Isle 116', 'GI 110 + GI 116', '0.005 each', '0.5% of unit (deep)', 'Only below 13,000 ft; true tract split 19.27/80.73 (WoodMac shows 64/36). Operator Fieldwood post-Ch.11', 'Below 13,000 ft', 'GrandIsle/SourceDocs/5. ORRI ASSIGNMENT p3', 'Med'),
      ('Main Pass 59', 'MP 59 S/2 & NE/4', '0.02604167', '2.604%', '5/192; $750k production payment payout unverified; unit allocation with G08461 unknown', '-', 'MainPass/SourceDocs/3. MP 59 ORRI ASSIGNMENT.pdf p4-5', 'Med / Low'),
      ('Ship Shoal 219', 'SS 219', '0.08', '4% (8% upside)', 'Trap: Amoco reserved 8% from its own 50% -> 4% of 8/8', '-', 'ShipShoal/SourceDocs/3. SS 219 ORRI ASSIGNMENT.pdf p3, p8', 'Med'),
      ('Orion', 'MC 110', '0.013125', '1.3125%', 'Small, declining; lease likely lapses ~2019', '-', 'Orion/SourceDocs/3. ORRI ABOS p16', 'High'),
      ('Pompano', 'MC 72 S/2 & S/2 S/2 N/2', '0.05625', '~0 (no ORRI-area production)', 'Trap: WoodMac "Pompano" is a different field/blocks. ORRI covers only LLOG/Nexen-assignee production to 13,405 ft', 'Surface-13,405 ft', 'Pompano/SourceDocs/3. MC 72 Assignment pp6-7', 'High')]
for i, row in enumerate(TI):
    for k, v in enumerate(row):
        c = ti.cell(row=4 + i, column=2 + k, value=v); c.font = f_norm; c.alignment = Alignment(wrap_text=True, vertical='top')
    ti.row_dimensions[4 + i].height = 48
put(ti, 'B14', 'Package-wide gaps: Amoco->BP vesting, KC 874 creating instrument, MP 1979 letter, LLOG 2007 farmout, SSC 2014 agreement, WR 551 missing page. Two seller entities (BP America Production Co. and BP E&P Inc.) must both sign.', f_note)

# ---------------------------------------------------------------- Sources & facts ledger
so = sheet('Facts_vs_Assumptions')
so.column_dimensions['A'].width = 2; so.column_dimensions['B'].width = 60; so.column_dimensions['C'].width = 16; so.column_dimensions['D'].width = 60
put(so, 'B1', 'FACTS vs ASSUMPTIONS LEDGER  (and what we deliberately excluded as hindsight)', f_t)
hdr(so, 3, 2, ['Item', 'Type', 'Source / why'])
LED = [('ORRI decimals per interest (Attachment A)', 'Fact', 'PurchasePriceAllocation.pdf'),
       ('Lucius unit tract factors 24.77 / 46.67 / 10.39 / 18.17%', 'Fact', 'BSEE-approved unit agreement, Exhibit C'),
       ('Monthly production Jan-2015 to May-2018 by lease', 'Fact', 'BOEM OGOR-A, public by Aug 15, 2018'),
       ('NYMEX strip and prime rate 5.00% on Aug 15, 2018', 'Fact', 'CME settlements; WSJ prime'),
       ('Closing credit = Jan-Jun 2018 receipts', 'Assumption', '~60-day payment lag; standard PSA settlement'),
       ('Decline rates, uptime, economic limits', 'Assumption', 'Set from public monthly data (judgement); two views shown'),
       ('Stones restarts Sep-2018', 'Assumption', 'Cause of Mar-May shut-in unknown at Aug 15 -> ask seller'),
       ('Ship Shoal at 4% (not 8%)', 'Assumption', 'Our reading of the assignment; seller represents 8%'),
       ('Anchor equity commitment by Aug 8', 'Assumption', 'Go/no-go gate; no commitment exists in the case'),
       ('Post-close loan $25-30M at prime + 2.25%', 'Assumption', 'Capital-markets panel; optional, not in bid math'),
       ('EXCLUDED: Jun-Dec 2018 BOEM months', 'Hindsight', 'Not public by Aug 15, 2018'),
       ('EXCLUDED: 2019 Lucius filing (79187.pdf) in the data room', 'Hindsight', 'Dated July 2019'),
       ('EXCLUDED: any later ownership/sale information about these ORRIs', 'Hindsight', 'Post-2018'),
       ('EXCLUDED: later filings showing different Kodiak depth range', 'Hindsight', 'Post-2018; data-room document governs'),
       ('EXCLUDED: Fed Sept-2018 hike and any post-Aug-15 market commentary', 'Hindsight', 'After bid date'),
       ("Case's 'production workbook' not in our folder", 'Note', 'Replaced by public BOEM data + WoodMac PDFs')]
for i, (a, b_, c_) in enumerate(LED):
    put(so, f'B{4+i}', a); put(so, f'C{4+i}', b_, fill=fill_fact if b_ == 'Fact' else (fill_ass if b_ == 'Assumption' else None)); put(so, f'D{4+i}', c_)

# ---------------------------------------------------------------- AI log
ai = sheet('AI_Log')
ai.column_dimensions['A'].width = 2
for c, w in zip('BCDE', [34, 50, 50, 40]): ai.column_dimensions[c].width = w
put(ai, 'B1', 'AI USE LOG - what AI did, how we checked it, where it was wrong', f_t)
hdr(ai, 3, 2, ['Task', 'What the AI said / did', 'How we checked', 'Outcome'])
AIL = [('Read 60+ title PDFs', 'Extracted decimals, depth limits, parties', 'Re-read key pages ourselves (Lucius Exh. C, Kodiak ABOS, SS 219)', 'Kept, with page citations'),
       ('Lucius share', 'Said the ORRI is 4% (2% + 2%)', 'Unit Exhibit C tract factors', 'CORRECTED to 1.4288% - value 2.8x lower'),
       ('Pompano', "Applied the 5.625% ORRI to WoodMac's 'Pompano' field (~$71M)", 'Read the MC 72 assignment; checked BOEM by lease', 'CORRECTED to ~$0 (different field)'),
       ('First valuation', "Used seller's WoodMac forecast, risked (~$220M+)", 'Compared WoodMac 2018 with BOEM Jan-May 2018 actuals', 'CORRECTED - forecast running hot; base = existing wells'),
       ('Our own model', 'Closing credit $29M; loan $45M; 2017 rebuild printed $28.9M', '6 independent AI reviewer agents + our recomputation', 'CORRECTED: credit $17.5M, loan $25-30M, 2017 = lease basis'),
       ('Kodiak decline', '22%/yr exponential', 'Plotted 2016-18 monthly data ourselves', 'CORRECTED: shown as cautious 35% view vs 22% operator view')]
for i, row in enumerate(AIL):
    for k, v in enumerate(row):
        c = ai.cell(row=4 + i, column=2 + k, value=v); c.font = f_norm; c.alignment = Alignment(wrap_text=True, vertical='top')
    ai.row_dimensions[4 + i].height = 36

# ---------------------------------------------------------------- Dashboard
d = dash
d.column_dimensions['A'].width = 2; d.column_dimensions['B'].width = 46
for c in 'CDEFGHI': d.column_dimensions[c].width = 15
put(d, 'B1', 'BID OR WALK AWAY? - GoM ORRI package (19 interests, 9 platforms) - decision as of Aug 15, 2018', f_t)
put(d, 'B2', 'Change any blue cell in Inputs or Cases (column C = live case) and every number here recalculates.', f_note)
put(d, 'B4', 'RECOMMENDATION', f_b)
put(d, 'B5', '=IF(Bid<=WalkAway,"BID $"&TEXT(Bid,"0")&"M cash + up to $24M paid only if BOEM data proves Kodiak/new wells; fixed-price ceiling $"&TEXT(WalkAway,"0")&"M","CHECK: bid exceeds walk-away")', f_b)
d['B5'].fill = fill_key
put(d, 'B6', 'Gate: signed unconditional equity commitment by Aug 8, 2018 - otherwise walk away (no unfunded bid).', f_norm)
hdr(d, 8, 2, ['Key number', 'Cautious view', 'Operator-trend view', 'Live case'])
KN = [('PV of existing wells @12% ($M)', f'=Valuation!D{VROW[1]}', f'=Valuation!D{VROW[2]}', f'=Valuation!D{VROW[0]}', M0),
      ('PV of existing wells @15% ($M)', f'=Valuation!E{VROW[1]}', f'=Valuation!E{VROW[2]}', f'=Valuation!E{VROW[0]}', M0),
      ('IRR at cash price, before performance payments', f'=Returns!C{MOIC_ROW[1]}', f'=Returns!C{MOIC_ROW[2]}', f'=Returns!C{MOIC_ROW[0]}', P1),
      ('IRR at bid with $45 oil', f'=Returns!C{MOIC_ROW[3]}', f'=Returns!C{MOIC_ROW[4]}', '', P1),
      ('MOIC at bid', f'=Returns!D{MOIC_ROW[1]}', f'=Returns!D{MOIC_ROW[2]}', f'=Returns!D{MOIC_ROW[0]}', '0.00x'),
      ('Undiscounted profit at bid ($M)', f'=Returns!E{MOIC_ROW[1]}', f'=Returns!E{MOIC_ROW[2]}', f'=Returns!E{MOIC_ROW[0]}', M0),
      ('Closing credit, Jan-Jun 2018 receipts ($M)', f'=Valuation!G{VROW[1]}', f'=Valuation!G{VROW[2]}', f'=Valuation!G{VROW[0]}', M0),
      ('Cash needed at closing ($M, live case)', '', '', '=CashAtClose', M0),
      ('Risked drilling upside @12% - NOT paid for ($M)', '=UpsideRisked', '=UpsideRisked', '=UpsideRisked', M0),
      ('Monte Carlo P50 value @12% ($M, cautious mechanics)', f'=Valuation!D{MCROW}', '', '', M0)]
for i, (a, b_, c_, e_, fmt) in enumerate(KN):
    r_ = 9 + i
    put(d, f'B{r_}', a); put(d, f'C{r_}', b_, f_link, fmt); put(d, f'D{r_}', c_, f_link, fmt); put(d, f'E{r_}', e_, f_link, fmt)
put(d, 'B20', 'Why $98M: below base-case value at 12% (~$102M) -> ~15% IRR. Kodiak upside is paid only when BOEM data shows it. Performance payments: Kodiak 2019/20/21 oil >= 11.0/8.5/6.5 kb/d & WTI >= $55 ($5M each); Kodiak 2nd well ($5M); Stones new well ($4M).', f_note)
# IRR vs bid chart data
put(d, 'B22', 'IRR vs bid (existing wells only)', f_b)
hdr(d, 23, 2, ['Bid ($M)', 'Cautious - strip', 'Operator - strip', 'Cautious - $45 oil', 'Kodiak fails 2020'])
for k, b in enumerate(BIDS):
    r_ = 24 + k
    put(d, f'B{r_}', b, f_norm, '0')
    for m_, j in enumerate((1, 2, 3, 5)):
        put(d, f'{CL(3+m_)}{r_}', f'=Returns!{CL(3+k)}{IRR_ROW[j]}', f_link, P1)
ch = LineChart(); ch.title = 'Unlevered IRR vs bid'; ch.y_axis.title = 'IRR'; ch.x_axis.title = 'Bid ($M)'
ch.y_axis.number_format = '0%'; ch.height = 7.5; ch.width = 16
ch.add_data(Reference(d, min_col=3, max_col=6, min_row=23, max_row=23 + len(BIDS)), titles_from_data=True)
ch.set_categories(Reference(d, min_col=2, min_row=24, max_row=23 + len(BIDS)))
d.add_chart(ch, 'G4')
bc = BarChart(); bc.type = 'bar'; bc.title = 'PV @12% by property ($M)'; bc.height = 7.5; bc.width = 16
bc.add_data(Reference(va, min_col=3, max_col=4, min_row=PP0 - 1, max_row=PP0 + 7), titles_from_data=True)
bc.set_categories(Reference(va, min_col=2, min_row=PP0, max_row=PP0 + 7))
d.add_chart(bc, 'G21')

for ws in wb.worksheets:
    for row in ws.iter_rows():
        for c in row:
            if c.font is None or c.font.name != F:
                c.font = Font(name=F, size=c.font.size if c.font else 10, bold=c.font.bold if c.font else False,
                              italic=c.font.italic if c.font else False, color=c.font.color if c.font else None)
wb.calculation.fullCalcOnLoad = True
wb.save(OUT)
print('wrote', OUT)
