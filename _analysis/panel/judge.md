# Judging panel review: decision memo v1 ("Strategy C, bid $110M")

Two judges: **CEO** (the sponsor; royalty-recovery background; has seen deals like this fail to finance) and **FAC** (faculty: analytic rigor, descriptive and predictive analysis, communication, responsible AI use). The submission is due **tonight (Nov 12, 11:59 pm CT)**, so every fix below can be done in hours.

## 1. Scorecard against the case requirements

| Requirement (close to the case wording) | Score | What costs points |
|---|---|---|
| Q1. Can you make a credible bid? What must be done in 5 weeks, and what could stop you? | 6 | There is a gate (equity signed by Aug 10) but no week-by-week plan. The fallback subset bid is only $8–12M lower, so it does not solve the money problem. |
| Q2. Funding sources, their cost and time needed; the prime rate and how it relates to the loan rate | 7 | Prime 5.00% + 2.25% is good. Equity cost and fees are left out of the returns. The loan is sized at 40% of a low-deck PV10 ($113M) that still includes $41.5M of 2018 revenue. After closing, the remaining collateral is about $75M, so the $45M loan is about **61%** of it, above the sponsor's "up to 50%". |
| Q3. Bid and maximum price; DCF to Aug 15, 2018; profit and return | 8 | Discounting to Aug 15 is correct. Missing: profit in dollars, the **allocation across all 19 interests** (the bid instruction requires it), and transaction costs. |
| Q4. Prices, production, drilling and weather; base vs. better and worse cases; biggest drivers | 7 | There is no tornado chart. The two deciding scenarios are missing: **Kodiak goes down again** (about −$17M PV for a year offline) and **Stones stays shut** (value about $112M, roughly the bid). |
| Q5. What other bidders see; value others overlook | 7 | The traps are strong, but the competitor story is inconsistent: some rivals see "$300M+", others see "$20.4M of revenue". |
| Q6. What stands out; questions for the seller | 9 | The best section. Add operator credit risk (Fieldwood, after its Ch.11) and the Lucius Jan–May true-up. |
| Facts kept separate from assumptions | 6 | Mixed in places, e.g. Ship Shoal "8% but may be 4%", and anchor equity reads as if it is available. |
| No hindsight (information as of Aug 15, 2018) | 7 | Labelled well in the notes. The leaks are in the data and assumptions (Section 5). |
| 8–10 slides, Excel or notebook, 1–2 AI slides with **at least one corrected AI response**, team names | 3 | There is no AI record yet. The model is Python with hard-coded constants; the CEO will expect an Excel DCF. |
| "Production workbook provided with the case" | ? | It is not in the folder. State that BOEM OGOR-A data and the WoodMac PDFs replace it, or confirm with the organizers. |
| FAC: descriptive and predictive analysis | 5 | Descriptive work is excellent. Decline rates (22%, 25%, 20%) are set by hand, not fitted. |

**About 68/100 today.** The underlying work deserves 85 or more.

## 2. Bid or walk away?

Most teams will **walk away**, because the case practically invites it ("can you secure the money soon enough?"). The next largest group will bid $150–300M off the WoodMac data with a vague loan. The sponsor probably lived this deal and could not finance it. A bare "Bid $110M" will not persuade him unless the team shows why its money arrives when his did not. A bare "Walk" throws away the team's advantage. The memo's decision tree also never says what is submitted at 4 pm on Aug 15.

**The hybrid scores best:** *Bid $110M for the whole package (max $125M) as lead of a **buying group** with a royalty fund that already has committed capital. Ask the seller to close on Oct 31; the Jan 1 effective date stays, so the seller gives up nothing economically. If commitment papers are not signed by Aug 13, do not bid, and register with EnergyNet as backup buyer.*
- The bid instructions explicitly allow a "buying group".
- An ORRI assignment is a non-required BOEM filing, so no regulator gates closing.
- The effective-date credit cuts the cash needed at close to about $81M.
- The team's finished title and production work removes the equity investor's "5 weeks too short" objection. Pitch line: **"The bottleneck was diligence speed, not money."** That is Lease Analytics' own product.
- Drop the subset-bid fallback.
- State the price rules plainly. $110M ≈ PV10 on the low deck ($113M): "we still earn 10% at $45 oil". $125M ≈ PV15 on the strip ($126M).

**Over-engineering: yes.** Kodiak, Lucius and Stones hold **93% of value** ($72M + $30M + $21M of $133M). Present those three and put the other six in one appendix table.

## 3. Winning storyline (in the case's required order)

| # | Headline | One visual |
|---|---|---|
| 1 | Bid $110M (max $125M) as a buying group; walk if capital is not committed by Aug 13 | Decision box: value $115–140M, bid $110M, cash at close about $81M; team name and members |
| 2 | 19 leases, but 3 fields carry 93% of value | PV-by-property bars; Attachment A decimal vs. effective share |
| 3 | The seller's $20.4M is the wrong base year; 2018 runs at about 2x | Waterfall from 2017 to 2018E: Kodiak back online, Lucius unit basis, price, declines |
| 4 | Three traps that inflate rival bids | Naive vs. verified: Lucius 4% vs. 1.43%; Pompano $71M vs. $0; WoodMac 2018 vs. BOEM actuals |
| 5 | Existing wells only, fitted to public production data | Monthly BOEM history with **fitted** decline curves; facts and assumptions colour-tagged |
| 6 | PV $115–140M at 10–20%; $110M earns about 25% unlevered | Table of PV by discount rate; bridge from bid to cash at close; profit in $, IRR, MOIC, payback |
| 7 | Funding: the problem is speed, not value | Timeline Jul 9 → Sep 14 / Oct 31 → Jan 2019: equity at 12–15%; reserve-based loan at prime 5.00% + 2.25%, at most 50% of collateral after closing |
| 8 | What would change our decision | Tornado: price, Kodiak outage, Stones stays shut, decline, hurricane, discount rate; drilling shown as an unpaid option |
| 9 | What other bidders see | Bidder map (naive WoodMac, disciplined fund, strategic buyer) vs. our bid; failed auction → backup buyer |
| 10 | Questions for the seller before we commit | Top 6 questions, fact/assumption ledger, references in the footer |
| A1–A2 | How we used AI, and where it was wrong | Tools and prompts; checks against the source PDFs and BOEM; 2–3 **real** corrections |

**Moments that will impress this sponsor:**
- Rebuilding the seller's 2017 revenue from public BOEM data.
- Lucius: 2% + 2% becomes 1.43% of the unit. That is still more than double the 2017 lease-located share (about 0.66%).
- WoodMac's Pompano is a different field, so that interest is worth $0.
- Seven of the eight Stones leases are unallocated and subject to a contraction clause.
- WoodMac's report is stale: the Lucius unit was approved three weeks before its June 12 download.
- The team **excluded a 2019 document found in the data room** (`79187.pdf`).
- The retroactive Lucius unit implies Jan–May 2018 true-ups (assumed to be about $2–3M). Ask who receives them; this is the sponsor's own recovery business.

**Noise to cut:** Kosmos as exit buyer, Hadrian North figures, Ship Shoal 8% vs 4% (3% of value), the MP 59 production payment, Orion, the Kimbell precedent, cash-sweep detail, the +100% drilling case, the INPEX/Eni label swap.

**AI corrections to use only if they actually happened:** AI applied 4% to all of Lucius; AI matched WoodMac's Pompano to MC 72; AI cited post-2018 sources.

## 4. The ten hardest final-round questions

✗ marks a question the memo cannot answer well today.

1. ✗ "Our bank said no and our investor said five weeks was too short. Who says yes, and why?"
2. ✗ "Kodiak is 54% of value, from one well that was just down for 260 days. What if it goes down in 2019?" (Answer: about −$17M PV.)
3. ✗ "Your $20.4M 'match' uses a $3/bbl deduction you picked. Isn't that circular?" Also, `engine2.rev2017()` applies the 2018 unit share to 2017 and prints **$28.9M**. A judge who opens the notebook will see this.
4. "Lucius was 19.4 kb/d in May; you assume 30. Why?" (Anadarko's Jul 31 report cites planned tie-in downtime. Put that source on the slide.)
5. ✗ "Stones was shut in from March to May. What evidence from before Aug 15 supports a 20 kb/d restart?"
6. "Seller's reserve value is $100–150M, WoodMac implies $300M, and you bid $110M. What is your probability of winning?"
7. ✗ "There are 22 payors. How do you know they pay correctly? What is the audit upside?"
8. "The seller has already been paid for January through July. How does the effective-date credit work, including Lucius suspense?"
9. ✗ "Are the decline rates fitted or assumed? Show me the fit."
10. "The instrument creating the KC 874 ORRI is missing. Why call 2% a fact?" (It is the seller's representation, so it is an assumption.)

## 5. Credibility risks

- **Calibration presented as validation.** Before deductions, the reconstruction gives $21.8M, within 7% of the seller's $20.4M; the deductions were chosen to close the gap. Say that, and fix the 2017 basis in `engine2.py`.
- **False precision:**
  - $138.4M, $133.1M, an unlevered IRR of 25.8% and a levered IRR of 32.7%: round to the nearest $5M and to whole percents.
  - 1.4288% is fine, because it comes straight from the tract factors.
- **The loan breaks the sponsor's 50% limit.** Re-size it to about $35–37M and restate the levered IRR.
- **Weak precedents:**
  - Apollo/Kimbell was preferred equity in a listed onshore company.
  - Kosmos's facility is a corporate E&P loan.
  - Neither shows that a single-package offshore royalty loan is available, and the sponsor's bank already refused one.
- **Hindsight leaks:**
  - The BOEM data was downloaded in 2026, so it includes later revisions and current operator names. "Kosmos operator from Oct-2017" is an artifact; on Aug 15 the Kosmos deal had only been announced (Aug 6).
  - The Stones restart assumption (see question 5).
  - Never cite the 2025 BOEM filing. Its "Surface to 23,000'" depth for Kodiak contradicts the data room's 17,500'–99,999'.
  - Never cite "BP still held these in 2024" or the September 2018 rate hike.
- **Jargon to define or drop:** PDP, RBL, PV10, OGOR-A, tract participation, "proportionately reduced", HPHT, MOIC, strip, contraction.
- **Checks against the sponsor's case figures:**
  - The value ($115–140M) sits inside the sponsor's $100–150M. Say so.
  - The 12% rate and the 14-year horizon fit the case ranges, but the memo never explains why they were chosen.
  - "Equity signed by Aug 10" contradicts the sponsor's own investor experience; the buying-group framing must carry it.
  - A loan after closing is consistent with "2–3 months" only if a bank will lend offshore at all. Present it as possible, never as confirmed.

---

**Verdict: Hybrid at $110M (max $125M).** Bid as lead of a buying group with committed capital and request an Oct 31 closing; otherwise walk away and register as backup buyer.

**Predicted placement:** finalist, **2nd–4th** as the memo stands; it can win with the fixes.

**The three changes that would most raise the score:**
1. **Replace the conditional fallback with the buying-group hybrid**, and re-size the loan to no more than 50% of post-closing collateral. This answers the money-in-time question on the sponsor's own terms.
2. **Build the required deliverables honestly:**
   - an AI appendix with real corrections;
   - a fact/assumption ledger;
   - the 19-line allocation;
   - an Excel DCF;
   - the $20.4M check restated as independent (within 7% gross), with the 2017 basis bug fixed.
3. **Add the predictive layer and the tornado chart.** Fit decline curves to BOEM data for Kodiak, Lucius and Stones. Lead the risks with Kodiak going offline again and Stones staying shut. Cut the noise so the 10 minutes cover three fields and three traps.
