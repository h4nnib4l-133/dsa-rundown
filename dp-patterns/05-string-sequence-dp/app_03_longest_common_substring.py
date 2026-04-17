import os, sys
_d = os.path.dirname(os.path.abspath(__file__))
while _d and not os.path.exists(os.path.join(_d, 'test_runner.py')):
    _d = os.path.dirname(_d)
sys.path.insert(0, _d)
from test_runner import run_tests


# Longest Common Substring (contiguous) -- Medium
# Input:  s1: str, s2: str
# Output: int (length of longest CONTIGUOUS common substring)
# Different from LCS: must be contiguous.
#
# Example:
# #   "abcdef", "zbcdy" -> 3   ("bcd")
#   "abc", "def"      -> 0
#
#   Pattern: STRING DP (contiguous variant)
#   Key: dp[i][j] = length of common substring ENDING at s1[i-1], s2[j-1].
#        If s1[i-1]==s2[j-1]: dp[i][j] = dp[i-1][j-1] + 1. Else 0.
#        Track global max.

def longest_common_substring(s1, s2):
    pass

run_tests(longest_common_substring, [
    (("abcdef", "zbcdy"),  3),
    (("abc", "def"),       0),
    (("abc", "abc"),       3),
    (("", "abc"),          0),
    (("xabyzc", "pxyzq"),  2),     # "yz"? wait p_x_yzq -> xyz present. "xy"... wait s1 has "aby" s2 has "xyz". Intersection: just "y"/"z" single. Actually: s1=xabyzc, has yzc, s2=pxyzq has xyz. Common: "yz" length 2.
])
