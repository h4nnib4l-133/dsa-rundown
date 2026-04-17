import os, sys
_d = os.path.dirname(os.path.abspath(__file__))
while _d and not os.path.exists(os.path.join(_d, 'test_runner.py')):
    _d = os.path.dirname(_d)
sys.path.insert(0, _d)
from test_runner import run_tests


# Longest Arithmetic Subsequence (LC #1027) -- Medium
# Input:  nums: List[int]
# Output: int (length of longest arithmetic subsequence)
# Subsequence (not contiguous) with constant difference.
#
# Example:
# #   [3,6,9,12]      -> 4
#   [9,4,7,2,10]    -> 3   (4,7,10)
#   [20,1,15,3,10,5,8] -> 4  (20,15,10,5)
#
#   Pattern: STATE DP (2D: index + diff)
#   Key: dp[i][d] = length of arith subseq ending at i with diff d.
#        dp[i][d] = dp[j][d] + 1 for j < i where nums[i]-nums[j] == d.

def longest_arith_seq_length(nums):
    pass

run_tests(longest_arith_seq_length, [
    (([3,6,9,12],),          4),
    (([9,4,7,2,10],),         3),
    (([20,1,15,3,10,5,8],),   4),
    (([1],),                  1),
    (([1,2],),                2),
])
