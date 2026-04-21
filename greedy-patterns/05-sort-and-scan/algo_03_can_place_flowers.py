import os, sys
_d = os.path.dirname(os.path.abspath(__file__))
while _d and not os.path.exists(os.path.join(_d, 'test_runner.py')):
    _d = os.path.dirname(_d)
sys.path.insert(0, _d)
from test_runner import run_tests


# Can Place Flowers (LC #605) -- Easy
# Input:  flowerbed: List[int], n: int (flowers to plant)
# Output: bool (can plant n without violating no-adjacent rule?)
# flowerbed[i]=1 if occupied. Place n flowers such that none are adjacent.
#
# Example:
# #   [1,0,0,0,1], n=1  -> True   (plant at index 2)
#   [1,0,0,0,1], n=2  -> False
#
#   Greedy insight: Scan. If curr=0 and prev=0 and next=0, plant here, set curr=1.

def can_place_flowers(flowerbed, n):
    pass

run_tests(can_place_flowers, [
    (([1,0,0,0,1], 1),  True),
    (([1,0,0,0,1], 2),  False),
    (([0,0,1,0,0], 1),  True),
    (([0], 1),          True),
    (([1,0,0,0,0,1], 2), False),
])
