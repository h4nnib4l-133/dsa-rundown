import os, sys
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))
from test_runner import run_tests


# Longest Palindromic Subsequence (LC #516) -- Medium
# Input:  s: str
# Output: int (length of longest palindromic subsequence)
# Subsequence, not substring. Not necessarily contiguous.
#
# Trick: This equals LCS(s, reverse(s)).
#
# Example:
# #   "bbbab" -> 4   ("bbbb")
#   "cbbd"  -> 2   ("bb")
#
#   Key: dp[i][j] = length of LPS in s[i..j].
#        Match: dp[i+1][j-1] + 2. No match: max(dp[i+1][j], dp[i][j-1]).

def longest_palindrome_subseq(s):
    pass

run_tests(longest_palindrome_subseq, [
    (("bbbab",), 4),
    (("cbbd",),  2),
    (("a",),     1),
    (("aa",),    2),
    (("ab",),    1),
    (("abcba",), 5),
])
