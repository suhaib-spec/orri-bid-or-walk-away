# FINAL DECISION v2 (after 6-expert panel + rebuttal round)

Panel reports: `panel/` (reserves_engineer, model_auditor, title_attorney, capital_markets, auction_strategist, judge).
IRR grid: `python -I panel/scripts/final_irr.py "<_analysis path>"`. Allocation shares: `panel/scripts/alloc.py`.

---

## 1. The decision (slide 1)

**BID $105M all-cash for the whole package, as lead of a buying group. Never pay more than $115M.**
- **Go/no-go gate (internal, not in the bid letter):** a royalty fund with already-raised capital signs an unconditional commitment by **Aug 13, 2018**. No signature → do not bid; send BP a 90-day standing offer instead.
- **$105M = our P50 value at a 12% return**, counting existing wells plus only *risked* development (~$93M existing-wells P50 after title risk + ~$13M risked development).
- **$110–115M** only if BP confirms before award: (1) Kodiak's current rate/pressure, (2) why Stones was shut in Mar–May 2018 and that it has restarted, (3) that Shell has been paying the Stones ORRI despite royalty relief.

## 2. How the panel moved us

| Expert | Opening call | Final call |
|---|---|---|
| Reserves engineer | $95M / $105M | **$100M / $110M** |
| Model auditor | – | **$105M / $118M** |
| Title attorney | – | **$105–110M / $120M** (with title protections) |
| Capital markets | – | **$105M / $115M** |
| Auction strategist | $132M / $140M | **$108M / $115M** (withdrew $132M) |
| Judges | $110M / $125M (pre-correction numbers) | hybrid "buying group" structure |
| **Consensus** | | **≈ $105M bid, ≈ $115M walk-away** |

What changed vs. v1 ($110M / $125M):
1. **Kodiak declines faster than 22%/yr.** Public BOEM data: 1st zone 11.7→7.3 kb/d in 6 months (2016); 2017 zone ≈ −37%/yr; 2018 restart −13% Apr→May; the well has run only ~66% of the time since first oil. Kodiak is >50% of value, so this is the biggest swing.
2. **Cash at close is ~$90M, not $81M.** BP only credits money it has *received* by Sept 14 (~2-month payment lag → Jan–Jun 2018 receipts ≈ $17.5M, not $29M). The rest arrives at final settlement.
3. **Post-close loan is ~$25–30M, not $45M** (v1 sized the loan on 2018 revenue already credited away).
4. **Ship Shoal is 4%** (the 8% override was carved from Amoco's 50%). 8% is upside only.
5. **New risk: Stones royalty relief.** WR 508 is a deepwater royalty-relief lease; the Stones ORRI is "calculated in the same manner as Lessor's royalty" with no protective clause (Kodiak, KC 875 and SSC all have one). Mitigant: the 2017 $20.4M tie-out only works if Stones was being paid. Priced as ~−$2M expected value + seller indemnity.
6. **Dropped "upsides":** Hadrian North (risked ≈ +$3M only — tariff goes to working-interest owners if it's a separate tieback) and Kosmos as exit buyer.

## 3. The numbers (all valued at closing, Sept 14, 2018; strip prices as of Aug 15, 2018)

**Two production views, both from public data — we show both.**

| | Cautious view (panel engineer) | Operator-trend view (our v1 inputs) |
|---|---|---|
| Kodiak | 15 kb/d, 35% 1st-yr hyperbolic, 90% uptime | 16 kb/d, 22% exponential |
| Lucius | 29 kb/d, 35% | 30 kb/d, 25% |
| Stones | restart Sep-2018 | restart Jul-2018 |
| **Existing wells PV @12%** | **$102M** | **$133M** |
| **Existing wells PV @15%** | **$98M** | **$126M** |

**Unlevered IRR on cash paid at closing** (Ship Shoal at 4%; Jan–Jun receipts credited at closing):

| Bid | Cautious, strip | Cautious, $45 oil | Cautious, Kodiak dies 2020 | Operator-trend, strip | Operator-trend, $45 oil |
|---|---|---|---|---|---|
| $100M | 13.5% | 2.3% | −2.8% | 30.3% | 16.4% |
| **$105M** | **10.5%** | **0.0%** | **−5.4%** | **26.5%** | **13.6%** |
| $110M | 7.8% | −2.0% | −7.7% | 23.1% | 11.1% |
| $115M | 5.4% | −3.9% | −9.7% | 20.2% | 9.0% |
| $125M | 1.4% | −7.0% | −13.1% | 15.2% | 5.4% |

(The cautious columns exclude all development upside; adding the ~$13M risked development lifts them by roughly 2–3 points.)

**How to say it:** "At $105M we earn about 26% if Kodiak behaves the way the operator's own data trended, and still about 10% — the bottom of the sponsor's 10–20% range — on our cautious view. The risk we cannot diversify away is one Kodiak well; that is why we stop at $115M."

**Sensitivities to show (tornado, PV @12%):** oil price ($45 vs strip), Kodiak decline (22% vs 35%), Kodiak outage, Stones stays shut, Lucius paid on lease basis instead of unit basis (−$7.7M), discount rate 10–20%, hurricane 2% vs 3%.

## 4. Funding (Sources & Uses at Sept 14, 2018, bid $105M) — label all as ASSUMPTIONS

| Uses | $M | Sources | $M |
|---|---|---|---|
| Purchase price | 105.0 | Anchor royalty fund equity (95%) | ~86 |
| Less closing credit (Jan–Jun 2018 receipts) | (17.5) | Team / sponsor co-invest (5%) | ~4.5 |
| Transaction costs | 1.6 | | |
| Liquidity reserve | 1.5 | | |
| **Cash needed at close** | **≈ 90.6** | **Total** | **≈ 90.6** |

- Commitment sized ~$5M above uses for Lucius suspense risk.
- 10% deposit (~$10.5M) wired at award (Aug 30).
- **After closing (optional, not in the bid math):** ~$11M arrives at final settlement; a royalty-backed loan of ~$25–30M (prime 5.00% + 0.75–2.25%, Kodiak given little loan credit, 50–75% of oil hedged at ~$60–64) returns capital → net equity at risk ~$50–55M.
- **Why this answers the case's "bank said no / 5 weeks too short":** the bank is not on the critical path; the equity is *already raised* (a fund, not a first-time raise); our title and production diligence is finished, which removes the investor's "not enough time to diligence" objection. **"The bottleneck was diligence speed, not money."**
- Ask BP for an Oct 31 alternative closing date (effective date stays Jan 1, so BP loses ~$1M of time value but gains certainty).

## 5. Allocation by interest (bid instruction requires it; 19 lines, $105.0M)

| Interest | $M | | Interest | $M |
|---|---|---|---|---|
| Kodiak MC 727 | 45.6 | | Stones WR 508 | 16.6 |
| Kodiak MC 771 | 8.7 | | Stones WR 507/509/551/552/553/596/597 | 0.1 each (0.7) |
| Lucius KC 875 | 17.55 | | South Santa Cruz MC 563 | 2.1 |
| Lucius KC 874 | 9.45 | | Ship Shoal SS 219 | 2.0 |
| Main Pass MP 59 | 1.0 | | Grand Isle GI 116 / GI 110 | 0.73 / 0.17 |
| Orion MC 110 | 0.3 | | Pompano MC 72 | 0.1 |

Logic: allocated values become the title-defect remedy schedule, so weight them to the producing tracts (Kodiak well is on MC 727; Lucius by tract factors 46.67/24.77; Stones only WR 508 produces). Pompano gets a token $0.1M, not $0, so the bid isn't read as partial.

## 6. Bid-letter terms (the title attorney's protections)
1. Defensible title per interest = at least the Attachment A decimal on production *allocated* to the lease (unit basis where applicable), within stated depths, **and actually being paid at that decimal**.
2. Title-defect price cut = allocated value × shortfall ÷ stated decimal; $25k threshold; right to drop an interest with a defect >50% of its value.
3. 10% holdback (~$10.5M) for 12 months; special warranty.
4. All post-Jan-1-2018 proceeds to buyer, **including the Lucius retroactive unit true-up (~$2–3M)** and any suspense; seller keeps pre-closing recoupment risk.
5. Closing deliverables: payor remittances and division orders 2016–2018; KC 874 instrument; Devon confirmatory assignment; Amoco→BP vesting; Kodiak lease-maintenance evidence; complete WR 551 copy.
6. No financing contingency (the anchor commitment makes it real); no casualty condition (royalties own no facilities); no re-trade after award.

## 7. The ELI5 (say this in 60 seconds)

We'd own a few cents of every dollar of oil sold from 9 offshore platforms — no costs, no cleanup bill. BP's brochure makes it look worth ~$300M. We read the fine print and checked the government's public production records:
- some slices are smaller than they look (Lucius 1.43%, not 2–4%; Pompano is someone else's field, worth $0; Ship Shoal 4%, not 8%);
- the brochure's 2018 forecast is running hot (Lucius, Stones and South Santa Cruz are well below it);
- more than half the value is one Kodiak well that was offline for 260 days and declines fast.

Valuing only what is already producing, plus a risked allowance for what is being drilled, the package is worth about **$100–130M**. We bid **$105M**, earn **~10–26%** depending on how Kodiak behaves, and walk away above **$115M**. We fund it with a royalty fund's already-raised capital — so the bank's "no" and the 5-week clock don't kill us. If BP's price expectations are too high and the auction fails, we're the buyer with money and finished diligence.

## 8. Four phrases to repeat
1. "We checked the seller's numbers against public government data."
2. "Facts from documents in blue, our assumptions in orange."
3. "We pay for what's producing; drilling is a risked bonus, not a promise."
4. "A bid only counts if it can close. Ours can."

## 9. Deck (10 slides + 2 AI)

| # | Headline | Visual |
|---|---|---|
| 1 | Bid $105M, walk at $115M — funded by committed capital | Decision box + team names |
| 2 | 19 interests, but 3 fields are ~93% of value | PV-by-property bar; Attachment A decimal vs true share |
| 3 | The fine print shrinks the package | Naive vs verified: Lucius 4%→1.43%, Pompano $71M→$0, Ship Shoal 8%→4% |
| 4 | We rebuilt the seller's 2017 revenue from public data (within ~7%) | Our $21.8M gross / $20.4M net vs listing $20.4M — stated honestly as a cross-check |
| 5 | The brochure's 2018 forecast is running hot | WoodMac 2018 vs BOEM actual, by field; Kodiak decline chart |
| 6 | Value: ~$100–130M on existing wells | Two-view table + bridge from ~$300M brochure to our range |
| 7 | What could change our mind | Tornado; Kodiak and Stones scenarios first |
| 8 | Returns at $105M and why we stop at $115M | IRR grid (bid × case); profit $ and MOIC |
| 9 | Funding in 5 weeks: diligence speed, not money | Timeline Jul 9→Aug 13→Aug 15→Aug 30→Sep 14; sources & uses; prime 5.00% |
| 10 | What other bidders see, and our questions for BP | Bidder map + top 6 seller questions |
| A1 | How we used AI | Tools, tasks, how we checked (source PDFs, BOEM) |
| A2 | Where AI was wrong and how we caught it | 3 real corrections (below) |

**AI corrections (all really happened in our work):**
1. AI first read the Lucius override as 4% (adding both leases); the unit's Exhibit C tract factors give 1.4288%.
2. AI applied the Pompano override to WoodMac's "Pompano" field — a different field on different blocks. Real value ≈ $0.
3. AI's first valuation trusted the seller's 2018 forecast (~$220M+ risked); BOEM actuals showed it running hot.
4. Expert-panel review (AI agents) caught that our own model overstated the closing credit ($29M → $17.5M) and loan size ($45M → $25–30M), and that our "$20.4M match" was coded wrong ($28.9M printed).

## 10. Excel model tabs
Inputs (blue facts / orange assumptions) · Title & Shares (decimal, source doc + page, confidence) · BOEM Actuals (monthly, public-by-Aug-15 flag) · 2017 Revenue Check · Forecast (two views) · Prices (Aug 15, 2018 strip + low/high) · Cash Flow & DCF by property · Sensitivities/Tornado · Returns (IRR grid, MOIC, payback, profit $) · Funding (S&U, loan at prime + spread) · Allocation (19 lines) · AI Log.

## 11. Never say / never use
- Anything after Aug 15, 2018: BP still holding the interests in 2024, Hadar / Five Stones, the 2019 Lucius filing (`79187.pdf`), the "Surface to 23,000'" Kodiak depth from a later filing, Jun–Jul 2018 BOEM months, sources dated after Aug 15 (Argus Sep-5, Haynes Boone Fall-2018, Mercer Dec-2018, Citi/SPEE Jan-2019, CME FedWatch Aug 20–22, the Fed's Sept-2018 hike).
- Over-precise numbers in the deck: say "about $100M", "about 26%".
- "The AI found…" → "we found; here's where AI helped and where it misled us."
- Note in the deck that the "production workbook" the case mentions was not in our folder; we used public BOEM data and the WoodMac PDFs instead.

## 12. Hard Q&A — prepared answers
1. **"Bank said no, investor said 5 weeks is too short. Who says yes?"** An existing royalty fund with already-raised capital; it decides in weeks because our diligence is done and the asset needs no development spend. The bank comes in after closing, optional.
2. **"Kodiak is half the value from one well. What if it fails?"** If it dies in 2020 we lose money (≈ −5% IRR at $105M). That's exactly why we bid $105M not $125M, and why we ask BP for Kodiak's current rate before award.
3. **"Isn't your $20.4M match circular?"** Before any deductions we get $21.8M, within 7% — that's independent. The deductions are an assumption and we label them.
4. **"Lucius fell to 19 kb/d in May — why assume 29–30?"** All three Lucius leases fell ~45–50% together (oil, gas, water) — a planned shutdown, not reservoir decline; the operator's Jul 31 report cites tie-in downtime. Underlying decline is still steep, so we use 25–35%.
5. **"Stones was shut in. Why assume it restarts?"** We don't assume it in the cautious view until September, and we ask BP why it shut in. Value at risk ≈ $5M.
6. **"$105M is a lowball. What's your chance of winning?"** Roughly 1 in 3 to be top bid, single-digit chance BP accepts on the day. But BP's own data supports a price no funded buyer can pay, so the auction likely fails — and round two goes to committed money with finished diligence. Overpaying to win is how buyers lose.
7. **"22 payors — how do you know they pay correctly?"** We don't, yet. We demand remittance history by payor; Lucius likely owes a ~$2–3M retroactive true-up from the Jan 1 unit date, which our bid letter claims.
8. **"How does the effective-date credit actually work?"** BP credits what it has received by closing (~Jan–Jun, ~$17.5M); later receipts for pre-closing months come at final settlement.
9. **"Are declines fitted or assumed?"** Fitted to public monthly data (show the Kodiak/Lucius curves), with a cautious and an operator-trend view.
10. **"KC 874's creating instrument is missing — why call 2% a fact?"** We don't: it's the seller's representation, confirmed by four third-party recitals, and covered by a title-defect price cut in our bid letter.

## 13. Questions for BP (slide 10)
1. Payor remittances and division orders 2016–2018 — and is Lucius paying on the 1.4288% unit basis or holding funds in suspense?
2. Why was Stones shut in Mar–May 2018; is it back; has Shell paid the ORRI through royalty relief?
3. Kodiak current rate/pressure, lease-continuity approval for the 2017–18 gap, second-well plans.
4. Ship Shoal: 8% of 8/8 or 8% of Amoco's 50%?
5. Missing instruments: KC 874 creation, Amoco→BP, MP 59 1979 letter, LLOG 2007 farmout, SSC 2014 agreement, WR 551 complete copy.
6. Why is the WR 199 royalty in the Devon→BP schedule excluded from this sale?
