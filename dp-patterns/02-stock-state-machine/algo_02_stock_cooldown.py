import os, sys
_d = os.path.dirname(os.path.abspath(__file__))
while _d and not os.path.exists(os.path.join(_d, 'test_runner.py')):
    _d = os.path.dirname(_d)
sys.path.insert(0, _d)
from test_runner import run_tests


# Best Time to Buy/Sell with Cooldown (LC #309) -- Medium
# Input:  prices: List[int]
# Output: int (max profit with unlimited transactions but 1-day cooldown after sell)
# After selling, must wait 1 day before buying again.
# Three states: HOLD (own stock), SOLD (just sold, cooling), REST (no stock, can buy).
#
# Example:
# #   [1,2,3,0,2] -> 3   (buy@1, sell@2, cooldown, buy@0, sell@2)
#
#   Key: hold = max(hold, rest - price)       # buy today
#        sold = hold + price                   # sell today
#        rest = max(rest, sold)                # stay in rest or enter from sold

def max_profit_cooldown(prices):
    pass

run_tests(max_profit_cooldown, [
    (([1,2,3,0,2],), 3),
    (([1],),         0),
    (([1,2,4],),     3),     # no need for cooldown if one transaction
    (([2,1,4],),     3),
    (([1,2,3,0,2,4],), 6),
])
