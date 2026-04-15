import sys, os; sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from test_runner import run_tests


# Balanced Brackets (HackerRank) -- Medium
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
