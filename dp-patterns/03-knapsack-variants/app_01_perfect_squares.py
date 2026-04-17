import os, sys
_d = os.path.dirname(os.path.abspath(__file__))
while _d and not os.path.exists(os.path.join(_d, 'test_runner.py')):
    _d = os.path.dirname(_d)
sys.path.insert(0, _d)
from test_runner import run_tests


# Perfect Squares (LC #279) -- Medium
# Input:  n: int
# Output: int (min number of perfect squares summing to n)
# Find min perfect squares (1,4,9,16,...) that sum to n.
#
# Unbounded knapsack. Items are perfect squares <= n.
#
# Example:
# #   n=12 -> 3   (4+4+4)
#   n=13 -> 2   (4+9)
#
#   WHY THIS IS A UNBOUNDED KNAPSACK:
#   Squares are coins, target is n, minimize count. Same as Coin Change.
#
#   Key: dp[i] = min(dp[i-j*j] + 1) for j*j <= i.

def num_squares(n):
    pass

run_tests(num_squares, [
    ((12,),   3),
    ((13,),   2),
    ((1,),    1),
    ((4,),    1),
    ((7,),    4),     # 4+1+1+1
    ((100,),  1),
])
