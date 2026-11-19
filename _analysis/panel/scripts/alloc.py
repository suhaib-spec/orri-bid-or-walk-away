import os, sys; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'model'))
from common import analysis_dir, load_script
S = analysis_dir()
rr = load_script('rr', 'panel/scripts/reserves_rebuttal.py', S)
rr.rp.SHARE['ShipShoal'] = 0.04
for nm, P in (('cautious', rr.P), ('team', rr.M)):
    F = rr.flows(P); tot = rr.total(F, .12)
    print(nm, round(tot, 1), {k: (round(rr.pv(f, .12), 1), round(100 * rr.pv(f, .12) / tot, 1)) for k, f in F.items()})
