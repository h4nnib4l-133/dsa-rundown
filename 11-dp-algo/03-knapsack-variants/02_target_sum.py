import os, sys
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))
from test_runner import run_tests


# Target Sum (LC #494) -- Medium
# Input:  nums: List[int] (non-negative), target: int
# Output: int (number of ways to assign +/- to nums to reach target)
# Assign +/- to each num to make sum == target. Count ways.
#
# Trick: Let P = positive subset, N = negative subset.
# P - N = target, P + N = total. So P = (total + target) / 2.
# Reduces to "count subsets summing to P" -- classic knapsack.
#
# Example:
# #   nums=[1,1,1,1,1], target=3  -> 5
#     -1+1+1+1+1, +1-1+1+1+1, +1+1-1+1+1, +1+1+1-1+1, +1+1+1+1-1
#
#   Key: P = (total + target) / 2. If not integer or > total, return 0.
#        dp[s] = number of subsets summing to s. Unbounded knapsack count.

def find_target_sum_ways(nums, target):
    pass

run_tests(find_target_sum_ways, [
    (([1,1,1,1,1], 3),  5),
    (([1], 1),          1),
    (([1], 2),          0),
    (([1,0], 1),        2),     # +1+0 or +1-0
    (([1,2,3], 0),      2),     # +1-2+... hmm: {-1,+2,-1}? Let's verify: +1-2+... actually -1+2-... Let's think: need sum=0. +1+2-3=0, -1-2+3=0 -> 2 ways. ✓
])
