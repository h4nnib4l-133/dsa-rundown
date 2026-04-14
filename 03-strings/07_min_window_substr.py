import sys, os; sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from test_runner import run_tests


def min_window(s, t):
    """Return min window substring of s containing all chars of t"""
    pass


run_tests(min_window, [
    (("ADOBECODEBANC", "ABC"), "BANC"),
    (("a", "a"),               "a"),
    (("a", "aa"),              ""),
])
