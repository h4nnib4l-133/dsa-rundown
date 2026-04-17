import os, sys
_d = os.path.dirname(os.path.abspath(__file__))
while _d and not os.path.exists(os.path.join(_d, 'test_runner.py')):
    _d = os.path.dirname(_d)
sys.path.insert(0, _d)
from test_runner import run_tests


# Uncrossed Lines (LC #1035) -- Medium
# Input:  nums1: List[int], nums2: List[int]
# Output: int (max connecting lines that don't cross)
# Connect equal values across lists without lines crossing.
# EXACTLY the LCS problem in disguise.
#
# Example:
# #   [1,4,2], [1,2,4]  -> 2   (connect 1-1 and 2-2 or 1-1 and 4-4)
#
#   Pattern: LCS (disguised)
#   Key: Classic LCS on the two arrays.

def max_uncrossed_lines(nums1, nums2):
    pass

run_tests(max_uncrossed_lines, [
    (([1,4,2], [1,2,4]),                2),
    (([2,5,1,2,5], [10,5,2,1,5,2]),     3),
    (([1,3,7,1,7,5], [1,9,2,5,1]),      2),
    (([1], [1]),                         1),
    (([1], [2]),                         0),
])
