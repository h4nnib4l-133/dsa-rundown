import os, sys
_d = os.path.dirname(os.path.abspath(__file__))
while _d and not os.path.exists(os.path.join(_d, 'test_runner.py')):
    _d = os.path.dirname(_d)
sys.path.insert(0, _d)
from test_runner import run_tests


# Combination Sum (LC #39) -- Medium
# Input:  candidates: List[int] (distinct, positive), target: int
# Output: List[List[int]] (all combos summing to target, can reuse elements)
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
