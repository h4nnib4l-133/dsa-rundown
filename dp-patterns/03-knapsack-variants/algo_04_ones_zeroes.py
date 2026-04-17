import os, sys
_d = os.path.dirname(os.path.abspath(__file__))
while _d and not os.path.exists(os.path.join(_d, 'test_runner.py')):
    _d = os.path.dirname(_d)
sys.path.insert(0, _d)
from test_runner import run_tests


# Ones and Zeroes (LC #474) -- Medium
# Input:  strs: List[str], m: int (max 0s), n: int (max 1s)
# Output: int (max subset size with at most m zeros and n ones)
# Two-dimensional knapsack: each 'item' has 0-cost and 1-cost.
# Pick as many strings as possible within m zeros and n ones.
#
# Example:
# #   strs=["10","0001","111001","1","0"], m=5, n=3  -> 4
#     e.g., pick "10","0001","1","0" uses 4 zeros + 3 ones.
#
#   Key: dp[i][j] = max subset size using up to i zeros, j ones.
#        For each string with (z,o): dp[i][j] = max(dp[i][j], dp[i-z][j-o]+1).
#        Iterate i,j BACKWARDS (0/1 knapsack).

def find_max_form(strs, m, n):
    pass

run_tests(find_max_form, [
    ((["10","0001","111001","1","0"], 5, 3),  4),
    ((["10","0","1"], 1, 1),                  2),
    (([], 0, 0),                              0),
    ((["0","0","1"], 1, 0),                   1),
])
