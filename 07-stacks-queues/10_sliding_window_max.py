import sys, os; sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from test_runner import run_tests
from collections import deque


# Sliding Window Maximum (LC #239) -- Hard
# Max element in each sliding window of size k.
#
#   Key: Monotonic decreasing deque. Front = current max. Remove from back if smaller.

def max_sliding_window(nums, k):
    pass


run_tests(max_sliding_window, [
    (([1,3,-1,-3,5,3,6,7], 3), [3,3,5,5,6,7]),
    (([1], 1),                  [1]),
    (([9,11], 2),               [11]),
])
