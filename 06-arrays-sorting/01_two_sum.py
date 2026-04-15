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
# Given array and target, return indices of two numbers that add up to target.
# Exactly one solution exists. Can't use same element twice.
#
# Example:
#   nums=[2,7,11,15], target=9  -> [0,1]  (2+7=9)
#   nums=[3,2,4], target=6      -> [1,2]  (2+4=6)
#   nums=[3,3], target=6        -> [0,1]  (3+3=6)
#
#   Key: Hash map. For each num, check if (target - num) exists in map.
#        Store {value: index} as you iterate.

def two_sum(nums, target):
    """Return indices of two numbers that add up to target"""
    pass


# Order doesn't matter, so sort result
def solve(nums, target):
    r = two_sum(nums, target)
    return sorted(r) if r else r


run_tests(solve, [
    (([2,7,11,15], 9),    [0, 1]),
    (([3,2,4], 6),        [1, 2]),
    (([3,3], 6),          [0, 1]),     # duplicate values
    (([1,5,3,7], 8),      [1, 2]),     # 5+3=8? no 5+3=8. [1,2]
    (([0,4,3,0], 0),      [0, 3]),     # zeros
    (([-1,-2,-3,-4], -6), [1, 3]),     # negatives: -2+-4=-6
])
