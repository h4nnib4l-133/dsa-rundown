import sys, os; sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from test_runner import run_tests



# Subarray Sum Equals K (LC #560) -- Medium
# Count the number of contiguous subarrays whose sum equals k.
# Array can have negative numbers.
#
# Example:
#   nums=[1,1,1], k=2  -> 2  ([1,1] starting at index 0, [1,1] starting at index 1)
#   nums=[1,2,3], k=3  -> 2  ([1,2] and [3])
#
#   Key: Prefix sum + hash map.
#        prefix_sum[i] - prefix_sum[j] = k means subarray j+1..i sums to k.
#        Count how many times (prefix_sum - k) has appeared before.

def subarray_sum(nums, k):
    pass


run_tests(subarray_sum, [
    (([1,1,1], 2),        2),
    (([1,2,3], 3),        2),     # [1,2] and [3]
    (([1,-1,0], 0),       3),     # [1,-1], [-1,0+1? wait: [1,-1], [0], [1,-1,0]
    (([1], 1),            1),     # single element match
    (([1], 2),            0),     # single element no match
    (([0,0,0], 0),        6),     # every subarray sums to 0
    (([-1,-1,1], 0),      1),     # [-1,1]
    (([3,4,7,2,-3,1,4,2], 7), 4), # multiple subarrays
])
