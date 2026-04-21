import os, sys
_d = os.path.dirname(os.path.abspath(__file__))
while _d and not os.path.exists(os.path.join(_d, 'test_runner.py')):
    _d = os.path.dirname(_d)
sys.path.insert(0, _d)
from test_runner import run_tests


# Largest Number (LC #179) -- Medium
# Input:  nums: List[int] (non-negative)
# Output: str (largest number formable by concatenating)
# Rearrange to form the largest possible number.
#
# Example:
# #   [10,2]     -> "210"
#   [3,30,34,5,9] -> "9534330"
#   [0,0]      -> zero as string
#
#   Greedy insight: Sort with custom comparator: a+b vs b+a (string concatenation).
#        If a+b > b+a, a should come first.

def largest_number(nums):
    pass

run_tests(largest_number, [
    (([10,2],),             "210"),
    (([3,30,34,5,9],),      "9534330"),
    (([0,0],),              "0"),
    (([1],),                "1"),
    (([1,2,3,4,5,6,7,8,9],), "987654321"),
])
