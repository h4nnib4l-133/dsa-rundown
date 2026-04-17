import os, sys
_d = os.path.dirname(os.path.abspath(__file__))
while _d and not os.path.exists(os.path.join(_d, 'test_runner.py')):
    _d = os.path.dirname(_d)
sys.path.insert(0, _d)
from test_runner import run_tests


# Arithmetic Slices (LC #413) -- Medium
# Input:  nums: List[int]
# Output: int (count of arithmetic subarrays of length >= 3)
# Count contiguous subarrays where consecutive differences are equal.
#
# Example:
# #   [1,2,3,4] -> 3   ([1,2,3], [2,3,4], [1,2,3,4])
#   [1,2,3]   -> 1
#   [1,2]     -> 0
#
#   Pattern: KADANE-LIKE running count
#   Key: Track length of arithmetic run ending at i. If extends previous, add (run-1) to count.

def number_of_arithmetic_slices(nums):
    pass

run_tests(number_of_arithmetic_slices, [
    (([1,2,3,4],),        3),
    (([1,2,3],),          1),
    (([1,2],),            0),
    (([1,1,2,5,7],),      0),
    (([1,2,3,4,5,6,7],), 15),
    (([],),               0),
])
