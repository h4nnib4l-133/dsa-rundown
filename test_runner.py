"""
Simple test runner. Import this in any problem file.

Usage:
    from test_runner import run_tests

    def solve(nums, target):
        # your code here
        pass

    run_tests(solve, [
        (([1,2,3,4], 3), 2),        # (args_tuple, expected)
        (([1,2,3,4], 5), -1),
    ])
"""

import sys
import time


def run_tests(fn, cases):
    passed = 0
    failed = 0
    total = len(cases)

    for i, (args, expected) in enumerate(cases, 1):
        # handle single arg (not wrapped in tuple)
        if not isinstance(args, tuple):
            args = (args,)

        start = time.perf_counter()
        try:
            result = fn(*args)
        except Exception as e:
            print(f"  [{i}/{total}] CRASH: {e}")
            failed += 1
            continue
        elapsed = (time.perf_counter() - start) * 1000

        if result == expected:
            print(f"  [{i}/{total}] PASS  ({elapsed:.2f}ms)")
            passed += 1
        else:
            print(f"  [{i}/{total}] FAIL")
            print(f"         input:    {args}")
            print(f"         expected: {expected}")
            print(f"         got:      {result}")
            failed += 1

    print(f"\n  {passed}/{total} passed", end="")
    if failed:
        print(f"  ({failed} failed)")
    else:
        print("  ✓")
