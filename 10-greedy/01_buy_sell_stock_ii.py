# ============================================================
# PATTERN: GREEDY
# ============================================================
# Greedy makes the locally optimal choice at each step, hoping for a global optimum. Works when:
# 1. **Greedy choice property** -- local optimum leads to global optimum
# 2. **Optimal substructure** -- optimal solution contains optimal sub-solutions
#
# **Common strategies:**
# - Sort by some criteria (end time, ratio, etc.) then scan
# - Two pointers from both ends
# - Track running max/min/sum
#
# **How to verify greedy works:** Try to construct a counterexample. If you can't, it's likely correct.
#
# ---
# ============================================================

import sys, os; sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from test_runner import run_tests



# Best Time to Buy and Sell Stock II (LC #122) -- Medium
# Can make unlimited transactions (buy/sell). Find max profit.
# Must sell before buying again. Can buy and sell same day.
#
# Example:
#   [7,1,5,3,6,4] -> 7  (buy@1 sell@5=4, buy@3 sell@6=3, total=7)
#   [1,2,3,4,5]   -> 4  (buy@1 sell@5)
#   [7,6,4,3,1]   -> 0  (no profitable transaction)
#
#   Key: Collect every upward slope.
#        If prices[i] > prices[i-1], add the difference.

def max_profit(prices):
    pass


run_tests(max_profit, [
    (([7,1,5,3,6,4],),  7),     # two transactions
    (([1,2,3,4,5],),    4),     # one long hold
    (([7,6,4,3,1],),    0),     # all decreasing
    (([1],),             0),     # single day
    (([1,2],),           1),     # one increase
    (([2,1],),           0),     # one decrease
    (([3,3,3],),         0),     # flat
    (([1,2,1,2,1,2],),  3),     # oscillating: 3 x (buy@1 sell@2)
])
