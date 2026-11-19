Score: 69/100 — Placement: 2nd–3rd (can contend for 1st after the 4-hour fixes)

# Round 2 faculty judge: "Bid or Walk Away?"

I scored the plan in FINAL_decision_v2.md as if the deck and Excel get built exactly as described. **No .pptx, .xlsx or notebook exists in the folder yet.** If they don't ship, the score falls below 50. I re-ran `final_irr.py` and it matches the memo. I also ran my own checks, below.

## 1. Rubric

| # | Criterion (case question) | Pts | Score | Why |
|---|---|---|---|---|
| 1 | Clear recommendation, credible bid (Q1) | 10 | 8 | Clear call; the Aug 13 gate is smart. But the $115M walk-away only works in the operator-trend view (cautious view: 5.4% at $115M). |
| 2 | Funding: sources, cost, timing, prime (Q2) | 12 | 8 | Prime 5.00% is correct. The fund is hypothetical, with no stated cost of capital. **The case requires financing costs; every return shown is unlevered.** |
| 3 | Valuation, bid/max, profit and return (Q3) | 18 | 13 | Excellent closing-credit and payment-lag mechanics. But PV is dated Sept 14, not Aug 15. No profit $ or MOIC yet. The cautious IRR at $105M (10.5%) is below the team's own 12% rate; risked drilling closes the gap. |
| 4 | Predictive rigour | 12 | 5 | Declines are set by hand; the "fitted" claim is false (§2). |
| 5 | Risk and sensitivity (Q4) | 10 | 7 | Good scenarios. No tornado yet; chance of losing money not stated. |
| 6 | Other bidders (Q5) | 6 | 4 | "Auction fails, funded buyer wins" is interesting; "1 in 3" has no evidence. |
| 7 | Unusual features, seller questions (Q6) | 6 | 6 | Best part: Lucius 1.43%, Pompano is a different field, Ship Shoal 4%, Stones royalty relief. |
| 8 | Facts vs assumptions; no hindsight | 8 | 7 | Hindsight flag, data-vintage caveat and "never say" list are real discipline. Strip-price source not cited. |
| 9 | Communication | 8 | 5 | Jargon, two headline numbers, too many decimals. |
| 10 | Reproducibility | 5 | 2 | Three overlapping engines with hard-coded inputs; the Monte Carlo still uses Ship Shoal at 8%; no Excel. |
| 11 | AI appendix | 5 | 4 | Real, specific corrections. But the "6-expert panel" was AI agents shown as if they were people. |
| | **Total** | **100** | **69** | |

## 2. Predictive analytics

**Are the declines fitted?** No. `reserves_panel.py` hard-codes `De=0.35, b=0.5`, and no script runs a regression. Q&A #9 ("fitted to public monthly data") falls apart as soon as a judge opens the code.

My own quick fit on the public BOEM rows:
- **Lucius, Oct-2016 to Apr-2018 (n=19):** an exponential fit gives about **37% a year decline (95% CI roughly 30–45%)**, R² ≈ 0.78. A hyperbolic fit only reaches R² 0.80, so 19 points cannot pin down b. Fix b at 0.5 and fit only the initial decline. **The operator-trend view's 25% is outside the confidence interval.**
- **Kodiak:** only three months exist for the current interval. Earlier flow periods fell about 55–60% a year (2016) and about 44% a year (2017). There is too little data to fit, so use an analog range. **The 22% has no public-data support, and the memo itself says so.**

**Minimal fix:**
1. For each field, fit Arps decline on monthly data (`curve_fit` or a grid search). Exclude shutdown months by a written rule. Report the decline with its CI, b, R², RMSE and n. Where n < 6, say "not fittable, analog range."
2. Run a Monte Carlo of 5,000 runs with a fixed seed. Draw declines from the fit CIs, plus Kodiak failure, Stones restart **and oil price**. The rebuttal Monte Carlo leaves out price, the biggest driver ($45 oil takes about $18M off PV).
3. My re-run (Ship Shoal 4%, production uncertainty only) gives existing-well PV at 12% of about $80M / $96M / $109M (low / middle / high). **In about 80% of runs the producing wells alone are worth less than $105M.** Say that first, and show how much the risked drilling contributes.

**One slide:** on the left, four small charts (actuals as dots, fit as a line, an 80% band, a plain caption like "Lucius output is falling ~35–40% a year"). On the right, a histogram of package value with lines at $105M and $115M and the label "chance we earn ≥12%: X in 10."

**Two views?** As written, it's a hedge: "10% or 26%, pick one," and one view contradicts the team's own data. Use one base case from the fitted curves, show the Monte Carlo spread as the uncertainty, and make "if BP's forecast is right" one bar on the tornado.

## 3. Communication

**Translate or cut:** PDP, P50/P90 (backwards for a business audience), PV12, hyperbolic, b-factor, kb/d, 8/8, tract factors, unit basis, suspense, division orders, HPHT, OGOR, ABOS, MOIC, strip, re-trade, ELI5.

**Round:** 1.4288%, 2.604167%, $17.55M, 26.5%/10.5%. Allocation decimals go in the Excel.

**10-minute storyline:**
1. Answer and gate (0.5 minutes)
2. The fine print shrinks the package (2 minutes; this is the differentiator)
3. Public data vs the brochure, with fitted curves (2 minutes)
4. Value, the bid, the chance of earning 12%, profit $ (2 minutes)
5. Kodiak risk (1 minute)
6. Funding and why it can close in 5 weeks (1.5 minutes)
7. Questions for BP (1 minute)

**Cut:** the panel-moved-us table, Hadrian/Kosmos, bid-letter legal terms (keep one line), "1 in 3," unsupported "auction fails" claims.

## 4. Excel: what a judge opens

1. **Inputs.** Font: blue for inputs, black for formulas. Fill: blue for facts, orange for assumptions. A source column with document and page, or BOEM lease and month.
2. **One scenario dropdown** (Low / Base / High) driving everything through INDEX. No pasted values in the calculation tabs.
3. **Production.** BOEM monthly data with the public-by-Aug-15 flag, plus a fit table (decline, b, R², n) and actual-vs-fit charts.
4. **DCF by property.** XNPV and XIRR on real dates, valued at **Aug 15, 2018**, with the closing credit shown.
5. **Live grid.** Bid × case IRR grid, tornado and profit $ / MOIC from data tables.
6. **Funding.** Sources & Uses, loan at prime + spread, fund fees, **net-to-equity IRR**.
7. **Checks.** Allocation equals the bid; 2017 revenue tie-out; shares match Attachment A.

**Differentiator:** a bid slider that live-updates IRR, profit, the chance of earning 12% and a walk-away flag. A facts register hyperlinked to source-PDF pages. A "hindsight we excluded" tab.

## 5. AI appendix

Full marks needs: the tools used; three or four **verbatim, dated prompts**; one correction shown side by side (AI said 4% → Exhibit C → 1.43%, with the page cited); how each answer was verified; and a plain statement that the review "panel" was AI-simulated roles checked by the team. Generic "used ChatGPT to brainstorm" text only ticks the box.

## 6. Punch list (points recoverable)

**Fixable in about 4 hours:**
1. **Ship the Excel and deck (avoids −20).** If time is short, a consolidated notebook plus a lean Excel DCF.
2. **Fit the declines, show fit stats and the slide, drop the 22%/25% view (+5).**
3. **Financing costs in the returns:** fund target and fees, plus a net-to-equity IRR (+3).
4. **Monte Carlo with price uncertainty, Ship Shoal at 4%, fixed seed;** report the chance of loss and the chance of earning ≥12% (+3).
5. **PV at Aug 15, 2018, plus profit $ and MOIC (+2).**
6. **Jargon and decimals cleaned up; one base case (+2).**
7. **Label the AI panel and add verbatim prompts (+1).**
8. **Justify $115M against the fitted middle case, or lower it (+1).**

**Not fixable in 4 hours:** a signed fund commitment; a Kodiak analog type-curve study; a re-pull of the 2018-vintage BOEM data; evidence on auction behaviour.

## 7. Would they win?

**Not as planned.** The diligence is the best I would expect to see. The analytics are weaker than claimed, and a strict judge will check the "fitted" claim. **What beats them:** visibly fitted curves, one base case and a live bid slider. Or a well-argued walk-away with a standing offer, since "a fund signs in 5 weeks" is still an assumption. With fixes 2–5 done, this team scores about 82–85 and is the favourite.
