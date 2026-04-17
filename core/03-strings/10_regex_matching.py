import os, sys
_d = os.path.dirname(os.path.abspath(__file__))
while _d and not os.path.exists(os.path.join(_d, 'test_runner.py')):
    _d = os.path.dirname(_d)
sys.path.insert(0, _d)
from test_runner import run_tests



# Regular Expression Matching (LC #10) -- Hard
# Input:  s: str (lowercase a-z), p: str (lowercase a-z, '.', '*')
# Output: bool (True if p matches entire string s)
# Implement regex matching with '.' and '*'.
#   '.' matches any single character.
#   '*' matches zero or more of the PRECEDING element.
#
# Example:
#   s="aa",  p="a"    -> False  (single 'a' doesn't match "aa")
#   s="aa",  p="a*"   -> True   ('a*' = zero or more 'a')
#   s="ab",  p=".*"   -> True   ('.*' = zero or more of any char)
#   s="aab", p="c*a*b" -> True  (c*=empty, a*="aa", b="b")
#
#   Key: DP. dp[i][j] = does s[0:i] match p[0:j]?
#        If p[j-1]=='*': dp[i][j] = dp[i][j-2] (zero match)
#                        OR dp[i-1][j] if p[j-2] matches s[i-1].

def is_match(s, p):
    """'.' matches any char, '*' matches zero or more of preceding"""
    pass


run_tests(is_match, [
    (("aa", "a"),        False),
    (("aa", "a*"),       True),
    (("ab", ".*"),       True),
    (("aab", "c*a*b"),   True),     # c*=empty, a*=aa, b=b
    (("mississippi", "mis*is*p*."), False),
    (("", ""),           True),     # both empty
    (("", "a*"),         True),     # a* can match zero
    (("a", ""),          False),    # pattern empty, string not
    (("aaa", "a*a"),     True),     # a*=aa, a=a
    (("ab", ".*c"),      False),    # .* matches "a" but c != b
])
