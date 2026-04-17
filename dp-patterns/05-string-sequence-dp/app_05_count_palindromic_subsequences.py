import os, sys
_d = os.path.dirname(os.path.abspath(__file__))
while _d and not os.path.exists(os.path.join(_d, 'test_runner.py')):
    _d = os.path.dirname(_d)
sys.path.insert(0, _d)
from test_runner import run_tests


# Count Different Palindromic Subsequences (LC #730) -- Hard
# Input:  s: str (chars 'a','b','c','d')
# Output: int (count of DISTINCT palindromic subsequences, mod 10^9+7)
# Count distinct palindromic subsequences (not substrings).
#
# Example:
# #   "bccb" -> 6   ("b","c","bb","cc","bcb","bccb")
#   "abcdabcdabcdabcdabcdabcdabcdabcddcbadcbadcbadcbadcbadcbadcbadcba" -> 104860361
#
#   Pattern: INTERVAL DP
#   Key: dp[i][j] = count on s[i..j]. Classic interval DP, handle 4 cases for s[i]==s[j]:
#        chars between exist, all equal to s[i], or none.

def count_palindromic_subsequences(s):
    pass

run_tests(count_palindromic_subsequences, [
    (("bccb",),    6),
    (("a",),       1),
    (("aa",),      2),     # "a", "aa"
    (("abc",),     3),     # "a","b","c"
    (("aba",),     4),     
])
