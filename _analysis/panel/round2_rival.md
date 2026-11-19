# Round 2: rival team vs. "Bid $105M, walk at $115M"

All returns below come from their own engine (final_irr mechanics: Ship Shoal 4%, Jan–Jun credit at close). Contingent-payment runs are in `panel/scripts/rival_cp.py` (`python -I panel/scripts/rival_cp.py "<_analysis>"`). It reproduces their $105M row exactly.

## 1. Our answer: bid, but make BP's Kodiak forecast pay for itself

**Bid $98M guaranteed cash plus up to $24M in cash performance payments, for the whole package. Headline: up to $122M. Walk-away: $105M guaranteed. Conforming fixed-price alternate: $105M.**

Performance payments are triggered only by **public BOEM OGOR-A production**, so neither side needs an audit:

| Tranche | Trigger | Pay |
|---|---|---|
| Kodiak 2019 / 2020 / 2021 | Unit oil averages ≥11.0 / 8.5 / 6.5 kb/d **and** WTI averages ≥$55 that year | $5M each, paid Mar 31 of the following year |
| Kodiak 2nd well | A second completion produces for 90 days by end-2021 | $5M |
| Stones Phase 2 | A new well on any of the 8 WR blocks produces by end-2021 | $4M |

- **Security for BP:** if we miss a payment, part of the Kodiak ORRI reverts to BP, so BP's credit risk on a newco is minimal.
- **Precedent before Aug 15, 2018:** Fieldwood/Noble deepwater (Apr 2018) paid $480M cash plus a $100M contingent payment. Kosmos/DGE used a 10% holdback.

The triggers sit between the two Kodiak views they built themselves. Their cautious case gives 9.5 / 6.6 / 4.8 kb/d, so no payments. Their operator-trend case gives 13.1 / 10.3 / 8.0, so all three are paid. BP's WoodMac case (17 kb/d with a second well) pays every tranche, so **BP books about $122M while we expect to pay about $98–110M.** We bridge the bid–ask gap with the one asset where BP and the buyer genuinely disagree.

| Unlevered IRR | Theirs: $105M flat | **Ours: $98M + payments** |
|---|---|---|
| Cautious, strip | 10.5% | **14.8%** (pays $0) |
| Cautious, $45 oil | 0.0% | **3.4%** |
| Cautious, Kodiak dies in 2020 | −5.4% | **−1.6%** |
| Operator-trend, strip | 26.5% | **25.4%** (pays $15M) |
| Operator-trend, $45 oil | 13.6% | **17.6%** (price gate suspends payments) |
| Cash at close (after ~$17.5M credit, plus costs and reserve) | ~$90.6M | **~$83.6M** |
| Value in BP's eyes | $105M | ~$115–122M |
| P(top sealed bid), their own simulation | 34% | ~46–52% (their $115–120M rows) |

It buys about 4 points more IRR in every downside case for about 1 point less upside, $7M less equity at close, and better bid-ranking odds. It also answers the case's drilling rule with a contract rather than an opinion: *"We can't assume when drilling happens, so we pay for it when BOEM shows it happened."* For a sponsor whose business is lease data and royalty audits, a price that settles on public production data is his own product.

**One free add-on:** BP assigns its pre-closing underpayment claims across the 22 payors. One example is the KC 875 "free of all costs… transporting" clause against our modeled $3/bbl deduction. BP values these at $0 today, and the sponsor's other company recovers exactly these claims.

**Options we rejected:**
- **(a) Walk with a standing offer.** Their simulation gives a 55–65% chance the auction fails, and round two goes to the top sealed bidders. A team that walks gives up that position, and most teams will walk anyway.
- **(b) Partial bid on Kodiak + Lucius + Stones.** The six tail interests are worth only ~$6.4M of the $105M allocation. Dropping them saves about 6% and pushes BP to rank us lower.
- **(c) Same answer, better executed.** Section 4 shows why that still loses to this one.

## 2–3. Their five weakest points, ranked by damage, with tonight's fix

**1. Their own anchor would reject the deal (the funding thesis was never re-run).**
- *Attack:* Their capital-markets panelist sets the anchor's test at a 15% strip hurdle plus an 8–10% downside floor. That passed only on the old production inputs (27.7% / 13.6%). On the cautious production view the final memo adopted, $105M gives **10.5% strip, 0.0% at $45 oil and −5.4% if Kodiak fails**. After an 8% pref and a 20% promote, the LP is in single digits. "Who writes ~$86M of first-loss equity for a 10.5% gross base case with a 0% downside?"
- *Fix:* Put the anchor test on the funding slide. Clear the strip hurdle with the contingent structure (14.8% cautious) or a guaranteed price near $95M (17.0%). No price alone fixes cautious-plus-$45 (3–5%), so show a hedge on 50–75% of 2019–20 oil at the Aug 15 Cal-19 settle (use the CME settle, not the post-cutoff Argus source).

**2. A zero-margin bid that almost never wins: "why bid at all?"**
- *Attack:* "$105M = our P50 value at 12%" means expected NPV is about $0 at their own discount rate. Their cautious IRR (10.5%) is below that 12% rate; calling it "the bottom of the sponsor's 10–20% range" is a dodge. The strategist puts P(award) at 3%, and Q&A #6 admits single digits. The bid is low enough to lose and high enough to earn nothing, while the case explicitly asks for expected profit.
- *Fix:* State expected profit in dollars. Reframe the bid's job as winning the top-sealed-bid seat for round two (34%), or move to the contingent structure, which raises both profit and odds.

**3. The Aug 13 gate is theater.**
- *Attack:* The gate is two days before bids. How long has the anchor had the data room? The EnergyNet NDA likely bars sharing it with financing sources without consent. An independent reserve letter takes 2–3 weeks and an anchor needs two IC meetings. The fund is unnamed. If the fund has both the money and the diligence, why does it need this team? The sponsor's own investor said five weeks was too short, and "diligence speed, not money" is asserted, not shown.
- *Fix:* A dated plan: Jul 16 NDA consent → Jul 20 model sent → Jul 27 term sheet and reserve engineer → Aug 3 IC #1 → **Aug 8 IC #2, signed commitment and deposit proof (the gate)** → Aug 13 PSA markup. Cast the team as originator and asset manager on a promote.

**4. The standing offer is unfunded, and it leaks their walk-away.**
- *Attack:* The standing offer triggers on "no signature", which is exactly when they have no money. Their own strategist says it is the most likely outcome (55–65%), so the modal result of their plan is an unfunded letter. "Up to $115M for 90 days" also tells BP their maximum, so BP counters at $115M. It is walking away with extra steps.
- *Fix:* If there is no signature, say **"Walk"** plainly and send a non-binding indication at the bid price. Keep the standing offer only for the funded failed-auction case, with no number above the bid, framed as "we close once our 2–3-month lender process finishes."

**5. Number soup, and a headline that contradicts their own engineer.**
- *Attack:* Existing-wells value appears as $93M, $98M, $102M and $104M. The ELI5 says the package is worth $100–130M, yet they bid at the bottom. "How to say it" leads with 26%, which rests on a Kodiak decline their engineer places near the P10. "~10–26%" is not the base case the case asks for. Phrase 3 ("drilling is a risked bonus, not a promise") contradicts the price: $13M of the $105M *is* drilling.
- *Fix:* Present one base case ($93M existing-wells P50 plus $13M risked development = $106M) with one downside and one upside. Lead with the base-case IRR (~12%). Either own the $13M development payment or move it into a contingent tranche, which makes phrase 3 true.

(Also: the Oct 31 closing request signals funding weakness.)

## 4. Verdict

- **Before fixes: we win by about 8–10 points out of 100** (~80 vs ~71).
  - They win Q5/Q6 on diligence: the title work, the BOEM rebuild and the Lucius 1.43%.
  - We win Q1–Q4. Our cautious case clears their own anchor's strip hurdle (with a hedge for the $45 case), we have a real expected profit, and our instrument converts the drilling rule and the Kodiak risk into a priced term. A judge also asks them the "why bid at all?" question, and it lands.
- **After fixes 2–5 only (same $105M flat): we still win by about 3–4.** Their gate, base case and messaging improve, but weak point 1 survives. At $105M flat, the cautious case cannot clear any anchor's hurdle.
- **If they adopt the structure: they win by about 3–5.** Their diligence is the deepest in the room. What holds them back is the price structure, not the evidence.

**What they should change:**
- **Keep "Bid"**, with $105M as the ceiling on *guaranteed* cash.
- **Change the structure:** $98M guaranteed, up to $24M in public-data performance payments, a $105M fixed conforming alternate, a funding gate on Aug 8, and a plain "Walk" if unfunded.
- **New slide-1 line:** "We pay $98M for what is producing and up to $24M more only if BOEM's own data proves BP's Kodiak forecast right. BP sees $122M; we earn about 15% even if BP is wrong."
