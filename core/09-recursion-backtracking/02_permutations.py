import os, sys
_d = os.path.dirname(os.path.abspath(__file__))
while _d and not os.path.exists(os.path.join(_d, 'test_runner.py')):
    _d = os.path.dirname(_d)
sys.path.insert(0, _d)
from test_runner import run_tests



# Permutations (LC #46) -- Medium
# Input:  nums: List[int] (distinct integers)
# Output: List[List[int]] (all possible permutations)
# Given array of DISTINCT integers, return all possible permutations.
#
# Example:
#   [1,2,3] -> [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
#   [1]     -> [[1]]
#
#   Key: Backtrack with used[] boolean array.
#        Or swap-based: swap current index with each remaining.

def permute(nums):
    pass


def solve(nums):
    return sorted(permute(nums))


run_tests(solve, [
    (([1,2,3],), [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]),
    (([1],),     [[1]]),
    (([0,1],),   [[0,1],[1,0]]),
])
