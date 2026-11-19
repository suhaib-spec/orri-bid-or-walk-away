"""Performance-payment returns on Excel-consistent basis (operator-trend Stones restart Jul)."""
import io, contextlib
import os, sys; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'model'))
from common import analysis_dir, load_script
A = analysis_dir()
with contextlib.redirect_stdout(io.StringIO()):  # rival_cp prints its own grid on load
    cp = load_script('cp', 'panel/scripts/rival_cp.py', A)
rr = cp.rr
orig = rr.flows
def run(cash, P, kind, fail, sr, pay=True):
    F = rr.flows(P, kind=kind, kodiak_fail_year=fail, stones_restart_month=sr)
    cf = [(0.0, -cash)]
    for fl in F.values():
        for t, v in fl: cf.append((max(t - rr.T_CLOSE, 0.0), v))
    paid = 0
    if pay and kind != 'low':
        for y, q in cp.kod_rates(P, fail).items():
            if q >= cp.TRIG[y]: cf.append((y - 2018 + 0.25 + 1 - rr.T_CLOSE, -cp.PAY)); paid += cp.PAY
    return round(cp.irr(cf) * 100, 1), paid
for lbl, P, k, f, sr in (('base', rr.P, 'strip', None, 9), ('oper', rr.M, 'strip', None, 7), ('base45', rr.P, 'low', None, 9), ('oper45', rr.M, 'low', None, 7), ('Kfail', rr.P, 'strip', 2020, 9)):
    print(lbl, '98+cp', run(98, P, k, f, sr), '105 fixed', run(105, P, k, f, sr, False))
