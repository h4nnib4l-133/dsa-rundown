import os, sys
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))
from test_runner import run_tests


# Distinct Subsequences (LC #115) -- Hard
# Input:  s: str, t: str
# Output: int (number of distinct subsequences of s that equal t)
# How many ways can t be formed as a subsequence of s?
#
# Example:
# #   s="rabbbit", t="rabbit" -> 3   (three ways to pick the 'bb')
#   s="babgbag", t="bag"    -> 5
#
#   Key: dp[i][j] = # ways s[0..i] forms t[0..j].
#        Always dp[i-1][j] (skip s[i]).
#        If s[i]==t[j], add dp[i-1][j-1] (use s[i]).

def num_distinct(s, t):
    pass

run_tests(num_distinct, [
    (("rabbbit", "rabbit"),  3),
    (("babgbag", "bag"),      5),
    (("a", "a"),              1),
    (("a", "b"),              0),
    (("", ""),                1),     # empty matches empty
])
