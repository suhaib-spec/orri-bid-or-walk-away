# Judging criteria, sponsor profile, and stand-out strategy
Research date: 2026-11-12. Labels: FACT (sourced), INFERRED (our judgment), HINDSIGHT (post-Aug-15-2018; must NOT be used to justify the decision in the deck).

## 1. Judging rubric

### What was found (FACT)
- No published rubric for the 2026 "Bid or Walk Away?" hackathon was found on cob.unt.edu, the UNT news site, PR feeds, or general web search. Instagram/LinkedIn/Handshake pages are not indexed or not reachable by the tools used.
- The only prior UNT Ryan College event page found is the **ITDS November 2024 Business Analytics Hackathon** (https://cob.unt.edu/events/business-analytics-hackathon.html), organizer Sourav Chatterjee. Its format:
  - 24-hour analysis window; "Use any analytical tool and software."
  - Presentation main body of at most 8 pages, appendices allowed; "Findings, underlying analyses, and recommendations must be stated clearly"; "should include both descriptive and predictive analyses."
  - **Top 5 teams present: 10 minutes + 5 minutes Q&A.** Top 3 get gift cards. No rubric or weights published.
- No news about past UNT BA hackathon winners was found.
- The 2026 case document itself (local file `UNT_Hackathon_2026_Bid_or_Walk_Away_Case.docx`) contains the only official evaluation signals:
  - "Either decision can be persuasive if it is supported by sound analysis."
  - "Keep assumptions separate from facts; do not present estimated ownership percentages or possible financing as confirmed information."
  - "Evaluate the opportunity as of August 15, 2018 ... Do not use later events to justify your decision."
  - "Begin with a brief recommendation, followed by your financial model, funding plan, risk analysis, AI record, and references. Make your calculations easy to follow."
  - "Students should use methods they can explain and defend; more advanced methods are useful when they add insight. Clear reasoning and well-supported assumptions matter throughout."
  - "The Lease Analytics team is interested in your thought process: what you ask, how you follow up, and how you decide whether an answer is useful."
  - AI appendix must include "at least one example of an AI response your team corrected, challenged, or rejected."
  - Schedule: finalists announced Nov 13, 4 pm; finals Nov 14, 10 am to 4 pm, BLB 015.

### Inferred rubric (INFERRED, no official weights exist publicly)
Built from the case's six questions, its "organize your submission" order, and typical analytics case-competition rubrics.

| Criterion | Likely weight | What earns full marks |
|---|---|---|
| Clear recommendation + decision logic | 15% | Bid/walk answer on slide 1, with bid, max price, and the conditions that would flip it |
| Financial model and valuation (Q3) | 25% | Transparent DCF to Aug 15 2018, per-interest allocation, decline curves tied to the production workbook, effective-date adjustment, financing costs included, NPV/IRR/MOIC |
| Funding plan and feasibility (Q1, Q2) | 15% | Realistic sources, cost, and timeline; prime rate 5.00% on Aug 15 2018 and the spread logic; honest about the 5-week constraint |
| Risk and sensitivity (Q4) | 15% | Base, upside, and downside cases; tornado chart; price, decline, hurricane downtime, drilling upside handled without assuming timing |
| Competitive insight and diligence (Q5, Q6) | 10% | Evidence-based "what others miss"; unusual sale terms; sharp seller questions |
| Assumptions vs facts discipline, data integrity | 10% | Every number tagged as fact (source) or assumption (rationale); no hindsight |
| AI-use record | 5-10% | Real prompts, verification, at least one documented correction |
| Communication and Q&A | 5-10% | 10-minute story, readable charts, team that can defend every number |

## 2. Sponsor profile

### Lease Analytics (FACT)
- Dallas-based oil and gas back-office analytics consultancy, founded 2015, 4925 Greenville Ave, Dallas (https://prospeo.io/c/lease-analytics-revenue; third-party directory, size estimate 11-50 staff).
- Services (https://www.lease-analytics.com/): data assessment, land data capture and cleanup, systems integration, **revenue recovery** ("100% track record"), **M&A / divestiture support** ("preparing data for valuations and deals"), BPO/staff augmentation. Claims "$50 million in lost revenue recovered" and "40,000 net acres discovered."
- 2018 press release: applies "AI and machine learning to recover lost revenue and find errors in oil and gas asset data"; partnered with Lone Star Analysis (predictive analytics) on Aug 28, 2018, CEO Tom Agnew quoted about optimizing "asset acquisitions" (https://www.prnewswire.com/news-releases/lease-analytics-partners-with-lone-star-analysis-300703090).
- **Existing UNT tie:** July 20, 2017, Lease Analytics funded UNT's Human Intelligence and Language Technologies (HiLT) lab (College of Engineering) to build NLP that tags "oil and gas leases and contracts with categories of interest." Agnew: "UNT has had a preeminent position in both oil and gas accounting and information sciences," and the research "will drastically reduce back office error rates" (https://www.prnewswire.com/news-releases/lease-analytics-funds-machine-learning-research-at-the-university-of-north-texas-300491901.html; https://northtexan.unt.edu/issues/2017-fall/unts-hilt-lab-receives-funding.html).

### Tom Agnew (FACT, from profile aggregators and press)
- Co-founder, President and CEO of Lease Analytics since Sept 2015; also founder/CEO of **EquityMetrix** (since 2004), a Dallas firm that recovers oil and gas revenue underpayments for owners through data mining and forensic accounting of leases, deeds and contracts, paid by retainer plus a share of recoveries; raised $5M from Peterson Partners in 2014 (https://theorg.com/org/equitymetrix/org-chart/tom-agnew; https://legacy.xconomy.com/2014/03/04/data-miner-equitymetrix-digitizes-energys-back-office/2; https://www.privateequitywire.co.uk/equitymetrix-receives-usd5m-growth-investment-oeterson-partners/).
- Background: Accenture Partner 1981-2004; MBA Tulane; BS Electrical Engineering, RPI (per search-aggregated profile; LinkedIn not directly fetched).
- Quoted idea: a typical well changes hands about five times and records get lost in transfers (Xconomy).
- Co-founder listed in directory data: Gayle Burch Agnew.
- Last modifier of the bid-instruction file is "Tom Agnew" (local file metadata).

### Connection to the real 2018 BP package (INFERRED)
- No public source says Lease Analytics or Agnew bid on the package. However, the case phrasing ("The sponsor discussed an estimated reserve value of $100-$150 million", "the bank consulted was unwilling to finance offshore assets", "an equity investor also considered the five-week timeline too short") reads as a first-person account: the sponsor appears to have evaluated the deal in July 2018 and could not line up financing in time. The data folder is named `ORRI-20180717`, consistent with a data-room download on July 17, 2018.
- Implication: judges know the real obstacles and will reward teams that confront the financing and timing problem honestly rather than assuming a loan. A walk-away, or a "conditional bid with a pre-arranged partner," is not penalized ("Either decision can be persuasive").

### What the sponsor will likely reward (INFERRED)
1. **Document and title diligence.** Their business is finding errors in land records. Each property folder has leases, BOEM serial register pages, ORRI assignments and unit agreements. Verify ORRI decimals, depth limits, unit tract participation, and assignment chains from source documents, and flag anything that does not match the seller's numbers.
2. **Skepticism of seller data**, for example reserve value versus 2017 revenue, and whether the "19 interests" equal "19 leases."
3. **Revenue-recovery thinking:** check whether payors (22 per Hart) have historically paid correctly; underpayment and late-payment recovery is upside others miss.
4. **Data analytics on public data:** BOEM/BSEE production by lease and well, decline-curve fits, hurricane shut-in history (e.g., 2005, 2008, 2017).
5. **Realistic financing:** prime 5.00% on Aug 15 2018 (raised June 14 2018, next raised to 5.25% Sept 27 2018; https://fred.stlouisfed.org/data/PRIME). RBL loans were typically priced at LIBOR or prime plus a spread, and offshore royalty loans were hard to obtain, which matches the case.
6. **Thought process and AI discipline**, explicitly stated in the case.

## 3. The 2018 BP / EnergyNet listing

### Hart Energy "Marketed: BP Offshore ORRI Package, Gulf Of Mexico" (FACT; page returns HTTP 403, so details come from search-engine extracts of the page, not a direct read)
URL: https://www.hartenergy.com/news/marketed-bp-offshore-orri-package-gulf-mexico-117686/
- BP Exploration & Production Inc. retained EnergyNet to sell an offshore ORRI package in the U.S. Gulf of Mexico through a sealed-bid offering.
- "nine total properties covering 19 leases with 22 total payors."
- "Total net revenue from the assets for 2017 was roughly $20.4 million." This is **revenue to the ORRI package for calendar 2017, whole package**, not cash flow or PV. Because ORRIs bear no operating cost, net revenue is close to pre-tax cash flow, but it may be net of severance/transport deductions; ask the seller. The extract also references a June 2018 reserve source (likely a reserve report effective mid-2018).
- Highlights the Lucius field (Anadarko) and the Stones field (Shell). Operators listed include Anadarko US Offshore, Cantium, Deep Gulf Energy III, Energy XXI GOM, Fieldwood Energy, Renaissance Offshore, Shell Offshore.
- Bids due 4 p.m. CST Aug 15; closing Sept 14; effective date Jan 1, 2018. These match the bid instructions.
- **Discrepancy to flag:** Hart says "19 leases"; the case says "19 individual interests across nine platforms."
- Sanity check (INFERRED): a $100-150M reserve value against about $20M a year of revenue implies roughly 5-7.5x revenue. That is plausible only with modest decline or upside at Stones and Lucius. At a 10-20% discount rate with steep deepwater declines, value may be well below $100M. Test this explicitly.

### Outcome (HINDSIGHT; do not use in the recommendation)
- A BOEM filing dated Jan 8, 2025 (https://data.boem.gov/PDFDocs/Scan/ADJUD/87/87222.pdf) shows **BP still owned** ORRIs in Kodiak (MC 727/771), Lucius (KC 874/875), Hickory (GI 110/111/116), South Santa Cruz (MC 563), Orion (MC 110) and MP 59 in December 2024. It sold them effective Dec 1, 2024: 25% to Five Stones Energy, L.L.C. and 75% to Hadar Investment III LLC.
- In Oct 2024, BP re-marketed a GoM ORRI package through Indigo Energy Advisors (Hart: https://www.hartenergy.com/exclusives/marketed-bp-ep-gom-orri-opportunity-210798/). The listing cites about 1,100 boe/d in Q1 2024 and about $23.1M of next-twelve-month cash flow.
- Interpretation: the 2018 EnergyNet sale appears not to have closed for at least 6 of the 9 properties. Possible reasons are bids below BP's reserve price or a withdrawn sale. Stones, Pompano and Ship Shoal were not in that filing; their status is unknown.
- Use only as private context in Q&A if asked "what happened?", clearly labeled as hindsight. It is also consistent with "the seller may not accept a low bid," which is a fair 2018-era point: a sealed bid with no reserve disclosed can still be rejected.

## 4. What stands out in the sale (for Q6; FACT from bid instructions and case, with INFERRED implications)
- Effective date Jan 1, 2018, closing Sept 14, 2018. The buyer is entitled to roughly 8.5 months of revenue already earned. The usual purchase-price adjustment credits that revenue to the buyer at closing, so the net cash outlay is lower than the headline bid. Ask the seller how adjustments, suspense funds and prior-period audits are handled.
- All-cash; seller "strongly prefers" one buyer for the whole package but "may consider separate bids"; **allocation by interest required**. This creates an opening for a cherry-pick strategy (bid on Lucius, Stones and Kodiak only).
- Bid instructions say "Today's date is 7/15/2018", while the case says instructions were issued July 9. The seller is not named in the bid instructions. Hart names BP and EnergyNet.
- Five weeks from instructions to bid is shorter than the 2-3 months a bank needs. The structure favors buyers with cash already committed, such as royalty funds and private equity, and reduces competition.
- Legal: an ORRI ends when the underlying lease terminates. Older shelf leases (MP 59 from 1979, SS 219 / OCS 00829) carry termination and decommissioning risk. Depth limits apply. BOEM filing footnotes show Lucius KC 874 limited to "Surface to 23,000'" and South Santa Cruz MC 563 limited to "Surface down to 19,000' TVDSS". Check the case's source documents for the same limits. Unit agreements dilute or expand the ORRI by tract participation.

## 5. Stand-out recommendations (INFERRED)
1. Slide 1 gives the answer, the number and the condition, for example "Bid $X (max $Y) only with a committed equity partner by Aug 10; otherwise walk." A conditional decision tree shows judgment.
2. Show a "Fact vs Assumption" ledger: a color-coded table, with every number sourced (case file, BOEM, EIA strip on Aug 15 2018, FRED prime).
3. Include a title and data-integrity slide that speaks the sponsor's language: an ORRI decimal reconciliation from the assignments and unit agreements against the seller's figures, with discrepancies found. This is the "value others overlook" and maps to Lease Analytics' revenue-recovery business.
4. Run the funding plan as a timeline (Gantt over July 9 to Sept 14) against lender and equity lead times. Show cost of capital per source and how 5.00% prime plus a spread feeds into the loan rate and a blended hurdle rate.
5. Valuation should use per-property decline curves from the workbook and BOEM data, the NYMEX strip as of Aug 15 2018, a hurricane downtime haircut (expected shut-in days per year), no assumed drilling in the base case, and drilling only as upside. Report NPV at 10/15/20%, IRR, MOIC and payback, and give the max bid as the price at which IRR equals the hurdle.
6. Add a tornado chart and three scenarios, and optionally a simple Monte Carlo, but only if it can be explained in 30 seconds.
7. Show the competitor lens: who bids (royalty aggregators, PE-backed mineral funds, family offices), what they would pay at their cost of capital, and therefore what a winning bid probably looks like.
8. Write Q6 seller questions that sound like a landman and auditor: payor remittance history, suspense balances, post-production deductions, unit tract factors, depth limits, decommissioning status by lease, title opinions, a reserve report author, date and price deck, and reconciliation of the $100-150M versus $20.4M revenue.
9. The AI appendix should show prompt, then follow-up, then verification against the source PDF, then correction (for example, AI mis-stating an ORRI decimal or the prime rate). This matches "interested in your thought process."
10. For the 10-minute presentation and Q&A, rehearse defending the discount rate, decline assumptions and the walk-away trigger. Keep hindsight out of the deck. If asked, acknowledge only that the team avoided post-2018 information.
