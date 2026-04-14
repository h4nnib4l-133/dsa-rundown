import sys, os; sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from test_runner import run_tests


def partition(s):
    pass


def solve(s):
    return sorted(partition(s))


run_tests(solve, [
    (("aab",), [["a","a","b"],["aa","b"]]),
    (("a",),   [["a"]]),
])
