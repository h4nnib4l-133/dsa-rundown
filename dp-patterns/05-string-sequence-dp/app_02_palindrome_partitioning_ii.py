import os, sys
_d = os.path.dirname(os.path.abspath(__file__))
while _d and not os.path.exists(os.path.join(_d, 'test_runner.py')):
    _d = os.path.dirname(_d)
sys.path.insert(0, _d)
from test_runner import run_tests


# Palindrome Partitioning II (LC #132) -- Hard
# Input:  s: str
# Output: int (MIN cuts to partition s into palindromes)
# Return min cuts (not all possible partitions).
#
# Example:
# #   "aab" -> 1   ("aa" | "b")
#   "ab"  -> 1
#   "abba" -> 0   (whole string)
#
#   Pattern: STRING DP
#   Key: Precompute is_pal[i][j] (is s[i..j] palindrome).
#        dp[i] = min cuts for s[0..i]. dp[i] = min(dp[j-1]+1) for is_pal[j..i].

def min_cut(s):
    pass

run_tests(min_cut, [
    (("aab",),      1),
    (("ab",),       1),
    (("abba",),     0),
    (("a",),        0),
    (("abcba",),    0),
])
