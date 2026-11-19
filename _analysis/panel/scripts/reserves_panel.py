"""Reserves-engineer panel re-run (copy-based; does not modify model/engine2.py).
Inputs: only BOEM rows with public_by_2018_08_15 == 'Y' (Jan-2015..May-2018).
Adds: separate Jun-Dec 2018 average vs. decline base rate, hyperbolic decline, availability
(operational uptime beyond hurricanes), economic-limit cut-off, Kodiak single-well failure,
Stones restart timing, and a Monte Carlo for P90/P50/P10.
Run:  python -I panel/scripts/reserves_panel.py <_analysis dir>
"""
import csv, sys, collections, calendar, random, math
S = sys.argv[1] if len(sys.argv) > 1 else '.'
rows = [r for r in csv.DictReader(open(S + '/boem/monthly_by_lease.csv')) if r['public_by_2018_08_15'] == 'Y']
PMAP = {'Kodiak':'Kodiak','Lucius':'Lucius','Stones':'Stones','South Santa Cruz':'SoSantaCruz','Grand Isle 116 unit':'GrandIsle',
        'Main Pass 59':'MainPass','Ship Shoal 219':'ShipShoal','Orion':'Orion'}
mon = collections.defaultdict(lambda: [0.0, 0.0])
for r in rows:
    p = PMAP.get(r['property'])
    if not p: continue
    mon[(p, r['yyyymm'])][0] += float(r['oil_bbl']) + float(r['condensate_bbl'])
    mon[(p, r['yyyymm'])][1] += float(r['gas_mcf'])
SHARE = {'Kodiak':0.06375,'Lucius':0.014288,'Stones':0.015,'SoSantaCruz':0.0093,'GrandIsle':0.005,
         'MainPass':0.02604167,'ShipShoal':0.08,'Orion':0.013125}
WTI = {2018:66.5, 2019:64.5, 2020:61.0, 2021:58.5, 2022:57.0}
HH  = {2018:2.95, 2019:2.82, 2020:2.66, 2021:2.65, 2022:2.65}
OIL_ADJ, OIL_DED, GAS_DED = 0.7, 3.0, 0.40

# Memo/engine2 inputs reproduced as exponential, 2018 avg == base, no uptime, no econ limit
MEMO = {p: dict(q18=o, base=o, gor=g/o if o else 0, g0=g, De=d, b=0.0, end=e, up=1.0, qlim=0.0)
        for p, (o, g, d, e) in {
 'Kodiak':(16.0,13.0,0.22,2035),'Lucius':(30.0,29.0,0.25,2040),'Stones':(20.0,3.0,0.20,2040),
 'SoSantaCruz':(3.4,1.8,0.15,2035),'GrandIsle':(1.5,18.5,0.18,2030),'MainPass':(0.35,1.6,0.10,2032),
 'ShipShoal':(0.6,2.8,0.20,2025),'Orion':(0.4,0.0,0.20,2022)}.items()}

# Panel base (P50). q18 = Jun-Dec 2018 average gross kb/d; base = rate the decline starts from (~Oct-2018);
# De = first-year effective decline; b = Arps exponent; up = availability; qlim = gross oil economic limit kb/d.
PANEL = {
 'Kodiak':      dict(q18=15.0, base=14.5, g0=12.3, De=0.35, b=0.5, end=2035, up=0.90, qlim=1.5),
 'Lucius':      dict(q18=29.0, base=27.0, g0=27.0, De=0.35, b=0.5, end=2040, up=0.97, qlim=3.0),
 'Stones':      dict(q18=12.0, base=23.0, g0=3.3,  De=0.30, b=0.5, end=2040, up=0.95, qlim=5.0),  # restart ~Sep-1 at ~23
 'SoSantaCruz': dict(q18=3.3,  base=3.2,  g0=1.75, De=0.25, b=0.3, end=2035, up=0.95, qlim=0.8),
 'GrandIsle':   dict(q18=1.5,  base=1.45, g0=18.3, De=0.20, b=0.3, end=2030, up=0.97, qlim=0.0),
 'MainPass':    dict(q18=0.35, base=0.35, g0=1.6,  De=0.12, b=0.0, end=2030, up=0.97, qlim=0.0),
 'ShipShoal':   dict(q18=0.6,  base=0.6,  g0=2.7,  De=0.20, b=0.0, end=2025, up=0.97, qlim=0.0),
 'Orion':       dict(q18=0.35, base=0.35, g0=0.0,  De=0.20, b=0.0, end=2022, up=0.97, qlim=0.0),
}

def frac(De, b, t):
    """rate multiplier at time t (yrs) for Arps with first-year effective decline De."""
    if b == 0: return (1 - De) ** t
    Di = ((1 - De) ** (-b) - 1) / b
    return (1 + b * Di * t) ** (-1 / b)

def deck(y, kind, pm=1.0):
    if kind == 'strip': w, h = WTI.get(y, 57.0), HH.get(y, 2.65)
    elif kind == 'low': w, h = (WTI[y], HH[y]) if y <= 2018 else (45.0, 2.25)
    else: raise ValueError
    if y > 2018: w *= pm
    return w, h

def value(P, rate=0.12, kind='strip', horizon=2032, hurricane=0.02, gas_mult=1.10, pm=1.0,
          kodiak_fail_year=None, detail=False):
    res = {}; cfy = collections.defaultdict(float)
    for p, c in P.items():
        pv = 0.0
        ratio = c['g0'] / c['q18'] if c['q18'] else 0.0
        gbase = c['base'] * ratio if c['q18'] else c['g0']
        for y in range(2018, horizon + 1):
            if y == 2018:
                o = sum(mon[(p, f'2018{m:02d}')][0] for m in range(1, 6)) + c['q18'] * 1000 * 214 * (c['up'] if c is not MEMO.get(p) else 1)
                g = sum(mon[(p, f'2018{m:02d}')][1] for m in range(1, 6)) + c['g0'] * 1000 * 214 * (c['up'] if c is not MEMO.get(p) else 1)
            else:
                if y > c['end']: break
                f = frac(c['De'], c['b'], y - 2018)
                q = c['base'] * f
                if q < c['qlim']: break
                if p == 'Kodiak' and kodiak_fail_year and y >= kodiak_fail_year:
                    break
                days = 366 if calendar.isleap(y) else 365
                o = q * 1000 * days * c['up']; g = gbase * f * 1000 * days * c['up']
            w, h = deck(y, kind, pm)
            rev = (o * SHARE[p] * (w + OIL_ADJ - OIL_DED) + g * SHARE[p] * (h * gas_mult - GAS_DED)) / 1e6
            if y > 2018: rev *= (1 - hurricane)
            cfy[y] += rev
            df = (0.70/(1+rate)**0.08 + 0.30/(1+rate)**0.25) if y == 2018 else 1/(1+rate)**(y - 2018 + 0.5 - 0.62)
            pv += rev * df
        res[p] = pv
    res['TOTAL'] = sum(res.values())
    return (res, dict(cfy)) if detail else res

def remaining(P, p, horizon=2040):
    c = P[p]; tot = c['q18'] * 214 / 1000
    for y in range(2019, horizon + 1):
        if y > c['end']: break
        q = c['base'] * frac(c['De'], c['b'], y - 2018)
        if q < c['qlim']: break
        tot += q * 365 / 1000
    return tot  # gross MMbbl Jun-2018 onward, before uptime

def show(lbl, d):
    print(f'{lbl:44s}' + ''.join(f'{d[h]:8.1f}' for h in list(PANEL) + ['TOTAL']))

if __name__ == '__main__':
    print(f"{'case':44s}" + ''.join(f'{h[:7]:>8s}' for h in list(PANEL) + ['TOTAL']))
    for r in (0.12, 0.15): show(f'MEMO reproduction {int(r*100)}%', value(MEMO, r))
    for r in (0.10, 0.12, 0.15, 0.20): show(f'PANEL base {int(r*100)}%', value(PANEL, r))
    show('PANEL base 12% low deck', value(PANEL, 0.12, 'low'))
    show('PANEL base 12% gas_mult 1.0', value(PANEL, 0.12, gas_mult=1.0))
    show('PANEL base 12% hurricane 3%', value(PANEL, 0.12, hurricane=0.03))
    show('PANEL base 12% horizon 2040', value(PANEL, 0.12, horizon=2040))
    # one-at-a-time bridges from memo to panel
    import copy
    for p in ('Kodiak', 'Lucius', 'Stones', 'SoSantaCruz'):
        M = copy.deepcopy(MEMO); M[p] = PANEL[p]
        show(f'MEMO + panel {p} only 12%', value(M, 0.12))
    print('Remaining gross oil Jun-2018+ (MMbbl): memo vs panel')
    for p in ('Kodiak', 'Lucius', 'Stones', 'SoSantaCruz'):
        print(f'  {p:12s} memo {remaining(MEMO, p):6.1f}   panel {remaining(PANEL, p):6.1f}')
    r, cf = value(PANEL, 0.12, detail=True)
    print('PANEL annual ORRI revenue $M:', {y: round(v, 1) for y, v in cf.items()})

    # Monte Carlo (production + price). Triangular / lognormal ranges per property.
    random.seed(7)
    out12, out15, prod12 = [], [], []
    for i in range(10000):
        P = copy.deepcopy(PANEL)
        for p, c in P.items():
            m = random.lognormvariate(0, 0.10)  # rate uncertainty
            c['q18'] *= m; c['base'] *= m; c['g0'] *= m
            c['De'] = min(0.65, max(0.08, c['De'] * random.triangular(0.7, 1.4, 1.0)))
            c['b'] = random.uniform(max(0, c['b'] - 0.3), c['b'] + 0.3) if c['b'] else 0.0
        # Stones restart timing: Jul..Dec 2018 or (10%) not before Jun-2019
        k = random.random()
        if k < 0.10:
            P['Stones']['q18'] = 0.0; P['Stones']['base'] *= 0.75   # delayed restart; crude proxy for lost 2019 H1
        else:
            months_on = random.choice([6, 5, 4, 3, 2])  # restart Jul..Nov
            P['Stones']['q18'] = P['Stones']['base'] * months_on * 30.5 / 214
        # Kodiak single HPHT well: 6%/yr chance of a long failure ending PDP (sidetrack = not PDP)
        fy = None
        for y in range(2019, 2033):
            if random.random() < 0.06: fy = y; break
        pm = random.lognormvariate(0, 0.18)
        out12.append(value(P, 0.12, pm=pm, kodiak_fail_year=fy)['TOTAL'])
        out15.append(value(P, 0.15, pm=pm, kodiak_fail_year=fy)['TOTAL'])
        prod12.append(value(P, 0.12, pm=1.0, kodiak_fail_year=fy)['TOTAL'])
    def pct(a, q): a = sorted(a); return a[int(q * (len(a) - 1))]
    for lbl, a in (('MC 12% (prod+price)', out12), ('MC 15% (prod+price)', out15), ('MC 12% production only, strip', prod12)):
        print(f'{lbl:34s} P90 {pct(a, 0.10):6.1f}  P50 {pct(a, 0.50):6.1f}  P10 {pct(a, 0.90):6.1f}  mean {sum(a)/len(a):6.1f}')
