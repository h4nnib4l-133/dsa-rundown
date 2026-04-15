import sys, os; sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from test_runner import run_tests

# Sliding Window Maximum (LC #239) -- Hard
# Given array and window size k, return max of each sliding window.
#
# Example:
#   nums=[1,3,-1,-3,5,3,6,7], k=3
#   Window [1,3,-1]   max=3
#   Window [3,-1,-3]  max=3
#   Window [-1,-3,5]  max=5
#   Window [-3,5,3]   max=5
#   Window [5,3,6]    max=6
#   Window [3,6,7]    max=7
#   -> [3,3,5,5,6,7]
#
#   Key: Monotonic decreasing deque. Front = current max index.
#        Remove from back if smaller than current.
#        Remove from front if outside window.

from collections import deque


# Sliding Window Maximum (LC #239) -- Hard
# Max element in each sliding window of size k.
#
#   Key: Monotonic decreasing deque. Front = current max. Remove from back if smaller.

def max_sliding_window(nums, k):
    pass


run_tests(max_sliding_window, [
    (([1,3,-1,-3,5,3,6,7], 3),  [3,3,5,5,6,7]),
    (([1], 1),                    [1]),            # single element window
    (([9,11], 2),                 [11]),           # window = array size
    (([4,3,2,1], 2),              [4,3,2]),        # decreasing
    (([1,2,3,4], 2),              [2,3,4]),        # increasing
    (([1,3,1,2,0,5], 3),          [3,3,2,5]),
    (([7,2,4], 2),                [7,4]),
])
