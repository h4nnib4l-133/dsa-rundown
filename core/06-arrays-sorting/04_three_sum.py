import os, sys
_d = os.path.dirname(os.path.abspath(__file__))
while _d and not os.path.exists(os.path.join(_d, 'test_runner.py')):
    _d = os.path.dirname(_d)
sys.path.insert(0, _d)
from test_runner import run_tests



# 3Sum (LC #15) -- Medium
# Input:  nums: List[int] (unsorted, may have duplicates)
# Output: List[List[int]] (all unique triplets summing to 0)
# Find all unique triplets [a,b,c] where a+b+c = 0.
# No duplicate triplets in result.
#
# Example:
#   [-1,0,1,2,-1,-4] -> [[-1,-1,2], [-1,0,1]]
#   [0,1,1]           -> []  (no triplet sums to 0)
#   [0,0,0]           -> [[0,0,0]]
#
#   Key: Sort array. Fix one element, two-pointer on rest.
#        Skip duplicates at all levels to avoid duplicate triplets.

def three_sum(nums):
    """Return all unique triplets that sum to 0"""
    pass


def solve(nums):
    result = three_sum(nums)
    return sorted([sorted(t) for t in result])


run_tests(solve, [
    (([-1,0,1,2,-1,-4],),   [[-1,-1,2],[-1,0,1]]),
    (([0,1,1],),             []),
    (([0,0,0],),             [[0,0,0]]),
    (([0,0,0,0],),           [[0,0,0]]),     # extra zeros
    (([-2,0,1,1,2],),        [[-2,0,2],[-2,1,1]]),
    (([1,-1,0],),            [[-1,0,1]]),
])
