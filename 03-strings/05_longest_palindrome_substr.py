import sys, os; sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from test_runner import run_tests



# Longest Palindromic Substring (LC #5) -- Medium
# (Same as DP version -- can solve with expand-around-center here)
#
# Example:
#   "babad" -> "bab" or "aba"
#   "cbbd"  -> "bb"
#
#   Key: For each index, expand outward while chars match.
#        Check both odd (single center) and even (two center) palindromes.

def longest_palindrome(s):
    pass


def validate(s):
    r = longest_palindrome(s)
    return r is not None and r == r[::-1] and r in s


run_tests(validate, [
    (("babad",),     True),
    (("cbbd",),      True),
    (("a",),         True),
    (("racecar",),   True),
    (("abacab",),    True),     # "bacab" or "abacaba"? "bacab" len 5
    (("aaaa",),      True),     # whole string
    (("ab",),        True),     # "a" or "b"
])
