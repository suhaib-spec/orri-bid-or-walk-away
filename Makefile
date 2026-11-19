# Rebuild the deliverables from the model scripts.
PY ?= python3
A  := _analysis

.PHONY: all xlsx deck deck-simple irr install test expected

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

# Regression tests: script outputs vs _analysis/tests/expected
test:
	$(PY) -m unittest discover -s $(A)/tests -v

# Re-capture expected outputs after an intended change (review the diff before committing)
expected:
	@for s in model/engine model/engine2 model/returns model/levered \
	          panel/scripts/reserves_panel panel/scripts/reserves_rebuttal panel/scripts/audit_model \
	          panel/scripts/audit_extra panel/scripts/alloc panel/scripts/rival_cp panel/scripts/final_cp \
	          panel/scripts/final_irr; do \
	  $(PY) -I $(A)/$$s.py $(A) > $(A)/tests/expected/$$(basename $$s).out || exit 1; \
	done
