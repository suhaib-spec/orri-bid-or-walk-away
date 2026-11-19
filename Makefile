# Rebuild the deliverables from the model scripts.
PY ?= python3
A  := _analysis

.PHONY: all xlsx deck deck-simple irr install

all: xlsx deck deck-simple

install:
	$(PY) -m pip install -r requirements.txt

xlsx:
	$(PY) $(A)/model/build_xlsx.py $(A)

deck:
	$(PY) $(A)/model/build_deck.py $(A)/deliverables

deck-simple:
	$(PY) $(A)/model/build_deck_simple.py $(A)/deliverables

irr:
	$(PY) $(A)/panel/scripts/final_irr.py $(A)
