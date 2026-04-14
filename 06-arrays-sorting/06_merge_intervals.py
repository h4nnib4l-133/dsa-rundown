import sys, os; sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from test_runner import run_tests


def merge(intervals):
    pass


run_tests(merge, [
    (([[1,3],[2,6],[8,10],[15,18]],), [[1,6],[8,10],[15,18]]),
    (([[1,4],[4,5]],),                 [[1,5]]),
    (([[1,4],[0,4]],),                 [[0,4]]),
])
