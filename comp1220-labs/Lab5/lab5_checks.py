"""Tiny self-check helper used by every Lab 5 starter file.

You do not need to change this file. Run a problem file directly, e.g.

    python p4_insertion_sort.py

and it prints PASS or FAIL for each check.
"""

_results = []


def check(description, actual, expected):
    """Print PASS/FAIL comparing `actual` to `expected`."""
    ok = actual == expected
    _results.append(ok)
    if ok:
        print(f"  PASS  {description}")
    else:
        print(f"  FAIL  {description}")
        print(f"          expected: {expected!r}")
        print(f"          got:      {actual!r}")
    return ok


def run(label, function, *args):
    """Call function(*args), printing a FAIL instead of crashing on an error."""
    try:
        return function(*args)
    except NotImplementedError:
        print(f"  TODO  {label} is not written yet")
    except Exception as error:  # show students the error without a traceback wall
        print(f"  ERROR {label} raised {type(error).__name__}: {error}")
    return None


def summary():
    passed = sum(_results)
    print(f"\n{passed} of {len(_results)} checks passed.")
