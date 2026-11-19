"""Shared helpers for the model and panel scripts.

- analysis_dir(): the _analysis folder. Taken from the first CLI argument when one is
  given (every script has always accepted it), otherwise worked out from this file's
  location, so `python _analysis/model/engine2.py` runs from anywhere.
- load_script(): execute a sibling script as a module. The scripts read sys.argv[1] at
  import time, so argv is pinned to the analysis folder before the load.
- irr(): internal rate of return by bisection. Each caller keeps the bracket and
  iteration count it was written with, so published figures reproduce exactly.
"""
import importlib.util
import os
import sys

MODEL_DIR = os.path.dirname(os.path.abspath(__file__))
ANALYSIS_DIR = os.path.dirname(MODEL_DIR)


def analysis_dir(argv=None):
    argv = sys.argv if argv is None else argv
    return argv[1] if len(argv) > 1 else ANALYSIS_DIR


def load_script(name, relpath, analysis=None):
    """Load `<analysis>/<relpath>` as module `name`."""
    analysis = analysis or analysis_dir()
    sys.argv = [sys.argv[0], analysis]
    spec = importlib.util.spec_from_file_location(name, os.path.join(analysis, relpath))
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def npv(rate, cfs):
    """Net present value of [(t_years, cashflow), ...] at `rate`."""
    return sum(c / (1 + rate) ** t for t, c in cfs)


def irr(cfs, lo=-0.9, hi=5.0, iters=200):
    """Rate in [lo, hi] at which npv(rate, cfs) changes sign (cash out first, then in)."""
    for _ in range(iters):
        mid = (lo + hi) / 2
        lo, hi = (mid, hi) if npv(mid, cfs) > 0 else (lo, mid)
    return mid
