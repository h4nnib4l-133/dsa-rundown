import os, sys
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))
from test_runner import run_tests


# Contiguous Array (LC #525) -- Medium
# Input:  nums: List[int] (only 0s and 1s)
# Output: int (longest contiguous subarray with equal 0s and 1s)
# Find longest subarray where #0s == #1s.
#
# Pattern: TRANSFORMATION + PREFIX SUM + HASH MAP
# Map 0 -> -1, 1 -> +1. Equal counts means subarray sum = 0.
# Use prefix sums: if same prefix appears twice, the range between is zero-sum.
#
# Example:
# #   [0,1]           -> 2   (whole array)
#   [0,1,0]         -> 2   ([0,1])
#   [0,1,1,1,1,1,0,0,0]  -> 6  ([1,1,1,1,0,0])
#
#   Key: Hashmap {prefix_sum: first_index}. For each i:
#        if prefix_sum seen before, length = i - first_index.

def find_max_length(nums):
    pass

run_tests(find_max_length, [
    (([0,1],),                 2),
    (([0,1,0],),               2),
    (([0,1,1,1,1,1,0,0,0],),   6),
    (([1,1,1],),               0),     # no zeros
    (([0,0],),                 0),     # no ones
    (([0,1,0,1],),             4),
])
