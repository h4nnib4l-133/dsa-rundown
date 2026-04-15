import sys, os; sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from test_runner import run_tests


# Permutations (LC #46) -- Medium
# Generate all permutations of distinct integers.
#
#   Key: Backtrack with used[] array. Or swap-based approach.

def permute(nums):
    pass


def solve(nums):
    return sorted(permute(nums))


run_tests(solve, [
    (([1,2,3],), [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]),
    (([1],),     [[1]]),
])
