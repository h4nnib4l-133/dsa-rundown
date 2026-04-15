import sys, os; sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from test_runner import run_tests


# Minimum Window Substring (LC #76) -- Hard
# Find smallest window in s containing all characters of t.
#
#   Key: Sliding window + two frequency maps. Expand right, shrink left.
#   Hint: Track `have` vs `need` count to know when window is valid

def min_window(s, t):
    """Return min window substring of s containing all chars of t"""
    pass


run_tests(min_window, [
    (("ADOBECODEBANC", "ABC"), "BANC"),
    (("a", "a"),               "a"),
    (("a", "aa"),              ""),
])
