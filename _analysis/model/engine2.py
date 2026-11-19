"""Actuals-anchored (BOEM) ORRI valuation. Valuation date 2018-08-15; effective date 2018-01-01; closing 2018-09-14.
Base = existing wells only (PDP), per case rule 'cannot assume when drilling will happen'. Drilling = separate upside layer."""
import csv, sys, collections, calendar, itertools
S = sys.argv[1] if len(sys.argv) > 1 else '.'
rows = list(csv.DictReader(open(S + '/boem/monthly_by_lease.csv')))
PMAP = {'Kodiak':'Kodiak','Lucius':'Lucius','Stones':'Stones','South Santa Cruz':'SoSantaCruz','Grand Isle 116 unit':'GrandIsle',
        'Main Pass 59':'MainPass','Ship Shoal 219':'ShipShoal','Orion':'Orion'}
mon = collections.defaultdict(lambda: [0.0, 0.0])
for r in rows:
    p = PMAP.get(r['property'])
    if not p: continue   # excludes WR464, G08461, Pompano (no ORRI-area production since 2014)
    mon[(p, r['yyyymm'])][0] += float(r['oil_bbl']) + float(r['condensate_bbl'])
    mon[(p, r['yyyymm'])][1] += float(r['gas_mcf'])
SHARE = {'Kodiak':0.06375,'Lucius':0.014288,'Stones':0.015,'SoSantaCruz':0.0093,'GrandIsle':0.005,
         'MainPass':0.02604167,'ShipShoal':0.08,'Orion':0.013125,'Pompano':0.0}
# Forecast for Jun-Dec 2018 gross rate (kb/d, mmcf/d) and annual decline thereafter (existing wells only)
PDP = {  # rate_jun_dec18 oil, gas, decline/yr, life_end_year
 'Kodiak':     (16.0, 13.0, 0.22, 2035),   # Mar-May18 avg 16.9/14.0; single HPHT well
 'Lucius':     (30.0, 29.0, 0.25, 2040),   # Jan-May18 36.8, Apr 34.7, May 19.4; 2017-18 decline ~35%
 'Stones':     (20.0,  3.0, 0.20, 2040),   # Jan-Feb18 25.8; shut-in Mar-May; assume Jul restart -> Jun-Dec avg ~ 20
 'SoSantaCruz':( 3.4,  1.8, 0.15, 2035),
 'GrandIsle':  ( 1.5, 18.5, 0.18, 2030),
 'MainPass':   ( 0.35, 1.6, 0.10, 2032),
 'ShipShoal':  ( 0.6,  2.8, 0.20, 2025),
 'Orion':      ( 0.4,  0.0, 0.20, 2022),
}
WTI = {2017:50.8, 2018:66.5, 2019:64.5, 2020:61.0, 2021:58.5, 2022:57.0}
HH  = {2017:2.99, 2018:2.95, 2019:2.82, 2020:2.66, 2021:2.65, 2022:2.65}
def deck(y, kind):
    if kind == 'strip':  return WTI.get(y, 57.0), HH.get(y, 2.65)
    if kind == 'low':    return (WTI[y] if y <= 2018 else 45.0), (HH[y] if y <= 2018 else 2.25)
    if kind == 'high':   return (WTI[y] if y <= 2018 else 75.0*1.02**(y-2019)), (HH[y] if y <= 2018 else 3.25)
    if kind == 'flat50': return (WTI[y] if y <= 2018 else 50.0), (HH[y] if y <= 2018 else 2.50)
OIL_ADJ, OIL_DED, GAS_MULT, GAS_DED = 0.7, 3.0, 1.10, 0.40   # calibrated to Hart's $20.4M 2017 net revenue
def annual_gross(p, y, cfg):
    """gross field bbl, mcf for year y (actual months Jan-May 2018; forecast after)."""
    o0, g0, dec, end = PDP[p]
    dec = dec * cfg.get('decl_mult', 1.0)
    if y == 2017:
        return tuple(sum(mon[(p, f'2017{m:02d}')][i] for m in range(1, 13)) for i in (0, 1))
    if y > end: return 0.0, 0.0
    if y == 2018:
        a = [sum(mon[(p, f'2018{m:02d}')][i] for m in range(1, 6)) for i in (0, 1)]
        d = 214  # Jun-Dec
        return a[0] + o0*1000*d, a[1] + g0*1000*d
    # mid-year rate after decline from Jun-Dec 2018 level
    f = (1 - dec) ** (y - 2018)
    days = 366 if calendar.isleap(y) else 365
    return o0*1000*days*f, g0*1000*days*f
def run(rate=0.12, kind='strip', horizon=2032, hurricane=0.02, cfg=None, share=None, upside=0.0, detail=False):
    cfg = cfg or {}; share = dict(SHARE, **(share or {}))
    res = {}; cfy = collections.defaultdict(float)
    for p in PDP:
        pv = 0.0
        for y in range(2018, horizon + 1):
            o, g = annual_gross(p, y, cfg)
            wti, hh = deck(y, kind)
            rev = (o*share[p]*(wti + OIL_ADJ - OIL_DED) + g*share[p]*(hh*GAS_MULT - GAS_DED)) / 1e6
            rev *= (1 - hurricane) if y > 2018 else 1.0
            rev *= (1 - cfg.get('haircut', {}).get(p, 0.0))
            rev += upside * UPSIDE.get(p, {}).get(y, 0.0)
            cfy[y] += rev
            # timing: 2018 Jan-Sep14 (~70%) arrives as closing credit at t=0.08; rest mid-Nov t=0.25; later years mid-year
            df = (0.70/(1+rate)**0.08 + 0.30/(1+rate)**0.25) if y == 2018 else 1/(1+rate)**(y - 2018 + 0.5 - 0.62)
            pv += rev * df
        res[p] = pv
    res['TOTAL'] = sum(res.values())
    return (res, dict(cfy)) if detail else res
def rev2017():
    t = {}
    for p in PDP:
        o, g = annual_gross(p, 2017, {}); wti, hh = deck(2017, 'strip')
        t[p] = (o*SHARE[p]*(wti+OIL_ADJ-OIL_DED) + g*SHARE[p]*(hh*GAS_MULT-GAS_DED))/1e6
    return t
# Drilling upside layer ($M ORRI revenue/yr, unrisked) = WoodMac-implied incremental vs PDP, filled in later
UPSIDE = {}
if __name__ == '__main__':
    r17 = rev2017(); print('2017 calibration ($M):', {k: round(v, 2) for k, v in r17.items()}, 'TOTAL', round(sum(r17.values()), 2))
    hdr = list(PDP) + ['TOTAL']
    print(f"{'case':34s}" + ''.join(f'{h[:8]:>9s}' for h in hdr))
    def show(lbl, d): print(f'{lbl:34s}' + ''.join(f'{d[h]:9.1f}' for h in hdr))
    for r in (0.10, 0.12, 0.15, 0.20): show(f'PDP strip {int(r*100)}%', run(r))
    for k in ('low', 'flat50', 'high'): show(f'PDP {k} 12%', run(0.12, k))
    show('PDP strip 12% decline x1.3', run(0.12, cfg={'decl_mult': 1.3}))
    show('PDP strip 12% decline x0.7', run(0.12, cfg={'decl_mult': 0.7}))
    show('PDP strip 12% SS at 4%', run(0.12, share={'ShipShoal': 0.04}))
    show('PDP strip 12% horizon 2027 (10y)', run(0.12, horizon=2027))
    show('PDP strip 12% horizon 2040', run(0.12, horizon=2040))
    show('PDP strip 12% no hurricane', run(0.12, hurricane=0))
    show('PDP strip 12% hurricane 5%', run(0.12, hurricane=0.05))
    res, cf = run(0.12, detail=True)
    print('Annual package ORRI revenue ($M, PDP strip):', {y: round(v, 1) for y, v in cf.items()})
