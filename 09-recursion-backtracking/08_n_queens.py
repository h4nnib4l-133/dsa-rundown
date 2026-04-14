import sys, os; sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from test_runner import run_tests


def solve_n_queens(n):
    """Return number of solutions"""
    pass


run_tests(solve_n_queens, [
    ((4,), 2),
    ((1,), 1),
    ((8,), 92),
])
