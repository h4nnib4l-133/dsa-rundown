import os, sys
_d = os.path.dirname(os.path.abspath(__file__))
while _d and not os.path.exists(os.path.join(_d, 'test_runner.py')):
    _d = os.path.dirname(_d)
sys.path.insert(0, _d)
from test_runner import run_tests


# Two Sum Less Than K (LC #1099) -- Easy
# Input:  nums: List[int], k: int
# Output: int (max sum of two distinct elements < k, or -1)
# Find max sum of a pair with sum strictly less than k.
#
# Example:
# #   nums=[34,23,1,24,75,33,54,8], k=60  -> 58   (34+24)
#
#   Greedy insight: Sort. Two pointers. If sum < k, update max and move left ptr right. Else right ptr left.

def two_sum_less_than_k(nums, k):
    pass

run_tests(two_sum_less_than_k, [
    (([34,23,1,24,75,33,54,8], 60),   58),
    (([10,20,30], 15),                -1),
    (([1,2], 3),                      -1),
    (([1,2], 4),                       3),
])
