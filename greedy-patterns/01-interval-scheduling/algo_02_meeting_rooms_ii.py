import os, sys
_d = os.path.dirname(os.path.abspath(__file__))
while _d and not os.path.exists(os.path.join(_d, 'test_runner.py')):
    _d = os.path.dirname(_d)
sys.path.insert(0, _d)
from test_runner import run_tests


# Meeting Rooms II (LC #253) -- Medium
# Input:  intervals: List[[start, end]]
# Output: int (min rooms needed to schedule all)
# Find minimum number of rooms needed.
#
# Example:
# #   [[0,30],[5,10],[15,20]]  -> 2
#   [[7,10],[2,4]]           -> 1
#
#   Greedy insight: Sort intervals by start. Use min-heap of end times.
#        For each interval, if heap top <= start, pop (room freed). Push current end.
#        Answer = final heap size.

def min_meeting_rooms(intervals):
    pass

run_tests(min_meeting_rooms, [
    (([[0,30],[5,10],[15,20]],),  2),
    (([[7,10],[2,4]],),            1),
    (([],),                        0),
    (([[1,5],[2,6],[3,7]],),       3),
    (([[1,2],[3,4],[5,6]],),       1),
])
