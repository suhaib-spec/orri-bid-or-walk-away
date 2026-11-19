"""Final IRR grid: bids vs cautious (panel engineer) and team (memo) production cases, auditor mechanics.
Ship Shoal at 4%. t=0 at closing; Jan-Jun 2018 receipts credited at closing. Run: python -I final_irr.py [<_analysis>]"""
import os, sys; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'model'))
from common import analysis_dir, load_script, irr as _irr
S = analysis_dir()
rr = load_script('rr', 'panel/scripts/reserves_rebuttal.py', S)
rr.rp.SHARE['ShipShoal'] = 0.04
def irr(cf):
    return _irr(cf, -0.5, 2.0)
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
