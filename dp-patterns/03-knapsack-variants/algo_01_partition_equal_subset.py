import os, sys
_d = os.path.dirname(os.path.abspath(__file__))
while _d and not os.path.exists(os.path.join(_d, 'test_runner.py')):
    _d = os.path.dirname(_d)
sys.path.insert(0, _d)
from test_runner import run_tests


# Partition Equal Subset Sum (LC #416) -- Medium
# Input:  nums: List[int] (positive)
# Output: bool (True if can be split into two equal-sum subsets)
# Subset sum variant: find subset summing to total/2.
#
# Pattern: 0/1 KNAPSACK (exists variant)
# dp[s] = True if some subset sums to s.
#
# Example:
# #   [1,5,11,5] -> True   ([1,5,5] and [11], both sum to 11)
#   [1,2,3,5]  -> False  (total=11 is odd)
#
#   Key: Target = total/2. dp[0]=True. For each num, iterate s from target down:
#        dp[s] = dp[s] or dp[s-num].

def can_partition(nums):
    pass

run_tests(can_partition, [
    (([1,5,11,5],), True),
    (([1,2,3,5],),  False),
    (([1,1],),      True),
    (([2,2,3,5],),  False),
    (([1,2,5],),    False),     # total 8, no subset sums to 4
])
