import sys, os; sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from test_runner import run_tests


def erase_overlap_intervals(intervals):
    """Return min intervals to remove"""
    pass


run_tests(erase_overlap_intervals, [
    (([[1,2],[2,3],[3,4],[1,3]],), 1),
    (([[1,2],[1,2],[1,2]],),       2),
    (([[1,2],[2,3]],),             0),
])
