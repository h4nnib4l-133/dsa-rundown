import sys, os; sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from test_runner import run_tests


# 0/1 Knapsack -- Medium
# Max value with weight constraint, each item used at most once.
#
#   State: `dp[i][w]` = max value using items 0..i with capacity w
#   Transition: `dp[i][w] = max(dp[i-1][w], dp[i-1][w-wt[i]] + val[i])`
#   Optimize: 1D array, iterate w backwards

def knapsack(weights, values, capacity):
    """0/1 knapsack: max value within capacity"""
    pass


run_tests(knapsack, [
    (([1,2,3], [6,10,12], 5),          22),   # items 1+2 -> wt 5, val 22
    (([2,3,4,5], [3,4,5,6], 5),         7),   # items 0+1 -> wt 5, val 7
    (([10], [100], 5),                   0),   # can't fit
    (([1,1,1], [10,20,30], 2),          50),   # items 1+2 -> val 50
])
