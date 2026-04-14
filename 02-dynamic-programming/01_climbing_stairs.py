import sys, os; sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from test_runner import run_tests


def climb_stairs(n):
    pass


run_tests(climb_stairs, [
    ((2,), 2),
    ((3,), 3),
    ((1,), 1),
    ((5,), 8),
    ((10,), 89),
])
