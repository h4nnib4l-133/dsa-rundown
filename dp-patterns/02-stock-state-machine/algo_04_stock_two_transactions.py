import os, sys
_d = os.path.dirname(os.path.abspath(__file__))
while _d and not os.path.exists(os.path.join(_d, 'test_runner.py')):
    _d = os.path.dirname(_d)
sys.path.insert(0, _d)
from test_runner import run_tests


# Best Time to Buy/Sell III (LC #123) -- Hard
# Input:  prices: List[int]
# Output: int (max profit with AT MOST 2 transactions)
# At most 2 buy+sell pairs.
# 4 states: buy1 (own after 1st buy), sell1 (sold 1st), buy2 (own after 2nd buy), sell2 (sold 2nd).
#
# Example:
# #   [3,3,5,0,0,3,1,4] -> 6   (buy@0, sell@3; buy@1, sell@4)
#   [1,2,3,4,5]       -> 4   (buy@1, sell@5, one transaction)
#
#   Key: buy1 = max(buy1, -price)
#        sell1 = max(sell1, buy1 + price)
#        buy2 = max(buy2, sell1 - price)
#        sell2 = max(sell2, buy2 + price)

def max_profit_two(prices):
    pass

run_tests(max_profit_two, [
    (([3,3,5,0,0,3,1,4],), 6),
    (([1,2,3,4,5],),       4),
    (([7,6,4,3,1],),       0),
    (([1,2,4,2,5,7,2,4,9,0],), 13),
])
