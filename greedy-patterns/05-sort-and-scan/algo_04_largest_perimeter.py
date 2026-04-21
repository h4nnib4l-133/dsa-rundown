import os, sys
_d = os.path.dirname(os.path.abspath(__file__))
while _d and not os.path.exists(os.path.join(_d, 'test_runner.py')):
    _d = os.path.dirname(_d)
sys.path.insert(0, _d)
from test_runner import run_tests


# Largest Perimeter Triangle (LC #976) -- Easy
# Input:  nums: List[int]
# Output: int (largest perimeter of valid triangle, 0 if none)
# Triangle valid iff sum of two smallest > largest.
#
# Example:
# #   [2,1,2]  -> 5
#   [1,2,1]  -> 0
#   [3,2,3,4] -> 10
#
#   Greedy insight: Sort desc. Check consecutive triplets. First valid = largest perimeter.

def largest_perimeter(nums):
    pass

run_tests(largest_perimeter, [
    (([2,1,2],),     5),
    (([1,2,1],),     0),
    (([3,2,3,4],),  10),
    (([3,6,2,3],),   8),
    (([1,1,1],),     3),
])
