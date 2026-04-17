import os, sys
_d = os.path.dirname(os.path.abspath(__file__))
while _d and not os.path.exists(os.path.join(_d, 'test_runner.py')):
    _d = os.path.dirname(_d)
sys.path.insert(0, _d)
from test_runner import run_tests



# Merge Intervals (LC #56) -- Medium
# Input:  intervals: List[[start, end]] (may be unsorted)
# Output: List[[start, end]] (merged non-overlapping intervals)
# Given array of intervals [start, end], merge all overlapping intervals.
#
# Example:
#   [[1,3],[2,6],[8,10],[15,18]] -> [[1,6],[8,10],[15,18]]
#   [[1,4],[4,5]]                -> [[1,5]]  (touching = overlapping)
#
#   Key: Sort by start time. Iterate: if current overlaps previous,
#        extend end. Otherwise start new interval.

def merge(intervals):
    pass


run_tests(merge, [
    (([[1,3],[2,6],[8,10],[15,18]],),  [[1,6],[8,10],[15,18]]),
    (([[1,4],[4,5]],),                  [[1,5]]),
    (([[1,4],[0,4]],),                  [[0,4]]),     # unsorted input
    (([[1,4],[2,3]],),                  [[1,4]]),     # one inside another
    (([[1,4]],),                        [[1,4]]),     # single interval
    (([[1,4],[0,0]],),                  [[0,0],[1,4]]),  # non-overlapping
    (([[1,10],[2,3],[4,5],[6,7]],),     [[1,10]]),    # one big swallows all
])
