import sys, os; sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from test_runner import run_tests


# Subarray Sum Equals K (LC #560) -- Medium
# Count subarrays with sum equal to k.
#
#   Key: Prefix sum + hash map. Count how many times `prefix_sum - k` has occurred.

def subarray_sum(nums, k):
    pass


run_tests(subarray_sum, [
    (([1,1,1], 2),      2),
    (([1,2,3], 3),      2),
    (([1,-1,0], 0),     3),
])
