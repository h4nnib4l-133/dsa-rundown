import sys, os; sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from test_runner import run_tests


# Non-overlapping Intervals (LC #435) -- Medium
# Min intervals to remove to make rest non-overlapping.
#
#   Key: Sort by end time. Greedily keep intervals that don't overlap with last kept.
#   Equivalent to: Total intervals - max non-overlapping intervals (activity selection)

def erase_overlap_intervals(intervals):
    """Return min intervals to remove"""
    pass


run_tests(erase_overlap_intervals, [
    (([[1,2],[2,3],[3,4],[1,3]],), 1),
    (([[1,2],[1,2],[1,2]],),       2),
    (([[1,2],[2,3]],),             0),
])
