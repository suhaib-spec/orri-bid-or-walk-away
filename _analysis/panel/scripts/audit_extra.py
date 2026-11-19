import sys, runpy
S = sys.argv[1]
g = runpy.run_path(S + '/panel/scripts/audit_model.py', run_name='audit')  # re-runs prints; REANCHOR ends True
cd, e2 = g['corr_deal'], g['e2']
for b in (105, 115, 118):
    a = cd(b); l = cd(b, kind='low'); s = cd(b, decl_mult=1.3); lu = cd(b, share={'Lucius': 0.010585})
    print(f'EXTRA bid {b}: IRR {a[0]*100:.1f}% low {l[0]*100:.1f}% decl {s[0]*100:.1f}% LuciusPreUnit {lu[0]*100:.1f}% cash@close {a[3]:.1f}')
w, h = e2.deck(2018, 'strip')
luc = sum((e2.mon[('Lucius', f'2018{m:02d}')][0]*0.014288*(w-2.3) + e2.mon[('Lucius', f'2018{m:02d}')][1]*0.014288*(h*1.1-0.4))/1e6 for m in range(1, 6))
print('EXTRA Lucius Jan-May18 ORRI rev $M', round(luc, 2), '+ Jun (reanchored)', round(g['RA']['Lucius'][0]*1000*30*0.014288*(w-2.3)/1e6, 2))
