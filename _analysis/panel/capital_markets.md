# Panel review: funding plan and returns (RBL banker + mineral/royalty PE partner)

Reviewed: decision_memo.md, market.md, upside_structures.md, criteria.md, the case and bid instructions, and engine2.py, returns.py and levered.py (re-run). Re-run figures come from scratch copies (cm_check.py, cm_lev.py). They change timing, costs and loan size only. Valuation inputs are untouched.

**Overall:** the asset is fundable, but the plan as written is not. It treats a price adjustment as a source of funds, rests on a precedent that doesn't fit, and oversizes the post-close loan by about $15M.

## 1. Effective-date credit — **Critical** (if equity is sized at $81M)

- **How it settles.** In a standard A&D PSA (EnergyNet uses the seller's form), the preliminary settlement statement is delivered 3–5 days before closing. It credits only post-effective proceeds the seller has **actually received**. Later receipts are remitted after closing, and everything is trued up in a **final settlement 90–120 days later** (mid-Dec 2018 to mid-Jan 2019). Payor transfer orders after the BOEM filing take another 1–3 months.
- **How much is known by Sept 14.** Deepwater payors pay about 60 days in arrears. By Sept 14, BP holds cash for about **Jan–Jun production: $18.8M** of the $28.2M attributable to Jan 1–Sep 14.
- **Lucius suspense risk.** About $11.4M of 2018E is Lucius on the new unit basis. If that is in **suspense** pending new division orders, the closing credit could be only **$12–15M**.
- **Internal inconsistency.** upside_structures.md estimates the credit at $17–21M; the memo uses $29M.
- **Fix.** An $81M commitment leaves a **$12–17M hole at closing**, and the deposit would be forfeited. Underwrite equity at **price + costs − about $17M**.

## 2. Anchor equity in about 4 weeks — **Critical**

- **Apollo/Kimbell is not a comparable.**
  - Apollo bought a senior, 7%, convertible preferred in a **listed MLP** with management, audited reserves, a revolver and a diversified onshore book.
  - The roughly 6.5 weeks ran from **signing to funding (May 28 to Jul 12)**. The commitment was negotiated before signing.
  - Here: first-loss equity in a newco with no track record, 54% in one HPHT well that was down 260 days in 2017.
- **What a 2018 anchor demands:**
  - 8–10% pref, 10–20% tiered promote
  - a 2–5% GP co-invest, which the team can't fund
  - control and a veto on price and PSA terms, plus exclusivity
  - its own dead-deal budget ($0.5–1M)
  - an independent PDP reserve audit (2–3 weeks at best), federal ORRI title work and two IC meetings

  "Subject to diligence" is not a commitment.
- **Who can write $95M+ by Aug 15?**
  - Not the public mineral companies: Black Stone, Kimbell, Viper and Dorchester were onshore and unit- or revolver-funded in 2018.
  - Not royalty trusts, which are passive and cannot acquire.
  - Not insurers, which take months and need a rating.
  - Realistic: committed-capital investors that already know GoM, such as GoM non-op specialists (Ridgewood- or HEQ-type), structured energy capital (EIG-, Riverstone Credit- or Macquarie-type), a streamer with a revolver (Franco-Nevada-type) or a large GoM family office. These are types, not confirmed parties.
  - They will want to bid in their own name. The team's realistic role is originator and asset manager on a small promote.
- **Process gate.** The EnergyNet confidentiality agreement likely bars sharing the data room with financing sources without consent. Get it first.

## 3. Post-close offshore ORRI RBL — **Major**

- **Bankability.**
  - In 2018 offshore RBLs went to scaled corporate borrowers: Talos ($600M borrowing base, L+275–375) and Kosmos (an international RBL upsized by $200M for the Deep Gulf Energy deal).
  - **Kosmos's bank group is no precedent for a $30M newco.**
  - The case bank's "no" is the base case. Best realistic outcome: a $25–35M bilateral from a Gulf Coast regional bank that lends to royalty owners (Hancock Whitney-, IberiaBank-, Amegy- or Frost-type), 2–3 months after an engineering report.
- **Likely terms:**
  - borrowing base of 35–50% of PDP PV9 on a bank deck (about $50–55 WTI, $2.75 HH)
  - Kodiak advanced at 0–30% until 12 months of clean uptime
  - 50–75% of PDP oil hedged for 24–36 months
  - semiannual redeterminations, debt/EBITDAX ≤ 3.0x, and a hurricane-season liquidity reserve (royalty owners can't buy BI cover)
  - pricing of **L+300–350 (about 5.1–5.6%) or prime +0.75–1.50 (5.75–6.50%)**, plus a 1–1.5% fee
- **The rate isn't the problem; the base is.** Prime +2.25% is conservative. But levered.py takes 40% of low-deck PV10 **including the $41.5M of 2018 revenue already credited**, which is $113M, giving a $45.2M loan. On the collateral that exists at 1/1/2019:

  | 2019+ PDP at 1/1/2019 | Value |
  |---|---|
  | PV9, strip | $103.5M |
  | PV9, $50/$2.50 (bank deck proxy) | $85.6M |
  | PV10, low deck | $74.6M |
  | PV9 ex-Kodiak, bank deck | $38.5M |

  A realistic borrowing base is **$25–30M**.
- **Alternatives:**
  - Private-credit royalty term loan: L+700–900, 50–60% LTV with hedges, 4–6 weeks if pre-screened. This is the most credible debt.
  - Mezz at about 8–11%: cost with no closing benefit.
  - Seller notes, earn-outs or a BP carried interest: non-conforming. BP announced the $10.5B BHP purchase on Jul 27 and wants cash.
  - Kodiak/SSC sell-down to Kosmos, or Stones to Shell: the best de-risking exit, but it can't be signed in 5 weeks.

## 4. "Conditioned on equity" bid — **Major**

- As an **internal go/no-go gate**, it is sound. Written into the bid letter, it makes the bid non-conforming. BP asked for "binding proposals" and all cash, and sellers value a financing out at zero.
- The fallback doesn't solve funding: the top-3 subset bid still needs about $95M.
- **Needed by Aug 15:**
  - an executed equity commitment letter for **100% of price + costs**, with no diligence or financing outs
  - proof of funds (an undrawn-commitment certificate or bank letter) and IC minutes
  - a light PSA markup
  - the **10% deposit (about $11M)** ready to wire at award (Aug 30)
- Keep the memo's best instinct: no closing dependency on any loan.

## 5. Discount rate and IRR cash base — **Major**

- **Hurdle.**
  - 2018 onshore PDP royalty buyers used PV10–12 on the strip. Offshore, single-HPHT-well PDP warrants about **15%** (PV $126M).
  - The memo calls 12% its rate but bids at a **24–26% base IRR**, and its walk-away gives about 5% in the downside cases.
  - One rule: a 15% strip hurdle **and** a downside IRR of at least 8–10%.
- **Cash base.**
  - Netting the credit against price is right in concept.
  - But returns.py books all $28–29M at t=0, omits transaction costs (the case requires financing costs), dates t=0 at Sept 14 rather than Aug 15, and ignores the anchor's pref and promote.
- **Re-run with about $17M at close, the rest at t≈0.3, and 1.5% costs:**

  | Bid | Unlevered, strip | Unlevered, low | Unlevered, steep decline | Levered ($30M loan, 2% fee), strip | LP net of 8%/20% promote |
  |---|---|---|---|---|---|
  | $105M | 27.7% | 13.6% | 16.5% | 30.0% | 25.1% |
  | $110M | **23.9%** (memo 25.8%) | 10.9% | 13.0% | **25.4%** (memo 32.7%) | 21.7% |
  | $115M | 20.6% | 8.5% | 10.0% | 21.6% | 18.8% |
  | $125M | 15.1% | 4.6% | 5.0% | 15.5% | 14.0% |

- Correctly sized leverage adds **about 1.5 points**. On a 2.5-year-duration asset, debt returns capital; it doesn't justify price.
- Minor: levered.py's "repaid by" print is hard-coded to 2019, and the fixed 7.25% ignores the September and December hikes the market expected.

## Hindsight flags

- **Post-cutoff sources:** Argus (Sep 5), Haynes Boone Fall-2018, FedWatch (Aug 20–22), Citi/SPEE (Jan 2019), Mercer (Dec 2018) and Franco-Nevada/Continental (closed Oct 2018). Replace them with Aug 15 CME settles and pre-cutoff sources.
- **OGOR-A for May 2018:** confirm it was posted before Aug 15.
- **Labeling:** label all financing as assumption, per the case.

## 6. Most credible 5-week structure

**Single anchor, 100% equity at close, no debt dependency.** One GoM-literate committed-capital investor signs a commitment letter by Aug 13 and funds the deposit. The team holds a 5% sponsor-funded co-invest and a promote. After closing come an optional Q1-2019 royalty term loan ($25–30M recap) and an optional Kodiak/SSC sell-down. **Neither is in the bid math.**

**Sources and uses at Sept 14 ($M)**

| | Bid $110 | Bid $105 (preferred) |
|---|---|---|
| Purchase price | 110.0 | 105.0 |
| Less preliminary effective-date credit (Jan–Jun receipts) | (17.0) | (17.0) |
| Transaction costs | 1.6 | 1.6 |
| Liquidity reserve | 1.5 | 1.5 |
| **Total uses** | **96.1** | **91.1** |
| Anchor equity (95%, includes the 10% deposit) | 91.3 | 86.5 |
| Sponsor/team co-invest (5%) | 4.8 | 4.6 |
| **Total sources** | **96.1** | **91.1** |

**After closing:** about $11M of credit comes back at final settlement and a $25–30M loan is returned to equity, so net equity at risk falls to about $50–55M. Size the commitment about $5M above uses to cover the Lucius suspense risk.

---

**Fundable bid: $105M via a single-anchor all-equity commitment (100% equity at close, no financing condition, post-close royalty term loan as optional recap); walk-away $115M.**

Only capital that has already been raised can commit, wire a 10% deposit and close by Sept 14. That capital will price an offshore, Kodiak-concentrated, fast-declining PDP package at a 15% strip hurdle with an 8–10% downside floor, after its own pref and promote. At $105M, with realistic settlement (about $17M credited at close, not $29M) and costs, the package returns 27.7% unlevered on the strip, 13.6% at $45/$2.25 and 16.5% under steep decline, with about 25% to the LP after promote. That gives an IC room to approve in four weeks. At $115M the downside cases fall to 8.5–10%, the edge of fundability. At the memo's $125M they fall to about 5%, below the cost of any capital in the stack. Debt adds only about 1.5 points and can't close in time, so it must not set the price. If no unconditional commitment for about $96M (plus $5M headroom) is signed by Aug 13, walk away and tell BP you can transact in Q4.
