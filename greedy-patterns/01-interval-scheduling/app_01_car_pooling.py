import os, sys
_d = os.path.dirname(os.path.abspath(__file__))
while _d and not os.path.exists(os.path.join(_d, 'test_runner.py')):
    _d = os.path.dirname(_d)
sys.path.insert(0, _d)
from test_runner import run_tests


# Car Pooling (LC #1094) -- Medium
# Input:  trips: List[[passengers, from, to]], capacity: int
# Output: bool (can all trips be completed without exceeding capacity?)
# Each trip picks up passengers at 'from' and drops at 'to'.
# Like Meeting Rooms but with passenger counts.
#
# Example:
# #   trips=[[2,1,5],[3,3,7]], capacity=4  -> False   (5 passengers at t=3)
#   trips=[[2,1,5],[3,3,7]], capacity=5  -> True
#
#   Greedy insight: Sweep line: +passengers at from, -passengers at to. Sort events. Check running sum.

def car_pooling(trips, capacity):
    pass

run_tests(car_pooling, [
    (([[2,1,5],[3,3,7]], 4),   False),
    (([[2,1,5],[3,3,7]], 5),   True),
    (([[2,1,5],[3,5,7]], 3),   True),
    (([[3,2,7],[3,7,9],[8,3,9]], 11), True),
    (([[9,0,1],[3,3,7]], 4),   False),
])
