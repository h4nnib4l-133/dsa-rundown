import os, sys
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))
from test_runner import run_tests


# Best Time to Buy/Sell IV (LC #188) -- Hard
# Input:  k: int, prices: List[int]
# Output: int (max profit with AT MOST k transactions)
# Generalization: at most k buy+sell pairs.
# If k >= n/2, reduces to unlimited transactions (Stock II).
#
# Example:
# #   k=2, [3,2,6,5,0,3] -> 7  (buy@2 sell@6; buy@0 sell@3)
#   k=2, [2,4,1]       -> 2  (only one good trade)
#
#   Key: buy[j] = max(buy[j], sell[j-1] - price)
#        sell[j] = max(sell[j], buy[j] + price)
#        for j in 1..k

def max_profit_k(k, prices):
    pass

run_tests(max_profit_k, [
    ((2, [3,2,6,5,0,3]),   7),
    ((2, [2,4,1]),         2),
    ((1, [1,2,3,4,5]),     4),
    ((0, [1,2,3]),         0),     # zero transactions
    ((100, [1,2,3,4,5]),   4),     # k > n/2
])
