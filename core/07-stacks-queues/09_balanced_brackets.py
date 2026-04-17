import os, sys
_d = os.path.dirname(os.path.abspath(__file__))
while _d and not os.path.exists(os.path.join(_d, 'test_runner.py')):
    _d = os.path.dirname(_d)
sys.path.insert(0, _d)
from test_runner import run_tests


# Balanced Brackets (HackerRank) -- Medium
# Input:  s: str (only brackets: '(', ')', '{', '}', '[', ']')
# Output: bool (True if balanced)
# Like valid parentheses but specifically the HackerRank version.
#
#   Key: Same stack matching pattern. Handle edge cases: empty string, single bracket.

def is_balanced(s):
    pass


run_tests(is_balanced, [
    (("{[()]}",),  True),
    (("{[(])}",),  False),
    (("{{[[(())]]}}", ), True),
    (("",),        True),
    (("{",),       False),
])
