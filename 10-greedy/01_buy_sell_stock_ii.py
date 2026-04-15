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
# Max profit with unlimited transactions.
#
#   Key: Collect every upward slope: if `prices[i] > prices[i-1]`, add the difference

def max_profit(prices):
    pass


run_tests(max_profit, [
    (([7,1,5,3,6,4],), 7),
    (([1,2,3,4,5],),   4),
    (([7,6,4,3,1],),   0),
])
