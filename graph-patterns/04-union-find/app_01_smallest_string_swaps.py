import os, sys
_d = os.path.dirname(os.path.abspath(__file__))
while _d and not os.path.exists(os.path.join(_d, 'test_runner.py')):
    _d = os.path.dirname(_d)
sys.path.insert(0, _d)
from test_runner import run_tests


# Smallest String With Swaps (LC #1202) -- Medium
# Input:  s: str, pairs: List[[i,j]] (swappable index pairs)
# Output: str (lexicographically smallest string after any number of swaps)
# You can swap characters at allowed index pairs any number of times.
# Return lexicographically smallest resulting string.
#
# Example:
# #   s="dcab", pairs=[[0,3],[1,2]]  -> "bacd"
#   s="dcab", pairs=[[0,3],[1,2],[0,2]]  -> "abcd" (all positions connected)
#
#   WHY THIS IS A UNION-FIND:
#   Pairs form groups of indices that are interchangeable (transitively).
#   Within each group, you can reorder chars freely. Sort chars within each group,
#   place them back at sorted indices.
#
#   Key: 1. Union-Find on pairs to find groups.
#        2. For each group: extract its chars, sort them, place back at group's sorted indices.

def smallest_string_with_swaps(s, pairs):
    pass

run_tests(smallest_string_with_swaps, [
    (("dcab", [[0,3],[1,2]]),                 "bacd"),
    (("dcab", [[0,3],[1,2],[0,2]]),           "abcd"),
    (("cba", [[0,1],[1,2]]),                  "abc"),
    (("a", []),                               "a"),
    (("abc", []),                             "abc"),
])
