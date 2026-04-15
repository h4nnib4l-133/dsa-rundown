# ============================================================
# PATTERN: ARRAYS SORTING
# ============================================================
# 1. **Two pointers** -- sorted arrays, pair/triplet sum, container problems
# 2. **Prefix sum** -- range sum queries, subarray sum problems
# 3. **Hash map** -- O(1) lookup for complement, frequency counting
# 4. **Merge intervals** -- sort by start, merge overlapping
# 5. **Dutch National Flag** -- 3-way partition with lo/mid/hi pointers
#
# ---
# ============================================================

import sys, os; sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from test_runner import run_tests


# Two Sum (LC #1) -- Easy
# Find two numbers that add up to target. Return indices.
#
#   Key: Hash map: for each num, check if `target - num` exists

def two_sum(nums, target):
    """Return indices of two numbers that add up to target"""
    pass


# Order doesn't matter, so sort result
def solve(nums, target):
    r = two_sum(nums, target)
    return sorted(r) if r else r


run_tests(solve, [
    (([2,7,11,15], 9),   [0, 1]),
    (([3,2,4], 6),       [1, 2]),
    (([3,3], 6),         [0, 1]),
])
