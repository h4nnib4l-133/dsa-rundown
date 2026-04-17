import os, sys
_d = os.path.dirname(os.path.abspath(__file__))
while _d and not os.path.exists(os.path.join(_d, 'test_runner.py')):
    _d = os.path.dirname(_d)
sys.path.insert(0, _d)
from test_runner import run_tests



# Sort Colors / Dutch National Flag (LC #75) -- Medium
# Input:  nums: List[int] (only values 0, 1, 2; modify in-place)
# Output: None (array sorted in-place) [we return nums for testing]
# Array of 0s, 1s, 2s. Sort in-place in one pass.
#
# Example:
#   [2,0,2,1,1,0] -> [0,0,1,1,2,2]
#   [2,0,1]        -> [0,1,2]
#
#   Key: Three pointers: lo (0s boundary), mid (current), hi (2s boundary).
#        If nums[mid]==0: swap with lo, advance both.
#        If nums[mid]==1: advance mid.
#        If nums[mid]==2: swap with hi, shrink hi (don't advance mid).

def sort_colors(nums):
    """Sort in-place. Return nums for testing."""
    pass
    return nums


run_tests(sort_colors, [
    (([2,0,2,1,1,0],),  [0,0,1,1,2,2]),
    (([2,0,1],),         [0,1,2]),
    (([0],),             [0]),               # single element
    (([1,0],),           [0,1]),
    (([0,0,0],),         [0,0,0]),           # all same
    (([2,2,1,1,0,0],),  [0,0,1,1,2,2]),     # reverse sorted
    (([0,1,2],),         [0,1,2]),           # already sorted
    (([2,1,0],),         [0,1,2]),           # reverse
])
