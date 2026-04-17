import os, sys
_d = os.path.dirname(os.path.abspath(__file__))
while _d and not os.path.exists(os.path.join(_d, 'test_runner.py')):
    _d = os.path.dirname(_d)
sys.path.insert(0, _d)
from test_runner import run_tests


# Count Substrings Differing By One Char (LC #1638) -- Medium
# Input:  s: str, t: str
# Output: int (number of (sub_s, sub_t) pairs differing by EXACTLY one char)
# Count pairs of equal-length substrings (from s and t) with exactly one mismatch.
#
# Example:
# #   s="aba", t="baba"  -> 6
#
#   WHY THIS IS A DP ON SUBSTRING PAIRS:
#   For each (i,j) pair, count subproblems: 'extending left, how many with 0 mismatches'
#   and 'how many with 1 mismatch'. Key insight: one-mismatch pairs = (consecutive matches left) * 1.
#
#   Key: For each (i,j) where s[i]!=t[j]: count matches to the left and right.
#        Contribution = (left_matches+1) * (right_matches+1).

def count_substrings(s, t):
    pass

run_tests(count_substrings, [
    (("aba", "baba"),    6),
    (("ab", "bb"),        3),
    (("a", "a"),          0),
    (("abe", "bbc"),      10),
])
