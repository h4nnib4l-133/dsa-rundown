import os, sys
_d = os.path.dirname(os.path.abspath(__file__))
while _d and not os.path.exists(os.path.join(_d, 'test_runner.py')):
    _d = os.path.dirname(_d)
sys.path.insert(0, _d)
from test_runner import run_tests


# Meeting Rooms (LC #252) -- Easy
# Input:  intervals: List[[start, end]]
# Output: bool (can a person attend all meetings?)
# Given meeting times, can you attend all without conflict?
#
# Example:
# #   [[0,30],[5,10],[15,20]]  -> False   (overlap between 0-30 and 5-10)
#   [[7,10],[2,4]]           -> True
#
#   Greedy insight: Sort by start. Check if any meeting starts before previous ends.

def can_attend_meetings(intervals):
    pass

run_tests(can_attend_meetings, [
    (([[0,30],[5,10],[15,20]],), False),
    (([[7,10],[2,4]],),           True),
    (([],),                       True),
    (([[1,5]],),                  True),
    (([[1,5],[5,10]],),           True),     # touching, not overlapping
])
