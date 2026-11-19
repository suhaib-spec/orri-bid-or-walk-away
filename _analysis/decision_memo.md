# Decision memo (v1, pre-panel) — "Bid or Walk Away?" ORRI package

Case: UNT Business Analytics Hackathon 2026, sponsor Lease Analytics (CEO Tom Agnew, also founder of EquityMetrix, royalty-underpayment recovery).
Role-play date: valuation as of Aug 15, 2018 (bid due 4pm CST). Effective date 1/1/2018. Award Aug 30, closing Sept 14, 2018. All-cash. NO HINDSIGHT allowed (nothing public after Aug 15, 2018).
Case figures from sponsor: 10–15 yr investment life; discount rate 10–20%; "reserve value" $100–150M; loan up to 50%; bank declined offshore exposure (hurricanes); bank approval takes 2–3 months; an equity investor said 5 weeks is too short. Case rule: "you cannot assume when [drilling] will happen or how much it will add."
Deliverable: 8–10 slide deck + Excel/notebook + 1–2 slide AI appendix (must include at least one AI response the team corrected). Facts must be kept separate from assumptions.

## Recommendation: "Strategy C — disciplined, fundable bid"
- Bid **$110M** all-cash for the whole package. Walk-away max **$125M**.
- Condition: bid only if an anchor-equity commitment is signed by ~Aug 10, 2018; otherwise submit a top-3 subset bid (Kodiak + Lucius + Stones, ~$8–12M lower) or walk away and position as backup buyer.
- Allocation by PDP value: Kodiak ~54%, Lucius ~23% (KC 875/KC 874 ≈ 65/35 by tract factors 46.67/24.77), Stones ~16% (mostly WR 508), SSC ~2%, Ship Shoal ~3%, rest small; Pompano and Orion nominal.

## Title/share conclusions used (see kodiak.md, lucius.md, stones.md, mc_trio.md, shelf_trio.md)
| Property | Net ORRI (Attachment A) | Effective share of unit/field production used |
|---|---|---|
| Kodiak (MC 727/771) | 0.06375 each | 6.375% of unit production (10% × 63.75%), 17,500–99,999 ft |
| Lucius (KC 874/875) | 0.02 each | 1.4288% of unit (2% × (24.77%+46.67%)) — unit effective 1/1/2018 |
| Stones (8 WR blocks) | 0.015 | 1.5% (only WR 508 allocated production; 7 other leases risk contraction ~2021) |
| South Santa Cruz (MC 563) | 0.0093 | 0.93% |
| Grand Isle 116 unit | 0.005 | 0.5% below 13,000 ft |
| Main Pass 59 | 0.02604167 | 2.604% (5/192); $750k production payment payout unverified |
| Ship Shoal 219 | 0.08 | used 8% but flagged may be 4% |
| Orion (MC 110) | 0.013125 | ~$0, lease likely lapses ~2019 |
| Pompano (MC 72 S/2…) | 0.05625 | $0 — ORRI covers only LLOG/Nexen-assignee production in limited area to 13,405 ft; WoodMac "Pompano" is a different field; no ORRI-area production since Oct 2014 |

## Data and model
- WoodMac PDFs (downloaded for BP 2018-06-12) → Rem PV = PV10 of gross revenue at 1/1/2018. Naive WoodMac-based ORRI value ~$300M+ unrisked; risked strip ~$200–255M.
- BOEM OGOR-A monthly production (public through ~May 2018) shows WoodMac 2018 overstated: Lucius 50.3 kb/d forecast vs 36.8 actual Jan–May (May 19.4); Stones 60.3 vs 25.8 Jan–Feb then 0 Mar–May (shut in); SSC 13.7 vs 3.5; Kodiak 17.0 vs 16.9 (on track after 260-day outage 6/7/2017–2/22/2018).
- 2017 ORRI revenue reconstructed $20.4M after $3/bbl and $0.40/mcf deductions = matches Hart listing "$20.4M 2017 net revenue" (~5%).
- engine2.py PDP-only (existing wells), BOEM-anchored, strip deck (WTI 66.5/64.5/61/58.5/57 flat; HH 2.95/2.82/2.66/2.65), 2%/yr hurricane haircut, horizon 2032, calibration OIL_ADJ 0.7 / OIL_DED $3 / GAS_MULT 1.10 / GAS_DED $0.40.
- PDP inputs (Jun–Dec 2018 gross oil kb/d, gas mmcf/d, decline, end): Kodiak 16.0/13.0/22%/2035; Lucius 30/29/25%/2040; Stones 20/3/20%/2040; SSC 3.4/1.8/15%/2035; GI 1.5/18.5/18%/2030; MP 0.35/1.6/10%/2032; SS 0.6/2.8/20%/2025; Orion 0.4/0/20%/2022.
- PDP value @10/12/15/20%: $138.4 / 133.1 / 126.2 / 116.6M. Low price (45/2.25) $108.9M; high (75+2%) $161.5M; decline ×1.3 $112.7M, ×0.7 $161.9M. Kodiak ~54% of value.
- Drilling upside layer (WoodMac strip revenue minus PDP, floored 0): +25% risked → $167M, +50% → $201M, +100% → $270M.

## Returns
- Effective-date credit: ~70% of 2018E revenue ($41.5M) ≈ $29M credited at closing → cash at close ≈ $81M on a $110M bid.
- $110M: unlevered IRR 25.8%, MOIC 1.61x; levered equity IRR 32.7% (strip), 14.5% (low price), 16.5% (steep decline).
- $125M: levered 18.6% strip, 4.7% low price.

## Funding plan
1. Effective-date credit cuts cash at close to ~$81M.
2. Anchor-equity commitment letter (royalty fund / family office, target 12–15%). Precedent: Apollo $110M into Kimbell (2018), ~6.5 weeks.
3. Post-close RBL ~4 months later: ~$45M (40% of low-deck PV10) at prime 5.00% + 2.25% = 7.25%, 75% cash sweep; Gulf-experienced lenders (e.g., Kosmos's bank group behind its Aug 6, 2018 Deep Gulf Energy deal).
4. Hedge 2019–20 oil (~$60–64). ORRI owners carry no decommissioning liability (30 CFR 250.1701).

## Competitive read
- Bidders anchoring on BP's WoodMac data will see ~$300M+; seller expectation likely high → bid-ask gap → possible failed auction → position as credible fallback buyer.
- Traps: Pompano at $71M, Lucius at 2%/4%, double counting per-block lines, Ship Shoal 8 vs 4%.
- Overlooked value: effective-date credit, Lucius unitization roughly doubling ORRI share vs pre-unit, Stones all-8-blocks coverage for Phase 2, Hadrian North into Lucius unit, Kosmos as natural buyer for Kodiak/SSC.

## Seller questions
Payment history by payor; Lucius unit-basis payments or suspense; why Stones shut in Mar–May 2018; Kodiak suspension approvals, depth coverage, 2nd well; missing instruments (KC 874 creation, Amoco→BP, MP 1979 letter, LLOG 2007 farmout, SSC Oct 2014 agreement, WR 551 page); Ship Shoal 4% vs 8%; why WR 199 excluded; Stones Exhibit C & WR 464 allocation.
