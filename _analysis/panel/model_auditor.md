# Model audit: engine2.py / returns.py / levered.py (as of Aug 15, 2018)

Reviewer: forensic model auditor (adversarial panel). Scripts: `panel/scripts/audit_model.py`, `panel/scripts/audit_extra.py` (these call engine2.py read-only; no model file was edited). Inputs: BOEM months through May-2018 only, plus the model's own Aug-2018 deck.

**Reproduction.** I rebuilt every cash flow from scratch. My numbers match engine2 exactly (138.4 / 133.1 / 126.2 / 116.6), returns.py IRRs (35.0 / 25.8 / 19.1 / 13.9%) and levered.py (32.7 / 18.6 / 14.5 / 4.7 / 16.5 / 5.7%). The arithmetic, the IRR solver, the units (kb/d×1000×days = bbl; mmcf/d×1000 = mcf) and the 214-day Jun–Dec count are correct. Jan–May 2018 actuals are not double counted with the forecast (engine2.py:42-45). The errors are in timing, financing and calibration logic.

## Findings

**F1 — Major (funding: +$10.5M equity at close; PV −$1.0M). The effective-date credit is overstated and mistimed.** engine2.py:63-64, returns.py:33-34, levered.py:11,15.
- 2018 revenue is counted once (credit + remainder = 100% of cf[2018]), so there is **no double counting**.
- 70% is a calendar fraction. On a revenue basis, Jan 1–Sep 14 is 67.9% of 2018, because of the Kodiak outage in Jan–Feb and the Stones shut-in in Mar–May.
- The bigger problem is the payment lag. With ~60-day arrears, by Sep 14 the seller has been paid only for **Jan–Jun production: $18.8M (45%)**, not $29.1M.
- Jul 1–Sep 14 production (~$9.4M) is paid to the seller after closing (Sept 25–Nov 25, before division orders change). It reaches the buyer through the final settlement (~Jan 2019).
- Sep 15–Dec production is paid Nov 2018–Feb 2019, not "mid-Nov" (t=0.17/0.25).
- **Cash at close on a $110M bid is ≈$91.4M, not $80.9M** (decision_memo.md:36,41). If Anadarko is holding Lucius unit-basis proceeds in suspense, the credit falls by up to another ~$6M (Lucius Jan–Jun ORRI ≈ $6.1M), and the equity cheque rises with it.

**F2 — Major (levered IRR overstated 4–9 pts). Debt is sized on revenue that no longer exists at the draw date.** levered.py:12.
- `loan = 0.40 × run(0.10,'low')['TOTAL']` includes **$41.0M of PV10 from 2018 revenue**. That revenue is credited or collected before the Jan-2019 draw.
- 40% of the low-deck PV10 of 2019+ PDP at the draw date is **$29.9M, not $45.2M** (−$15.3M). Under decline ×1.3 it is $23.2M, not $38.5M.
- Combined with F1, levered equity IRR at $110M moves:
  - strip: 32.7% → **23.4%**
  - low price: 14.5% → **10.9%**
  - decline ×1.3: 16.5% → **13.5%**
- At $125M strip it moves from 18.6% to **15.0%**.
- **Confirmed:** "debt repaid by" always prints 2019 (levered.py:21, `next(... if True)` returns the first year). On the model's own basis, debt is actually repaid around mid-2021 on strip and mid-2023 on the low deck. No balance is left unpaid at 2032, which I checked.

**F3 — Major (credibility; PV risk −$7.7M). The calibration claim is not reproduced by the code and does not validate the key share.** engine2.py:34,69-74; decision_memo.md:29-30.
- `rev2017()` prints **$28.9M, not $20.4M**. It applies the post-unit Lucius share (1.4288%) to 2017 volumes.
- The $20.4M match in boem_actuals.md:42-68 used 2% × lease-located KC 874/875 volumes. With that fix the code gives $20.55M.
- The fit cannot identify its own parameters:
  - with no deductions at all: $21.8M (+7%)
  - cash basis (Nov-16 to Oct-17 production): $21.3M
  - Ship Shoal at 4%: ≈$19.9M
- Every variant falls inside "~5%". The $3/bbl and $0.40/mcf deductions are therefore a plug, fitted to an unaudited, rounded seller marketing number of unknown basis.
- Most important: the 2017 match proves **nothing about the 1.4288% unit share**, which is the main title assumption for 2018 onward. In Jan–May 2018, 52.9% of Lucius volumes were on KC 874/875, so a lease-basis outcome means 1.06% → **−$7.7M PV12**.
- **OIL_ADJ 0.7 is not a fudge.** It is an *additive* +$0.70/bbl (2017 Mars $51.5 vs WTI $50.8, boem_actuals.md:46), not a 0.7 multiplier. Net realisation is WTI −$2.30. Mars on Aug 15 was WTI −$1.90 (market.md:80), so this is reasonable. ±$1/bbl = ±$2.1M PV12. Charging $3/bbl to Lucius KC 875 contradicts its "free of all costs … transporting" clause (lucius.md:165), which is a small understatement (~$0.6M).

**F4 — Minor (two offsetting errors, net −$0.5M). Decline indexing.** engine2.py:18-25,47.
- `(1−dec)**(y−2018)` steps a full year from the Jun–Dec 2018 average, which is centred on Sep 15. That average is only 0.80 yr before mid-2019, so 2019+ volumes are understated by 5–6% (+$4.9M).
- Separately, the Jun–Dec rates are set 5–9% above the Mar–May 2018 actuals rolled forward 0.42 yr at the model's own decline:
  - Kodiak 16.0 vs 15.25 kb/d
  - Lucius 30.0 vs 28.1
  - SSC 3.4 vs 3.1
  - Lucius gas 29.0 vs 26.6
- That effect is −$5.4M. The two errors cancel by luck. Fix both.

**F5 — Minor (−$1.7M). No payment lag after 2018.** engine2.py:64; returns.py:34; levered.py:18. Mid-year t ignores the ~2-month arrears. This adds 0.17 yr to every 2019+ flow.

**F6 — Minor (+$1.2M). Valuation date.**
- The offsets themselves are right: 0.62 = Aug 15 (226/365) and 0.71 ≈ Sep 14 (0.701).
- engine2 discounts to Aug 15, but the price is paid at closing. returns.py and levered.py use closing.
- Value should be compared with the bid at **Sep 14**. The mid-year arithmetic is otherwise correct.

**F7 — Minor (+$0.4M). Horizon truncation is immaterial.**
- 2033–2040 holds $2.6M undiscounted, worth $0.41M at PV12.
- The real issue runs the other way: the model keeps single subsea wells running down to 0.15–0.23 kb/d (Kodiak 2035), which is below plausible economic limits.
- Cutting at Kodiak 2028, Lucius 2030 and SSC 2026 costs −$1.3M.

**F8 — Minor (−$0.3M).** engine2.py:59 applies no hurricane haircut to 2018, although Aug 15 is the middle of the season.

**F9 — Minor. Shares (engine2.py:14-15) match the memo table exactly.**
- Lucius 0.02×(0.2477+0.4667) = 0.014288 ✓.
- For Stones only G17001 produces; G18730 (WR 507) is zero in every month ✓.
- Open risks:
  - SS 219 at 4%: −$2.0M.
  - The MP 59 basis differs from engine.py:33 (×0.3301), but is immaterial.
  - Orion runs to 2022, although the memo says the lease lapses around 2019: −$0.2M.
  - Leakage of the Stones allocation to WR 464 (G32690 joined the unit in Mar-2018) is not modelled.

**F10 — Minor. Upside layer** (returns.py:8-18).
- It subtracts PDP on engine2 pricing (WTI −2.3, gas ×1.1 −0.4) from WoodMac on engine.py pricing (diff −2, per-field transport, gas at HH). Part of the "upside" is therefore just a pricing-basis difference.
- It uses WoodMac Kodiak gas, which is 2–5× the actual GOR.
- It escapes the hurricane haircut (engine2.py:59-61 order).
- Lines 10-11 are a dead loop.
- None of this is in the base case, but "+25% → $167M" is overstated.

**F11 — Minor (hygiene).** engine2.py:9-13 loads HINDSIGHT Jun–Dec 2018 rows into `mon` (the CSV runs to 201812) without filtering on `public_by_2018_08_15`. Current code reads only months 1–5, so nothing leaks today. Filter at load. The CSV is a 2026 vintage that includes later operator corrections.

## Corrected PDP value ($M; PV at closing Sep 14, 2018; Aug-15 basis in brackets)

| Rate | Model | Corrected | Δ |
|---|---|---|---|
| 10% | 138.4 | **137.1** (136.0) | −1.3 |
| 12% | 133.1 | **131.5** (130.3) | −1.6 |
| 15% | 126.2 | **124.2** (122.8) | −2.0 |
| 20% | 116.6 | **114.2** (112.5) | −2.4 |

Waterfall at 12%:
1. Model as-is: 133.1
2. Re-date to closing: +1.2
3. 2018 cash timing: −1.0
4. Lag: −1.7
5. Anchor fix: +4.9
6. Horizon to 2040: +0.4
7. Rate re-anchor: −5.4
8. Result: **131.5**

Sensitivities at PV12:
- Low deck: 107.3
- Decline ×1.3: 112.2
- Lucius on pre-unit basis: 123.8
- SS 4%: 129.5

## Corrected unlevered returns (t=0 = closing; credit = Jan–Jun 2018 receipts)

| Bid | Model IRR | **Corrected IRR** | MOIC | Cash at close | Low-price IRR | Decline ×1.3 IRR | Lucius pre-unit IRR |
|---|---|---|---|---|---|---|---|
| 100 | 35.0% | **29.8%** | 1.79x | 81.4 | 16.0% | 20.1% | – |
| 105 | – | **25.9%** | – | 86.4 | 13.2% | 16.4% | 21.5% |
| 110 | 25.8% | **22.5%** | 1.63x | 91.4 | 10.7% | 13.2% | – |
| 120 | 19.1% | **16.9%** | 1.49x | 101.4 | 6.7% | 8.0% | – |
| 125 | 16.3% | **14.6%** | 1.43x | 106.4 | 5.0% | 5.8% | – |
| 130 | 13.9% | **12.6%** | 1.38x | 111.4 | 3.5% | 3.9% | – |

Levered at $110M on the corrected basis (loan $29.9M, 7.25%, 75% sweep, repaid within ~12 months of the draw): **23.4%** strip, 10.9% low, 13.5% steep decline. At $125M: 15.0% strip, 4.9% low.

## Bottom line

The corrected PDP value differs from the model by only about −$1.6M at 12%. The memo's financing story is materially wrong in three ways:
- Cash at close is ~$91M, not $81M.
- The RBL is ~$30M, not $45M.
- Levered IRR at $110M is ~23%, not 33%.

The "calibrated to $20.4M" claim is false as coded. Even when fixed, it cannot validate the Lucius unit share or the deductions.

**My bid: $105 M, walk-away $118 M**

At $105M the corrected base IRR is 25.9%. The deal still clears the 12–13% equity-hurdle floor under the low deck (13.2%) and under steep decline (16.4%), and it holds 21.5% if Lucius pays only on a lease basis. Cash at close is ~$86M, which an anchor-equity cheque plus the ~$30M RBL (refinanced in Jan 2019) can realistically cover.

The walk-away of $118M is the corrected PV15 ($124.2M) less roughly half of the two unresolved title risks: Lucius unit vs lease basis (−$7.7M) and Ship Shoal 8% vs 4% (−$2.0M). That leaves about $119M, rounded down for the Stones/WR 464 allocation risk. At $118M the base IRR is 18.0% but falls to 7–9% in the low-price and steep-decline cases.

Above that, we would be paying for the drilling upside the case says we cannot assume. That upside is also overstated as built (F10). The memo's $110M is defensible on base economics (22.5%). Its $125M walk-away leaves no margin: it sits at PV15 before any title haircut and returns only ~5% in either downside.
