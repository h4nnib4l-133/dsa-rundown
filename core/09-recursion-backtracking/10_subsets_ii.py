import os, sys
_d = os.path.dirname(os.path.abspath(__file__))
while _d and not os.path.exists(os.path.join(_d, 'test_runner.py')):
    _d = os.path.dirname(_d)
sys.path.insert(0, _d)
from test_runner import run_tests


# Subsets II (LC #90) -- Medium
# Input:  nums: List[int] (may contain duplicates)
# Output: List[List[int]] (all unique subsets)
# Generate all subsets when array may contain duplicates.
#
#   Key: Sort first. Skip duplicate elements at same recursion level: `if i > start and nums[i] == nums[i-1]: continue`

def subsets_with_dup(nums):
    pass


def solve(nums):
    return sorted([sorted(s) for s in subsets_with_dup(nums)])


run_tests(solve, [
    (([1,2,2],), [[],[1],[1,2],[1,2,2],[2],[2,2]]),
    (([0],),     [[],[0]]),
])
