import os, sys
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))
from test_runner import run_tests


# Interleaving String (LC #97) -- Medium
# Input:  s1: str, s2: str, s3: str
# Output: bool (True if s3 is an interleaving of s1 and s2)
# s3 formed by interleaving chars of s1 and s2 preserving relative order.
#
# Example:
# #   s1="aabcc", s2="dbbca", s3="aadbbcbcac"  -> True
#   s1="aabcc", s2="dbbca", s3="aadbbbaccc" -> False
#
#   Key: dp[i][j] = can s3[0..i+j-1] be formed from s1[0..i-1] + s2[0..j-1].
#        dp[i][j] = (dp[i-1][j] and s1[i-1]==s3[i+j-1]) or (dp[i][j-1] and s2[j-1]==s3[i+j-1]).

def is_interleave(s1, s2, s3):
    pass

run_tests(is_interleave, [
    (("aabcc", "dbbca", "aadbbcbcac"),   True),
    (("aabcc", "dbbca", "aadbbbaccc"),    False),
    (("", "", ""),                        True),
    (("a", "", "a"),                      True),
    (("", "b", "b"),                      True),
    (("a", "b", "ab"),                    True),
    (("a", "b", "ba"),                    True),
])
