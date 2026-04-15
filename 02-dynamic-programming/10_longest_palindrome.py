import sys, os; sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from test_runner import run_tests



# Longest Palindromic Substring (LC #5) -- Medium
# Input:  s: str (1 <= len(s) <= 1000)
# Output: str (longest palindromic substring)
# Find the longest substring that is a palindrome.
#
# Example:
#   "babad" -> "bab" or "aba"  (both valid, length 3)
#   "cbbd"  -> "bb"  (length 2)
#   "a"     -> "a"
#   "racecar" -> "racecar"  (whole string)
#
#   Key: Expand around center for each index.
#        Try both odd length (single center) and even length (double center).
#        O(n^2) time, O(1) space.

def longest_palindrome(s):
    """Return the longest palindromic substring"""
    pass


# Multiple valid answers possible, so check length and palindrome property
def validate(s):
    result = longest_palindrome(s)
    if result is None:
        return False
    return result == result[::-1]


# Multiple valid answers possible, so we check length and palindrome property
def validate(s):
    result = longest_palindrome(s)
    if result is None:
        return False
    return result == result[::-1] and result in s


run_tests(validate, [
    (("babad",),      True),     # "bab" or "aba"
    (("cbbd",),       True),     # "bb"
    (("a",),          True),     # single char
    (("racecar",),    True),     # whole string
    (("ac",),         True),     # "a" or "c"
    (("aacabdkacaa",),True),     # "aca" somewhere
    (("aaaa",),       True),     # all same
    (("abcba",),      True),     # whole string is palindrome
])
