import sys, os; sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from test_runner import run_tests


def subsets_with_dup(nums):
    pass


def solve(nums):
    return sorted([sorted(s) for s in subsets_with_dup(nums)])


run_tests(solve, [
    (([1,2,2],), [[],[1],[1,2],[1,2,2],[2],[2,2]]),
    (([0],),     [[],[0]]),
])
