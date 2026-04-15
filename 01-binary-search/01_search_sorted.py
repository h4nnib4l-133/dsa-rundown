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

import os
import sys

sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
from test_runner import run_tests


# Binary Search (LC #704) -- Easy
# Input:  nums: List[int] (sorted ascending), target: int
# Output: int (index of target, or -1 if not found)
# Given a sorted array and a target, return the index of target or -1.
#
# Example:
#   nums = [-1, 0, 3, 5, 9, 12], target = 9
#   -> 4  (nums[4] == 9)
#
#   nums = [-1, 0, 3, 5, 9, 12], target = 2
#   -> -1  (2 is not in the array)
#
#   Key: lo, hi, mid. Compare nums[mid] with target.
#        If equal, found. If less, search right. If more, search left.

def search(nums, target):
    lo, hi = 0, len(nums) - 1
    while lo <= hi:
        mid = (hi + lo) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1

    return -1


run_tests(search, [
    (([1, 2, 3, 4, 5], 3),        2),     # mid element
    (([1, 2, 3, 4, 5], 1),        0),     # first element
    (([1, 2, 3, 4, 5], 5),        4),     # last element
    (([1, 2, 3, 4, 5], 6),       -1),     # greater than all
    (([1, 2, 3, 4, 5], 0),       -1),     # less than all
    (([-1, 0, 3, 5, 9, 12], 9),   4),     # with negatives
    (([5], 5),                     0),     # single element found
    (([5], 3),                    -1),     # single element not found
    (([], 3),                     -1),     # empty array  (handle len=0)
    (([1, 2], 1),                  0),     # two elements, find first
    (([1, 2], 2),                  1),     # two elements, find second
    (([2, 5, 8, 12, 16, 23, 38, 56, 72, 91], 23), 5),  # larger array
])
