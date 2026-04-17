import os, sys
_d = os.path.dirname(os.path.abspath(__file__))
while _d and not os.path.exists(os.path.join(_d, 'test_runner.py')):
    _d = os.path.dirname(_d)
sys.path.insert(0, _d)
from test_runner import run_tests



# Longest Common Subsequence (LC #1143) -- Medium
# Input:  text1: str, text2: str
# Output: int (length of longest common subsequence)
# Given two strings, find the length of their longest common subsequence.
# Subsequence = chars in order but not necessarily contiguous.
#
# Example:
#   "abcde", "ace"  -> 3  (LCS = "ace")
#   "abc", "abc"    -> 3  (identical)
#   "abc", "def"    -> 0  (no common chars)
#
#   Key: dp[i][j] = LCS of text1[0:i], text2[0:j].
#        If chars match: dp[i-1][j-1] + 1.
#        Else: max(dp[i-1][j], dp[i][j-1]).

def longest_common_subseq(text1, text2):
    pass


run_tests(longest_common_subseq, [
    (("abcde", "ace"),     3),     # ace
    (("abc", "abc"),       3),     # identical
    (("abc", "def"),       0),     # nothing in common
    (("", "abc"),          0),     # empty string
    (("abc", ""),          0),     # other empty
    (("abcba", "abcbcba"), 5),     # abcba
    (("oxcpqrsvwf", "shmtulqrypy"), 2),  # qr
    (("a", "a"),           1),     # single char match
    (("a", "b"),           0),     # single char no match
])
