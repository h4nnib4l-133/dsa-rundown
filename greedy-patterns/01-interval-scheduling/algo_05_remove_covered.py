import os, sys
_d = os.path.dirname(os.path.abspath(__file__))
while _d and not os.path.exists(os.path.join(_d, 'test_runner.py')):
    _d = os.path.dirname(_d)
sys.path.insert(0, _d)
from test_runner import run_tests


# Remove Covered Intervals (LC #1288) -- Medium
# Input:  intervals: List[[start, end]]
# Output: int (count after removing intervals covered by another)
# Remove [a,b] if [c,d] exists with c<=a and b<=d.
#
# Example:
# #   [[1,4],[3,6],[2,8]]  -> 2   ([3,6] covered by [2,8])
#
#   Greedy insight: Sort by start ascending, end descending (ties). Scan: keep interval if its end
#        exceeds the max end seen so far.

def remove_covered_intervals(intervals):
    pass

run_tests(remove_covered_intervals, [
    (([[1,4],[3,6],[2,8]],),    2),
    (([[1,4],[2,3]],),          1),
    (([[0,10],[5,12]],),        2),
    (([[3,10],[4,10],[5,11]],), 2),
    (([[1,2],[1,4],[3,4]],),    1),
])
