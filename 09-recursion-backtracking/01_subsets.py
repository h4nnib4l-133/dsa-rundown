import sys, os; sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from test_runner import run_tests


def subsets(nums):
    pass


def solve(nums):
    return sorted([sorted(s) for s in subsets(nums)])


run_tests(solve, [
    (([1,2,3],), [[],[1],[1,2],[1,2,3],[1,3],[2],[2,3],[3]]),
    (([0],),     [[],[0]]),
])
