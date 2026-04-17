import os, sys
_d = os.path.dirname(os.path.abspath(__file__))
while _d and not os.path.exists(os.path.join(_d, 'test_runner.py')):
    _d = os.path.dirname(_d)
sys.path.insert(0, _d)
from test_runner import run_tests



# Minimum Window Substring (LC #76) -- Hard
# Input:  s: str (haystack), t: str (chars to find, may have duplicates)
# Output: str (smallest window of s containing all chars of t, or "")
# Find smallest substring of s containing ALL characters of t (including duplicates).
# Return "" if no such window exists.
#
# Example:
#   s = "ADOBECODEBANC", t = "ABC"
#   -> "BANC"  (contains A, B, C in shortest window)
#
#   s = "a", t = "aa"
#   -> ""  (s doesn't have two 'a's)
#
#   Key: Sliding window with two frequency maps.
#        Expand right to include chars, shrink left to minimize window.
#        Track 'have' vs 'need' count for O(1) validity check.

def min_window(s, t):
    """Return min window substring of s containing all chars of t"""
    pass


run_tests(min_window, [
    (("ADOBECODEBANC", "ABC"), "BANC"),
    (("a", "a"),               "a"),
    (("a", "aa"),              ""),       # not enough chars
    (("a", "b"),               ""),       # char not in s
    (("abc", "abc"),           "abc"),    # whole string
    (("ab", "b"),              "b"),      # single char target
    (("cabwefgewcwaefgcf", "cae"), "cwae"),
    (("bba", "ab"),            "ba"),     # window at end
])
