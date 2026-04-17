import os, sys
_d = os.path.dirname(os.path.abspath(__file__))
while _d and not os.path.exists(os.path.join(_d, 'test_runner.py')):
    _d = os.path.dirname(_d)
sys.path.insert(0, _d)
from test_runner import run_tests


# Best Time to Buy and Sell Stock (LC #121) -- Easy
# Input:  prices: List[int]
# Output: int (max profit from ONE buy+sell, 0 if none)
# One transaction only. Must buy before sell.
# State: track min price seen so far.
#
# Example:
# #   [7,1,5,3,6,4] -> 5   (buy@1, sell@6)
#   [7,6,4,3,1]   -> 0   (only decreasing)
#
#   Key: min_price = min(min_price, prices[i]).
#        profit = max(profit, prices[i] - min_price).

def max_profit(prices):
    pass

run_tests(max_profit, [
    (([7,1,5,3,6,4],), 5),
    (([7,6,4,3,1],),   0),
    (([1],),           0),
    (([1,2],),         1),
    (([2,4,1],),       2),
])
