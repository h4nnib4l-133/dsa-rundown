import os, sys
_d = os.path.dirname(os.path.abspath(__file__))
while _d and not os.path.exists(os.path.join(_d, 'test_runner.py')):
    _d = os.path.dirname(_d)
sys.path.insert(0, _d)
from test_runner import run_tests


# Wiggle Subsequence (LC #376) -- Medium
# Input:  nums: List[int]
# Output: int (length of longest alternating +/- subsequence)
# Differences between consecutive elements must alternate strictly positive/negative.
#
# Example:
# #   [1,7,4,9,2,5] -> 6   (whole array: +6,-3,+5,-7,+3)
#   [1,17,5,10,13,15,10,5,16,8] -> 7
#   [1,2,3,4,5,6,7,8,9] -> 2
#
#   Pattern: STATE MACHINE (up/down)
#   Key: up[i] = longest wiggle ending at i with last diff positive.
#        down[i] = same with negative.
#        If nums[i] > nums[i-1]: up = down + 1. And vice versa.

def wiggle_max_length(nums):
    pass

run_tests(wiggle_max_length, [
    (([1,7,4,9,2,5],),                           6),
    (([1,17,5,10,13,15,10,5,16,8],),             7),
    (([1,2,3,4,5,6,7,8,9],),                     2),
    (([1,1,1,1],),                                1),
    (([1],),                                      1),
])
