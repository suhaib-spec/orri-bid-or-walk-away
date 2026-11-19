# BOEM actual production vs Wood Mackenzie: ORRI package (valuation date 15-Aug-2018)

## Data and method

- **Source:** BOEM OGOR-A delimited yearly files `ogora{2009..2018}delimit.zip` from https://www.data.boem.gov/Production/Files/. These report production by lease, completion (API) and month. I also used BOEM borehole data (`Well/Files/5010delimit.zip`) and End-of-Operations Reports (`Well/Files/eWellEORRawData.zip`) for bottom-hole block/aliquot, TVD and perforation depths. The raw files are in `scratchpad\boem\raw\`. Filtered rows are in `scratchpad\boem\filtered_rows.csv`, and the tidy lease-month file is `scratchpad\boem\monthly_by_lease.csv`. The scripts are in `scratchpad\scripts\` (extract.py, analyze.py, eor.py, agg.py).
- **Months used for conclusions:** Jan-2015 to **May-2018**. Operators file OGOR-A by the 15th of the second month after production, so May-2018 was due 15-Jul-2018 and April-2018 is the conservative cut. Run-rates are shown for both. **Jun-Dec 2018 is labelled HINDSIGHT** and is not used in conclusions.
- **Vintage caveat:** the files were downloaded in Nov-2026, so they include later operator corrections. Figures a bidder could have pulled on 15-Aug-2018 may differ slightly, mostly in the latest 1-3 months.
- **Definitions:** oil means liquids on oil-coded (O) completions, and condensate means liquids on gas-coded (G) completions. Liquids = oil + condensate. Gas = all gas reported (casinghead plus gas-well gas), wet and before shrink. 1 boe = 6 mcf. Rates are calendar-day averages.
- **Property gross:**
  - Kodiak = well SS002 (API 608174129200), unit 754313008. It is reported on G24107 (S01 interval) through Dec-2016 and on G24102 (S02) from Jan-2017. The Eni Devils Tower well SS005 on G24107 is excluded: its bottom hole is in the S/2 of MC 771, outside the unit.
  - Lucius = all Anadarko-reported KC875-field completions on G26771, G21444, G21447 and G32654. ExxonMobil rows on G21447/G32654 report zero.
  - Stones = G17001. The other package leases report no production. WR 464 (G32690) is shown separately.
  - All other properties = all producing completions on the named leases.
- **ORRI base:**
  - Kodiak: 6.375% × unit well.
  - Lucius: 2% × lease-located production on G26771+G21444 for 2015-2017, then 1.4288% × unit total from Jan-2018.
  - Stones: 1.5% × G17001.
  - Pompano: 5.625% × well SS002 only (see below).
  - Orion: 1.3125%. South Santa Cruz: 0.93%. GI 116: 0.5% × unit (G13943+G13944).
  - MP 59: 2.604167% × G03194 lease-located production. Unit tract factors are not public in OGOR-A.
  - SS 219: 8%, with 4% as a sensitivity.

## Key comparison vs Wood Mackenzie (gross field)

| Field | Period | Actual liquids kb/d | WM | Ratio | Actual gas MMcf/d | WM | Ratio |
|---|---|---|---|---|---|---|---|
| Kodiak | 2017 | 5.0 | 10.5 | 0.48 | 4.8 | 25.2 | 0.19 |
| Kodiak | 2018: Jan-May actual / Mar-May actual | 11.2 / 16.9 | 17.0 | 0.66 / 1.00 | 9.2 / 13.9 | 20.1 | 0.46 / 0.69 |
| Lucius | 2017 | 56.9 | 56.9 | 1.00 | 63.2 | 63.2 | 1.00 |
| Lucius | 2018: Jan-May / Mar-May | 36.8 / 31.7 | 50.3 | 0.73 / 0.63 | 34.9 / 30.0 | 53.2 | 0.66 / 0.56 |
| Stones | 2017 | 19.9 | 21.6 | 0.92 | 3.0 | 5.9 | 0.51 |
| Stones | 2018: Jan-May / Jan-Feb | 10.1 / 25.8 | 60.3 | 0.17 / 0.43 | 1.5 / 3.8 | 8.7 | 0.17 / 0.44 |
| South Santa Cruz | 2017 | 2.4 (4.1 Jun-Dec) | 5.6 | 0.43 | 1.1 | 4.6 | 0.24 |
| South Santa Cruz | 2018: Jan-May | 3.5 | 13.7 | 0.26 | 1.8 | 11.1 | 0.16 |

How to read the table:
- **Lucius 2017** matches WM exactly, so WM's 2017 is BOEM history. WM's 2018 (50.3 kb/d) is 27-37% above what Jan-May 2018 actually shows. G21447 (KC 919) fell from about 30 kb/d in late 2017 to about 8-16 kb/d by Apr-May 2018.
- **Kodiak 2017:** WM's 10.5 kb/d is consistent with a no-outage year, since Jan-May 2017 averaged 11.5 kb/d. Actual was 5.0 kb/d because of the 7-Jun-2017 to 22-Feb-2018 shutdown. Mar-May 2018 at 16.9 kb/d is right on WM's 2018 rate. WM gas is 2-5x too high for Kodiak: the actual GOR is about 0.8-1.0 mcf/bbl.
- **Stones** produced zero from Mar to May 2018. All five wells are status 12 (shut-in) in Apr-May, and production resumes in Jun-2018 (HINDSIGHT). WM's 60.3 kb/d for 2018 is unsupported by anything public by Aug-2018. The best pre-shut-in month was 35 kb/d (Jul-2017).
- **South Santa Cruz** is a single well (M89 sand, 12,339-12,414 ft TVD). It has run at a flat 3.3-3.6 kb/d since start-up on 11-Jun-2017. WM's 13.7 kb/d would need additional wells. No second well appears in BOEM borehole data by Aug-2018.

## 2017 ORRI revenue reconciliation (Hart Energy: "2017 net revenue ~ $20.4 million")

Pricing assumptions:
- Deepwater oil (Mars-type) $51.5/bbl.
- Shelf oil (LLS-type) $54.0/bbl.
- Gas: Henry Hub $2.99/MMBtu × 1.10 MMBtu/mcf = $3.29/mcf.
- No severance tax (federal OCS). The base case takes no transport or processing deductions.

| Property | 2017 ORRI $M |
|---|---|
| Kodiak (6.375%) | 6.42 |
| Lucius (2% × G26771+G21444, lease-located) | 7.46 |
| Stones (1.5%) | 5.68 |
| South Santa Cruz (0.93%) | 0.43 |
| Pompano (5.625%) | 0.00 |
| Orion (1.3125%) | 0.11 |
| GI 116 (0.5%) | 0.20 |
| MP 59 (2.604167%, G03194 lease-located) | 0.33 |
| SS 219 (8%) | 1.15 |
| **Total (gross of deductions)** | **21.8** |

Sensitivities:
- Less $3/bbl and $0.40/mcf of transport and processing deductions: **$20.4M**. This matches the Hart figure.
- Flat WTI $50.8 and gas $2.99/mcf: $21.3M.
- SS 219 at 4%: −$0.57M.

**Conclusion:** BOEM volumes reproduce the advertised $20.4M within about 5%, assuming the seller's number is net of normal deductions and uses SS 219 at 8%. A 4% SS 219 basis still lands within about 4%.

Why 2017 is not a clean base year:
1. **The Kodiak outage cost about $8.3M.** At the Jan-May 2017 rate for the full year, Kodiak ORRI would have been about $14.7M instead of $6.4M.
2. **The Lucius basis changed on 1-Jan-2018.** In 2017 the two ORRI leases held only 33% of Lucius liquids, because most production sits on KC 919. Pre-unit lease-located 2% gave 137k net bbl. The 1.4288% unit share on 2017 volumes would have given 297k net bbl (about $16.4M vs $7.5M). The unit therefore more than doubles the ORRI's share of Lucius, but Lucius itself is declining fast in 2018.
3. **Stones ramped up through 2017,** with a near-zero Sep-2017.
4. **Pompano contributed $0** (see below).
5. **South Santa Cruz started mid-year.**

## Net production run-rate to the ORRI package (boe/d)

| Property | 2017 | Q1-2018 | Jan-Apr 2018 | Mar-May 2018 | Apr-May 2018 |
|---|---|---|---|---|---|
| Kodiak | 373 | 487 | 712 | 1,227 | 1,293 |
| Lucius | 430 | 719 | 683 | 524 | 446 |
| Stones | 307 | 260 | 195 | 0 (shut-in) | 0 |
| South Santa Cruz | 24 | 36 | 36 | 34 | 35 |
| Pompano | 0 | 0 | 0 | 0 | 0 |
| Orion | 6 | 6 | 6 | 5 | 4 |
| GI 116 unit | 17 | 23 | 23 | 23 | 23 |
| MP 59 | 29 | 17 | 17 | 16 | 16 |
| SS 219 (8%) | 81 | 77 | 80 | 87 | 85 |
| **Total** | **1,267** | **1,625** | **1,751** | **1,916** | **1,901** |

The Mar-May 2018 total of 1,916 boe/d is about 85% liquids. If Stones is normalised to its Jan-Feb 2018 rate (about 396 net boe/d), the package runs at about **2,300 net boe/d**. HINDSIGHT: Jun-Dec 2018 actually averaged about 2,130 net boe/d.

## Surprises and flags

1. **Pompano ORRI area has had zero production since Oct-2014.**
   - The only well in the ORRI area is SS002 on MC 72 (API 608174113700). It was drilled by LLOG, then operated by Energy XXI, and later by Cox.
   - Its bottom hole is in the S/2 of MC 72 (7,007 ft from the south line). Perforations are at 12,678-12,755 ft TVD, so it is inside the surface-to-13,405 ft window.
   - It produced gas from 9/2009 to 9/2014 and then went to zero, status shut-in. It is P&A'd 11/2022 (HINDSIGHT).
   - The only producing completion on G08483 from 2015 to 2018 is Talos TB008D (Pompano platform). That well bottoms at 4,111 ft from the north line, in the N/2 S/2 N/2, which is outside the ORRI aliquots, and it is not an LLOG/Nexen-assignee well. It is excluded.
   - Kosmos drilled well 003/ST01 on MC 72 in Feb-May 2018. Both bottoms are in the N/2 at 14,636 and 17,989 ft TVD, and the well was P&A'd 3-May-2018. It is outside the ORRI area and depth.
   - **Pompano value is option value only.**
2. **"Mt. Providence" is on MC 28 (G09771), not MC 72.** Talos/Stone well 004 (API 608174136600) is surface and bottom MC 28, M83A sand at about 10,000 ft TVD, completed 8-Jul-2018, with first production 10-Jul-2018. It is outside the package.
3. **Stones was shut in from Mar to May 2018,** and Sep-2017 was also near zero. WR 464 (G32690, outside the package) has a Stones well (SN206) that was completed Sep-2017. G32690 has carried the Stones unit number 754306006 since Mar-2018, so it was public by Aug-2018. This well first produced Oct-2018 (HINDSIGHT). Check whether G17001 stays the "only lease receiving allocation" once WR 464 produces into the unit.
4. **Kodiak** is a single well producing from two intervals (S01 reported on G24107, S02 on G24102). It is all within unit 754313008, so there is no allocation issue. The OGOR-A operator changed from Deep Gulf Energy II to Kosmos in Oct-2017.
5. **Lucius 2018 decline** (G21447 especially) is steep relative to WM. ExxonMobil-operated rows (Hadrian North area) on KC 918/919 report zero. G32654 (KC 918) shows its first volume only in Dec-2018 (HINDSIGHT).
6. **MP 59 gas collapsed in 2018** (4.4 → 1.7 MMcf/d), mainly gas well I002 on G03194. Operator moved from Chevron to Cantium in Oct-2017. ORRI basis vs unit 754300007 tract allocation is unresolved. Unit-coded wells sit on both G03194 and G08461.
7. **GI 116:** every producing completion with known perforations is below 13,000 ft subsea (A002 about 15,800 ft TVD; A005 about 18,260-19,300 ft; A007 about 19,270 ft). A004's perforation depth is not in the EOR file; its TD is 17,392 ft TVD. The ORRI depth limit probably excludes nothing. GI 116 gas rose from 13.8 to 18.8 MMcf/d in 2018.
8. **South Santa Cruz** is entirely above 19,000 ft TVDSS, so the full well is ORRI-bearing.
9. WM's Kodiak and SSC gas forecasts are 2-6x actual GORs. Value gas off actual GORs.

---

# Appendix: generated tables (scripts/analyze.py)

## Gross property production (BOEM OGOR-A), liquids kb/d and gas MMcf/d (calendar-day averages)

| Property | 2015 | 2016 | 2017 | Q1-2018 | Jan-Apr 2018 | Jan-May 2018 | Mar-May 2018 | Apr-May 2018 | HINDSIGHT Jun-Dec 2018 |
|---|---|---|---|---|---|---|---|---|---|
| Kodiak | 0.00 / 0.00 | 5.83 / 4.02 | 5.05 / 4.82 | 6.75 / 5.31 | 9.83 / 8.02 | 11.22 / 9.17 | 16.93 / 13.92 | 17.81 / 14.85 | 14.88 / 11.67 |
| Lucius | 60.79 / 67.43 | 73.62 / 83.03 | 56.90 / 63.16 | 43.41 / 41.44 | 41.25 / 39.15 | 36.77 / 34.92 | 31.66 / 30.02 | 26.96 / 25.31 | 25.30 / 23.84 |
| Stones | 0.00 / 0.00 | 2.01 / 0.39 | 19.94 / 2.98 | 16.90 / 2.55 | 12.68 / 1.91 | 10.07 / 1.52 | 0.00 / 0.03 | 0.00 / 0.00 | 32.31 / 5.00 |
| South Santa Cruz | 0.00 / 0.00 | 0.00 / 0.00 | 2.40 / 1.09 | 3.59 / 1.75 | 3.59 / 1.79 | 3.53 / 1.80 | 3.34 / 1.78 | 3.44 / 1.87 | 3.02 / 1.54 |
| Pompano | 0.14 / 0.17 | 0.14 / 0.30 | 0.16 / 0.17 | 0.11 / 0.14 | 0.13 / 0.16 | 0.16 / 0.20 | 0.20 / 0.26 | 0.23 / 0.29 | 0.23 / 0.29 |
| Orion | 0.48 / 0.06 | 0.48 / 0.08 | 0.44 / 0.02 | 0.43 / 0.03 | 0.41 / 0.03 | 0.38 / 0.03 | 0.36 / 0.03 | 0.31 / 0.03 | 0.45 / 0.02 |
| Grand Isle 116 unit | 1.25 / 14.91 | 1.16 / 13.72 | 1.15 / 13.81 | 1.48 / 18.82 | 1.48 / 18.84 | 1.48 / 18.71 | 1.51 / 18.95 | 1.49 / 18.54 | 1.42 / 18.33 |
| Main Pass 59 | 0.52 / 6.39 | 0.42 / 4.83 | 0.38 / 4.41 | 0.36 / 1.69 | 0.35 / 1.74 | 0.35 / 1.68 | 0.36 / 1.57 | 0.34 / 1.67 | 0.42 / 1.30 |
| Ship Shoal 219 | 0.96 / 5.71 | 0.75 / 3.38 | 0.57 / 2.60 | 0.57 / 2.39 | 0.59 / 2.52 | 0.58 / 2.54 | 0.61 / 2.84 | 0.60 / 2.75 | 0.50 / 2.14 |

## Annual / period gross volumes (liquids Mbbl, gas MMcf)

| Property | 2016 liq | 2016 gas | 2017 liq | 2017 gas | Jan-May18 liq | Jan-May18 gas | Jan-May18 annualized liq | annualized gas |
|---|---|---|---|---|---|---|---|---|
| Kodiak | 2,132 | 1,472 | 1,842 | 1,759 | 1,694 | 1,384 | 4,095 | 3,345 |
| Lucius | 26,946 | 30,389 | 20,768 | 23,052 | 5,552 | 5,274 | 13,420 | 12,747 |
| Stones | 734 | 144 | 7,277 | 1,089 | 1,521 | 229 | 3,677 | 554 |
| South Santa Cruz | 0 | 0 | 875 | 398 | 533 | 271 | 1,288 | 655 |
| Pompano | 52 | 108 | 60 | 61 | 24 | 30 | 58 | 73 |
| Orion | 174 | 28 | 159 | 8 | 58 | 4 | 139 | 11 |
| Grand Isle 116 unit | 424 | 5,022 | 422 | 5,040 | 224 | 2,825 | 542 | 6,828 |
| Main Pass 59 | 155 | 1,769 | 140 | 1,609 | 53 | 253 | 128 | 613 |
| Ship Shoal 219 | 275 | 1,238 | 209 | 950 | 88 | 383 | 212 | 926 |

## Actual vs Wood Mackenzie (gross field; liquids kb/d, gas MMcf/d)

| Field | Period | Actual liq | WM liq | Actual/WM | Actual gas | WM gas | Actual/WM |
|---|---|---|---|---|---|---|---|
| Kodiak | 2017 vs WM 2017 | 5.0 | 10.5 | 0.48 | 4.8 | 25.2 | 0.19 |
| Kodiak | 2018 (Jan-May act.) vs WM 2018 | 11.2 | 17.0 | 0.66 | 9.2 | 20.1 | 0.46 |
| Kodiak | 2018 (Mar-May act.) vs WM 2018 | 16.9 | 17.0 | 1.00 | 13.9 | 20.1 | 0.69 |
| Lucius | 2017 vs WM 2017 | 56.9 | 56.9 | 1.00 | 63.2 | 63.2 | 1.00 |
| Lucius | 2018 (Jan-May act.) vs WM 2018 | 36.8 | 50.3 | 0.73 | 34.9 | 53.2 | 0.66 |
| Lucius | 2018 (Mar-May act.) vs WM 2018 | 31.7 | 50.3 | 0.63 | 30.0 | 53.2 | 0.56 |
| Stones | 2017 vs WM 2017 | 19.9 | 21.6 | 0.92 | 3.0 | 5.9 | 0.51 |
| Stones | 2018 (Jan-May act.) vs WM 2018 | 10.1 | 60.3 | 0.17 | 1.5 | 8.7 | 0.17 |
| Stones | 2018 (Mar-May act.) vs WM 2018 | 0.0 | 60.3 | 0.00 | 0.0 | 8.7 | 0.00 |
| South Santa Cruz | 2017 vs WM 2017 | 2.4 | 5.6 | 0.43 | 1.1 | 4.6 | 0.24 |
| South Santa Cruz | 2018 (Jan-May act.) vs WM 2018 | 3.5 | 13.7 | 0.26 | 1.8 | 11.1 | 0.16 |
| South Santa Cruz | 2018 (Mar-May act.) vs WM 2018 | 3.3 | 13.7 | 0.24 | 1.8 | 11.1 | 0.16 |

## Implied 2017 ORRI revenue (gross of any post-production deductions/taxes). Oil: Mars-ish $51.5 deepwater, LLS-ish $54.0 shelf; gas $3.29/mcf

| Property | ORRI decimal | 2017 net liq (bbl) | 2017 net gas (mcf) | Oil rev $M | Gas rev $M | Total $M |
|---|---|---|---|---|---|---|
| Kodiak | 6.375% | 117,407 | 112,129 | 6.05 | 0.37 | 6.42 |
| Lucius | 2% on G26771+G21444 (lease-located) | 137,210 | 119,347 | 7.07 | 0.39 | 7.46 |
| Stones | 1.5% (G17001) | 109,153 | 16,330 | 5.62 | 0.05 | 5.68 |
| South Santa Cruz | 0.93% | 8,138 | 3,702 | 0.42 | 0.01 | 0.43 |
| Pompano | 5.625% (SS002 only) | 0 | 0 | 0.00 | 0.00 | 0.00 |
| Orion | 1.3125% | 2,088 | 101 | 0.11 | 0.00 | 0.11 |
| Grand Isle 116 unit | 0.5% | 2,108 | 25,202 | 0.11 | 0.08 | 0.20 |
| Main Pass 59 | 2.604167% (G03194 lease-located) | 3,640 | 41,890 | 0.20 | 0.14 | 0.33 |
| Ship Shoal 219 | 8% | 16,754 | 76,037 | 0.90 | 0.25 | 1.15 |
| **Total** | | | | | | **21.77** |

Total with Ship Shoal at 4%: 21.20 $M. Without any gas uplift (gas at $2.99/mcf): see sensitivity.

Sensitivities (2017, $M): 
- WTI flat $50.8 for all oil, gas $2.99/mcf: 21.32
- Base less $3/bbl & $0.40/mcf transport/processing deductions: 20.43
- Ship Shoal at 4%: 21.20
- Kodiak if Jan-May 2017 rate had continued all year: Kodiak ORRI 14.68 vs actual 6.42 (+8.26)
- Lucius if 2017 had been on 1.4288% unit basis: 16.36 vs lease-located basis 7.46

## Net ORRI production run-rate (boe/d, 6 mcf = 1 boe)

| Property | 2017 | Q1-2018 | Jan-Apr 2018 | Mar-May 2018 | Apr-May 2018 | HINDSIGHT Jun-Dec 2018 |
|---|---|---|---|---|---|---|
| Kodiak | 372.9 | 486.9 | 711.9 | 1,227.2 | 1,292.9 | 1,072.7 |
| Lucius | 430.4 | 719.0 | 682.5 | 523.9 | 445.5 | 418.3 |
| Stones | 306.5 | 259.9 | 194.9 | 0.1 | 0.0 | 497.1 |
| South Santa Cruz | 24.0 | 36.1 | 36.1 | 33.8 | 34.8 | 30.5 |
| Pompano | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Orion | 5.8 | 5.7 | 5.5 | 4.8 | 4.1 | 5.9 |
| Grand Isle 116 unit | 17.3 | 23.1 | 23.1 | 23.3 | 22.9 | 22.4 |
| Main Pass 59 | 29.1 | 16.7 | 16.7 | 16.2 | 16.1 | 16.7 |
| Ship Shoal 219 | 80.6 | 77.2 | 80.4 | 86.8 | 84.8 | 68.2 |
| **Total** | **1,266.5** | **1,624.5** | **1,751.2** | **1,916.1** | **1,901.3** | **2,131.8** |

Net liquids / net gas split (bbl/d ; mcf/d), Mar-May 2018:
- Kodiak: 1,079.2 bbl/d ; 887.6 mcf/d
- Lucius: 452.4 bbl/d ; 428.9 mcf/d
- Stones: 0.0 bbl/d ; 0.5 mcf/d
- South Santa Cruz: 31.0 bbl/d ; 16.5 mcf/d
- Pompano: 0.0 bbl/d ; 0.0 mcf/d
- Orion: 4.8 bbl/d ; 0.3 mcf/d
- Grand Isle 116 unit: 7.5 bbl/d ; 94.8 mcf/d
- Main Pass 59: 9.4 bbl/d ; 41.0 mcf/d
- Ship Shoal 219: 49.0 bbl/d ; 227.0 mcf/d

## First month each lease carried a unit agreement number in OGOR-A (2015-2018 window)
- G03194 (Main Pass 59): 201501 unit 754300007
- G08461 (Main Pass 59 (G08461, no ORRI)): 201501 unit 754300007
- G13943 (Grand Isle 116 unit): 201501 unit 754398019
- G13944 (Grand Isle 116 unit): 201501 unit 754398019
- G17001 (Stones): 201609 unit 754306006
- G21444 (Lucius): 201801 unit 754318001
- G21447 (Lucius): 201801 unit 754318001
- G24102 (Kodiak): 201701 unit 754313008
- G24107 (Kodiak): 201602 unit 754313008
- G26771 (Lucius): 201801 unit 754318001
- G32690 (Stones (WR 464, outside pkg)): 201803 unit 754306006

## Monthly gross by property (liquids bbl/d ; gas mcf/d). Months after 2018-05 = HINDSIGHT

| Month | Kodiak | Lucius | Stones | South Santa Cruz | Pompano | Orion | Grand Isle 116 unit | Main Pass 59 | Ship Shoal 219 |
|---|---|---|---|---|---|---|---|---|---|
| 201501 | 0 ; 0 | 7,216 ; 6,641 | 0 ; 0 | 0 ; 0 | 359 ; 279 | 603 ; 44 | 1,324 ; 16,273 | 585 ; 7,021 | 952 ; 4,773 |
| 201502 | 0 ; 0 | 23,485 ; 27,294 | 0 ; 0 | 0 ; 0 | 117 ; 111 | 467 ; 33 | 1,302 ; 15,941 | 682 ; 7,141 | 746 ; 3,188 |
| 201503 | 0 ; 0 | 41,118 ; 41,022 | 0 ; 0 | 0 ; 0 | 81 ; 70 | 584 ; 36 | 1,353 ; 16,812 | 644 ; 6,796 | 943 ; 4,692 |
| 201504 | 0 ; 0 | 54,516 ; 55,327 | 0 ; 0 | 0 ; 0 | 138 ; 115 | 576 ; 35 | 1,323 ; 15,877 | 375 ; 6,684 | 514 ; 1,789 |
| 201505 | 0 ; 0 | 73,951 ; 85,415 | 0 ; 0 | 0 ; 0 | 14 ; 2 | 140 ; 12 | 1,295 ; 15,797 | 396 ; 7,065 | 933 ; 5,551 |
| 201506 | 0 ; 0 | 76,858 ; 89,367 | 0 ; 0 | 0 ; 0 | 142 ; 177 | 395 ; 30 | 1,257 ; 14,980 | 608 ; 6,829 | 1,242 ; 7,057 |
| 201507 | 0 ; 0 | 76,701 ; 87,631 | 0 ; 0 | 0 ; 0 | 6 ; 14 | 267 ; 18 | 1,229 ; 14,395 | 557 ; 6,249 | 1,233 ; 7,885 |
| 201508 | 0 ; 0 | 72,805 ; 82,882 | 0 ; 0 | 0 ; 0 | 294 ; 257 | 471 ; 77 | 1,056 ; 12,264 | 575 ; 6,712 | 1,056 ; 7,444 |
| 201509 | 0 ; 0 | 78,441 ; 86,157 | 0 ; 0 | 0 ; 0 | 125 ; 198 | 598 ; 84 | 1,247 ; 14,686 | 513 ; 6,493 | 959 ; 6,310 |
| 201510 | 0 ; 0 | 76,846 ; 85,934 | 0 ; 0 | 0 ; 0 | 158 ; 403 | 613 ; 106 | 1,228 ; 14,359 | 289 ; 5,131 | 828 ; 5,775 |
| 201511 | 0 ; 0 | 72,005 ; 78,086 | 0 ; 0 | 0 ; 0 | 127 ; 185 | 530 ; 55 | 1,186 ; 13,833 | 507 ; 5,540 | 1,148 ; 7,065 |
| 201512 | 0 ; 0 | 73,230 ; 80,742 | 0 ; 0 | 0 ; 0 | 154 ; 247 | 565 ; 135 | 1,171 ; 13,775 | 466 ; 5,071 | 981 ; 6,712 |
| 201601 | 0 ; 0 | 62,167 ; 68,720 | 0 ; 0 | 0 ; 0 | 141 ; 409 | 533 ; 106 | 1,154 ; 13,385 | 386 ; 4,449 | 974 ; 5,703 |
| 201602 | 0 ; 9 | 58,020 ; 64,186 | 0 ; 0 | 0 ; 0 | 86 ; 167 | 538 ; 85 | 1,167 ; 13,693 | 486 ; 4,616 | 877 ; 5,482 |
| 201603 | 309 ; 393 | 70,102 ; 78,487 | 0 ; 0 | 0 ; 0 | 119 ; 213 | 503 ; 97 | 1,162 ; 13,562 | 647 ; 4,828 | 978 ; 4,953 |
| 201604 | 0 ; 0 | 70,247 ; 79,127 | 0 ; 0 | 0 ; 0 | 220 ; 451 | 464 ; 37 | 1,172 ; 13,709 | 402 ; 4,466 | 732 ; 3,195 |
| 201605 | 3,951 ; 3,007 | 84,194 ; 95,239 | 0 ; 0 | 0 ; 0 | 121 ; 295 | 468 ; 20 | 1,134 ; 13,367 | 386 ; 4,208 | 724 ; 3,188 |
| 201606 | 11,696 ; 8,401 | 57,014 ; 62,484 | 0 ; 0 | 0 ; 0 | 213 ; 383 | 407 ; 21 | 1,154 ; 13,732 | 334 ; 4,139 | 699 ; 2,967 |
| 201607 | 11,415 ; 8,324 | 81,135 ; 91,593 | 0 ; 0 | 0 ; 0 | 0 ; 0 | 296 ; 77 | 1,125 ; 13,216 | 396 ; 3,872 | 792 ; 2,928 |
| 201608 | 9,436 ; 6,448 | 82,245 ; 93,946 | 0 ; 0 | 0 ; 0 | 147 ; 396 | 564 ; 126 | 1,148 ; 13,501 | 480 ; 3,916 | 683 ; 2,724 |
| 201609 | 8,990 ; 5,423 | 77,206 ; 88,842 | 3,554 ; 725 | 0 ; 0 | 99 ; 297 | 484 ; 170 | 1,153 ; 13,690 | 417 ; 4,554 | 663 ; 2,593 |
| 201610 | 8,931 ; 6,127 | 92,946 ; 105,823 | 10,055 ; 2,160 | 0 ; 0 | 192 ; 504 | 531 ; 135 | 1,165 ; 13,874 | 430 ; 6,072 | 686 ; 2,674 |
| 201611 | 8,393 ; 5,682 | 76,049 ; 85,552 | 6,844 ; 1,198 | 0 ; 0 | 176 ; 272 | 423 ; 18 | 1,184 ; 14,432 | 397 ; 6,275 | 604 ; 2,382 |
| 201612 | 6,594 ; 4,300 | 70,680 ; 80,621 | 3,563 ; 626 | 0 ; 0 | 177 ; 160 | 493 ; 23 | 1,193 ; 14,503 | 337 ; 6,588 | 617 ; 1,845 |
| 201701 | 8,371 ; 8,296 | 78,734 ; 89,893 | 409 ; 35 | 0 ; 0 | 163 ; 124 | 365 ; 20 | 1,191 ; 14,336 | 332 ; 6,244 | 380 ; 1,809 |
| 201702 | 14,214 ; 14,501 | 57,879 ; 66,887 | 5,136 ; 510 | 0 ; 0 | 142 ; 123 | 338 ; 15 | 1,185 ; 14,266 | 301 ; 6,358 | 716 ; 2,396 |
| 201703 | 11,719 ; 10,808 | 48,461 ; 55,876 | 25,201 ; 4,109 | 0 ; 0 | 118 ; 112 | 510 ; 22 | 1,158 ; 13,856 | 459 ; 6,584 | 624 ; 2,280 |
| 201704 | 10,986 ; 10,009 | 66,963 ; 76,832 | 22,987 ; 3,615 | 0 ; 0 | 176 ; 162 | 345 ; 14 | 1,148 ; 13,820 | 448 ; 6,075 | 397 ; 1,656 |
| 201705 | 12,664 ; 12,000 | 61,895 ; 70,664 | 14,457 ; 2,216 | 0 ; 0 | 135 ; 132 | 491 ; 23 | 1,117 ; 13,238 | 439 ; 5,954 | 610 ; 2,071 |
| 201706 | 3,290 ; 2,946 | 58,665 ; 65,918 | 29,614 ; 4,392 | 4,312 ; 2,095 | 137 ; 118 | 420 ; 23 | 1,112 ; 13,059 | 290 ; 4,341 | 566 ; 3,990 |
| 201707 | 0 ; 0 | 55,858 ; 62,515 | 34,962 ; 5,668 | 4,528 ; 2,081 | 308 ; 311 | 482 ; 24 | 1,049 ; 12,520 | 289 ; 3,081 | 556 ; 3,052 |
| 201708 | 0 ; 0 | 44,694 ; 47,682 | 32,163 ; 5,318 | 3,743 ; 1,698 | 143 ; 184 | 467 ; 26 | 1,191 ; 14,525 | 448 ; 4,726 | 608 ; 2,624 |
| 201709 | 0 ; 0 | 53,685 ; 59,008 | 2,410 ; 69 | 4,134 ; 1,790 | 127 ; 129 | 473 ; 19 | 1,267 ; 15,244 | 586 ; 3,680 | 654 ; 3,078 |
| 201710 | 0 ; 0 | 55,517 ; 60,860 | 27,722 ; 4,272 | 3,091 ; 1,390 | 147 ; 165 | 440 ; 21 | 1,106 ; 13,240 | 415 ; 1,714 | 607 ; 2,867 |
| 201711 | 0 ; 0 | 48,309 ; 49,315 | 23,517 ; 3,296 | 4,538 ; 2,038 | 165 ; 169 | 436 ; 26 | 1,190 ; 14,053 | 277 ; 2,123 | 617 ; 2,838 |
| 201712 | 0 ; 0 | 52,215 ; 52,748 | 19,189 ; 2,037 | 4,300 ; 1,939 | 198 ; 262 | 453 ; 21 | 1,151 ; 13,631 | 308 ; 2,148 | 563 ; 2,604 |
| 201801 | 0 ; 0 | 49,367 ; 47,626 | 25,427 ; 3,646 | 3,252 ; 1,400 | 36 ; 47 | 394 ; 47 | 1,340 ; 16,498 | 309 ; 1,975 | 480 ; 1,417 |
| 201802 | 4,871 ; 3,680 | 39,595 ; 36,971 | 26,171 ; 4,039 | 4,469 ; 2,300 | 172 ; 175 | 426 ; 18 | 1,564 ; 20,336 | 372 ; 1,690 | 588 ; 2,790 |
| 201803 | 15,203 ; 12,103 | 40,912 ; 39,291 | 0 ; 96 | 3,144 ; 1,592 | 139 ; 200 | 467 ; 21 | 1,540 ; 19,771 | 395 ; 1,396 | 632 ; 3,013 |
| 201804 | 19,062 ; 16,152 | 34,738 ; 32,289 | 0 ; 0 | 3,567 ; 1,914 | 192 ; 226 | 371 ; 29 | 1,482 ; 18,919 | 331 ; 1,907 | 643 ; 2,904 |
| 201805 | 16,592 ; 13,585 | 19,435 ; 18,558 | 0 ; 0 | 3,308 ; 1,824 | 262 ; 346 | 250 ; 28 | 1,503 ; 18,170 | 351 ; 1,431 | 563 ; 2,596 |
| 201806 (H) | 14,341 ; 11,332 | 33,760 ; 32,965 | 21,540 ; 3,142 | 2,821 ; 1,528 | 51 ; 76 | 408 ; 38 | 1,456 ; 18,712 | 298 ; 706 | 604 ; 2,620 |
| 201807 (H) | 16,287 ; 13,203 | 33,359 ; 32,248 | 27,221 ; 4,005 | 3,700 ; 2,018 | 170 ; 170 | 383 ; 14 | 1,453 ; 18,693 | 500 ; 1,094 | 573 ; 2,316 |
| 201808 (H) | 15,428 ; 12,118 | 27,146 ; 25,416 | 27,892 ; 4,193 | 3,045 ; 1,536 | 226 ; 175 | 523 ; 16 | 1,435 ; 18,573 | 484 ; 1,814 | 596 ; 2,609 |
| 201809 (H) | 14,742 ; 11,537 | 19,959 ; 18,331 | 39,796 ; 6,324 | 3,257 ; 1,624 | 214 ; 172 | 467 ; 22 | 1,418 ; 18,542 | 476 ; 1,656 | 602 ; 2,523 |
| 201810 (H) | 14,970 ; 11,827 | 20,738 ; 19,036 | 42,747 ; 7,031 | 2,438 ; 1,162 | 202 ; 242 | 458 ; 5 | 1,423 ; 18,285 | 225 ; 771 | 556 ; 2,070 |
| 201811 (H) | 14,471 ; 11,713 | 24,923 ; 22,888 | 26,187 ; 3,922 | 2,982 ; 1,461 | 278 ; 372 | 442 ; 3 | 1,417 ; 18,136 | 532 ; 1,624 | 0 ; 230 |
| 201812 (H) | 13,894 ; 9,947 | 17,323 ; 16,116 | 40,472 ; 6,317 | 2,906 ; 1,418 | 494 ; 844 | 449 ; 7 | 1,354 ; 17,386 | 461 ; 1,415 | 533 ; 2,565 |