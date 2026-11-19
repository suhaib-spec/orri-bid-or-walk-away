# Mississippi Canyon properties: Orion (MC 110), Pompano (MC 72), South Santa Cruz (MC 563)

Valuation date: Aug 15, 2018. Effective date: Jan 1, 2018. Only information available by Aug 15, 2018 is used.
Labels: **FACT** = cited from a case file. **INF** = my inference.
Abbreviations: WM = Wood Mackenzie summary (the image transcriptions in scratchpad\img). SR = BOEM Serial Register Page (all three printed 04-Jun-2018). RT = record title. OR = operating rights.

---

## 0. Cross-cutting findings

1. **What WM's "Rem PV" actually measures (FACT, verified by calculation).** In all three WM cash-flow tables, "Rem PV" equals the PV of the **Gross Revenue** column, discounted at 10% with mid-year timing from 01/01/2018:
   - Orion: 2.6 in the table vs 2.6 computed.
   - Pompano: 1,270.1 vs 1,270.2.
   - SSC: 1,317.8 vs 1,317.9.

   For a cost-free ORRI on the same production, the PV is therefore about Rem PV × the ORRI's net share, before risking. "Total PV" carries historical revenue forward at 10%, so ignore it. (Script: scratchpad\scripts\mc_calc.py.)
2. **Every Attachment A figure ties exactly to an instrument (FACT):**
   - Orion 0.013125 is stated directly in the instrument as "1.3125% of 100%".
   - Pompano 0.05625 = 7.5% × 75%. The instrument states "7.5% gross / 5.625% net".
   - SSC 0.0093 = 2% × 46.5% of 8/8. This is exact, not rounded.
3. **Only one of the three has real value.** Here is what each ORRI actually burdens:
   - **Orion:** the ORRI covers the whole lease, but the field is nearly depleted. WM's last production year is 2018.
   - **Pompano:** the ORRI covers only the LLOG/Nexen (now M21K/Nexen, Energy XXI-operated) farm-out area: S/2 & S/2 S/2 N/2, from the surface to 13,405 ft TVD. **It does not cover Stone's Pompano field** that WM models. Applying 5.625% to WM's Pompano production would wrongly add about $71M of PV. **This is the main trap in this trio.**
   - **SSC:** a new producing deepwater subsea tieback (first oil June 2017) on the ORRI block. The ORRI is limited to the surface down to 19,000 ft TVDSS. Base PV is about $12.3M at WM's price deck before risking.
4. **Date audit:**
   - No document in these three folders is dated after Aug 15, 2018.
   - Latest-dated items:
     - SSC ORRI scan: PDF created 2018-06-21, modified 2018-06-22.
     - SSC sourcing statement: 2018-06-22.
     - Serial registers: 2018-06-04.
     - Pompano assignment PDF: 2018-05-14.
     - Leases: modified 2018-05-17.
     - Orion ABOS: modified 2018-03-20.
   - The WM summary PDFs in the case folder have creation dates of 2026-11-10 (producer "iOS ... Quartz PDFContext"). These are the student's own re-saves, not case content. They should not be cited as evidence of a date.

---

## 1. ORION (MC 110), OCS-G 18192, Attachment A Net ORRI 0.013125

### 1.1 WM summary: full transcription (Orion (MC 110).pdf; images orion_00–07)
- **Title:** Orion (MC 110)
- **Location:** Sector/Basin: Central Gulf, East Gulf Coast Tertiary. Block: MC/110, Area: 23 km². Water depth: 442 m.
- **Timetable:** Discovery Dec 1983. Production started May 2000. Peak gas production (1 mmcfd) 2003. Peak oil production (1,880 b/d) 2003.
- **Operator:** Fieldwood Energy.
- **Participants:** Fieldwood Energy 58.33%, Marubeni 33.33%, Stone Energy 8.34%.
- **Remaining reserves at 01/01/2018:** 0.1 mmbbl oil; 0.0 bcf sales gas. (Source: Wood Mackenzie.)
- **Summary:** "Orion (MC 110) is an oil and gas field located in the Flextrend of the Gulf of Mexico. The field produces via three wells drilled from the Amberjack (MC 109) platform in the adjacent block."
- **Production:** standard WM downtime caveat (maintenance, hurricanes, equipment failure; annual averages hide troughs and peaks).
- **No** sections on key issues, unitisation or royalty override.

Production (Liquid '000 b/d / Gas mmcfd):

| | 2000 | 2001 | 2002 | 2003 | 2004 | 2005 | 2006 | 2007 |
|---|---|---|---|---|---|---|---|---|
| Liquid | 0.5 | 0.5 | 1.6 | 1.9 | 1.0 | 0.9 | 0.4 | 1.1 |
| Gas | 0.2 | 0.2 | 0.7 | 1.0 | 0.5 | 0.5 | 0.4 | 0.5 |

| | 2008 | 2009 | 2010 | 2011 | 2012 | 2013 | 2014 | 2015 |
|---|---|---|---|---|---|---|---|---|
| Liquid | 0.7 | 0.7 | 0.9 | 0.7 | 0.6 | 0.6 | 0.5 | 0.5 |
| Gas | 0.2 | 0.2 | 0.2 | 0.0 | 0.1 | 0.2 | 0.0 | 0.1 |

Cash flow (Year / Liquids 000b/d / Gas mmcfd / Gross Revenue US$M):

| Year | 1998 | 1999 | 2000 | 2001 | 2002 | 2003 | 2004 | 2005 | 2006 | 2007 | 2008 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Liq | 0.0 | 0.0 | 0.5 | 0.5 | 1.6 | 1.9 | 1.0 | 0.9 | 0.4 | 1.1 | 0.7 |
| Gas | 0.0 | 0.0 | 0.2 | 0.2 | 0.7 | 1.0 | 0.5 | 0.5 | 0.4 | 0.5 | 0.2 |
| Rev | 0.0 | 0.0 | 5.3 | 4.3 | 15.3 | 22.0 | 15.7 | 18.4 | 9.5 | 28.8 | 25.5 |

| Year | 2009 | 2010 | 2011 | 2012 | 2013 | 2014 | 2015 | 2016 | 2017 | 2018 | 2019 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Liq | 0.7 | 0.9 | 0.7 | 0.6 | 0.6 | 0.5 | 0.5 | 0.4 | 0.2 | 0.1 | 0.0 |
| Gas | 0.2 | 0.2 | 0.0 | 0.1 | 0.2 | 0.0 | 0.1 | 0.1 | 0.0 | 0.0 | 0.0 |
| Rev | 14.7 | 25.4 | 27.0 | 21.6 | 21.6 | 17.4 | 8.7 | 6.6 | 4.2 | 2.7 | 0.0 |

- **Totals:** 5.0 (mmbbl), 1.8 (bcf), revenue 294.6. (Check: the sum of 13.8 kb/d-years × 0.365 = 5.04 mmbbl, which matches.)
- **PVs:** Total PV 744.9; Rem PV 2.6. "Discounted at 10.0% from 01/01/2018."

**Status:**
- **FACT:** producing, with steep decline. WM models 0.1 kb/d in 2018 and zero from 2019.
- **FACT:** the wells are dry-tree platform wells drilled from the Amberjack platform on MC 109 (an adjacent block, Fieldwood-operated), with bottom-holes on MC 110.
- **FACT:** SR p.1 shows "Placed on continuous production on 05/12/2000" for MC 110 itself, so production is attributed to the ORRI lease.
- **Host risk:** a single third-party platform.
- **INF:** Fieldwood's Chapter 11 in early 2018 was public before Aug 2018. Verify this.

### 1.2 Chain of title (3. ORRI ABOS MC 110 Devon to BP.PDF, BOEM file 62528, 16 pp.)
- **p1:** BP cover letter dated July 15, 2010, stamped received by BOEMRE Adjudication on JUL 16 2010. It is a Non-Required Filing of "Assignment and Bill of Sale" for:
  - MC 110 (OCS-G 18192)
  - KC 875 (G 21444)
  - WR 199 (G 25237)
  - KC 874 (G 26771)

  Devon Energy Production Company, L.P. assigns BP E&P an ORRI, filed under category 5 ("Overriding Royalty, Production Payment, Net Profit").
- **p2:** Assignor is Devon Energy Production Co., L.P. Assignee is BP Exploration & Production Inc. **Effective 7:00 a.m. CST, Jan 1, 2010.** §1.1(a) conveys all of Assignor's interest in the leases in Exhibit A, including ORRIs.
- **p6:** the Purchase Agreement is dated March 10, 2010.
- **p7–8:** §3.1 is an AS-IS clause that **disclaims title warranty** except as stated in the PSA (Art. IV / §11.1(b)).
- **p9:** governed by Texas law; disputes go to arbitration.
- **p11:** signed by Mark K. Gress (Devon) and Kemper Howe (BP).
- **p12–15:** acknowledgments dated Apr 27, 2010.
- **p16, Exhibit A:**

  | Area | Block | Lease | Lease date | ORRI |
  |---|---|---|---|---|
  | KC | 874 | G 26771 | 11/1/2004 | 2% of 100% from surface to 23,000' |
  | KC | 875 | G 21444 | 12/1/1999 | 2% of 100% |
  | **MC** | **110** | **G 18192** | **8/1/1997** | **1.3125% of 100%** |
  | WR | 199 | G 25237 | 6/1/2003 | 1% of 100% |

- **Supports Attachment A? Yes (FACT).** 1.3125% of 100% = 0.013125. There is no depth limit, and it covers all of Block 110.
- **Derivation (INF):** 1.3125% = 1.5% × 7/8. It also equals 5.25% × 25% (Devon SFS's original 25% RT) and 3.9375% × 1/3. The instrument that **created** the ORRI (most likely Devon's reservation when Devon's 33.33% RT passed to Marubeni effective 1/1/2005, per SR p.2) **is not in the package.** This is a chain gap: we cannot confirm that the ORRI binds current RT owners. Request it.
- **Drafting quirk (FACT):** the Exhibit A header reads "by and between BP Exploration & Production Inc. and Devon". The party order is reversed from the body.
- **For other teammates (FACT):** the same instrument shows KC 874 is depth-limited ("surface to 23,000'"). WR 199 (1%) appears in this Devon→BP ORRI package but **not** in Attachment A, so ask the seller whether it lapsed or is excluded.

### 1.3 Lease status (SR MC 110, 4 pp., printed 04-Jun-2018)
- **Lease terms:**
  - Status PROD. Sale 166 (3/5/1997). Lease date 8/1/1997. 8-year term with a 5-year drilling requirement, which was satisfied.
  - Royalty 12.5%. Lease p.2 says it is eligible for royalty suspension under PL 104-58.
  - 5,760 acres; bonus $3,587,000; rental $7.50/acre. Original lessee Shell 100%.
- **RT (effective 7/1/2013):**
  - Fieldwood Energy LLC 49.99999%
  - Fieldwood Energy Offshore LLC 8.33334%
  - Marubeni Oil & Gas (USA) 33.33333%
  - Stone Energy Offshore 8.33334%

  This matches WM's 58.33 / 33.33 / 8.34.
- **OR, 6,688'–99,999' TVDSS (effective 7/1/2013):**
  - Marubeni 33.33333%
  - Fieldwood Energy Offshore 8.33334%
  - Stone Offshore 8.33334%
  - Fieldwood Energy LLC 25%
  - Apache Shelf Exploration 24.99999%
- **Operator:** Fieldwood Energy LLC.
- **Production history:**
  - Continuous production from 05/12/2000.
  - Suspension of production 2/24/2006–12/31/2006; production resumed 10/17/2006.
  - Held by prior production: production ceased 12/07/2008 and resumed 06/09/2009.
  - Production ceased 07/23/2012 and resumed 09/08/2012.
- No relinquishment or unit. Devon entities held RT from 2000 until Marubeni took over effective 1/1/2005.
- **INF: expiration risk.** With WM showing zero output from 2019, the lease will lapse after 180 days without operations. **The ORRI is extinguished with it.** There is no renewal or extension protection in the instrument.

### 1.4 Net ORRI production (gross × 0.013125)
- **Assumption:** 100% of the Orion field is on MC 110 (WM: "Orion (MC 110)", and the SR shows MC 110 producing).
- 2018: 0.1 kb/d × 0.013125 = **1.3 b/d** oil, about 0 gas. Revenue: $2.7M × 0.013125 = **$35k**.
- 2019–2033: 0.
- PV10: about 2.6 × 0.013125 = **$0.03M**.

**Conclusion: nominal value. Treat it as a zero-to-nuisance asset.**

---

## 2. POMPANO (MC 72 S/2 & S/2 S/2 N/2), OCS-G 08483, Attachment A Net ORRI 0.05625

### 2.1 WM summary: full transcription (Pompano.pdf; images pompano_00–13)
**Location:**
- Central Gulf, East Gulf Coast Tertiary.
- Blocks: MC/26, MC/27, MC/28, MC/29, MC/72, VK/989, VK/990. Each is listed with "Area: 23 km²".
- Water depth 340–541 m.

**Timetable:**
- Discovery: Pompano I (VK 990) Apr 1985; Pompano II (MC 28) May 1981; Amethyst (MC 26) Feb 2014.
- Production started: Pompano I Oct 1994; Pompano II May 1996; Amethyst Dec 2015.
- Peak gas (108 mmcfd) 2002. Peak oil (48,820 b/d) 1998.

**Operator:** Stone Energy. **Participants:** Stone Energy 100.00%.

**Remaining reserves at 01/01/2018:** 24 mmbbl oil; 0 mmbbl condensate; 57 bcf sales gas.

**Summary:** "Pompano, comprising Pompano I (VK 990), Pompano II (MC 28) and Amethyst (MC 26), is a large shelf-edge oil field that straddles the border of Mississippi Canyon and Viosca Knoll." It was developed in two stages:
- Phase I (Oct 1994): a 40-slot conventional steel platform with processing and export facilities.
- Phase II (May 1996): a 10-well subsea template tied back to the fixed platform. Phase II includes the Cardona and Cardona South developments.

**Key issues:**
- **Talos merger:** in Nov 2017 Stone and Talos announced a merger. Talos will own 63% of the new company.
- **Cardona new-drill programme:**
  - Stone completed a new-drill programme in early 2016, including four Cardona wells.
  - MC 29 #4 and MC 29 #5 were drilled and completed in 2014 and came online in Nov 2014, two months ahead of schedule.
  - "The third and fourth wells, MC 29 #5 and MC 29 #6, came onstream in August 2015 and February 2016."
  - These were Stone's first operated new-drill wells in deepwater GoM. All four performed strongly at first but declined over the last year.
- **Amethyst:** in Feb 2014 Stone announced a discovery at the "Amethyst prospect (MC29)", adjacent to Cardona.
  - The exploration well was completed and brought onstream in Dec 2015. It is gas-heavy and initial production was weaker than expected.
  - The well went offline in May 2016 and remains offline despite intervention. "The lease on the block has been relinquished."
- **Mt. Providence:** WM's reserves include upside from the Mt. Providence well, which is expected onstream in mid-2018.
- **Rig cost:** using the ENSCO 8503 rig, 35% cheaper than the prior rig, cut Cardona D&C costs by an estimated 30–35%.
- **BP sale:** BP announced in Nov 2011 that it had divested Mica, Pompano and surrounding leases to Stone for US$204 million.

**Participation:**
- BP announced the sale on 21 Nov 2011. It closed effective 1 July 2011 for a gross consideration of US$167.6M. Stone acquired the remaining 25% from Anadarko in Aug 2012, effective 1 July 2011, for US$67M.
- Pompano I (VK 990), Pompano II (MC 28) and Amethyst (MC 26) sit within six blocks: VK 989, VK 990, MC 26, MC 27, MC 28 and MC 72.
- BP and Kerr-McGee "pooled" the leases before first production and rationalised equities: BP 75% (operator), KMG 25%.
- **MC 29:** after a successful test, Pompano II was extended to include MC 29. MC 29 participation differed: BP 51% (operator), Hunt 27%, KMG 22%. An equity split negotiated for the MC 29 #TB9 well gave the MC 29 partnership a template slot and facility access.
- **Corporate history:** BP Amoco rebranded as BP in July 2000. Anadarko acquired Kerr-McGee in Aug 2006.
- **Cardona WI:** the Cardona/Cardona South (MC 29) WI is split 65% Stone / 35% Hunt. WM nevertheless allocates all Cardona cash flows to Stone (100%).

Participation table (%, * = operator):

| | MC/27 | MC/28 | MC/29 | MC/72 | VK/989 | VK/990 |
|---|---|---|---|---|---|---|
| Deep Gulf Energy | - | - | - | 30.00* | - | - |
| Hunt Oil | - | - | 34.62 | - | - | - |
| Ridgewood Energy | - | - | - | 15.00 | - | - |
| Riverstone Holdings | - | - | - | 15.00 | - | - |
| Stone Energy | 100.00* | 100.00* | 65.38* | 40.00 | 100.00* | 100.00* |
| Total | 100 | 100 | 100 | 100 | 100 | 100 |

**Block histories:**
- **VK 989 & 990** (G06898 and G06899): Lease Sale 81, Apr 1984, to BP 80% (operator) / KMG 20%. Bonuses $2.6M and $4.4M. Effective 1 June 1984, five-year terms. Held by production since Nov 1994 and Aug 1995. Stone (100%) operates.
- **MC 26** (G31474): Lease Sale 205, Oct 2007, to BP 100% for $1/2 million. Effective 1 Mar 2008, ten-year term. BP assigned 75% to Stone in July 2011. Stone became 100% owner and operator effective Oct 1, 2012.
- **MC 27** (G07923): Lease Sale 98, May 1985, to BP 100% for $2.1M. Effective 1 July 1985, eight-year term. 20% assigned to KMG effective 1 July 1985. Held by production since Oct 1994. Stone (100%) operates.
- **MC 28:**
  - Original lease G04256 went to Arco (Sale 58, July 1979, $25.1M), effective 1/1/1980 with a five-year term. It was relinquished Sept 1984.
  - The current lease G09771 went to BP 75% / KMG 25% (Sale 113, Mar 1988, $13.5M), effective 1 June 1988, eight-year term. Held by production since Oct 1994. Stone (100%) operates.
- **MC 29:**
  - G08795 went to Texaco (Sale 110, Apr 1987, $0.34M). It expired June 1992 with no wells drilled.
  - G13997 went to Sun Operating 66.66% / Chieftain 33.33% (Sale 142, Mar 1993, $0.25M), effective 1 July 1993.
  - In 1994 the block was split into E1/2 and W1/2; BP farmed in for 66.66% of the W1/2. The halves were re-merged in May 2001.
  - Sun farmed out, and KMG farmed in. Chieftain was acquired by Hunt in Aug 2001.
  - Current: Stone 65.38% (operator), Hunt 34.62%.
- **MC 72** (G08483) — the ORRI block:
  - Lease Sale 104, Apr 1986, to Exxon 100% for $0.93M. Effective 1 June 1986, eight-year term, with a well required in the first five years.
  - Dec 1988: Exxon farmed out 50% to Conoco. Mar 1989: it sold the other 50% plus operatorship to BP. Effective Dec 1993, BP was sole lessee.
  - Ownership was split into "shallow rights", all zones above 3,322 m (10,900 ft) TVD, and "deep rights", all zones below that depth. These were assigned BP 75% / KMG 25% effective Feb 2007 and Jan 2001 respectively. BP operated both depth intervals.
  - Held by production since May 1996.
  - **"During March 2007, Newfield farmed-in to part of the block with operating rights and subsequently LLOG obtained operating rights on the same portion of the block in August 2007. As of 21 August 2012, the operating rights on this portion of the block were held as LLOG (60%), Nexen (30%), and Stone Energy (10%). ... As of 25 September 2013, participation consisted of M21K (60%), Nexen (30%) and Stone Energy (10%)."**

**Unitisation:** "No federal unit has been awarded over the Pompano area."

**Production text:**
- Pompano I started Oct 1994 at about 10,000 b/d, reaching a plateau of about 20,000 b/d in 1995 with 10 pre-drilled wells.
- Pompano II started May 1996, taking output to about 45,000 b/d. 1997 output was restricted by pipeline work.
- Early 1998 peak: 50,000 b/d with about 65 mmcfd. In 2002, two Pompano I lower Miocene wells and more Pompano II wells (including one in MC 29) lifted output to over 30,000 b/d and 100 mmcfd.
- Development drilling in 2000 to early 2003, then decline.
- 2005: about 9,400 b/d and 18.6 mmcfd. Katrina damage to downstream facilities shut in production Aug 2005–Jan 2006.
- **Cardona wells (as WM describes them):**
  - MC 29 #4 (Nov 2014): ramped from 1,200 to 4,200 b/d by Jan 2015, then fell below 2,000 b/d by end-2016.
  - MC 29 #5 (Nov 2014): peaked at 4,500 b/d in June 2015, averaging 3,900 b/d in Jan 2017.
  - MC 29 #6: "came onstream in August 2016". Peak 5,500 b/d, about 4,400 b/d plateau, 3,200 b/d in Jan 2017.
  - MC 29 #7: "came onstream in February 2016". Peak 3,900 b/d in Mar 2016, then below "2,00 b/d" by June 2016, and 1,600 b/d in Jan 2017.
- **Amethyst (MC 26 #1):**
  - 90 ft net pay, completed Dec 2015, producing for only one day that month.
  - Jan 2016 averaged 26 mmcfd; Feb peak 28 mmcfd; 12 mmcfd by Apr 2016, then shut in.
  - Intervention in Nov 2016 failed; a tubing leak was found and the well was temporarily abandoned. WM models it as shut-in.
- June/July production was hit by a fire at a third-party downstream gas plant (July about 70% below June). An alternative route was secured in late July.

Production 2007–2016:

| | 2007 | 2008 | 2009 | 2010 | 2011 | 2012 | 2013 | 2014 | 2015 | 2016 |
|---|---|---|---|---|---|---|---|---|---|---|
| Pompano I (kb/d) | 5.7 | 4.5 | 4.6 | 4.3 | 3.3 | 3.4 | 3.3 | 2.3 | 2.0 | 2.5 |
| Pompano II (kb/d) | 4.0 | 3.4 | 2.9 | 2.3 | 1.6 | 1.2 | 1.3 | 2.2 | 10.2 | 13.4 |
| Amethyst (kb/d) | - | - | - | - | - | - | - | - | - | 0.3 |
| Total liquid | 9.7 | 7.9 | 7.5 | 6.6 | 4.9 | 4.6 | 4.6 | 4.5 | 12.2 | 16.2 |
| Pompano I (mmcfd) | 13.5 | 8.9 | 8.5 | 8.1 | 6.6 | 6.5 | 8.0 | 6.7 | 4.0 | 4.4 |
| Pompano II (mmcfd) | 4.7 | 4.4 | 8.1 | 5.3 | 13.2 | 9.8 | 10.2 | 11.3 | 11.4 | 25.9 |
| Amethyst (mmcfd) | - | - | - | - | - | - | - | - | 0.0 | 7.9 |
| Total gas | 18.2 | 13.3 | 16.6 | 13.4 | 19.8 | 16.3 | 18.2 | 18.0 | 15.4 | 38.2 |

Production 2017–2026:

| | 2017 | 2018 | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 | 2026 |
|---|---|---|---|---|---|---|---|---|---|---|
| Pompano I (kb/d) | 2.5 | 2.5 | 1.9 | 1.5 | 1.1 | 0.8 | 0.6 | 0.4 | 0.3 | 0.2 |
| Pompano II (kb/d) | 8.5 | 10.1 | 11.0 | 9.0 | 7.1 | 5.5 | 4.0 | 3.0 | 2.2 | 1.6 |
| Total liquid | 11.0 | 12.6 | 12.9 | 10.5 | 8.2 | 6.3 | 4.6 | 3.4 | 2.5 | 1.9 |
| Pompano I (mmcfd) | 4.5 | 3.2 | 2.4 | 1.8 | 1.4 | 1.0 | 0.7 | 0.5 | 0.4 | 0.3 |
| Pompano II (mmcfd) | 14.6 | 28.4 | 28.2 | 22.9 | 17.6 | 13.4 | 9.9 | 7.3 | 5.4 | 4.0 |
| Total gas | 19.1 | 31.6 | 30.6 | 24.7 | 19.0 | 14.4 | 10.6 | 7.8 | 5.8 | 4.2 |

Amethyst shows "-" for every year 2017–2026.

Cash flow (Liquids 000b/d / Gas mmcfd / Gross Revenue US$M):

| Year | Liq | Gas | Rev | Year | Liq | Gas | Rev |
|---|---|---|---|---|---|---|---|
| 1991 | 0.0 | 0.0 | 0.0 | 2011 | 4.9 | 19.8 | 228.9 |
| 1992 | 0.0 | 0.0 | 0.0 | 2012 | 4.6 | 16.3 | 202.6 |
| 1993 | 0.0 | 0.0 | 0.0 | 2013 | 4.5 | 18.2 | 201.6 |
| 1994 | 2.1 | 1.0 | 13.8 | 2014 | 4.4 | 18.0 | 185.5 |
| 1995 | 19.0 | 15.0 | 138.6 | 2015 | 12.2 | 15.4 | 241.2 |
| 1996 | 36.9 | 41.0 | 340.0 | 2016 | 16.1 | 38.2 | 294.6 |
| 1997 | 44.8 | 55.2 | 385.1 | 2017 | 11.0 | 19.1 | 238.9 |
| 1998 | 48.8 | 66.3 | 299.7 | 2018 | 12.6 | 31.6 | 312.1 |
| 1999 | 41.3 | 64.5 | 337.4 | 2019 | 12.9 | 30.6 | 305.0 |
| 2000 | 35.4 | 64.4 | 490.0 | 2020 | 10.5 | 24.7 | 244.1 |
| 2001 | 28.1 | 59.5 | 359.7 | 2021 | 8.2 | 19.0 | 227.4 |
| 2002 | 31.0 | 108.2 | 446.8 | 2022 | 6.3 | 14.4 | 177.1 |
| 2003 | 22.3 | 59.1 | 390.0 | 2023 | 4.6 | 10.6 | 133.4 |
| 2004 | 13.8 | 30.5 | 276.8 | 2024 | 3.4 | 7.8 | 100.2 |
| 2005 | 9.4 | 18.6 | 260.1 | 2025 | 2.5 | 5.8 | 75.3 |
| 2006 | 10.8 | 20.9 | 319.9 | 2026 | 1.9 | 4.2 | 56.6 |
| 2007 | 9.7 | 18.2 | 321.3 | 2027 | 1.4 | 3.1 | 42.7 |
| 2008 | 7.9 | 13.3 | 339.2 | 2028 | 1.0 | 2.3 | 32.1 |
| 2009 | 7.4 | 16.6 | 199.8 | 2029 | 0.8 | 1.7 | 24.3 |
| 2010 | 6.6 | 13.4 | 220.1 | 2030 | 0.6 | 1.3 | 18.2 |
| | | | | 2031 | 0.0 | 0.0 | 0.0 |

- **Totals:** 182.3 / 353.2 / 8,480.1.
- **PVs:** Total PV 27,331.7; Rem PV 1,270.1. "Discounted at 10.0% from 01/01/2018."
- **Remaining check:** 2018–2030 liquids sum to 66.7 kb/d-yr × 0.365 = 24.3 mmbbl. Gas sums to 157.1 × 0.365 = 57.3 bcf. Both match the reserves.

**WM internal inconsistencies (FACT):**
- Amethyst is described as both MC 26 and "MC29".
- Cardona well numbers and dates conflict: #5 appears twice; #6 is dated both Aug 2015 and Aug 2016; #7 is dated Feb 2016.
- The BP sale is given as $204M in one place and $167.6M in another.
- Small mismatches between the production and cash-flow tables: 2009 7.5 vs 7.4; 2014 4.5 vs 4.4; 2016 16.2 vs 16.1.
- The Location list includes MC 26, but the participation table has no MC 26 column (WM says that lease was relinquished).
- The MC 72 column (Stone 40 / DGE 30* / Ridgewood 15 / Riverstone 15) is **record title**. WM's economics are "Stone 100%".

**Status:**
- **FACT:** the field is producing through Stone's VK 989 platform plus the Pompano II subsea template (MC 28) and the Cardona MC 29 wells. Amethyst is shut in and temporarily abandoned.
- **FACT:** the host is the Pompano platform, which Stone owns (an owned host, not a third-party tieback).

### 2.2 Chain of title (3. MC 72 Assignment - BP to LLOG Nexen.pdf, BOEM file 112310, 10 pp.)
- **p1:** BOEM SR page dated 05-Nov-2008 (entry 31-Oct-2008). Operating rights effective 02/29/2008 in the S/2 and S/2S/2S/2N/2 [*sic*, an extra "S/2"], from the surface to 13,405' TVD:
  - KMG 15%
  - LLOG 60%
  - Nexen 25%

  The same page then designates LLOG operator for "S/2;S/2S/2N/2".
- **p2–3:** LLOG transmittal letters dated Oct 20, 2008 and Sept 9, 2008 (received 9/10/2008 and 10/21/2008). The Sept 9 letter says BP "has assigned a 50.0% operating rights interest ... to LLOG". This is incomplete: the form shows 75% split 50% LLOG and 25% Nexen.
- **p4–5:** MMS-151 Assignment of Operating Rights:
  - Area: "S/2 and S/2 S/2 N/2 of Block 72, Mississippi Canyon, from surface down to a true vertical depth of 13,405'."
  - Assignor BP E&P (02481) conveys 75%. LLOG (02058) receives 50% and Nexen (02079) receives 25%.
  - Approval is restricted to operating rights; record title is not affected. Approved by MMS on OCT 31 2008.
  - Effective Feb 29, 2008. Executed by BP on Aug 14, 2008, LLOG on Aug 29, 2008 and Nexen on Aug 25, 2008.
- **p6–7, Exhibit A:**
  - BP assigns LLOG 50% and Nexen 25% operating rights, "a combined operating rights interest of seventy-five percent (75%) **from the surface down to the stratigraphic equivalent of 13,405' (TVD)** (said stratigraphic equivalent depth being 100' below the total depth drilled and seen on the LWD Gamma Ray Resistivity TVD Log run in the **OCS-G 08483 #2 Well**) in and to the **S/2 and the S/2 S/2 N/2**".
  - The reservation reads: "Assignor does herein except and reserve unto itself and its assigns an **overriding royalty interest equal to seven and one-half percent (7.5%) gross / five and six hundred twenty-five one-thousandth percent (5.625%) net** of all oil, gas and other hydrocarbons, except helium gas, **produced and saved by Assignees, its successors or assigns from the assigned portion of Said Lease**."
  - The ORRI is free of all costs except its proportionate share of severance and production taxes, and is paid in the same way as lessor royalty.
  - It is subject to the Farmout Agreement of May 1, 2007 between BP and KMG (farmors) and LLOG (farmee). **The Farmout Agreement controls where it conflicts with the assignment.** It is not in the package.
  - BP warrants the interest is free of burdens other than lessor royalty. The assignment is otherwise without warranty, except by, through and under BP.
- **p8–10:** signatures and acknowledgments (BP Aug 14, 2008; LLOG Aug 29, 2008; Nexen Aug 25, 2008).

**Calculation:**
- 7.5% × 75% (the share assigned out of BP's interest) = **5.625% of 8/8 = 0.05625**. This **supports Attachment A (FACT)**.
- Lands: S/2 + S/2 S/2 N/2. That is 2,880 + 720 = **3,600 of 5,760 acres (62.5%)**.
- Depths: **surface to 13,405 ft TVD stratigraphic equivalent only.**
- Burdens only production "by Assignees, successors or assigns". KMG's 25% share of the same interval (now held by Stone 10%, Nexen 5% and LLOG/M21K 10%, all derived from KMG/Anadarko) is **not** burdened. The 5.625% of 8/8 figure already reflects this.

**Gaps:**
- (a) The Farmout Agreement, which controls, is missing. It could contain payout or BIAPO conversion or term language. Check for any ORRI conversion or term limit.
- (b) BP later sold its MC 72 record title to Stone (SR: Stone 100% RT effective 7/1/2011). We have **no evidence that BP excluded this ORRI from the 2011 Stone sale.** Get the BP–Stone PSA excluded-assets schedule and a payment history.

### 2.3 Lease status (SR MC 72, printed 04-Jun-2018)
- **Lease terms:**
  - PROD. Sale 104 (4/30/1986). Lease date 6/1/1986. Royalty 12.5%. 5,760 acres; bonus $928,000; rental $3.00/acre.
  - Original lessee Exxon. 5-year drilling requirement met.
- **Production history:**
  - Suspensions of production 6/1/94–3/31/96, then held by drilling.
  - **Began producing 5/2/96** (Pompano II start-up).
  - Production ceased 08/27/2005 and resumed 01/01/2006.
  - Ceased 07/29/2010, resumed 10/26/2010. Ceased 05/17/2011, resumed 09/17/2011.
- **Operating rights history:**
  - The 10,900 ft shallow/deep split dates to 1990–2001.
  - The rights were merged back into record title effective 4/16/2008 (BP 75% / KMG 25%).
  - The LLOG area was then carved out effective 2/21–2/29/2008.
- **RT (effective 7/1/2011):** Stone Energy Offshore 100%.
- **RT (effective 5/1/2017):** Stone Energy Offshore 40%, Deep Gulf Energy III 30%, Ridgewood Rampart 15%, ILX Prospect Rampart 15%.
- **OR, S/2; S/2S/2N/2, surface–13,405' TVD (the ORRI area):**
  - LLOG 60% / Nexen 30% / Stone Offshore 10% (effective 7/1/2011).
  - **M21K LLC 60% / Nexen 30% / Stone Offshore 10% (effective 4/1/2013).**
  - **Operator Energy XXI GOM, LLC** (re-designated Dec 2017).
- **OR, N1/2NE1/4; N1/2S1/2NE1/4, surface–13,405' TVDSS:** Stone Offshore 100% (effective 5/1/2017), operated by Stone.
- **Deep Gulf Energy III operates:** N1/2NW/4; N1/2S1/2NW/4 at all depths, and S1/2S1/2NW/4, NE/4 and S1/2 **below 13,405'** to 99,999' TVDSS. INF: this is the "Rampart" deep play, and it is outside the ORRI depth window.
- No federal unit. No relinquishment.
- **Lease risk:** the lease is held by production (Stone's Pompano production keeps it alive). Lease expiry is low risk while Pompano produces; WM shows production to 2030.

### 2.4 Inconsistencies and tricks
1. **The production WM models is not ORRI production (INF, high confidence):**
   - WM's Pompano is Stone's field: VK 989/990, MC 27, MC 28 and the MC 29 Cardona wells, all "Stone 100%".
   - The ORRI burdens only M21K/Nexen (Energy XXI-operated) production from the S/2 and S/2 S/2 N/2 above 13,405 ft.
   - WM's participation table for MC 72 omits M21K and Nexen entirely. The pre-farmout N/2 N/2 + N/2 S/2 N/2 strip (nearest MC 28 and the Pompano II template) was carved out of the farmout and is now Stone/DGE.
   - Applying 0.05625 to WM's Pompano production gives 709 b/d and about $71.5M PV. **That would be a large overstatement.**
2. **Production in the ORRI area is unknown.** Nothing in the package gives lease-, well- or interval-level volumes for the OCS-G 08483 #2 well or other M21K/Nexen wells.
   - The SR records production interruptions in 2010–2011, so some well was producing at that time. INF: plausibly the LLOG #2 well.
   - We cannot tell whether that interval is still producing in 2018. **Do diligence:** get BOEM OGOR-A / well production data for G08483 by completion (public before Aug 2018) and BP's ORRI revenue statements for 2017 to H1-2018.
3. **Depth limit:** the ORRI stops at 13,405 ft TVD (stratigraphic equivalent tied to a 2008 well log). Deep upside below 13,405 ft (the DGE "Rampart" interval) is **excluded**.
4. **Aliquot typo:** "S/2S/2S/2N/2" appears in the 2008 SR entry and on assignment p.1. The instrument itself says "S/2 S/2 N/2". If the narrower reading were applied, the area would be 3,240 acres rather than 3,600. Minor, but worth a curative note.
5. **Cover letter vs form:** the cover letter says 50% was assigned; the form says 75%. The form governs.
6. **Successor and operator credit risk (INF):** Energy XXI GOM is the operator and M21K is affiliated with Energy XXI. Energy XXI emerged from Chapter 11 at the end of 2016. Verify payment status.
7. **Pooling:** WM says BP and KMG "pooled" the Pompano leases. That was a lessee-level equity rationalisation. INF: it does not pool this 2008 ORRI into Pompano field production. The ORRI is tied to the assigned portion only.

### 2.5 Net ORRI production series
- **Base case:** no documented production can be attributed to the ORRI area. **Net = unknown; carry 0 in the base case** until OGOR data is obtained.
- **Illustration only. NOT recommended; this is the trap.** WM's Pompano gross × 0.05625:
  - 2018: 12.6 kb/d → 708.8 b/d, 31.6 mmcfd → 1,777.5 mcfd, $312.1M → $17.56M.
  - 2019: 725.6 b/d, $17.16M.
  - 2020: 590.6 b/d, $13.73M.
  - 2021: 461.2 b/d, $12.79M.
  - 2022: 354.4 b/d, $9.96M.
  - 2023: 258.8 b/d, $7.50M.
  - 2024: 191.2 b/d, $5.64M.
  - 2025: 140.6 b/d, $4.24M.
  - 2026: 106.9 b/d, $3.18M.
  - 2027: 78.8 b/d, $2.40M.
  - 2028: 56.2 b/d, $1.81M.
  - 2029: 45.0 b/d, $1.37M.
  - 2030: 33.8 b/d, $1.02M.
  - 2031–33: 0.
  - Totals: 1,369 kbbl and 3,226 mmcf, $98.4M undiscounted, **PV10 $71.5M**.
- **Sensible alternative if OGOR data show a producing well:** forecast that well's volumes × 0.05625. Any value is "optionality".

---

## 3. SOUTH SANTA CRUZ (MC 563), OCS-G 21176, Attachment A Net ORRI 0.0093

### 3.1 WM summary: full transcription (South Santa Cruz (MC 563).pdf; images ssc_00–10)
- **Title:** South Santa Cruz (MC 563)
- **Location:** Central Gulf, East Gulf Coast Tertiary. Block MC/563, Area 23 km². **Water depth 1,999 m.**
- **Timetable:** Discovery May 2015. FID May 2015. Peak gas (11 mmcfd) 2018. Peak oil (13,670 b/d) 2018. *No "Production started" line.*
- **Operator:** Deep Gulf Energy.
- **Participants:** Deep Gulf Energy 40.50, Ridgewood Energy 40.50, Houston Energy¹ 10.00, Red Willow Production 9.00. (Footnote 1 has no text.)
- **Remaining reserves at 01/01/2018:** 30.6 mmbbl oil; 24.8 bcf sales gas.
- **Summary:** "South Santa Cruz (MC 563) is an oil and gas field located in the Mississippi Canyon protraction area of the Central Gulf of Mexico. South Santa Cruz is developed as a **subsea tie-back to the nearby Blind Faith FPS**. First oil was achieved in June 2017."
- **Key issues:**
  - Sanctioned on discovery in May 2015, during depressed prices. It benefits from integrated exploration, appraisal and development, standardised equipment and existing infrastructure.
  - DGE will save cost by completing the exploration well as a producer.
  - In Sept 2016 DGE picked up the Ensco 8505 semisubmersible at $100,000/day, 25% below WM's base cost assumptions.
  - "We expect Deep Gulf Energy to spud a second well at South Santa Cruz in early 2018. **Potential upside could be realised by drilling a third location but we do not include this in our current model.**"
- **Participation:**
  - The original lease G09826 went to Conoco (Sale 113, Mar 1988, $0.2M) and expired May 1998 with no wells drilled.
  - The current lease G21176 went to TotalFinaElf 100% (Sale 172, Mar 1999, $0.2M), effective 1 July 1999, with a ten-year term.
  - Burlington Resources acquired 100% and operatorship effective 6 May 2002.
  - "Effective 1 August 2005, the **northwest fourth** of block MC 563 was **segregated** from the rest of the block." The quadrant interest went to Houston Energy (10%), Helis (45%) and Red Willow (45%).
  - Effective 1 May 2007: Noble 23.25%, Red Willow 20.25%, Houston Energy 10%, **BP 46.5%**, with Noble taking over operatorship from Helis.
  - "**Unit Contract No. 754309001** was approved on 1 January 2009 and consisted of leases G21176 and G27278."
  - Effective 1 Feb 2015: the NW fourth is held by Red Willow 9%, Houston 10%, DGE 40.5% and Ridgewood 40.5%. DGE became operator.
- **Production:**
  - First oil June 2017 from one well. A second well comes online in early 2018.
  - Peak in 2018 at an annual average of 13,700 b/d and 11.1 mmcfd.
  - Standard downtime caveat.
- No royalty-override or unitisation section beyond the text above.

Production 2017–2025 / 2026–2033 (Oil kb/d; Sales Gas mmcfd):

| | 2017 | 2018 | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 |
|---|---|---|---|---|---|---|---|---|---|
| Oil | 5.6 | 13.7 | 12.9 | 10.1 | 7.8 | 6.1 | 4.8 | 5.5 | 5.4 |
| Gas | 4.6 | 11.1 | 10.5 | 8.1 | 6.3 | 4.9 | 3.8 | 4.5 | 4.4 |

| | 2026 | 2027 | 2028 | 2029 | 2030 | 2031 | 2032 | 2033 |
|---|---|---|---|---|---|---|---|---|
| Oil | 4.2 | 3.3 | 2.6 | 2.0 | 1.6 | 1.2 | 0.9 | 0.7 |
| Gas | 3.4 | 2.7 | 2.1 | 1.6 | 1.3 | 1.0 | 0.8 | 0.6 |

Cash flow (Liquids / Gas / Gross Revenue US$M):

| Year | Liq | Gas | Rev | Year | Liq | Gas | Rev |
|---|---|---|---|---|---|---|---|
| 2016 | 0.0 | 0.0 | 0.0 | 2028 | 2.6 | 2.1 | 72.5 |
| 2017 | 5.6 | 4.6 | 111.2 | 2029 | 2.0 | 1.6 | 57.4 |
| 2018 | 13.7 | 11.1 | 297.4 | 2030 | 1.6 | 1.3 | 45.8 |
| 2019 | 12.9 | 10.5 | 269.6 | 2031 | 1.2 | 1.0 | 36.2 |
| 2020 | 10.1 | 8.1 | 206.8 | 2032 | 0.9 | 0.8 | 28.9 |
| 2021 | 7.8 | 6.3 | 193.5 | 2033 | 0.7 | 0.6 | 22.9 |
| 2022 | 6.1 | 4.9 | 153.7 | 2034 | 0.5 | 0.4 | 15.4 |
| 2023 | 4.8 | 3.8 | 122.3 | 2035 | 0.3 | 0.3 | 10.5 |
| 2024 | 5.5 | 4.5 | 145.4 | 2036 | 0.3 | 0.2 | 8.3 |
| 2025 | 5.4 | 4.4 | 144.3 | 2037 | 0.2 | 0.2 | 6.5 |
| 2026 | 4.2 | 3.4 | 114.7 | 2038 | 0.0 | 0.0 | 0.0 |
| 2027 | 3.3 | 2.7 | 91.1 | | | | |

- **Totals:** 32.7 / 26.5 / 2,154.2.
- **PVs:** Total PV 1,434.4; Rem PV 1,317.8. "Discounted at 10.0% from 01/01/2018."
- **Reserves check:** the 2018–2037 sums are 84.1 kb/d-yr × 0.365 = 30.7 mmbbl and 68.2 × 0.365 = 24.9 bcf. Both match.

**WM vs SR differences (FACT):**

| Item | WM says | SR says |
|---|---|---|
| Area carved out in 2005 | "Northwest fourth" | **N1/2 NW1/4** (1/8 of the block) |
| Nature of the carve-out | "Segregated" | An **operating-rights severance**, surface to 19,000' TVD (no new lease) |
| Burlington acquisition date | "6 May 2002" | RT effective 2/1/2002 |
| Ridgewood holding | Ridgewood 40.5% | Ridgewood SSC 20.25% + ILX Prospect SSC 20.25% |

- WM's peak oil is 13,670 b/d in the header and 13,700 b/d in the text.
- WM shows an unexplained 2024 uptick (4.8 → 5.5 kb/d). INF: a modeled workover or sidetrack.

**Status (FACT):**
- **Producing.** First oil June 2017; SR shows "Placed on continuous production on 06/11/2017".
- The field sits **on the ORRI block (MC 563)**. Development is a **subsea tieback to Blind Faith FPS**. INF: Blind Faith is Chevron-operated, on a different block.
- **Host risk (INF):** third-party processing, tariff, capacity and host-life risk. Host downtime shuts in SSC.

### 3.2 Chain of title (3. MC 563 ASSIGNMENT.pdf, 3 pp., scan with no text layer, read visually)
- **Instrument:** "ASSIGNMENT OF OVERRIDING ROYALTY INTEREST".
  - Assignor: **Houston Energy Deepwater Ventures I, LLC** ("HE"). Assignee: **BP Exploration & Production Inc.** Consideration: $10.
  - Grants "an overriding royalty interest of **two percent of forty-six and one half percent of eight-eighths (2% of 46.5% of 8/8ths)**".
  - Covers Federal Lease OCS-G 21176 (about 5,760 acres, Block 563, MC, NH 16-10), "**limited to depths from the surface to 19,000' TVDSS**".
- **Subject to:**
  - (a) the Lease terms;
  - (b) the "MC 563 (OCS-G 21176) Assignment Agreement dated October 10, 2014, between Assignee, BP, and HE". That agreement is not in the package.
- **Payment terms:**
  - Free of operating and drilling costs, computed like lessor royalty, and bears its proportionate taxes.
  - **Royalty relief or suspension (DWRRA 1995 or any successor) "shall not in any way affect, bar, delay or diminish payment" of the ORRI.** This is favourable.
- **Assignor's rights:** HE has no obligation to drill or maintain the lease, and may surrender or abandon it without liability.
- **Execution:**
  - p2: no warranty of title, express or implied. Effective **October 10, 2014**. Signed by P. David Amend (VP Land, HE) and David G. Peterson (Attorney-in-Fact, BP).
  - p3: HE acknowledged **17 Oct 2014** (notary Sue A. Alford, commission expired 5/24/2018). BP acknowledged **16 Oct 2014** (notary Karen Gail Crow).

**Calculation:**
- 2% × 46.5% = **0.93% of 8/8 = 0.0093 exactly**. This **supports Attachment A**; it is not a rounded figure.
- Origin (FACT, from the SR): BP held 46.5% RT and OR from 5/1/2007. Effective 10/10/2014, HEDV I's interest rose to 56.5% and then 79.75%, absorbing BP's 46.5%. BP took back the override as part of the sale.
- It is an **assigned (granted) ORRI**, not a reserved one. It covers **the whole block**, not just the N/2 NW/4, from the surface to 19,000 ft TVDSS.

**Red flags (FACT unless marked):**
- (a) **No BOEM filing stamp or "BOEM File Name" footer.** The Orion and Pompano instruments both carry these. The PDF was created 2018-06-21, after the SRs were printed. INF: it looks like an internal BP copy that may never have been filed as a Non-Required Filing. HE assigned most of its interest to DGE III, Ridgewood SSC, ILX SSC and Red Willow effective 2/1/2015. If those buyers lacked notice, enforceability against them is a question. **Get a payment history and division order from DGE since first oil in 06/2017.** That is the decisive proof.
- (b) **Depth cap mismatch.** The ORRI uses 19,000 ft **TVDSS**, while the OR severance uses 19,000 ft **TVD**. The reservoir depth is not stated anywhere in the package. Water depth is 1,999 m (6,558 ft), leaving about 12,400 ft below mudline. INF: Miocene targets in this area can approach or exceed 19,000 ft TVDSS. **If the producing sands are below 19,000 ft TVDSS, the ORRI receives nothing.** Get completion depths from BSEE well records (public).
- (c) The controlling Oct 10, 2014 Assignment Agreement is missing.

### 3.3 Lease status (SR MC 563, 5 pp., printed 04-Jun-2018)
- **Lease terms:**
  - PROD. Sale 172 (3/17/1999). Lease date 7/1/1999. 10-year primary term (would have expired 6/30/2009).
  - Royalty 12.5%. 5,760 acres (none relinquished). Bonus $247,000; rental $7.50/acre.
  - Original lessee TotalFinaElf E&P USA (renamed from Elf Exploration effective 1/1/2001).
- **Survival chain (FACT), checked in sequence:**
  1. Unit 754309001 (G21176 + G27278) effective 1/1/2009, before the primary term expired.
  2. Unit suspensions 10/08/2009–03/31/2010, 04/01–11/30/2010, 03/15–04/30/2011 and 01/18–07/31/2012.
  3. "Held by unit production, lease not receiving an allocation" through 2012–2015. G21176 was carried by production on the other unit lease, G27278.
  4. Drilling began 03/27/2015.
  5. **The unit terminated 6/5/2015.**
  6. Drilling operations ended 05/29/2015.
  7. SOP 11/26/2015–1/31/2017. The SOP starts exactly the day after the 180th day (5/30–11/25 = 180 days), so there is **no gap**, but the margin is zero.
  8. SOP 2/1–3/31/2017, then drilling operations ended 3/31/2017.
  9. **Continuous production from 06/11/2017**, 72 days later, which is within 180 days.

  **Conclusion: the lease has been continuously maintained and is alive.**
- **Current RT (effective 9/1/2016):**
  - Red Willow Offshore 9%
  - Houston Energy Deepwater Ventures XVI 10%
  - Deep Gulf Energy III 40.5% (operator)
  - Ridgewood South Santa Cruz 20.25%
  - ILX Prospect South Santa Cruz 20.25%
- **OR, N1/2NW1/4, surface–19,000' TVD:** held in the same proportions.
- **BP history:** 46.5% from 5/1/2007 until its exit effective 10/10/2014. BP designated DGE III as operator in Jan 2015, which is odd after its exit. INF: this was a filing lag.

### 3.4 Inconsistencies, tricks and upside
- WM never mentions the override, BP's exit or the depth cap.
- **Overlooked upside:** a third development location ("not in our current model") would add cost-free ORRI volumes. Also, the ORRI covers **all** of MC 563 above 19,000 ft TVDSS, not just the producing quarter-quarter.
- **Royalty relief carve-out:** favourable.
- **Host dependency:** Blind Faith (third-party).
- **Operator:** DGE III is a private-equity-backed small operator.

### 3.5 Net ORRI production (gross × 0.0093)
- **Assumption:** 100% of WM's South Santa Cruz production is from G21176 above 19,000 ft TVDSS. WM places the field entirely in MC 563; the depth is unverified.

| Year | Gross oil kb/d | Net oil b/d | Gross gas mmcfd | Net gas mcfd | Gross rev $M | Net rev $k |
|---|---|---|---|---|---|---|
| 2018 | 13.7 | 127.4 | 11.1 | 103.2 | 297.4 | 2,766 |
| 2019 | 12.9 | 120.0 | 10.5 | 97.6 | 269.6 | 2,507 |
| 2020 | 10.1 | 93.9 | 8.1 | 75.3 | 206.8 | 1,923 |
| 2021 | 7.8 | 72.5 | 6.3 | 58.6 | 193.5 | 1,800 |
| 2022 | 6.1 | 56.7 | 4.9 | 45.6 | 153.7 | 1,429 |
| 2023 | 4.8 | 44.6 | 3.8 | 35.3 | 122.3 | 1,137 |
| 2024 | 5.5 | 51.1 | 4.5 | 41.8 | 145.4 | 1,352 |
| 2025 | 5.4 | 50.2 | 4.4 | 40.9 | 144.3 | 1,342 |
| 2026 | 4.2 | 39.1 | 3.4 | 31.6 | 114.7 | 1,067 |
| 2027 | 3.3 | 30.7 | 2.7 | 25.1 | 91.1 | 847 |
| 2028 | 2.6 | 24.2 | 2.1 | 19.5 | 72.5 | 674 |
| 2029 | 2.0 | 18.6 | 1.6 | 14.9 | 57.4 | 534 |
| 2030 | 1.6 | 14.9 | 1.3 | 12.1 | 45.8 | 426 |
| 2031 | 1.2 | 11.2 | 1.0 | 9.3 | 36.2 | 337 |
| 2032 | 0.9 | 8.4 | 0.8 | 7.4 | 28.9 | 269 |
| 2033 | 0.7 | 6.5 | 0.6 | 5.6 | 22.9 | 213 |

- **2018–2033 totals:** 281 kbbl oil, 228 mmcf gas, $18.6M undiscounted.
- With the 2034–37 tail (0.5 / 0.3 / 0.3 / 0.2 kb/d), PV10 = 1,317.8 × 0.0093 = **$12.26M** at WM's price deck, before risking for depth, recordation or host.
- Revenue Jan 1 to closing belongs to the buyer through the effective-date adjustment.
- **Arithmetic example:** 2018 net oil = 13.7 × 1,000 × 0.0093 = 127.4 b/d.

---

## 4. Bottom line for the bid model (INF)

| Property | Attachment A share | Documents support it? | Burdened production | Base PV10 (WM deck, unrisked) | Key risk |
|---|---|---|---|---|---|
| Orion MC 110 | 0.013125 | Yes (Devon→BP ABOS, Exh. A) | Whole field, ends 2018/19 | ≈ $0.03M | Lease expiry about 2019; chain gap before Devon |
| Pompano MC 72 | 0.05625 | Yes (7.5% × 75%) | Only M21K/Nexen S/2 shallow (≤13,405') wells. **Not WM's Pompano.** | Unknown → $0 base (NOT $71.5M) | No production data; 2011 BP→Stone sale; missing farmout |
| S. Santa Cruz MC 563 | 0.0093 | Yes (2% × 46.5%) | Field on block, ≤19,000' TVDSS | ≈ $12.3M | Unfiled instrument; depth cap; Blind Faith host |

Requests for the seller and data room:
1. BP ORRI revenue statements and division orders for all three, covering 2017 to H1-2018.
2. BOEM OGOR / BSEE completion data: G08483 by well and interval; G21176 completion TVDSS.
3. The May 1, 2007 BP/KMG–LLOG Farmout Agreement.
4. The Oct 10, 2014 MC 563 Assignment Agreement.
5. The instrument that created the Orion ORRI.
6. The excluded-assets schedule from BP's 2011 sale to Stone.
7. Proof that the MC 563 ORRI was filed with BOEM.
