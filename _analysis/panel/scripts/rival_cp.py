import os, sys; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'model'))
from common import analysis_dir, load_script, irr as _irr
A = analysis_dir()
rr = load_script('rr', 'panel/scripts/reserves_rebuttal.py', A)
rr.rp.SHARE['ShipShoal'] = 0.04
def irr(cf):
    return _irr(cf, -0.5, 2.0)
def kod_rates(P, fail=None):
    c = P['Kodiak']; out = {}
    for y in (2019, 2020, 2021):
        q = c['q18']*rr.rp.frac(c['De'], c['b'], y-2018-rr.ANCH)*c['up']
        if fail and y >= fail: q = 0
        out[y] = q
    return out
TRIG = {2019: 11.0, 2020: 8.5, 2021: 6.5}; PAY = 5.0
def run(cash, P, kind='strip', fail=None, cp=True):
    F = rr.flows(P, kind=kind, kodiak_fail_year=fail) if fail else rr.flows(P, kind=kind)
    cf = [(0.0, -cash)]
    for fl in F.values():
        for t, v in fl: cf.append((max(t-rr.T_CLOSE, 0.0), v))
    paid = 0
    if cp and kind != 'low':
        for y, q in kod_rates(P, fail).items():
            if q >= TRIG[y]:
                cf.append((y-2018+0.25+1-rr.T_CLOSE, -PAY)); paid += PAY
    return irr(cf)*100, paid, kod_rates(P, fail)
for nm, P in (('cautious', rr.P), ('team', rr.M)):
    print(nm, 'kodiak avg kb/d', {y: round(q, 1) for y, q in kod_rates(P).items()})
for cash in (95, 98, 100, 105):
    row = []
    for lbl, P, kind, fail in (('caut', rr.P, 'strip', None), ('caut45', rr.P, 'low', None), ('cautKdies', rr.P, 'strip', 2020), ('team', rr.M, 'strip', None), ('team45', rr.M, 'low', None)):
        i, paid, _ = run(cash, P, kind, fail); row.append(f'{lbl}={i:5.1f}% (paid {paid:.0f})')
    print(cash, ' | '.join(row))
print('flat 105 check', [round(run(105, P, k, f, cp=False)[0], 1) for P, k, f in ((rr.P,'strip',None),(rr.P,'low',None),(rr.P,'strip',2020),(rr.M,'strip',None),(rr.M,'low',None))])
