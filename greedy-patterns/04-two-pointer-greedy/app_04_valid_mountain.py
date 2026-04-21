import os, sys
_d = os.path.dirname(os.path.abspath(__file__))
while _d and not os.path.exists(os.path.join(_d, 'test_runner.py')):
    _d = os.path.dirname(_d)
sys.path.insert(0, _d)
from test_runner import run_tests


# Valid Mountain Array (LC #941) -- Easy
# Input:  arr: List[int]
# Output: bool (True if mountain: strictly up then strictly down)
# Mountain: goes strictly up, hits a peak, then strictly down. Length >= 3.
#
# Example:
# #   [0,3,2,1]   -> True
#   [2,1]       -> False (no up phase)
#   [0,3,2,1,2] -> False
#
#   Greedy insight: Walk up from left. Walk down from right. Must meet at same index, not 0 or n-1.

def valid_mountain_array(arr):
    pass

run_tests(valid_mountain_array, [
    (([0,3,2,1],),       True),
    (([2,1],),            False),
    (([0,3,2,1,2],),      False),
    (([3,5,5],),          False),
    (([0,3,2,1,0],),      True),
    (([1,2,3,4,5],),      False),
])
