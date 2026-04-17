import os, sys
_d = os.path.dirname(os.path.abspath(__file__))
while _d and not os.path.exists(os.path.join(_d, 'test_runner.py')):
    _d = os.path.dirname(_d)
sys.path.insert(0, _d)
from test_runner import run_tests


# Generate Parentheses (LC #22) -- Medium
# Input:  n: int (number of pairs of parentheses)
# Output: List[str] (all valid combinations)
# Generate all valid combinations of n pairs of parentheses.
#
#   Key: Track open/close count. Can add `(` if open < n. Can add `)` if close < open.

def generate_parenthesis(n):
    pass


def solve(n):
    return sorted(generate_parenthesis(n))


run_tests(solve, [
    ((3,), ["((()))","(()())","(())()","()(())","()()()"]),
    ((1,), ["()"]),
])
