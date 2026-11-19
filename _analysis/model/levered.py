import sys, importlib.util
spec = importlib.util.spec_from_file_location('e2', sys.argv[1] + '/model/engine2.py'); e2 = importlib.util.module_from_spec(spec); spec.loader.exec_module(e2)
def irr(cfs):
    lo, hi = -0.9, 5.0
    for _ in range(200):
        m = (lo+hi)/2; v = sum(c/(1+m)**t for t, c in cfs); lo, hi = (m, hi) if v > 0 else (lo, m)
    return m
for kind, cfg in [('strip', None), ('low', None), ('strip', {'decl_mult':1.3})]:
  for bid in (110, 125):
    _, cf = e2.run(0.12, kind=kind, cfg=cfg, detail=True)
    credit = 0.7*cf[2018]; equity0 = bid - credit
    loan = 0.40*e2.run(0.10, kind='low', cfg=cfg)['TOTAL']   # bank deck: low price PV10, 40% advance
    rate = 0.0725  # prime 5.00% + 2.25%
    # t=0.33 (Jan 2019) loan drawn, returned to equity; cash sweep 75% of revenue to debt service
    flows = [(0.0, -equity0), (0.17, 0.30*cf[2018]), (0.33, loan)]
    bal = loan; t_prev = 0.33
    for y in range(2019, 2033):
        t = y - 2018 + 0.5 - 0.71; bal *= (1+rate)**(t - t_prev); t_prev = t
        pay = min(bal, 0.75*cf[y]); bal -= pay
        flows.append((t, cf[y] - pay))
    print(f"{kind:6s} {str(cfg):22s} bid {bid}: equity at close {equity0:5.1f}, loan {loan:4.1f}, levered equity IRR {irr(flows)*100:5.1f}%, MOIC {sum(c for t,c in flows if c>0)/ (equity0):.2f}x, debt repaid by {next((y for y in range(2019,2033) if True),0)}")
