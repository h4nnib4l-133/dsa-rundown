import os, sys
_d = os.path.dirname(os.path.abspath(__file__))
while _d and not os.path.exists(os.path.join(_d, 'test_runner.py')):
    _d = os.path.dirname(_d)
sys.path.insert(0, _d)
from test_runner import run_tests



# Best Time to Buy and Sell Stock (LC #121) -- Easy
# Input:  prices: List[int] (daily stock prices)
# Output: int (max profit from one buy + one sell, 0 if no profit)
# Given daily prices, find max profit from one buy and one sell.
# Must buy before you sell. Return 0 if no profit possible.
#
# Example:
#   [7,1,5,3,6,4] -> 5  (buy at 1, sell at 6)
#   [7,6,4,3,1]   -> 0  (prices only decrease, no profit)
#
#   Key: Track minimum price seen so far.
#        At each day: profit = price - min_so_far. Track max profit.

def max_profit(prices):
    pass


run_tests(max_profit, [
    (([7,1,5,3,6,4],),  5),     # buy@1 sell@6
    (([7,6,4,3,1],),    0),     # decreasing
    (([2,4,1],),         2),     # buy@2 sell@4
    (([1],),             0),     # single day
    (([2,1],),           0),     # two days, decreasing
    (([1,2],),           1),     # two days, increasing
    (([3,3,3],),         0),     # flat
    (([1,2,3,4,5],),     4),     # increasing: buy@1 sell@5
    (([2,1,2,1,2],),     1),     # oscillating
])
