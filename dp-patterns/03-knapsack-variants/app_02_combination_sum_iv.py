import os, sys
_d = os.path.dirname(os.path.abspath(__file__))
while _d and not os.path.exists(os.path.join(_d, 'test_runner.py')):
    _d = os.path.dirname(_d)
sys.path.insert(0, _d)
from test_runner import run_tests


# Combination Sum IV (LC #377) -- Medium
# Input:  nums: List[int] (distinct positive), target: int
# Output: int (count of combinations summing to target; ORDER MATTERS)
# Different orderings count as different combinations.
# (1,1,2) and (2,1,1) are different.
#
# Example:
# #   nums=[1,2,3], target=4 -> 7   (1+1+1+1, 1+1+2, 1+2+1, 2+1+1, 1+3, 3+1, 2+2)
#
#   Pattern: UNBOUNDED KNAPSACK (permutations)
#   Key: dp[t] = sum of dp[t-num] for each num <= t.
#        For permutations: iterate target OUTER, nums INNER.

def combination_sum_4(nums, target):
    pass

run_tests(combination_sum_4, [
    (([1,2,3], 4),     7),
    (([9], 3),         0),
    (([1], 5),         1),
    (([1,2], 10),      89),
])
