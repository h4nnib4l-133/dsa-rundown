# ============================================================
# PATTERN: BINARY SEARCH
# ============================================================
# Binary search eliminates half the search space each step. Works on any **monotonic** condition -- not just sorted arrays.
#
# **Template:**
# ```
# lo, hi = min_possible, max_possible
# while lo < hi:
#     mid = (lo + hi) // 2
#     if condition(mid):
#         hi = mid       # answer is mid or left
#     else:
#         lo = mid + 1   # answer is right
# return lo
# ```
#
# **Three flavors:**
# 1. **Search for value** -- classic sorted array lookup
# 2. **Search for boundary** -- first/last occurrence, lower/upper bound
# 3. **Search on answer** -- minimize/maximize some value (Koko, ships, cows)
#
# ---
# ============================================================

import sys, os

sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
from test_runner import run_tests

# Binary Search (LC #704) -- Easy
# Find target in sorted array. Return index or -1.
#
#   Key: Basic `lo, hi, mid` template


def search(nums, target):
    pass



run_tests(
    search,
    [
        (([1, 2, 3, 4, 5], 3), 2),
        (([1, 2, 3, 4, 5], 1), 0),
        (([1, 2, 3, 4, 5], 5), 4),
        (([1, 2, 3, 4, 5], 6), -1),
        (([-1, 0, 3, 5, 9, 12], 9), 4),
        (([5], 5), 0),
        (([5], 3), -1),
    ],
)
