import sys, os; sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from test_runner import run_tests


# Alternating Characters (HackerRank) -- Easy
# Count deletions to make no two adjacent characters the same.
#
#   Key: Count consecutive duplicates

def alternating_characters(s):
    """Return min deletions so no two adjacent are same"""
    pass


run_tests(alternating_characters, [
    (("AAAA",),   3),
    (("BBBBB",),  4),
    (("ABABABAB",),0),
    (("BABAB",),  0),
    (("AAABBB",), 4),
])
