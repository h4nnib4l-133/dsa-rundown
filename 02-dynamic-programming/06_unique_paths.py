import sys, os; sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from test_runner import run_tests


def unique_paths(m, n):
    pass


run_tests(unique_paths, [
    ((3, 7), 28),
    ((3, 2), 3),
    ((1, 1), 1),
    ((7, 3), 28),
    ((3, 3), 6),
])
