import os, sys
_d = os.path.dirname(os.path.abspath(__file__))
while _d and not os.path.exists(os.path.join(_d, 'test_runner.py')):
    _d = os.path.dirname(_d)
sys.path.insert(0, _d)
from test_runner import run_tests


# Minimum Absolute Difference (LC #1200) -- Easy
# Input:  arr: List[int]
# Output: List[[a,b]] (all pairs with min absolute difference, sorted)
# Find all pairs (a,b) with a<b and b-a = min absolute difference.
#
# Example:
# #   [4,2,1,3] -> [[1,2],[2,3],[3,4]]
#
#   Greedy insight: Sort. Scan adjacent pairs to find min diff. Second pass collects matching pairs.

def minimum_abs_difference(arr):
    pass

run_tests(minimum_abs_difference, [
    (([4,2,1,3],),             [[1,2],[2,3],[3,4]]),
    (([1,3,6,10,15],),         [[1,3]]),
    (([3,8,-10,23,19,-4,-14,27],), [[-14,-10],[19,23],[23,27]]),
])
