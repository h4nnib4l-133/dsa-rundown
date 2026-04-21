import os, sys
_d = os.path.dirname(os.path.abspath(__file__))
while _d and not os.path.exists(os.path.join(_d, 'test_runner.py')):
    _d = os.path.dirname(_d)
sys.path.insert(0, _d)
from test_runner import run_tests


# Max Number of K-Sum Pairs (LC #1679) -- Medium
# Input:  nums: List[int], k: int
# Output: int (max pairs that sum to k; each element used at most once)
# Count max pairs (a, b) with a+b == k. Each element used in at most one pair.
#
# Example:
# #   nums=[1,2,3,4], k=5  -> 2   ((1,4), (2,3))
#
#   Greedy insight: Sort + two pointers (or hash map counts).

def max_operations(nums, k):
    pass

run_tests(max_operations, [
    (([1,2,3,4], 5),      2),
    (([3,1,3,4,3], 6),    1),
    (([1,1,1,1], 2),      2),
    (([], 5),             0),
])
