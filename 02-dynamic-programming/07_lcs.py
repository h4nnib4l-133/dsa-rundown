import sys, os; sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from test_runner import run_tests


# Longest Common Subsequence (LC #1143) -- Medium
# LCS of two strings.
#
#   State: `dp[i][j]` = LCS of s1[0..i], s2[0..j]
#   Transition: Match: `dp[i-1][j-1] + 1`. No match: `max(dp[i-1][j], dp[i][j-1])`

def longest_common_subseq(text1, text2):
    pass


run_tests(longest_common_subseq, [
    (("abcde", "ace"),   3),
    (("abc", "abc"),     3),
    (("abc", "def"),     0),
    (("", "abc"),        0),
    (("bsbininm", "jmjkbkjkv"), 1),
])
