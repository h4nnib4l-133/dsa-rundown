import os, sys
_d = os.path.dirname(os.path.abspath(__file__))
while _d and not os.path.exists(os.path.join(_d, 'test_runner.py')):
    _d = os.path.dirname(_d)
sys.path.insert(0, _d)
from test_runner import run_tests


# Is Subsequence (LC #392) -- Easy
# Input:  s: str, t: str
# Output: bool (is s a subsequence of t?)
# Check if s can be formed by deleting chars from t (preserving order).
#
# Example:
# #   s="abc", t="ahbgdc" -> True
#   s="axc", t="ahbgdc" -> False
#
#   Greedy insight: Two pointers. Advance j (in t) always. Advance i (in s) when match.

def is_subsequence(s, t):
    pass

run_tests(is_subsequence, [
    (("abc", "ahbgdc"),    True),
    (("axc", "ahbgdc"),    False),
    (("", "abc"),          True),
    (("abc", ""),          False),
    (("abc", "abc"),       True),
])
