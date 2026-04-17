import os, sys
_d = os.path.dirname(os.path.abspath(__file__))
while _d and not os.path.exists(os.path.join(_d, 'test_runner.py')):
    _d = os.path.dirname(_d)
sys.path.insert(0, _d)
from test_runner import run_tests



# Non-overlapping Intervals (LC #435) -- Medium
# Input:  intervals: List[[start, end]]
# Output: int (min intervals to remove so rest don't overlap)
# Given intervals, find MINIMUM number to REMOVE so rest don't overlap.
#
# Example:
#   [[1,2],[2,3],[3,4],[1,3]] -> 1  (remove [1,3])
#   [[1,2],[1,2],[1,2]]       -> 2  (keep one, remove two)
#   [[1,2],[2,3]]             -> 0  (touching is NOT overlapping)
#
#   Key: Sort by end time. Greedily keep intervals that don't overlap
#        with last kept interval. Count = total - kept.

def erase_overlap_intervals(intervals):
    """Return min intervals to remove"""
    pass


run_tests(erase_overlap_intervals, [
    (([[1,2],[2,3],[3,4],[1,3]],),  1),
    (([[1,2],[1,2],[1,2]],),        2),
    (([[1,2],[2,3]],),              0),     # no overlap (touching OK)
    (([[1,10],[2,3],[4,5],[6,7]],), 1),     # remove the big one
    (([[1,2]],),                    0),     # single interval
    (([[1,3],[2,4],[3,5]],),        1),     # chain overlap
])
