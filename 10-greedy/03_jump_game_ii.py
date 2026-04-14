import sys, os; sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from test_runner import run_tests


def jump(nums):
    pass


run_tests(jump, [
    (([2,3,1,1,4],), 2),
    (([2,3,0,1,4],), 2),
    (([1],),         0),
])
