import os, sys
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))
from test_runner import run_tests


# Wildcard Matching (LC #44) -- Hard
# Input:  s: str, p: str (pattern with '?' and '*')
# Output: bool (True if pattern matches entire string)
# '?' matches any single char. '*' matches any sequence (including empty).
# Different from regex '*' which modifies the PREVIOUS char.
#
# Example:
# #   s="aa", p="*"     -> True
#   s="cb", p="?a"    -> False
#   s="adceb", p="*a*b"  -> True
#
#   Key: dp[i][j] = does s[0..i] match p[0..j]?
#        p[j]='*': dp[i][j] = dp[i-1][j] (* absorbs char) or dp[i][j-1] (* is empty).
#        p[j]='?' or s[i]==p[j]: dp[i][j] = dp[i-1][j-1].

def is_match_wildcard(s, p):
    pass

run_tests(is_match_wildcard, [
    (("aa", "*"),        True),
    (("cb", "?a"),       False),
    (("adceb", "*a*b"),  True),
    (("acdcb", "a*c?b"), False),
    (("", ""),           True),
    (("", "*"),          True),
    (("a", ""),          False),
])
