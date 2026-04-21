import os, sys
_d = os.path.dirname(os.path.abspath(__file__))
while _d and not os.path.exists(os.path.join(_d, 'test_runner.py')):
    _d = os.path.dirname(_d)
sys.path.insert(0, _d)
from test_runner import run_tests


# Furthest Building You Can Reach (LC #1642) -- Medium
# Input:  heights: List[int], bricks: int, ladders: int
# Output: int (furthest building index reachable)
# Climb from building i to i+1. Need bricks = diff if higher. Ladder = free any climb.
# Use ladders/bricks optimally.
#
# Example:
# #   heights=[4,2,7,6,9,14,12], bricks=5, ladders=1  -> 4
#
#   Greedy insight: Use ladders for BIGGEST climbs, bricks for smaller.
#        Min-heap of climbs (size = ladders). When heap full, smallest climb pays bricks.
#        Stop when bricks < 0.

def furthest_building(heights, bricks, ladders):
    pass

run_tests(furthest_building, [
    (([4,2,7,6,9,14,12], 5, 1),   4),
    (([4,12,2,7,3,18,20,3,19], 10, 2),  7),
    (([14,3,19,3], 17, 0),              3),
    (([1,5,1,2,3,4,10000], 4, 1),       5),
])
