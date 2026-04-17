import os, sys
_d = os.path.dirname(os.path.abspath(__file__))
while _d and not os.path.exists(os.path.join(_d, 'test_runner.py')):
    _d = os.path.dirname(_d)
sys.path.insert(0, _d)
from test_runner import run_tests


# Maximum Product Subarray (LC #152) -- Medium
# Input:  nums: List[int] (may contain negatives and zeros)
# Output: int (max product of any contiguous subarray)
# Like Kadane, but products flip sign with negatives.
# Track both max AND min at each step -- negative * min could become max.
#
# Example:
# #   [2,3,-2,4]      -> 6   ([2,3])
#   [-2,0,-1]       -> 0   (zero breaks product chains)
#   [-2,3,-4]       -> 24  ([-2,3,-4]=24, two negatives cancel)
#
#   Key: At each i, compute new_max = max(nums[i], max*nums[i], min*nums[i]).
#        Same for new_min. Track global max.

def max_product(nums):
    pass

run_tests(max_product, [
    (([2,3,-2,4],),    6),
    (([-2,0,-1],),     0),
    (([-2,3,-4],),    24),
    (([0,2],),         2),
    (([-2],),         -2),     # single negative
    (([-4,-3,-2],),   12),     # adjacent negatives
    (([2,-5,-2,-4,3],), 24),
])
