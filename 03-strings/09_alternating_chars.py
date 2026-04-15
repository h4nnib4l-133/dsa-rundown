import sys, os; sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from test_runner import run_tests



# Alternating Characters (HackerRank) -- Easy
# Given a string of 'A' and 'B', count minimum deletions
# so that no two adjacent characters are the same.
#
# Example:
#   "AAAA"     -> 3  (delete 3 A's, keep "A")
#   "ABABABAB" -> 0  (already alternating)
#   "AAABBB"   -> 4  (keep "AB")
#
#   Key: Count consecutive duplicate pairs. Each pair = 1 deletion.

def alternating_characters(s):
    """Return min deletions so no two adjacent are same"""
    pass


run_tests(alternating_characters, [
    (("AAAA",),     3),
    (("BBBBB",),    4),
    (("ABABABAB",), 0),     # already alternating
    (("BABAB",),    0),     # already alternating
    (("AAABBB",),   4),     # keep "AB"
    (("A",),        0),     # single char
    (("AB",),       0),     # already alternating
    (("AA",),       1),     # one deletion
    (("AABB",),     2),     # "AB"
    (("ABBA",),     1),     # delete one B -> "ABA"
])
