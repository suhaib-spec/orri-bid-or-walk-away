import os, sys; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import analysis_dir, load_script, irr as _irr
S = analysis_dir()
e1 = load_script('engine', 'model/engine.py', S); e2 = load_script('engine2', 'model/engine2.py', S)
# Upside layer = WoodMac-profile revenue (strip prices, no haircuts) minus PDP revenue, floored at 0
_, wm = e1.value(0.12, detail=True, hurricane=0.0)
up = {}
for p in ['Kodiak','Lucius','Stones','SoSantaCruz']:
    up[p] = {}
    for y in range(2019, 2033):
        o, g = e2.annual_gross(p, y, {}); wti, hh = e2.deck(y, 'strip'); sh = e2.SHARE[p]
        pdp = (o*sh*(wti+e2.OIL_ADJ-e2.OIL_DED) + g*sh*(hh*e2.GAS_MULT-e2.GAS_DED))/1e6
        up[p][y] = max(0.0, wm[p].get(y, 0.0) - pdp)
e2.UPSIDE = up
print('Unrisked drilling upside $M/yr by property (2019-2024):')
for p in up: print(f'  {p:12s}', [round(up[p][y],1) for y in range(2019,2025)], 'sum2019-32', round(sum(up[p].values()),1))
hdr = ['Kodiak','Lucius','Stones','SoSantaCruz','TOTAL']
for u in (0.0, 0.25, 0.5, 1.0):
    for r in (0.12, 0.15):
        res = e2.run(r, upside=u); print(f'PDP + {int(u*100)}% of drilling upside @{int(r*100)}%:', {k: round(res[k],1) for k in hdr})
def irr(cfs):
    return _irr(cfs, -0.9, 3.0)
def deal(bid, upside=0.0, kind='strip', cfg=None, horizon=2032):
    _, cf = e2.run(0.12, kind=kind, upside=upside, cfg=cfg, horizon=horizon, detail=True)
    credit = 0.70*cf[2018]
    flows = [(0.0, -bid + credit), (0.17, 0.30*cf[2018])] + [(y-2018+0.5-0.71, cf[y]) for y in range(2019, horizon+1)]
    tot = sum(c for _, c in flows[1:]) + credit
    # payback
    cum = -bid; pb = None
    for t, c in [(0.0, credit)] + flows[1:]:
        cum += c
        if cum >= 0 and pb is None: pb = t
    return irr(flows), tot/bid, pb, bid - credit
print('\nBid  | cash@close | IRR PDP | MOIC PDP | payback | IRR PDP+25%up | IRR low-price | IRR steep decline')
for bid in (90, 100, 110, 120, 130, 140, 150):
    a = deal(bid); b = deal(bid, 0.25); c = deal(bid, kind='low'); d = deal(bid, cfg={'decl_mult':1.3})
    print(f'{bid:4d} | {a[3]:9.1f} | {a[0]*100:6.1f}% | {a[1]:6.2f}x | {a[2]:5.1f}y | {b[0]*100:6.1f}% | {c[0]*100:6.1f}% | {d[0]*100:6.1f}%')
