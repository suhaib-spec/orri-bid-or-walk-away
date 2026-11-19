# ORRI Package: Bid or Walk Away

Our analysis for the **UNT Hackathon 2026, "Bid or Walk Away"** case: should we bid on BP's 2018 package of
Gulf of Mexico overriding royalty interests (Kodiak, Lucius, Stones, South Santa Cruz, Grand Isle 116,
Main Pass 59, Ship Shoal 219, Orion, Pompano), and if so, how much?

**Our answer: bid $105M all-cash as lead of a buying group, and walk away above $115M.**
The full reasoning is in [`_analysis/FINAL_decision_v2.md`](_analysis/FINAL_decision_v2.md).

## What's here

| Path | Contents |
|---|---|
| `_analysis/deliverables/ORRI_Bid_or_Walk_Away.pptx` | Full presentation deck (slide previews in `png/`) |
| `_analysis/deliverables/ORRI_Bid_or_Walk_Away_SIMPLE.pptx` | Simpler version of the deck (slide previews in `png_simple/`) |
| `_analysis/deliverables/Presentation_Script_10min.*` | 10-minute presentation script (`.docx`, `.pdf`), plus a formal version (`.docx`) |
| `_analysis/deliverables/Presenter_Guide*.md` | Presenter guides for both decks |
| `_analysis/deliverables/Judge_QA.*` | Prepared answers for judges' questions |
| `_analysis/deliverables/ORRI_Bid_Model.xlsx` | Valuation and bid model workbook |
| `_analysis/FINAL_decision_v2.md` | Final decision after the expert-panel review |
| `_analysis/decision_memo.md`, `criteria.md` | Earlier decision memo and evaluation criteria |
| `_analysis/*.md` | Per-asset notes (Kodiak, Lucius, Stones, MC trio, shelf trio), market and BOEM production data, upside structures |
| `_analysis/boem/monthly_by_lease.csv` | Public BOEM monthly production by lease |
| `_analysis/panel/` | Expert-panel reviews (reserves engineer, model auditor, title attorney, capital markets, auction strategist, judges, round 2) and their check scripts |
| `_analysis/model/` | Python valuation engine and the scripts that build the deck, simple deck and Excel model; `common.py` holds the shared path, loading and IRR helpers |
| `_analysis/tests/` | Regression tests: each script's output against `tests/expected/`. After an intended change, run `make expected` and review the diff |

## Rebuilding the deliverables

Requires Python 3 and `make`.

```bash
make install   # pip install -r requirements.txt
make           # Excel model, full deck and simple deck
make irr       # IRR grid from the final decision
make test      # check every script still reproduces the published figures
```

Every script finds `_analysis` on its own, so it runs from any directory. Passing the folder
explicitly still works:

```bash
python _analysis/model/build_xlsx.py _analysis
python _analysis/model/build_deck.py _analysis/deliverables
python _analysis/model/build_deck_simple.py _analysis/deliverables
python _analysis/panel/scripts/final_irr.py _analysis
```

## Not included

The case data room (lease documents, serial register pages, ORRI assignments, unit agreements,
reserves reports, location map, purchase price allocation, bid instructions and case brief) was provided
by the case sponsor and is not redistributed here. Citations in the analysis refer to those files by
their data-room paths (for example `Kodiak/SourceDocs/5. ABOS KODIAK.pdf`).

## Contributors

- Suhaibuddin Ahmed ([@suhaib-spec](https://github.com/suhaib-spec))
- Usama Bin Faheem ([@UB0013](https://github.com/UB0013))
