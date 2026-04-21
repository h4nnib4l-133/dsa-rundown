import os, sys
_d = os.path.dirname(os.path.abspath(__file__))
while _d and not os.path.exists(os.path.join(_d, 'test_runner.py')):
    _d = os.path.dirname(_d)
sys.path.insert(0, _d)
from test_runner import run_tests


# Insert Interval (LC #57) -- Medium
# Input:  intervals: List[[start, end]] (non-overlapping, sorted), newInterval: [start, end]
# Output: List[[start, end]] (merged result)
# Insert newInterval, merging with overlaps.
#
# Example:
# #   [[1,3],[6,9]], [2,5] -> [[1,5],[6,9]]
#   [[1,2],[3,5],[6,7],[8,10],[12,16]], [4,8] -> [[1,2],[3,10],[12,16]]
#
#   Greedy insight: Three phases: intervals ending before new (pass through), merge overlapping,
#        pass through remaining.

def insert_interval(intervals, new_interval):
    pass

run_tests(insert_interval, [
    (([[1,3],[6,9]], [2,5]),  [[1,5],[6,9]]),
    (([[1,2],[3,5],[6,7],[8,10],[12,16]], [4,8]), [[1,2],[3,10],[12,16]]),
    (([], [5,7]),              [[5,7]]),
    (([[1,5]], [2,3]),         [[1,5]]),
    (([[1,5]], [6,8]),         [[1,5],[6,8]]),
])
