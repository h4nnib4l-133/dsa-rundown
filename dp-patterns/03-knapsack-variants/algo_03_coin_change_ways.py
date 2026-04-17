import os, sys
_d = os.path.dirname(os.path.abspath(__file__))
while _d and not os.path.exists(os.path.join(_d, 'test_runner.py')):
    _d = os.path.dirname(_d)
sys.path.insert(0, _d)
from test_runner import run_tests


# Coin Change 2 (LC #518) -- Medium
# Input:  amount: int, coins: List[int]
# Output: int (number of ways to make amount using any # of each coin)
# Count ways (not minimum coins). Unlimited supply.
#
# Pattern: UNBOUNDED KNAPSACK (count variant).
# Order of coins matters for correctness: iterate coins OUTER, amount INNER,
# to avoid double-counting permutations.
#
# Example:
# #   amount=5, coins=[1,2,5] -> 4   (5; 2+2+1; 2+1+1+1; 1x5)
#   amount=3, coins=[2]     -> 0
#
#   Key: dp[0] = 1. For each coin: for s from coin to amount: dp[s] += dp[s-coin].

def change(amount, coins):
    pass

run_tests(change, [
    ((5, [1,2,5]),   4),
    ((3, [2]),       0),
    ((10, [10]),     1),
    ((0, [1,2,3]),   1),     # one way: use no coins
    ((4, [1,2,3]),   4),
])
