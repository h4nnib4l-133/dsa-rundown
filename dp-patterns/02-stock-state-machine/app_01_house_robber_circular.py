import os, sys
_d = os.path.dirname(os.path.abspath(__file__))
while _d and not os.path.exists(os.path.join(_d, 'test_runner.py')):
    _d = os.path.dirname(_d)
sys.path.insert(0, _d)
from test_runner import run_tests


# House Robber II (Circular) (LC #213) -- Medium
# Input:  nums: List[int] (houses arranged in a CIRCLE)
# Output: int (max money without robbing adjacent)
# Houses in a circle means first and last are ALSO adjacent.
#
# Trick: run House Robber twice:
#   - On nums[0..n-2] (exclude last)
#   - On nums[1..n-1] (exclude first)
# Return max of the two.
#
# Example:
# #   [2,3,2]   -> 3   (can't rob both 2s)
#   [1,2,3,1] -> 4
#   [1,2,3]   -> 3
#
#   WHY THIS IS A STATE MACHINE DP (with endpoints twist):
#   Circular constraint means one of the ends must be excluded.
#   Solving both versions and taking max handles it cleanly.
#
#   Key: def rob_linear(arr): classic House Robber.
#        return max(rob_linear(nums[:-1]), rob_linear(nums[1:])).

def rob(nums):
    pass

run_tests(rob, [
    (([2,3,2],),        3),
    (([1,2,3,1],),      4),
    (([1,2,3],),        3),
    (([0],),            0),
    (([100],),        100),
    (([1,2],),          2),
])
