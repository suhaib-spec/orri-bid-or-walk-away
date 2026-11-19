"""Independent audit of engine2.py / returns.py / levered.py.  Run:
python -I panel/scripts/audit_model.py "<path to _analysis>"
Uses only Jan-2015..May-2018 BOEM months (public by 2018-08-15) and the model's own Aug-2018 price deck."""
import csv, calendar, collections
import os, sys; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'model'))
from common import analysis_dir, load_script, irr as _irr
S = analysis_dir()
e2 = load_script('e2', 'model/engine2.py', S)

def irr(cfs, lo=-0.95, hi=5.0):
    return _irr(cfs, lo, hi, iters=300)

T_AUG15 = 226 / 365          # 2018-08-15 as fraction of 2018
T_CLOSE = 256 / 365          # 2018-09-14
LAG = 2 / 12                 # ~60-day ORRI payment lag
OIL = lambda w: w + e2.OIL_ADJ - e2.OIL_DED
GAS = lambda h: h * e2.GAS_MULT - e2.GAS_DED

print('=== 1. Reproduce engine2 baseline ===')
for r in (0.10, 0.12, 0.15, 0.20): print(f'  engine2.run({r}) TOTAL = {e2.run(r)["TOTAL"]:.1f}')

# ---------- independent rebuild of baseline (no call to run) ----------
RA = {}   # re-anchored Jun-Dec 2018 rates: Mar-May 2018 actual rate declined 0.42 yr (Apr 15 -> Sep 15) at the model's own decline
for p, (o0, g0, dec, end) in e2.PDP.items():
    if p == 'Stones': RA[p] = (o0, g0); continue    # shut in Mar-May; keep model restart assumption
    o = sum(e2.mon[(p, f'2018{m:02d}')][0] for m in (3, 4, 5)) / 92 / 1000; g = sum(e2.mon[(p, f'2018{m:02d}')][1] for m in (3, 4, 5)) / 92 / 1000
    RA[p] = (o * (1 - dec) ** 0.42, g * (1 - dec) ** 0.42)
REANCHOR = [False]
def rates(p):
    o0, g0, dec, end = e2.PDP[p]
    return (RA[p] + (dec, end)) if REANCHOR[0] else (o0, g0, dec, end)
def base_cf(kind='strip', horizon=2032, decl_mult=1.0, share=None, oil_adj_extra=0.0, ends=None, anchor_fix=False):
    sh = dict(e2.SHARE, **(share or {}))
    cf = collections.defaultdict(float); bypm = {}
    for p in e2.PDP:
        o0, g0, dec, end = rates(p)
        dec *= decl_mult
        end = (ends or {}).get(p, end)
        for y in range(2019, horizon + 1):
            if y > end: continue
            n = (y - 2018 - 0.21) if anchor_fix else (y - 2018)
            f = (1 - dec) ** n; d = 366 if calendar.isleap(y) else 365
            w, h = e2.deck(y, kind)
            rev = (o0 * 1000 * d * f * sh[p] * (OIL(w) + oil_adj_extra) + g0 * 1000 * d * f * sh[p] * GAS(h)) / 1e6 * 0.98
            cf[y] += rev
    return cf

def monthly_2018(share=None, oil_adj_extra=0.0):
    """ORRI revenue by production month 2018 ($M): Jan-May BOEM actual, Jun-Dec model forecast rate."""
    sh = dict(e2.SHARE, **(share or {})); w, h = e2.deck(2018, 'strip'); out = {}
    for m in range(1, 13):
        tot = 0.0
        for p in e2.PDP:
            o0, g0, dec, end = rates(p)
            if m <= 5: o, g = e2.mon[(p, f'2018{m:02d}')]
            else:
                dm = calendar.monthrange(2018, m)[1]; o, g = o0 * 1000 * dm, g0 * 1000 * dm
            tot += (o * sh[p] * (OIL(w) + oil_adj_extra) + g * sh[p] * GAS(h)) / 1e6
        out[m] = tot
    return out

m18 = monthly_2018(); R18 = sum(m18.values())
cf = base_cf()
pv_ind = lambda r: R18 * (0.7 / (1 + r) ** 0.08 + 0.3 / (1 + r) ** 0.25) + sum(v / (1 + r) ** (y - 2018 + 0.5 - 0.62) for y, v in cf.items())
print('  independent rebuild:', {r: round(pv_ind(r), 1) for r in (0.10, 0.12, 0.15, 0.20)}, ' 2018 rev', round(R18, 2))

print('\n=== 2. 2018 revenue phasing (production-month basis) ===')
print('  by month $M:', {m: round(v, 2) for m, v in m18.items()})
jan_jun = sum(m18[m] for m in range(1, 7)); jan_sep14 = sum(m18[m] for m in range(1, 9)) + m18[9] * 14 / 30
print(f'  Jan-Jun = {jan_jun:.1f} ({jan_jun/R18:.1%});  Jan1-Sep14 = {jan_sep14:.1f} ({jan_sep14/R18:.1%});  model credit 0.70x = {0.7*R18:.1f}')
print(f'  cash at close @110: model {110-0.7*R18:.1f}; corrected (seller has received only Jan-Jun production by Sep 14) {110-jan_jun:.1f}')

print('\n=== 3. 2017 calibration ===')
r17 = e2.rev2017(); print('  engine2.rev2017() TOTAL =', round(sum(r17.values()), 2), '(memo says 20.4)')
w17, h17 = e2.deck(2017, 'strip')
lucius_lease = sum(e2.mon.get(('Lucius', f'2017{m:02d}'), [0, 0])[0] for m in range(1, 13))  # all leases
import csv as _c
rows = list(_c.DictReader(open(S + '/boem/monthly_by_lease.csv')))
def lease_sum(prop, leases, months):
    o = g = 0.0
    for r in rows:
        if r['property'] == prop and r['lease'] in leases and r['yyyymm'] in months:
            o += float(r['oil_bbl']) + float(r['condensate_bbl']); g += float(r['gas_mcf'])
    return o, g
m17 = {f'2017{m:02d}' for m in range(1, 13)}
lo, lg = lease_sum('Lucius', {'G26771', 'G21444'}, m17)
luc_lease = (lo * 0.02 * OIL(w17) + lg * 0.02 * GAS(h17)) / 1e6
fixed17 = sum(r17.values()) - r17['Lucius'] + luc_lease
print(f'  Lucius 2017 @unit 1.4288% = {r17["Lucius"]:.2f}; @2% lease-located (actual 2017 basis) = {luc_lease:.2f}; corrected total = {fixed17:.2f}')
# cash-basis 2017 (Nov-2016..Oct-2017 production) with monthly WTI (EIA, public)
WTIm = {'201611': 45.7, '201612': 52.0, '201701': 52.5, '201702': 53.5, '201703': 49.3, '201704': 51.1, '201705': 48.5, '201706': 45.2,
        '201707': 46.6, '201708': 48.0, '201709': 49.8, '201710': 51.6, '201711': 56.6, '201712': 57.9}
def rev_months(months):
    t = 0.0
    for mm in months:
        for p in e2.PDP:
            if p == 'Lucius':
                o, g = lease_sum('Lucius', {'G26771', 'G21444'}, {mm}); s = 0.02
            else:
                o, g = e2.mon[(p, mm)]; s = e2.SHARE[p]
            t += (o * s * OIL(WTIm[mm]) + g * s * GAS(h17)) / 1e6
    return t
acc = rev_months([f'2017{m:02d}' for m in range(1, 13)])
cash = rev_months(['201611', '201612'] + [f'2017{m:02d}' for m in range(1, 11)])
print(f'  accrual 2017 (monthly WTI) = {acc:.2f};  cash-basis 2017 (Nov16-Oct17 prod) = {cash:.2f}')
gross = sum((e2.mon[(p, mm)][0] * e2.SHARE[p] * (WTIm[mm] + 0.7) + e2.mon[(p, mm)][1] * e2.SHARE[p] * h17 * 1.1) / 1e6
            for p in e2.PDP if p != 'Lucius' for mm in m17) + (lo * 0.02 * (w17 + 0.7) + lg * 0.02 * h17 * 1.1) / 1e6
print(f'  2017 with NO deductions = {gross:.2f} (also "within ~7%" of 20.4 -> deductions not identified by the fit)')
# Lucius 2018 lease-located share (risk if unit basis not honoured)
m18s = {f'2018{m:02d}' for m in range(1, 6)}
lo8, _ = lease_sum('Lucius', {'G26771', 'G21444'}, m18s); to8, _ = lease_sum('Lucius', {'G26771', 'G21444', 'G21447', 'G32654'}, m18s)
print(f'  Lucius Jan-May18 lease-located fraction = {lo8/to8:.1%} -> pre-unit-basis effective share {0.02*lo8/to8:.4%} vs 1.4288%')

print('\n=== 4. Price: OIL_ADJ is an ADDITIVE +$0.70/bbl (WTI+0.7-3.0 = WTI-2.3), not a 0.7 multiplier ===')
for x in (1.0, 3.0):
    cfx = base_cf(oil_adj_extra=x); m = monthly_2018(oil_adj_extra=x); R = sum(m.values())
    pv = R * (0.7 / 1.12 ** 0.08 + 0.3 / 1.12 ** 0.25) + sum(v / 1.12 ** (y - 2018 + 0.5 - 0.62) for y, v in cfx.items())
    print(f'  +${x:.0f}/bbl realisation -> PV12 {pv:.1f} (delta {pv-133.1:+.1f})')

print('\n=== 5. Horizon ===')
cfl = base_cf(horizon=2040)
print('  PV12 of 2033-2040 (dropped):', round(sum(v / 1.12 ** (y - 2018 + 0.5 - 0.62) for y, v in cfl.items() if y > 2032), 2),
      ' undiscounted:', round(sum(v for y, v in cfl.items() if y > 2032), 2))
print('  gross rates in final modeled year (kb/d):', {p: round(o0 * (1 - d) ** (e - 2018), 2) for p, (o0, g0, d, e) in e2.PDP.items()})
ec = {'Kodiak': 2028, 'Lucius': 2030, 'Stones': 2032, 'SoSantaCruz': 2026}
cfe = base_cf(horizon=2040, ends=ec)
print('  PV12 economic-limit cut', ec, ':', round(R18 * (0.7 / 1.12 ** 0.08 + 0.3 / 1.12 ** 0.25) + sum(v / 1.12 ** (y - 2018 + 0.5 - 0.62) for y, v in cfe.items()), 1))

print('\n=== 6. Corrected valuation (PV at closing 2018-09-14 unless noted) ===')
# 2018 corrected timing: month m paid ~25th of month m+2. Jan-Jun received by seller pre-close -> credit at close.
# Jul-Sep production paid to seller post-close (division orders not yet changed) -> remitted at final settlement ~Jan 15 2019.
# Oct-Dec production paid direct to buyer at m+2.  2% hurricane haircut on Aug15-Dec production.
def flows2018(m18, hurr=0.02):
    fl = []
    for m, v in m18.items():
        frac_post = 0 if m < 8 else (17 / 31 if m == 8 else 1.0)
        v = v * (1 - hurr * frac_post)
        if m <= 6: t = T_CLOSE
        elif m <= 9: t = 1 + 15 / 365
        else: t = (m + 1) / 12 + 25 / 365
        fl.append((t, v))
    return fl
def corrected_flows(kind='strip', decl_mult=1.0, horizon=2040, anchor_fix=True, lag=True, share=None, fix2018=True, oil_adj_extra=0.0):
    m = monthly_2018(share=share, oil_adj_extra=oil_adj_extra); R = sum(m.values())
    fl = flows2018(m) if fix2018 else [(T_CLOSE, 0.7 * R), (T_CLOSE + 0.17, 0.3 * R)]
    c = base_cf(kind=kind, horizon=horizon, decl_mult=decl_mult, anchor_fix=anchor_fix, share=share, oil_adj_extra=oil_adj_extra)
    fl += [(y - 2018 + 0.5 + (LAG if lag else 0), v) for y, v in c.items()]
    return fl
def pv(fl, r, t0=T_CLOSE): return sum(v / (1 + r) ** (t - t0) for t, v in fl)

base_fl = [(T_CLOSE, 0.7 * R18), (T_CLOSE + 0.17, 0.3 * R18)] + [(y - 2018 + 0.5, v) for y, v in cf.items()]
steps = [('engine2 as-is (PV @ Aug 15)', base_fl, T_AUG15),
         ('re-date PV to closing Sep 14', base_fl, T_CLOSE),
         ('+ 2018 cash timing (Jan-Jun credit; Jul-Sep via final settlement; lag; hurricane)', corrected_flows(horizon=2032, anchor_fix=False, lag=False), T_CLOSE),
         ('+ 60-day payment lag 2019+', corrected_flows(horizon=2032, anchor_fix=False, lag=True), T_CLOSE),
         ('+ decline anchored to Jun-Dec midpoint (exp y-2018-0.21)', corrected_flows(horizon=2032, anchor_fix=True, lag=True), T_CLOSE),
         ('+ horizon to field end (2035-2040)', corrected_flows(horizon=2040), T_CLOSE)]
print('  re-anchored Jun-Dec18 rates (oil kb/d, gas mmcf/d) vs model:', {p: (round(RA[p][0],2), round(RA[p][1],2), e2.PDP[p][:2]) for p in RA})
REANCHOR[0] = True; steps.append(('+ Jun-Dec18 rate re-anchored to Mar-May actual x decline', corrected_flows(horizon=2040), T_CLOSE))
prev = None
for lbl, fl, t0 in steps:
    v = pv(fl, 0.12, t0); print(f'  {lbl:85s} PV12 {v:6.1f}' + (f'  ({v-prev:+.1f})' if prev else '')); prev = v
FL = corrected_flows()
print('  CORRECTED PDP:', {f'{int(r*100)}%': round(pv(FL, r), 1) for r in (0.10, 0.12, 0.15, 0.20)},
      ' | @Aug15:', {f'{int(r*100)}%': round(pv(FL, r, T_AUG15), 1) for r in (0.10, 0.12, 0.15, 0.20)})
for lbl, kw in [('low 45/2.25', dict(kind='low')), ('decline x1.3', dict(decl_mult=1.3)), ('Ship Shoal 4%', dict(share={'ShipShoal': 0.04})),
                ('Lucius @ pre-unit lease-located share', dict(share={'Lucius': 0.02 * lo8 / to8})), ('+$3/bbl Mars/LLS premium', dict(oil_adj_extra=3.0))]:
    print(f'  corrected {lbl:40s} PV12 {pv(corrected_flows(**kw), 0.12):6.1f}  PV15 {pv(corrected_flows(**kw), 0.15):6.1f}')

print('\n=== 7. Returns: replicate returns.py, then corrected ===')
def model_deal(bid):
    _, c = e2.run(0.12, detail=True); credit = 0.7 * c[2018]
    fl = [(0.0, -bid + credit), (0.17, 0.3 * c[2018])] + [(y - 2018 + 0.5 - 0.71, c[y]) for y in range(2019, 2033)]
    return irr(fl)
def corr_deal(bid, **kw):
    fl = corrected_flows(**kw); t = [(tt - T_CLOSE, v) for tt, v in fl]
    credit = sum(v for tt, v in t if abs(tt) < 1e-9); rest = [(tt, v) for tt, v in t if tt > 1e-9]
    fl2 = [(0.0, -bid + credit)] + rest
    tot = sum(v for _, v in t)
    cum = -bid + credit; pb = None
    for tt, v in sorted(rest):
        cum += v
        if cum >= 0 and pb is None: pb = tt
    return irr(fl2), tot / bid, pb, bid - credit
print('  bid | model IRR (indep. recompute) | corrected IRR | MOIC | payback(y) | cash@close | corr. low-price IRR | corr. decl x1.3 IRR')
for b in (100, 110, 120, 125, 130):
    a = corr_deal(b); lo_ = corr_deal(b, kind='low'); st = corr_deal(b, decl_mult=1.3)
    print(f'  {b} | {model_deal(b)*100:5.1f}% | {a[0]*100:5.1f}% | {a[1]:.2f}x | {a[2]:.1f} | {a[3]:5.1f} | {lo_[0]*100:5.1f}% | {st[0]*100:5.1f}%')

print('\n=== 8. Levered (levered.py) ===')
def levered(bid, kind='strip', decl_mult=1.0, loan=None, corrected=True, draw_t=0.33, rate=0.0725, sweep=0.75):
    if corrected:
        fl = [(tt - T_CLOSE, v) for tt, v in corrected_flows(kind=kind, decl_mult=decl_mult)]
    else:
        cfg = {'decl_mult': decl_mult} if decl_mult != 1 else None
        _, c = e2.run(0.12, kind=kind, cfg=cfg, detail=True)
        fl = [(0.0, 0.7 * c[2018]), (0.17, 0.3 * c[2018])] + [(y - 2018 + 0.5 - 0.71, c[y]) for y in range(2019, 2033)]
    credit = sum(v for t, v in fl if abs(t) < 1e-9)
    eq = [(0.0, -(bid - credit)), (draw_t, loan)]; bal = loan; tp = draw_t; payoff = None
    for t, v in sorted((t, v) for t, v in fl if t > 1e-9):
        if t < draw_t: eq.append((t, v)); continue
        bal *= (1 + rate) ** (t - tp); tp = t; pay = min(bal, sweep * v); bal -= pay
        if bal <= 1e-6 and payoff is None: payoff = 2018 + T_CLOSE + t
        eq.append((t, v - pay))
    return irr(eq), payoff, bal
# model sizing: 40% x low-deck PV10 as of Aug-15-2018 INCLUDING 2018 revenue already credited/received
print('  model loan 40% x run(0.10,low) =', round(0.4 * e2.run(0.10, kind='low')['TOTAL'], 1))
for b in (110, 125):
    for kind, dm in (('strip', 1.0), ('low', 1.0), ('strip', 1.3)):
        cfg = {'decl_mult': dm} if dm != 1 else None
        L = 0.4 * e2.run(0.10, kind='low', cfg=cfg)['TOTAL']
        i, po, bal = levered(b, kind, dm, L, corrected=False)
        print(f'  model-basis {kind:5s} dx{dm} bid {b}: IRR {i*100:5.1f}%  debt repaid {po and round(po,1)}  residual {bal:.2f}')
# corrected sizing: 40% x low-deck PV10 of cash flows remaining after the Jan-2019 draw date, at that date
def loan_corrected(decl_mult=1.0, adv=0.40, draw=T_CLOSE + 0.33):
    fl = corrected_flows(kind='low', decl_mult=decl_mult)
    return adv * sum(v / 1.10 ** (t - draw) for t, v in fl if t > 1.2)   # 2019+ production only; 2018 receivables are not reserves
_, cl = e2.run(0.10, kind='low', detail=True)
print('  of which 2018 revenue in model PV10-low:', round(cl[2018] * (0.7 / 1.1 ** 0.08 + 0.3 / 1.1 ** 0.25), 1))
for b in (110, 125):
    for kind, dm in (('strip', 1.0), ('low', 1.0), ('strip', 1.3)):
        L = loan_corrected(dm); i, po, bal = levered(b, kind, dm, L)
        print(f'  corrected   {kind:5s} dx{dm} bid {b}: loan {L:4.1f}  IRR {i*100:5.1f}%  debt repaid {po and round(po,1)}  residual {bal:.2f}')
