"""Rebuttal round: reserves-engineer production assumptions on the model auditor's corrected mechanics
(PV at closing 2018-09-14; 2018 monthly cash timing per audit_model.flows2018; 2019+ mid-year + 60-day lag;
decline anchored to the Sep-centred Jun-Dec rate; horizon 2040; 2% hurricane on Aug15+ production).
Also: Kodiak P50/P90 and risked sanctioned-development items. Only public_by_2018_08_15 == 'Y' rows used.
Run: python -I panel/scripts/reserves_rebuttal.py <_analysis dir>"""
import copy, calendar, random
import os, sys; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'model'))
from common import analysis_dir, load_script
S = analysis_dir()
rp = load_script('rp', 'panel/scripts/reserves_panel.py', S)
T_CLOSE, LAG, ANCH = 256 / 365, 2 / 12, 0.21
OIL = lambda w: w + rp.OIL_ADJ - rp.OIL_DED
GAS = lambda h: h * 1.10 - rp.GAS_DED

def flows(P, kind='strip', pm=1.0, kodiak_fail_year=None, stones_restart_month=9, horizon=2040):
    """returns {prop: [(t, $M)]} on auditor mechanics."""
    out = {}
    w18, h18 = rp.deck(2018, 'strip')
    for p, c in P.items():
        fl = []; ratio = c['g0'] / c['q18'] if c['q18'] else 0.0
        for m in range(1, 13):
            if m <= 5:
                o, g = rp.mon[(p, f'2018{m:02d}')]
            else:
                dm = calendar.monthrange(2018, m)[1]
                if p == 'Stones':
                    on = 1.0 if m >= stones_restart_month else 0.0
                    o = c['base'] * on * c['up'] * 1000 * dm; g = o * (c['g0'] / c['base'] if c['base'] else 0)
                else:
                    o = c['q18'] * c['up'] * 1000 * dm; g = c['g0'] * c['up'] * 1000 * dm
            v = (o * rp.SHARE[p] * OIL(w18) + g * rp.SHARE[p] * GAS(h18)) / 1e6
            v *= 1 - 0.02 * (0 if m < 8 else (17 / 31 if m == 8 else 1.0))
            t = T_CLOSE if m <= 6 else (1 + 15 / 365 if m <= 9 else (m + 1) / 12 + 25 / 365)
            fl.append((t, v))
        q0 = c['q18'] if p != 'Stones' else c['base']
        gbase = (c['g0'] / c['base']) * q0 if p == 'Stones' else c['g0']
        for y in range(2019, horizon + 1):
            if y > c['end']: break
            f = rp.frac(c['De'], c['b'], y - 2018 - ANCH)
            q = q0 * f
            if q < c['qlim']: break
            if p == 'Kodiak' and kodiak_fail_year and y >= kodiak_fail_year: break
            d = 366 if calendar.isleap(y) else 365
            w, h = rp.deck(y, kind, pm)
            v = (q * 1000 * d * c['up'] * rp.SHARE[p] * OIL(w) + gbase * f * 1000 * d * c['up'] * rp.SHARE[p] * GAS(h)) / 1e6 * 0.98
            fl.append((y - 2018 + 0.5 + LAG, v))
        out[p] = fl
    return out

def pv(fl, r): return sum(v / (1 + r) ** (t - T_CLOSE) for t, v in fl)
def total(F, r): return sum(pv(f, r) for f in F.values())

P = copy.deepcopy(rp.PANEL)
P['Stones'].update(q18=12.0, base=23.0)  # restart Sep-1 at 23 kb/d (monthly model handles Jun-Aug zero)
P['Stones']['g0'] = 3.3                  # gas at restart rate (ratio to base)
M = copy.deepcopy(rp.MEMO)
if __name__ == '__main__':
    for lbl, X, sr in (('Memo inputs, auditor mechanics', M, 6), ('Panel inputs, auditor mechanics', P, 9)):
        F = flows(X, stones_restart_month=sr); print(f'{lbl:36s}', {f'{int(r*100)}%': round(total(F, r), 1) for r in (0.10, 0.12, 0.15)},
                            {p: round(pv(f, 0.12), 1) for p, f in F.items()})
    # Kodiak deterministic cases (PV12/PV15 Kodiak only)
    kc = {'P50 (35%,b.5,90%,1.5)': {}, 'De 25%': dict(De=0.25), 'De 45%, up 85%, q 14': dict(De=0.45, up=0.85, q18=14.0, g0=11.5),
          'up 1.0, qlim 1.0': dict(up=1.0, qlim=1.0)}
    for k, mod in kc.items():
        X = copy.deepcopy(P); X['Kodiak'].update(mod); F = flows(X)
        print(f'Kodiak {k:28s} PV12 {pv(F["Kodiak"], 0.12):5.1f}  PV15 {pv(F["Kodiak"], 0.15):5.1f}')
    # Monte Carlo on corrected mechanics
    random.seed(11); tot12, tot15, kod12, kod15 = [], [], [], []
    for i in range(6000):
        X = copy.deepcopy(P)
        for p, c in X.items():
            m = random.lognormvariate(0, 0.10); c['q18'] *= m; c['base'] *= m; c['g0'] *= m
            c['De'] = min(0.65, max(0.08, c['De'] * random.triangular(0.7, 1.4, 1.0)))
            c['b'] = random.uniform(max(0, c['b'] - 0.3), c['b'] + 0.3) if c['b'] else 0.0
        X['Kodiak']['up'] = random.uniform(0.82, 0.97)
        srm = 13 if random.random() < 0.10 else random.choice([7, 8, 9, 10, 11])
        fy = next((y for y in range(2019, 2033) if random.random() < 0.06), None)
        F = flows(X, kodiak_fail_year=fy, stones_restart_month=srm)
        tot12.append(total(F, 0.12)); tot15.append(total(F, 0.15)); kod12.append(pv(F['Kodiak'], 0.12)); kod15.append(pv(F['Kodiak'], 0.15))
    q = lambda a, x: sorted(a)[int(x * (len(a) - 1))]
    for lbl, a in (('Package 12%', tot12), ('Package 15%', tot15), ('Kodiak 12%', kod12), ('Kodiak 15%', kod15)):
        print(f'MC {lbl:12s} P90 {q(a, .1):6.1f} P50 {q(a, .5):6.1f} P10 {q(a, .9):6.1f} mean {sum(a)/len(a):6.1f}')

    # Risked sanctioned/planned development (incremental type-curve approach, not WoodMac-minus-PDP)
    def inc(share, q_first, De, b, start, P_succ, hair=1.0, r=0.12, years=12):
        v = 0.0
        for k in range(years):
            y = start + k; q = q_first * rp.frac(De, b, k)
            w, h = rp.deck(y, 'strip')
            v += q * 1000 * 365 * share * OIL(w) * 0.98 * 0.95 / 1e6 / (1 + r) ** (y - 2018 + 0.5 + LAG - T_CLOSE)
        return v * P_succ * hair, v
    items = {
     'Hadrian North (in unit; 15 kb/d from 2019.5)': (0.014288, 15.0, 0.30, 0.5, 2020, 0.80, 0.40),  # 2019 half-year approximated by 2020 start
     'Lucius 9th well / KC919 rework (10 kb/d 2019)': (0.014288, 10.0, 0.30, 0.5, 2019, 0.30, 1.0),
     'Stones Phase 2 (2 wells, 20 kb/d 2020)':        (0.015,    20.0, 0.30, 0.5, 2020, 0.30, 0.80),
     'Kodiak 2nd well (10 kb/d 2020)':                (0.06375,  10.0, 0.35, 0.5, 2020, 0.15, 1.0),
    }
    for k, a in items.items():
        r12, un = inc(*a); r15, _ = inc(*a, r=0.15)
        print(f'{k:48s} unrisked PV12 {un:5.1f}  risked PV12 {r12:5.1f}  PV15 {r15:5.1f}')
