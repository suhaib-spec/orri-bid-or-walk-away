# Panel review: reserves engineer (production assumptions)

**Bottom line.** The memo's PDP value of $133M at 12% and $126M at 15% (engine2.py) depends on one optimistic Kodiak decline and three generous starting rates. Re-running with assumptions I can defend from BOEM months public by 15-Aug-2018 gives **PDP $97.7M at 12% and $93.7M at 15%**, about 27% lower. At $110M the team is paying roughly $12–16M for undeveloped barrels while calling the bid PDP-only. The walk-away of $125M is above my P10.

Script: `_analysis\panel\scripts\reserves_panel.py`. It is a copy and does not touch engine2.py. It filters `public_by_2018_08_15 == 'Y'` and uses the same price deck, calibration and discounting as engine2.

## Challenges

### C1. Kodiak decline and availability: **Critical, −$22.6M at 12%**
- engine2.py line 18 starts Kodiak at 16.0 kb/d with 22%/yr exponential decline. That leaves **23.8 MMbbl of remaining gross oil for one completion**. WoodMac's whole two-well, multi-recompletion case is 38.8 MMbbl for 2018–33 (kodiak.md §6).
- Evidence on decline:
  - The first zone (S01, G24107) fell from 11.7 kb/d in Jun-2016 to 7.3 in Dec-2016. That is about 60%/yr effective.
  - S02 (G24102) went from 19.06 kb/d in Apr-2018 to 16.59 in May-2018, a 13% drop in one month. That is flush production after a 260-day shut-in.
  - WoodMac itself declines 24–26%/yr in 2019–21 **with** a second well being added (kodiak.md §1.4), which implies a steeper single-well decline.
  - WoodMac flags "weak drive" and compartmentalisation.
- The memo calls Kodiak "on track" (17.0 vs 16.9, decision_memo.md line 28). That is wrong reasoning: WoodMac's 17.0 kb/d includes a 1H-2018 second well, and BOEM shows exactly 1 producing completion in Feb–May 2018.
- Availability is missing entirely. The well was down 7-Jun-2017 to 22-Feb-2018, about 30% of its life since first oil, and the 2% hurricane haircut does not cover that.
- **Panel case:**
  - Jun–Dec 2018 average of 15.0 kb/d, with the decline starting from 14.5 kb/d.
  - Hyperbolic decline, first-year 35%, b = 0.5.
  - 90% availability and a 1.5 kb/d economic limit.
  - Remaining oil is 15.6 MMbbl.
  - Kodiak drops from $72.1M to $49.5M.
- Monte Carlo adds a 6%/yr chance of a well failure that ends PDP.
- Sensitivity: first-year decline of 25% gives +$13M; 40% gives −$5M.

### C2. Lucius starting rate and decline: **Major, −$5.8M**
- **The May-2018 drop is a turnaround, not the trend.** In May, all three producing leases fell 45–50% together, in oil, gas and water:
  - G21444: 10.7 → 5.8 kb/d.
  - G21447: 15.9 → 8.4 kb/d.
  - G26771: 8.1 → 5.3 kb/d.
  - That pattern points to a facility event, and Anadarko's 2Q18 ops report (31-Jul-2018, pre-cutoff, upside_structures.md A1) cites "planned downtime to tie back future wells".
- **The underlying trend is still steep:**
  - 52.2 kb/d (Dec-2017) to 34.7 kb/d (Apr-2018) is about 70%/yr annualised.
  - Jan–Apr 2018 vs Jan–Apr 2017 is −35% year on year.
  - Water is rising: KC 874 #1 at 50% and KC 919 #6 at 75% (lucius.md §1.4).
- engine2.py line 19 annotates "2017-18 decline ~35%" but inputs 25%. That is internally inconsistent.
- **Panel case:**
  - Jun–Dec average of 29 kb/d, with the decline starting from 27 kb/d.
  - Hyperbolic decline, first-year 35%, b = 0.5 (water drive flattens).
  - Remaining oil is 29.2 MMbbl vs 39.2 in the memo.

### C3. Stones restart: **Major, −$5.7M**
- BOEM shows all wells in status 12 (shut in) for Apr–May 2018.
- **No pre-cutoff source in the files explains the cause or the restart date.**
- Shell's Jul-2017 purchase of the Turritella FPSO and its Phase-2 subsea pumps due in 2018 (upside_structures.md A3) make a restart reasonably certain. The timing is not.
- An auditor would classify Stones as **PDNP (shut-in)**, not PDP.
- **Hindsight warning:** engine2.py line 20's "assume Jul restart → 20 kb/d" happens to match the Jun-2018 restart that boem_actuals.md line 39 labels HINDSIGHT. Those Jun–Dec actuals are displayed next to the inputs (boem_actuals.md lines 92, 118–122, 187–198).
- The 20% exponential decline also ignores the Jul-2017 to Feb-2018 slide from 35 to 26 kb/d.
- **Panel case:**
  - Restart about 1-Sep at 23 kb/d, so the Jun–Dec average is 12 kb/d.
  - Hyperbolic decline, first-year 30%, b = 0.5, with a 5 kb/d FPSO economic limit.
  - The Monte Carlo samples restart months from July to November, plus a 10% chance of no restart before mid-2019.
- **WR 464 is a second issue.** G32690 has carried the Stones unit number since Mar-2018 (public), and its well SN206 was completed in Sep-2017. A participating-area revision would dilute the 1.5%. The SN206 barrels may offset that. I did not apply a haircut, but this is an open item.

### C4. South Santa Cruz: **Minor, −$1.0M**
- A single well has held 3.1–4.5 kb/d since Jun-2017. That looks like a choke-managed plateau.
- A 15% exponential decline to 2035 implies 7.3 MMbbl from one well. When the plateau breaks, decline will be steeper.
- Panel case: first-year decline 25%, b = 0.3, giving 3.5 MMbbl.
- The second well WoodMac expected to spud in early 2018 does not appear in BOEM borehole data. It is not PDP.

### C5. Decline form, end years and horizon: **Major (conceptual)**
- A constant 20–25% exponential decline does not fit these assets:
  - Lucius is a water-drive field after breakthrough.
  - Kodiak is an HPHT depletion well.
  - Stones is Lower Tertiary.
- All three show 35–60% early declines in BOEM. A hyperbolic decline with b = 0.3–0.5 is the industry norm: steep early, then a longer tail. At 12–15% discount rates, the early steepness is what counts.
- The 2032 horizon is irrelevant: extending to 2040 adds only $0.4M in engine2.
- What matters is **economic limits**. The end years of 2035–2040 are never tested against the host's operating cost (Devils Tower life, an FPSO at 5 kb/d). In the panel case, economic limits cost about $6M; without them the panel value is $103.9M.

### C6. Is PDP-only the right reading of the case rule? **Major, upside to the team**
The case rule bars assuming when *future* drilling happens. It does not require ignoring wells already drilling or shut-in wells. How an auditor would classify each item:

| Item | Class | Pre-cutoff evidence |
|---|---|---|
| Stones restart | PDNP (shut-in) | OGOR status 12 |
| KC 919 #5ST3 tubing rework | PDNP (workover) | Permit filed (WoodMac) |
| **Hadrian North, inside the Lucius unit** | **PUD, under development** | 10-K Feb-2018 says sanctioned; Anadarko 2Q18 says first well spud Q2-2018, first oil 2019 |
| Lucius 9th well | PUD or probable | WoodMac only (Q4-2018) |
| Stones Phase 2 (6 wells) | PUD | Trees ordered, pumps due 2018 |
| Kodiak 2nd well, SSC 2nd well | Contingent (not proved) | No BOEM borehole; operator mid-sale to Kosmos |

- Hadrian North barrels earn 1.4288% because they sit in the unit, if the reservoirs are in the participating area.
- WoodMac treats Hadrian North as a tariff-paying tieback (lucius.md §0 item 3), so its unit status must be confirmed with the operator.
- Risked at 50–70%: about **+$5–12M**. This is my estimate and is not modelled.
- The memo instead prices undeveloped barrels implicitly, through a bid that sits above a correctly stated PDP.

### C7. Gas: **Minor, −$0.4M**
- GAS_MULT 1.10 is applied to OGOR-A **wet, pre-shrink** gas (boem_actuals.md line 8). Shrink, fuel and NGL offsets roughly cancel the Btu uplift, so 1.0 is safer.
- Gas is under 4% of value: Kodiak's GOR is about 0.8 mcf/bbl and Grand Isle is worth $0.9M.
- MP 59 gas fell from 4.4 to 1.7 MMcf/d in 2018, and its 10% decline is fine at that base.

### C8. Hurricane 2%/yr: **Minor as sized; Major as the only downtime term**
- 2% matches the EIA mean (market.md §4a). 3% costs only −$0.6M.
- The real omission is **operational availability**. This package lost:
  - Kodiak for 260 days.
  - Stones for 3+ months, plus Sep-2017.
  - Lucius for about half of May.
- Starting rates taken from good months need 90–97% availability on top of the hurricane haircut. Removing availability from the panel case adds about $5M.

### C9. Process and hindsight flags: **Minor**
- engine2.py line 5 reads every CSV row with no `public_by_2018_08_15` filter. It is safe today only because the months are hard-coded through May-2018.
- upside_structures.md A2 cites a "later BP filing" giving Kodiak depth as "Surface to 23,000'". That filing is HINDSIGHT, and it contradicts the instrument's 17,500'–99,999' (kodiak.md §2.3). Delete it.
- market.md cites an EIA article dated 5-Oct-2018. The data in it is historical, but the source postdates the cutoff.
- engine2's printed "2017 calibration" is $28.9M, not $20.4M, because it applies the unit share to 2017. The real tie-out is in boem_actuals.md lines 42–68. Fix the printout before anyone audits it.

## Quantification (PDP only, strip, 2% hurricane, same timing and calibration as engine2)

| Case | 12% | 15% |
|---|---|---|
| Memo (engine2) | 133.1 | 126.2 |
| **Panel base** | **97.7** | **93.7** |
| Panel, low deck (45 / 2.25) | 81.4 | n/a |
| Panel, no economic limits | 103.9 | 98.5 |

Bridge at 12%, swapping one property at a time into the memo case:

| Change | Δ |
|---|---|
| Kodiak | −22.6 |
| Lucius | −5.8 |
| Stones | −5.7 |
| SSC | −1.0 |

Monte Carlo (10,000 runs):
- Inputs varied: rate ±10%, decline ×0.7–1.4, b ±0.3, Stones restart timing, Kodiak failure at 6%/yr, price lognormal σ = 18%.

| Case | P90 | P50 | P10 |
|---|---|---|---|
| 12% | $74M | $92.5M | $113.5M |
| 15% | $72M | $89M | $108M |
| Production only at strip, 12% | $78M | $93M | $106M |

- **$110M sits at about the P15 of value.** $125M is beyond the P10.
- Kodiak is still 51% of panel value, so the range is really a one-well range.

## Effect on the bid
- The 2018E revenue behind the effective-date credit falls from $41.5M to about $37M.
- Every return in decision_memo.md lines 36–38 is built on the $133M PDP stream and is overstated by roughly 5–8 IRR points at $110M. This is my estimate; I did not rerun levered.py.

**My bid: $95 M, walk-away $105 M.**

**Justification.** $95M is about my PDP value at 15% ($93.7M). That is the norm for offshore PDP with single-well and host risk, and it sits at about the P50 of a distribution that includes a Kodiak failure and a late Stones restart. Above that, I would pay only for development that is **already happening** before 15-Aug-2018, mainly Hadrian North drilling inside the Lucius unit plus the Stones restart upside, risked at about $5–12M. That takes the walk-away to $105M, which is near my 12% P50 plus a partial in-progress credit. I would not go higher, because the memo's $110–125M range only clears if Kodiak declines at 22% and does not fail again. The data shows a 60% first-zone decline and a 260-day outage. The fastest way to close the gap is to ask the seller (and Kosmos) for Kodiak's current rate and pressure, and the cause of the Stones shut-in. If those come back favourable, moving toward $110M is justified on evidence rather than assumption.

## Rebuttal round

Script: `panel/scripts/reserves_rebuttal.py`. It puts my production inputs on the auditor's mechanics: PV at closing, 2018 monthly cash timing, 60-day lag, Sep-anchored decline, horizon 2040. Only rows public by 15-Aug-2018 are used. Run on the memo's inputs it gives $136.9M at 12%; less the auditor's −$5.4M rate re-anchor that is his $131.5M, so the mechanics tie.

**Q4. No, my $97.7M did not include the indexing fix.** On corrected mechanics my existing wells are worth **$104.4M at 12% and $99.7M at 15%**, $27M below the auditor. The gap is purely production. The Monte Carlo P50 is $98.3M / $94.2M, pulled down by Kodiak failure risk and Stones timing.

**Q5. Kodiak: my case is the P50.**
- The same zone fell from 14.2 kb/d (Feb-2017) to 12.7 (May-2017), about 37%/yr effective. The first zone fell about 60%/yr.
- 90% uptime is generous against the roughly 66% achieved since first oil.

| Kodiak, $M | 12% | 15% |
|---|---|---|
| Deterministic P50 | 52.8 | 50.4 |
| Monte Carlo P50 (incl. well failure) | 47.7 | 45.9 |
| Monte Carlo P90 | 32.3 | 31.7 |

The memo's 22% decline sits near my P10 ($59.6M; my 25% case gives $66.1M).

**Q1. Auction strategist.**
- I agree the case rule bars a fixed schedule, not a risked and delayed value for wells under way.
- But "WoodMac-minus-PDP" is a residual. It re-labels WoodMac's optimism on *existing* wells as development, and it grows as PDP is corrected (Lucius 50.3 vs 36.8 kb/d actual; Stones 60.3 vs about 10).
- Only Hadrian North is sanctioned with a spud before the cutoff. Stones Phase 2 has no spud. The Kodiak second well has no borehole and its operator is mid-sale.
- Priced item by item with type curves, the four items are about $59M unrisked and **$13M risked** (table below).
- At $132M, existing wells return about **0%**; at $110M, 8.9%.
- **Deck:** base = existing wells (PDP plus the Stones restart, as PDNP). Upside goes on a separate line; label Hadrian North "sanctioned" and the rest "planned".

**Q2. Hadrian North.**
- Exhibit C (effective 1/1/2018) already carries KC 918/919 at 10.39% and 18.17%. The expansion dilution is already inside 1.4288%; further dilution needs an Article 11.4 revision.
- The attorney is right on tariffs: if Hadrian North is a separate participating area or tieback, the ORRI gets nothing.
- 80% execution × 40% chance of unit allocation gives **+$3.2M**, less about $0.5M of revision risk to the base. Net about +$3M, down from +$5–12M.

**Q3. Stones royalty relief.**
- The Hart mitigant is strong: Stones is 28% of the $20.4M, and without it the tie-out fails.
- Hart's figure may be pro-forma rather than actual receipts, so I carry a 10–15% probability: **−$2M**. Stones goes from $16.9M to about $14.9M.
- Require Shell remittances and an indemnity.

## Final numbers ($M, PV at closing)

| Item | 12% | 15% |
|---|---|---|
| Existing wells, deterministic | 104.4 | 99.7 |
| Existing wells, Monte Carlo P50 | 98.3 | 94.2 |
| Title expected value (SS 4%, Stones relief, Kodiak continuity, other) | −5.0 | −5.0 |
| **Existing wells P50, net of title** | **93.3** | **89.2** |
| Upside: Hadrian North (80% × 40%) | +3.2 | +2.9 |
| Upside: Lucius 9th well / rework (30%) | +2.3 | +2.1 |
| Upside: Stones Phase 2 (30% × 0.8) | +3.3 | +3.0 |
| Upside: Kodiak 2nd well (15%, 2020) | +4.0 | +3.6 |
| **Risked upside total** | **+12.8** | **+11.6** |

**Final: bid $100 M, walk-away $110 M.**
- The bid is the existing-wells P50 at 12% net of title ($93M) plus Hadrian North and about half of the other risked items.
- The walk-away is deterministic existing wells net of title ($99M) plus the full risked upside ($13M), rounded down for the one-well Kodiak concentration.
- The strategist's own simulation gives a 57% chance the auction fails. That favours a disciplined standing offer near $110M over $132M.
