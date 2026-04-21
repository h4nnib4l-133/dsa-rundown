import os, sys
_d = os.path.dirname(os.path.abspath(__file__))
while _d and not os.path.exists(os.path.join(_d, 'test_runner.py')):
    _d = os.path.dirname(_d)
sys.path.insert(0, _d)
from test_runner import run_tests


# Reduce Array Size to Half (LC #1338) -- Medium
# Input:  arr: List[int]
# Output: int (min number of DISTINCT values to remove to shrink arr by >= half)
# Pick a set of integers, remove all occurrences. Minimize distinct count.
#
# Example:
# #   [3,3,3,3,5,5,5,2,2,7] -> 2   (remove 3 and 5: removes 7 elements, array shrinks 70%)
#
#   Greedy insight: Count frequencies. Sort desc. Pick largest counts until sum >= n/2.

def min_set_size(arr):
    pass

run_tests(min_set_size, [
    (([3,3,3,3,5,5,5,2,2,7],),          2),
    (([7,7,7,7,7,7],),                    1),
    (([1,9],),                            1),
    (([1000,1000,3,7],),                  1),
])
