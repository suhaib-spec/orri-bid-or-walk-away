"""Levered equity returns: bank loan drawn Jan 2019, 75% cash sweep to debt service.
Run: python -I model/levered.py [<_analysis dir>]"""
import os, sys; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import analysis_dir, load_script, irr as _irr

e2 = load_script('e2', 'model/engine2.py', analysis_dir())

RATE = 0.0725      # prime 5.00% + 2.25%
ADVANCE = 0.40     # bank advances 40% of low-price PV10
SWEEP = 0.75       # share of revenue to debt service
T_DRAW = 0.33      # Jan 2019, in years from closing


def irr(cfs):
    return _irr(cfs, -0.9, 5.0)


def levered(bid, kind='strip', cfg=None):
    _, cf = e2.run(0.12, kind=kind, cfg=cfg, detail=True)
    credit = 0.7 * cf[2018]
    equity0 = bid - credit
    loan = ADVANCE * e2.run(0.10, kind='low', cfg=cfg)['TOTAL']
    # loan drawn at T_DRAW and returned to equity; the sweep then services it
    flows = [(0.0, -equity0), (0.17, 0.30 * cf[2018]), (T_DRAW, loan)]
    bal, t_prev, repaid = loan, T_DRAW, None
    for y in range(2019, 2033):
        t = y - 2018 + 0.5 - 0.71
        bal *= (1 + RATE) ** (t - t_prev); t_prev = t
        pay = min(bal, SWEEP * cf[y]); bal -= pay
        if repaid is None and bal <= 1e-9:
            repaid = y
        flows.append((t, cf[y] - pay))
    moic = sum(c for _, c in flows if c > 0) / equity0
    return equity0, loan, irr(flows), moic, repaid


if __name__ == '__main__':
    for kind, cfg in [('strip', None), ('low', None), ('strip', {'decl_mult': 1.3})]:
        for bid in (110, 125):
            equity0, loan, r, moic, repaid = levered(bid, kind, cfg)
            print(f"{kind:6s} {str(cfg):22s} bid {bid}: equity at close {equity0:5.1f}, loan {loan:4.1f}, "
                  f"levered equity IRR {r*100:5.1f}%, MOIC {moic:.2f}x, debt repaid by {repaid or 'not by 2032'}")
