import sys, os; sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from test_runner import run_tests


# Combination Sum (LC #39) -- Medium
# Find combinations that sum to target. Can reuse elements.
#
#   Key: Backtrack with start index. Include current element (don't advance index) or skip (advance).

def combination_sum(candidates, target):
    pass


def solve(candidates, target):
    return sorted(combination_sum(candidates, target))


run_tests(solve, [
    (([2,3,6,7], 7), [[2,2,3],[7]]),
    (([2,3,5], 8),   [[2,2,2,2],[2,3,3],[3,5]]),
    (([2], 1),       []),
])
