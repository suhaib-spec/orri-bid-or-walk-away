"""Final IRR grid: bids vs cautious (panel engineer) and team (memo) production cases, auditor mechanics.
Ship Shoal at 4%. t=0 at closing; Jan-Jun 2018 receipts credited at closing. Run: python -I final_irr.py <_analysis>"""
import sys, importlib.util
S = sys.argv[1]
sp = importlib.util.spec_from_file_location('rr', S + '/panel/scripts/reserves_rebuttal.py')
sys.argv = [sys.argv[0], S]; rr = importlib.util.module_from_spec(sp); sp.loader.exec_module(rr)
rr.rp.SHARE['ShipShoal'] = 0.04
def irr(cf):
    lo, hi = -0.5, 2.0
    for _ in range(200):
        m = (lo + hi) / 2
        npv = sum(v / (1 + m) ** t for t, v in cf)
        lo, hi = (m, hi) if npv > 0 else (lo, m)
    return m
def cfs(F, bid):
    cf = [(0.0, -bid)]
    for fl in F.values():
        for t, v in fl: cf.append((max(t - rr.T_CLOSE, 0.0), v))
    return cf
cases = {'cautious strip': rr.flows(rr.P), 'cautious $45oil': rr.flows(rr.P, kind='low'),
         'cautious Kodiak fails 2020': rr.flows(rr.P, kodiak_fail_year=2020),
         'team strip': rr.flows(rr.M), 'team $45oil': rr.flows(rr.M, kind='low')}
print('PV12/PV15:', {k: (round(rr.total(F, .12), 1), round(rr.total(F, .15), 1)) for k, F in cases.items()})
cred = {k: round(sum(v for fl in F.values() for t, v in fl if t <= rr.T_CLOSE), 1) for k, F in cases.items()}
print('closing credit:', cred)
for bid in (100, 105, 110, 115, 120, 125):
    print(bid, ' '.join(f'{k}={irr(cfs(F, bid))*100:5.1f}%' for k, F in cases.items()))
