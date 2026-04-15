import sys, os; sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from test_runner import run_tests



# 3Sum (LC #15) -- Medium
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
