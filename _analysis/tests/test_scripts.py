"""Regression tests for the valuation scripts.

Each script is run as a subprocess and its stdout compared line for line with
tests/expected/<name>.out. The expected files were captured from the scripts that
produced the figures in FINAL_decision_v2.md and the panel reviews, so any change to
a number shows up here. When a change is intended, regenerate with
`make expected` and review the diff before committing.

Run: python -m unittest discover -s _analysis/tests -v
"""
import os
import subprocess
import sys
import unittest

TESTS = os.path.dirname(os.path.abspath(__file__))
ANALYSIS = os.path.dirname(TESTS)
sys.path.insert(0, os.path.join(ANALYSIS, 'model'))
from common import irr, npv  # noqa: E402

SCRIPTS = {
    'engine': 'model/engine.py',
    'engine2': 'model/engine2.py',
    'returns': 'model/returns.py',
    'levered': 'model/levered.py',
    'reserves_panel': 'panel/scripts/reserves_panel.py',
    'reserves_rebuttal': 'panel/scripts/reserves_rebuttal.py',
    'audit_model': 'panel/scripts/audit_model.py',
    'audit_extra': 'panel/scripts/audit_extra.py',
    'alloc': 'panel/scripts/alloc.py',
    'rival_cp': 'panel/scripts/rival_cp.py',
    'final_cp': 'panel/scripts/final_cp.py',
    'final_irr': 'panel/scripts/final_irr.py',
}


def run(relpath):
    out = subprocess.run([sys.executable, '-I', os.path.join(ANALYSIS, relpath), ANALYSIS],
                         capture_output=True, text=True, check=True)
    return out.stdout


class ScriptOutputTest(unittest.TestCase):
    maxDiff = None

    def test_outputs_match_expected(self):
        for name, relpath in SCRIPTS.items():
            with self.subTest(script=name):
                with open(os.path.join(TESTS, 'expected', name + '.out')) as f:
                    expected = f.read()
                self.assertEqual(run(relpath).splitlines(), expected.splitlines())


class HeadlineFiguresTest(unittest.TestCase):
    """The numbers the deck and the decision memo quote."""

    def test_pdp_strip_pv(self):
        lines = run(SCRIPTS['engine2']).splitlines()
        # rows are a 34-char case label followed by per-property PVs and TOTAL
        totals = {l[:34].strip(): float(l.split()[-1]) for l in lines if l.startswith('PDP ')}
        self.assertEqual(totals['PDP strip 10%'], 138.4)
        self.assertEqual(totals['PDP strip 12%'], 133.1)

    def test_levered_debt_repayment_year(self):
        # model_auditor.md: repaid around mid-2021 on strip, mid-2023 on the low deck
        rows = run(SCRIPTS['levered']).splitlines()
        self.assertTrue(rows[0].endswith('debt repaid by 2021'))
        self.assertTrue(rows[2].endswith('debt repaid by 2023'))


class FinanceHelpersTest(unittest.TestCase):

    def test_npv_discounts_by_time(self):
        self.assertAlmostEqual(npv(0.10, [(0, -100), (1, 110)]), 0.0, places=9)

    def test_irr_single_period(self):
        self.assertAlmostEqual(irr([(0, -100), (1, 110)]), 0.10, places=9)

    def test_irr_multi_period(self):
        cfs = [(0, -100)] + [(t, 30) for t in range(1, 5)]
        r = irr(cfs)
        self.assertAlmostEqual(npv(r, cfs), 0.0, places=6)
        self.assertAlmostEqual(r, 0.0771, places=4)

    def test_irr_respects_bracket(self):
        # a loss-making deal sits below zero; the bracket must allow it
        self.assertLess(irr([(0, -100), (1, 90)], lo=-0.5, hi=2.0), 0)


if __name__ == '__main__':
    unittest.main()
