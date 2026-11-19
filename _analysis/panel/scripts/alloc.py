import sys, importlib.util
S = sys.argv[1]
sp = importlib.util.spec_from_file_location('rr', S + '/panel/scripts/reserves_rebuttal.py')
sys.argv = [sys.argv[0], S]; rr = importlib.util.module_from_spec(sp); sp.loader.exec_module(rr)
rr.rp.SHARE['ShipShoal'] = 0.04
for nm, P in (('cautious', rr.P), ('team', rr.M)):
    F = rr.flows(P); tot = rr.total(F, .12)
    print(nm, round(tot, 1), {k: (round(rr.pv(f, .12), 1), round(100 * rr.pv(f, .12) / tot, 1)) for k, f in F.items()})
