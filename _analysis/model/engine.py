"""Quick scenario valuation engine for the BP GoM ORRI package (valuation date 2018-08-15).
Volumes: Wood Mackenzie gross field profiles (transcribed by diligence agents). Shares: documented effective ORRI share of field/unit output."""
import json, sys
Y = list(range(2018, 2047))
def pad(d, start):  # list starting at year start -> dict
    return {start+i: v for i, v in enumerate(d)}
# gross field liquids kb/d, gas mmcfd, WoodMac gross revenue $M (nominal)
kod_l=[17.0,16.4,12.5,9.3,6.9,5.1,6.0,9.1,6.9,5.2,3.8,2.8,2.1,1.4,1.0,0.8,0.6,0.4,0.3,0.2]
kod_g=[20.1,14.9,11.1,8.2,14.8,29.5,22.6,16.8,12.5,9.3,6.9,5.1,3.8,2.8,2.1,1.6,1.2,0.8,0,0]
kod_r=[398.1,364.5,273.0,243.7,195.2,171.1,188.2,268.6,209.1,158.5,120.2,90.9,67.7,47.1,35.7,26.9,20.3,15.5,10.9,7.3]
luc_l=[50.3,58.8,52.7,44.7,35.8,28.0,23.7,24.8,31.2,28.1,27.2,22.0,17.8,14.5,11.9,9.7,8.0,6.6,5.5,4.6,3.8,3.2,2.7,2.2,1.9,1.6,1.3,1.1,1.0]
luc_g=[53.2,62.1,55.0,46.4,37.0,28.9,24.0,24.1,31.6,28.6,27.7,22.4,18.2,14.8,12.1,10.0,8.2,6.8,5.7,4.7,3.9,3.3,2.8,2.3,2.0,1.7,1.4,1.2,1.0]
luc_r=[1228.1,1380.1,1213.1,1116.5,996.9,804.6,708.6,750.5,948.3,876.4,869.3,733.5,624.3,529.0,454.4,393.8,341.5,286.5,240.9,202.2,170.2,143.7,121.7,103.7,88.2,75.2,56.5,48.8,42.0]
sto_l=[60.3,68.0,54.8,41.4,30.6,22.5,16.6,12.3,9.0,10.0,13.7,16.4,18.4,19.9,21.1,22.0,19.2,14.2,10.5,7.7,5.7,4.2,3.1,2.3,1.7,1.2,0.9,0.7]
sto_g=[8.7,9.9,7.9,6.0,4.4,3.3,2.4,1.8,1.3,1.4,2.0,2.4,2.7,2.9,3.1,3.2,2.8,2.1,1.5,1.1,0.8,0.6,0.5,0.3,0.2,0.2,0.1,0.1]
sto_r=[1332.8,1443.6,1143.2,1043.9,785.9,591.2,444.8,334.4,251.7,284.9,397.2,485.2,554.6,612.1,662.0,705.0,627.7,472.2,355.1,267.3,200.9,151.3,113.5,85.5,64.2,48.4,36.2,27.2]
ssc_l=[13.7,12.9,10.1,7.8,6.1,4.8,5.5,5.4,4.2,3.3,2.6,2.0,1.6,1.2,0.9,0.7,0.5,0.3,0.3,0.2]
ssc_g=[11.1,10.5,8.1,6.3,4.9,3.8,4.5,4.4,3.4,2.7,2.1,1.6,1.3,1.0,0.8,0.6,0.4,0.3,0.2,0.2]
ssc_r=[297.4,269.6,206.8,193.5,153.7,122.3,145.4,144.3,114.7,91.1,72.5,57.4,45.8,36.2,28.9,22.9,15.4,10.5,8.3,6.5]
# shelf: gross kboe/d split (gas kboe/d, liquids kb/d); WoodMac gas boe at ~5.68 mcf/boe
gi_gas=[0.93,0.76,0.62,0.50,0.41,0.34,0.27,0.22,0.18,0.15,0.12,0.10,0.08,0.07,0.05,0.04,0.04,0.03,0.02,0.02]
gi_liq=[0.39,0.32,0.26,0.21,0.18,0.14,0.12,0.10,0.08,0.06,0.05,0.04,0.03,0.03,0.02,0.02,0.02,0.01,0.01,0.01]
mp_gas=[5.55,5.30,5.06,4.83,4.61,4.41,4.21,4.02,3.84,3.67,3.50,3.34,3.19,3.05,2.91,2.78,2.66,2.54,2.42,2.31]
mp_liq=[0.34+2.47,0.33+2.32,0.31+2.18,0.30+2.04,0.28+1.91,0.27+1.80,0.26+1.68,0.25+1.58,0.24+1.48,0.22+1.39,0.21+1.30,0.21+1.22,0.20+1.15,0.19+1.07,0.18+1.01,0.17+0.94,0.16+0.89,0.16+0.83,0.15+0.78,0.14+0.73]
# Ship Shoal 219: agent base 30%/yr decline from ~467 bopd + 2.56 MMcf/d (2018)
ss_l=[467*0.7**i/1000 for i in range(8)]; ss_g=[2.56*0.7**i for i in range(8)]
PROPS = {
 'Kodiak':  dict(l=pad(kod_l,2018), g=pad(kod_g,2018), r=pad(kod_r,2018), share=0.06375, trans=2.0),
 'Lucius':  dict(l=pad(luc_l,2018), g=pad(luc_g,2018), r=pad(luc_r,2018), share=0.014288, trans=0.0),
 'Stones':  dict(l=pad(sto_l,2018), g=pad(sto_g,2018), r=pad(sto_r,2018), share=0.015, trans=2.0),
 'SoSantaCruz': dict(l=pad(ssc_l,2018), g=pad(ssc_g,2018), r=pad(ssc_r,2018), share=0.0093, trans=2.0),
 'GrandIsle': dict(l=pad(gi_liq,2018), g=pad([x*5.68 for x in gi_gas],2018), r=None, share=0.005, trans=1.0),
 'MainPass':  dict(l=pad(mp_liq,2018), g=pad([x*5.68 for x in mp_gas],2018), r=None, share=0.02604167*0.3301, trans=1.0),
 'ShipShoal': dict(l=pad(ss_l,2018), g=pad(ss_g,2018), r=None, share=0.08, trans=1.0),
 'Pompano': dict(l={}, g={}, r=None, share=0.0, trans=0),
 'Orion':   dict(l={2018:0.1}, g={}, r=None, share=0.013125, trans=0),
}
DECKS = {  # nominal WTI $/bbl, HH $/mmbtu
 'strip_aug2018': (dict(zip(range(2018,2023),[66.5,64.5,61.0,58.5,57.0])), dict(zip(range(2018,2023),[2.95,2.82,2.66,2.65,2.65])), 57.0, 2.65, 0.0),
 'eia_aug2018':   (dict(zip(range(2018,2020),[66.2,64.3])), dict(zip(range(2018,2020),[2.96,3.10])), 64.3, 3.10, 0.02),
 'low':           ({2018:66.5}, {2018:2.95}, 45.0, 2.25, 0.0),
 'high':          ({2018:66.5}, {2018:2.95}, 75.0, 3.25, 0.02),
}
def price(deck, y):
    o, g, ol, gl, esc = DECKS[deck]
    if y in o: return o[y], g[y]
    last = max(o); n = y - last
    return ol*(1+esc)**n, gl*(1+esc)**n
def value(rate=0.12, deck='strip_aug2018', horizon=2032, diff=-2.0, hurricane=0.02,
          haircut=None, share_over=None, vol_scale=None, wm_revenue=False, detail=False):
    haircut = haircut or {}; share_over = share_over or {}; vol_scale = vol_scale or {}
    out = {}; cf_total = {}
    for name, p in PROPS.items():
        sh = share_over.get(name, p['share']); hc = haircut.get(name, 0.0); vs = vol_scale.get(name, 1.0)
        pv = 0.0; cfs = {}
        for y in Y:
            if y > horizon: break
            if wm_revenue and p['r'] is not None:
                rev = p['r'].get(y, 0.0) * sh
            else:
                op, gp = price(deck, y)
                days = 366 if y % 4 == 0 else 365
                liq = p['l'].get(y, 0.0) * 1000 * days * sh
                gas = p['g'].get(y, 0.0) * 1000 * days * sh
                rev = (liq * (op + diff - p['trans']) + gas * gp) / 1e6
            rev *= (1 - hurricane) * (1 - hc) * vs
            cfs[y] = rev
            # timing from valuation date 2018-08-15 (t=0). 2018: 70% pre-close credit at Sep14 (t=0.08), 30% mid Nov (t=0.25)
            if y == 2018: df = 0.70/(1+rate)**0.08 + 0.30/(1+rate)**0.25
            else: df = 1/(1+rate)**((y - 2018) + 0.5 - 0.62)
            pv += rev * df
        out[name] = pv; cf_total[name] = cfs
    out['TOTAL'] = sum(v for k, v in out.items())
    return (out, cf_total) if detail else out
if __name__ == '__main__':
    def show(lbl, d): print(f"{lbl:46s}" + " ".join(f"{k[:7]:>8s}" for k in d) if lbl=='hdr' else f"{lbl:46s}" + " ".join(f"{v:8.1f}" for v in d.values()))
    base = value(); show('hdr', base)
    show('WM revenue, 10%, no haircuts, to 2046', value(0.10, wm_revenue=True, horizon=2046, hurricane=0))
    show('Strip, 10%, no haircuts, to 2046', value(0.10, horizon=2046, hurricane=0))
    for r in (0.10, 0.12, 0.15, 0.20):
        show(f'Strip, {int(r*100)}%, 15yr, hurricane 2%', value(r))
    HC = {'Kodiak':0.25,'Lucius':0.15,'Stones':0.10,'SoSantaCruz':0.30,'ShipShoal':0.5,'MainPass':0.3,'GrandIsle':0.2}
    for r in (0.10, 0.12, 0.15, 0.20):
        show(f'RISKED strip {int(r*100)}% 15yr', value(r, haircut=HC))
    for d in ('low','eia_aug2018','high'):
        show(f'RISKED {d} 12%', value(0.12, deck=d, haircut=HC))
    o, cf = value(0.12, haircut=HC, detail=True)
    for y in range(2018, 2024): print(y, round(sum(cf[k].get(y,0) for k in cf),2))
