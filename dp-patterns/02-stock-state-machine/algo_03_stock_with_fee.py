import os, sys
_d = os.path.dirname(os.path.abspath(__file__))
while _d and not os.path.exists(os.path.join(_d, 'test_runner.py')):
    _d = os.path.dirname(_d)
sys.path.insert(0, _d)
from test_runner import run_tests


# Best Time to Buy/Sell with Fee (LC #714) -- Medium
# Input:  prices: List[int], fee: int
# Output: int (max profit with unlimited transactions, fee per transaction)
# Each transaction (buy+sell pair) costs a fee.
# Only sell when profit > fee.
#
# Example:
# #   prices=[1,3,2,8,4,9], fee=2  -> 8
#     buy@1 sell@8 profit=7-2=5; buy@4 sell@9 profit=5-2=3. Total=8.
#
#   Key: cash = max(cash, hold + price - fee)   # sell today
#        hold = max(hold, cash - price)         # buy today

def max_profit_fee(prices, fee):
    pass

run_tests(max_profit_fee, [
    (([1,3,2,8,4,9], 2),  8),
    (([1,3,7,5,10,3], 3), 6),
    (([1,2], 3),          0),     # fee > profit
    (([1], 1),            0),
])
