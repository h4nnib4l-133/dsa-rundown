import os, sys
_d = os.path.dirname(os.path.abspath(__file__))
while _d and not os.path.exists(os.path.join(_d, 'test_runner.py')):
    _d = os.path.dirname(_d)
sys.path.insert(0, _d)
from test_runner import run_tests


# Wiggle Sort (LC #280) -- Medium
# Input:  nums: List[int]
# Output: None (modify in-place so nums[0] <= nums[1] >= nums[2] <= ...)
# Arrange so adjacent satisfy alternating <= and >=.
#
# Example:
# #   [3,5,2,1,6,4] -> [1,6,2,5,3,4] (or other valid)
#
#   Greedy insight: O(n): for each i, if (i even and nums[i]>nums[i+1]) or (i odd and nums[i]<nums[i+1]),
#        swap nums[i] and nums[i+1]. Greedy maintains invariant.

def wiggle_sort(nums):
    pass


def solve(nums):
    wiggle_sort(nums)
    # validate
    for i in range(len(nums)-1):
        if i % 2 == 0:
            if nums[i] > nums[i+1]:
                return False
        else:
            if nums[i] < nums[i+1]:
                return False
    return True

run_tests(solve, [
    (([3,5,2,1,6,4],),   True),
    (([1,1,1,1],),        True),
    (([1],),              True),
    (([1,2],),            True),
    (([2,1],),            True),     # after: [1,2]
    (([6,5,4,3,2,1],),    True),
])
