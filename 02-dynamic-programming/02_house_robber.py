import sys, os; sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from test_runner import run_tests


def rob(nums):
    pass


run_tests(rob, [
    (([1,2,3,1],),       4),
    (([2,7,9,3,1],),    12),
    (([2,1,1,2],),       4),
    (([0],),             0),
    (([100],),         100),
])
