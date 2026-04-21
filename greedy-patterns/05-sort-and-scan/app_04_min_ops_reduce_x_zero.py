import os, sys
_d = os.path.dirname(os.path.abspath(__file__))
while _d and not os.path.exists(os.path.join(_d, 'test_runner.py')):
    _d = os.path.dirname(_d)
sys.path.insert(0, _d)
from test_runner import run_tests


# Min Operations to Reduce X to Zero (LC #1658) -- Medium
# Input:  nums: List[int], x: int
# Output: int (min elements removed from ends to make sum x, -1 if impossible)
# Remove from ends only. Each op removes from leftmost or rightmost.
#
# Example:
# #   nums=[1,1,4,2,3], x=5  -> 2   (remove 3 and 2 from end)
#
#   Greedy insight: Reframe: find LONGEST subarray summing to (total - x). Sliding window.

def min_operations_reduce(nums, x):
    pass

run_tests(min_operations_reduce, [
    (([1,1,4,2,3], 5),       2),
    (([5,6,7,8,9], 4),      -1),
    (([3,2,20,1,1,3], 10),   5),
    (([1,1], 3),            -1),
])
