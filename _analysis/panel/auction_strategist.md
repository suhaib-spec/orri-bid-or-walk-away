# Panel review: auction strategist (A&D banker + auction economist)

**Verdict.** The memo is strong on diligence but weak on strategy. A $110M bid has roughly a 0–5% chance of being awarded. In practice it is a walk-away presented as a bid. The fix is to value the development that is already sanctioned and being drilled (risked and delayed, not assumed away), bid about $132M, and sell certainty of closing.

Basis for the numbers: the team's own engine2/returns code, plus my auction simulation (scratchpad `auction/sim2.py`). All inputs are from before Aug 15, 2018.

---

## 1. Who bids, and what would they pay? — Major

| Bidder type (2018) | Package-bid odds | Rate / deck | Uses WoodMac? | Indicative bid |
|---|---|---|---|---|
| Private royalty funds and family offices with GoM experience (RAHR/Fairfield-type vehicles, LLOG-style royalty affiliates) | High (2–3 bidders) | PV12–15; strip, then $55–60 flat | Yes, haircut 15–30%, development risked 25–50% → value $150–185M | **$125–155M** |
| Trailing-multiple screeners | Medium | 5–7x the $20.4M 2017 revenue | Lightly | $100–140M |
| Non-op deepwater WI investors (Ridgewood, Houston Energy, Red Willow) | Single assets they already know | PV10–15 | Have their own data | $5–30M per asset |
| Burdened operators: Kosmos (Kodiak + SSC, DGE deal announced Aug 6), Shell (Stones) | Low before Aug 15; natural buyers after close | Corporate WACC 8–10% | Have their own drilling plans (informed bidders) | Kodiak alone could reach $70M+ |
| Streamers or public mineral companies (Franco-Nevada, Black Stone, Viper, Kimbell) | Low (onshore mandates) | 7–10% cost of capital | Yes | Tail risk: would outbid everyone |

**How rivals use the data.** Most rivals will start from BP's data room. Few will rebuild production from BOEM OGOR-A the way the team did. WoodMac's 2018 forecasts overstate actual production: Lucius 50.3 vs 36.8 kb/d, Stones 60.3 vs about 10 kb/d (Jan–May average; shut in Mar–May). Some rivals will also treat WoodMac's "Pompano" field as the ORRI area. Rival bids are therefore biased **upward**. That hurts the team's chance of winning but raises the chance that a rival re-trades the price later. Section 5 uses that.

## 2. Is $110M likely to win? — Critical

- **What BP sees.** BP receives the royalty checks. 2018E package revenue is about **$41.5M**, roughly double 2017 (Kodiak back online, the Lucius unit share, higher prices). On that basis $110M is **2.7x 2018E and 3.3x 2019E PDP cash flow**. Even the 5.4x multiple on 2017 revenue sits at the bottom of the sponsor's own $100–150M range. BP will read it as a lowball.
- **BP's likely reserve price: about $135–150M (central $140M).** The reasons are all knowable in 2018:
  - The asset costs BP nothing to hold (no opex, capex or ARO), so there is no pressure to sell.
  - BP's WoodMac-based view is $200M+.
  - Run-rate cash flow is about $40M a year.
- **Note on wording.** "Reserve value" in the case means the value of the oil and gas reserves, not the auction's minimum price. Say this explicitly. It still signals where the market sits.

**Simulated winning-bid distribution.** Assumptions: 1–4 serious rivals, correlated bids, central rival $125M, reserve $140M.

| | p10 | p50 | p90 |
|---|---|---|---|
| Best rival bid | $110M | **$135M** | $166M |

Chance the auction fails (no rival meets the reserve): **about 57%** (39–67% across scenarios).

| Our bid | P(top bid) | P(awarded) | P(awarded), low-rival scenario |
|---|---|---|---|
| $110M | 10% | **≈0–2%** | 2% |
| $125M | 31% | 5% | 23% |
| $132M | ~44% | ~14% | ~42% |
| $140M | 58% | 29% | 63% |

## 3. Winner's curse: is "Bid" really "Walk away"? — Critical

Yes. The team's PDP value is $126M at 15% and $117M at 20%. At those values, **no bid in the simulation produces meaningful positive expected surplus**. Under its own model, the rational action is to walk.

The underlying error is reading the case's rule ("cannot assume when or how much") as "assign zero". The rule forbids assuming a fixed schedule. It does not forbid risking and delaying wells that are already sanctioned. As of Aug 15:

- **Hadrian North:** inside the Lucius unit, sanctioned, first well spud Q2-2018 (Anadarko 2Q18 ops report, Jul 31, 2018).
- **Stones Phase 2:** subsea pumps due for delivery in 2018.
- **Kodiak second well:** planned, but the operator is mid-sale.

A "sanctioned-only" layer risks these at 50%, 25% and 15% of WoodMac-minus-PDP, delayed one year:

| Case | Value |
|---|---|
| Sanctioned-only, 15% | **$160M** |
| Sanctioned-only, 20% | **$144M** |
| Sanctioned-only, low deck ($45/$2.25), 12% | $148M |

Winner's-curse check: the operators are better informed, so do not bid alone on single assets such as Kodiak, where Kosmos knows more. The BOEM anchoring makes the team's PDP estimate less noisy than rivals', which partly offsets the curse. **Keep the low-price downside visible:** at $132M with PDP only and $45 oil, IRR is about 3% (1.08x). Hedge 2019–20 oil at about $60–63.

## 4. Package versus separate bids, and allocation — Major

- **Primary bid.** A conforming whole-package bid that is non-severable, except for one defined alternate.
- **Alternate.** Kodiak + Lucius + Stones at about **$122M** ($10M below the package).
  - It does not solve funding: it is only 7% cheaper.
  - It leaves BP with the tail of 6 interests and their payors, so BP will rank it below package bids.
  - Use it as an option for BP, not as the fallback plan.
- **Allocation is a contract term, not decoration.** In the PSA, allocated values set title-defect adjustments, exclusion prices and any preferential-right prices.
  - **Allocate fully to interests with open title questions:** Ship Shoal at 8% (if it is 4%, the claim recovers about $1.6M), Kodiak depth coverage, the Lucius unit basis, the MP 59 production payment.
  - **Allocate fully to Kodiak**, so a separate Kosmos-style Kodiak bid cannot beat the team on the allocation comparison.
  - **Move weight toward Lucius and Stones** (risked value), because those are the assets BP marketed. 16% on Stones looks dismissive.
- **Suggested allocation at $132M:**

| Interest | Allocation |
|---|---|
| Kodiak | $59.0M |
| Lucius | $41.0M (KC 875 $26.6M / KC 874 $14.4M) |
| Stones | $24.0M (WR 508 $20M; 7 other blocks $0.57M each) |
| Ship Shoal 219 | $3.2M |
| South Santa Cruz | $2.2M |
| MP 59 | $1.0M |
| GI 110/116 | $0.8M |
| Pompano | $0.5M |
| Orion | $0.3M |

- **Pompano at $0 is risky.** It can be read as excluding the interest, which makes it a partial bid. Use a **nominal $0.5M** with a short footnote: the ORRI covers only production above 13,405 ft in MC 72 S/2, and there has been no production in that area since Oct 2014. The footnote shows title skill. It also makes BP question any rival bid built on WoodMac's "Pompano" field, which will be re-traded in confirmatory diligence.

## 5. Non-price terms — Major

**Credible for this team:**
- **No re-trade pledge.** Title review of all 19 interests is already done from source documents, so only confirmatory diligence is needed.
- **Fast, unconditional closing.** No BOEM approval is needed (ORRI assignment is a non-required filing). No HSR filing is needed, because 16 CFR 802.3 exempts oil and gas reserves up to $500M. *Verify both with counsel.* Close on or before Sept 14.
- **No casualty-loss condition.** An ORRI has no facilities, so this costs nothing during hurricane season.
- **Accept BP's form PSA,** with a defect threshold of about $250k and a deductible of about 2%.
- **Effective-date settlement** on BP's revenue statements, with a 90-day true-up.

**Credible only if the anchor-equity letter is signed:**
- 10% deposit at award (about $13M).
- "No financing contingency".
- Proof of funds.

Without those, a small bidder's offer is worth less to BP than a lower bid from a known fund. Note also that BP asked for *binding* proposals. The "equity by Aug 10" condition decides whether to submit at all; it cannot be written into the bid letter.

## 6. Backup buyer if the auction fails — Minor (valid, but close to hindsight)

This argument is valid on 2018 facts alone:
- The asset costs the seller nothing to hold.
- The data room overstates 2018 volumes against BOEM actuals.
- An all-cash, five-week timeline thins the field (the sponsor's own bank and equity investor declined).

Present it as a **standing offer**: "If no bid clears, we remain a buyer at up to $140M for 90 days." By then the 2–3 month RBL can be approved, so the case's financing obstacle becomes an advantage in round two.

**Hindsight to strip from the deck:**
- The BOEM 87222 filing (BP still held 6 of 9 interests in 2024) and every "Hadar / Five Stones" reference.
- Sources published after Aug 15: Argus Sep 5, 2018; Haynes Boone Fall-2018; Mercer Dec 2018; Citi/SPEE Jan 2019; CME FedWatch Aug 20–22.
- The Franco-Nevada/Continental precedent, unless its announcement date can be confirmed as on or before Aug 15.

The failed-auction thesis must visibly rest on the three 2018 reasons above.

## 7. Other challenges

- **Major — funding scale.** At $132M, cash at close is about $103M after the roughly $29M effective-date credit, about $22M more equity than at $110M. Size the anchor-equity ask accordingly.
- **Minor — tie-breaking.** Use a non-round number ($131.7M) to avoid ties with rivals bidding round numbers.

## Bottom line

**Bid**, only if the anchor-equity commitment is signed by Aug 10. Otherwise walk away and send the standing-offer letter.

At $132M (team engine), unlevered IRR is:

| Case | IRR |
|---|---|
| PDP only, strip | 13% |
| PDP + sanctioned development, strip | 30% |
| PDP + sanctioned development, $45 oil | 20% |

Walk-away $140M is at or below every conservative-but-not-zero value: PDP at 10% ($138M), sanctioned-delayed at 20% ($144M), and sanctioned at 12% on the low deck ($148M).

**Pitch:** *"A fully funded, no-re-trade, close-by-Sept-14 bid for the whole package, from the one buyer whose title work is already done, and who will still be here if the auction doesn't clear."*

**My bid: $132M (submitted as $131.7M), walk-away $140M.** $110M has about a 0–5% chance of award and leaves BP no reason to deal. $132M roughly triples the base-case award odds (about 14%, or about 42% if rivals anchor on PDP). It still clears a 13% PDP-only IRR, and its value rests only on wells that were sanctioned before Aug 15, risked and delayed by a year.

## Rebuttal round

**I withdraw $132M / $140M.** That price rested on about $34M (at 15%) of value from wells already sanctioned. The panel's evidence removes most of it.

**1. Reserves engineer (concede most).**
- Kodiak's first zone fell about 60%/yr, the 2018 restart dropped 13% from April to May, and the well was offline about 30% of its life. That beats a 22% exponential decline.
- I don't take the full $94M at 15%: it stacks availability, a 35% hyperbolic decline and economic limits, and a 25% first-year decline adds $13M.
- My existing-wells value: **about $100M at 15%, about $105M at 12%**.
- Paying $20–35M for undeveloped value is acceptable to neither the case rule nor an anchor investor writing first-loss equity.

**2. Title attorney (concede Hadrian North and Ship Shoal; Stones partly).**
- **Hadrian North:** joining the participating area dilutes the KC 874/875 tract factors, and the tariff goes to the WI owners. I credit **$0**.
- **Ship Shoal:** use 4% (−$1.5M).
- **Stones royalty relief:** the 2017 revenue tie-out only works if Shell was paying about $5.7M. I carry an expected-value haircut of about $2M, not $17M, and require remittance history plus an indemnity.
- **Surviving upside:** Stones Phase 2 at 25%, the KC 919 rework, Kodiak's second well at 10%. Net of title expected-value haircuts, about $5–8M.
- **Value: about $103–108M at 15%.**

**3. Capital markets (concede).** At $132M:
- Cash at close is $113M or more.
- Committed capital with a 15% hurdle and an 8–10% downside floor cannot fund it in five weeks.
- The return on existing wells at $45 oil is about 3%.

It was not fundable.

**4. Competition vs. auction (steelman).**
- **Case for a fundable ~$105–115M bid:**
  - The value base fell about $25M.
  - Funding is the constraint the sponsor actually hit.
  - A bid that can't close, or gets re-traded, is worse than losing.
- **Case for bidding higher:**
  - About 5% odds of award is theatre.
  - A bid far below BP's minimum price may not earn the backup call.
- **Resolution:** my $140M minimum price and $125M rival median were assumptions. Revised inputs:
  - 0–3 funded rivals, with a 20% chance of none.
  - Rivals around $120M.
  - BP's minimum around $130M ± 15%.

  On those, the auction fails about 54–65% of the time. Round two goes to committed money with finished diligence. Being the **top** sealed bid (about 39% at $110M) matters more than clearing BP's minimum. **Bid what you can fund, state the odds, and make the standing offer the real play.**

**5. Buying-group hybrid with an Oct 31 closing.**
- It doesn't change the value, so it doesn't change the number.
- It does help funding:
  - about 6 more weeks for the anchor's investment committee;
  - a closing credit of about $25M (Jan–Aug receipts), cutting cash at close by about $7M.
- It costs BP about $1M of time value. Offset that with a 10% hard deposit at award and an alternative Sept 14 closing.

### Final numbers

**Bid $108M** (submitted as $107.9M), whole package, as lead of a buying group, with a 19-line allocation. **Walk-away $115M.**

Moving toward $115M requires BP to confirm before award:
- Kodiak's current rate and pressure;
- the cause of the Stones shut-in;
- that Shell is paying the Stones ORRI despite royalty relief.

No anchor commitment signed by Aug 13 means **do not bid**. Instead, give BP a 90-day standing offer for up to $115M.

**Win probability** (revised base case, range across scenarios):

| Bid | P(top sealed bid) | P(award at bid) |
|---|---|---|
| $105M | 34% | 3% (0–6%) |
| $110M | 39% | 5% (1–11%) |
| $115M | 46% | 10% (2–18%) |
| $120M | 52% | 16% (4–26%) |

At $108M, including a counter-offer up to $115M, the chance of a deal is about 10%. The chance the standing offer comes into play is about 55–65%.

**My bid: $108M, walk-away $115M.**
