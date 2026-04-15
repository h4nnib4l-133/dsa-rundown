import sys, os; sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from test_runner import run_tests



# 0/1 Knapsack (GFG) -- Medium
# Input:  weights: List[int], values: List[int], capacity: int
# Output: int (max total value fitting within capacity)
# Given n items with weights and values, and a knapsack capacity.
# Each item can be used at most once. Maximize total value.
#
# Example:
#   weights=[1,2,3], values=[6,10,12], capacity=5
#   Pick items 1+2 (weight=2+3=5, value=10+12=22) -> 22
#
#   weights=[2,3,4,5], values=[3,4,5,6], capacity=5
#   Pick items 0+1 (weight=2+3=5, value=3+4=7) -> 7
#
#   Key: dp[i][w] = max value using items 0..i with remaining capacity w.
#        dp[i][w] = max(skip: dp[i-1][w], take: dp[i-1][w-wt[i]] + val[i]).
#        Optimize: 1D array, iterate capacity BACKWARDS.

def knapsack(weights, values, capacity):
    """0/1 knapsack: max value within capacity"""
    pass


run_tests(knapsack, [
    (([1,2,3], [6,10,12], 5),         22),    # take items 1,2
    (([2,3,4,5], [3,4,5,6], 5),        7),    # take items 0,1
    (([10], [100], 5),                  0),    # can't fit anything
    (([1,1,1], [10,20,30], 2),         50),    # take items 1,2
    (([1,2,3], [6,10,12], 0),           0),    # zero capacity
    (([5], [10], 5),                   10),    # exactly fits
    (([1,1,1,1], [1,2,3,4], 3),        9),    # take items 1,2,3
    (([3,4,2], [4,5,3], 7),            9),    # take all (3+4+2=9<=7? no. 3+2=5, 3+4=7. take 0+1: wt=7, val=9)
])
