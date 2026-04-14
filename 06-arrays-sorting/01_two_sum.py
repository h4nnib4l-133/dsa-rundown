import sys, os; sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from test_runner import run_tests


def two_sum(nums, target):
    """Return indices of two numbers that add up to target"""
    pass


# Order doesn't matter, so sort result
def solve(nums, target):
    r = two_sum(nums, target)
    return sorted(r) if r else r


run_tests(solve, [
    (([2,7,11,15], 9),   [0, 1]),
    (([3,2,4], 6),       [1, 2]),
    (([3,3], 6),         [0, 1]),
])
