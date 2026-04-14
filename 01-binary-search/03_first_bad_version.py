import sys, os; sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from test_runner import run_tests


# The API isBadVersion is predefined -- we simulate it here
def make_checker(bad):
    def isBadVersion(v):
        return v >= bad
    return isBadVersion


def first_bad_version(n, isBadVersion):
    pass


# Wrapper for testing
def solve(n, bad):
    return first_bad_version(n, make_checker(bad))


run_tests(solve, [
    ((5, 4),  4),
    ((5, 1),  1),
    ((1, 1),  1),
    ((10, 7), 7),
    ((100, 50), 50),
])
