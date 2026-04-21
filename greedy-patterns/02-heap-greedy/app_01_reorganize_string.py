import os, sys
_d = os.path.dirname(os.path.abspath(__file__))
while _d and not os.path.exists(os.path.join(_d, 'test_runner.py')):
    _d = os.path.dirname(_d)
sys.path.insert(0, _d)
from test_runner import run_tests


# Reorganize String (LC #767) -- Medium
# Input:  s: str
# Output: str (rearranged so no two adjacent chars are same, or '' if impossible)
# Rearrange chars so no two adjacent match. Empty string if impossible.
#
# Example:
# #   "aab" -> "aba"
#   "aaab" -> "" (impossible)
#
#   Greedy insight: Max-heap of (count, char). Pop two most frequent, append both, push back if count > 0.
#        Ensures no two adjacent same char.

def reorganize_string(s):
    pass


def solve(s):
    result = reorganize_string(s)
    if not result:
        return result
    # validate: no two adjacent same, same letter counts
    from collections import Counter
    if Counter(s) != Counter(result):
        return "INVALID_COUNT"
    for i in range(1, len(result)):
        if result[i] == result[i-1]:
            return "ADJACENT_MATCH"
    return "OK"


# override to just return OK/empty for simpler testing

run_tests(reorganize_string, [
    (("aab",),     "OK"),
    (("aaab",),    ""),
    (("a",),       "OK"),
    (("aa",),      ""),
    (("aabb",),    "OK"),
])
