import os, sys
_d = os.path.dirname(os.path.abspath(__file__))
while _d and not os.path.exists(os.path.join(_d, 'test_runner.py')):
    _d = os.path.dirname(_d)
sys.path.insert(0, _d)
from test_runner import run_tests


# Detect Cycles in 2D Grid (LC #1559) -- Medium
# Input:  grid: List[List[str]] (chars)
# Output: bool (True if any cycle of length >= 4 with same char exists)
# Cycle: 4+ cells with SAME char forming a loop (4-directional).
#
# Trick: DFS with parent tracking (skip the cell you came from).
# Hitting visited cell means cycle.
#
# Example:
# #   [["a","a","a","a"],
#    ["a","b","b","a"],    -> True   (outer 'a' ring)
#    ["a","b","b","a"],
#    ["a","a","a","a"]]
#
#   Key: DFS. Pass parent (r_prev, c_prev). For each neighbor != parent with same char:
#        if already visited, cycle! Else recurse.

def contains_cycle(grid):
    pass

run_tests(contains_cycle, [
    (([["a","a","a","a"],["a","b","b","a"],["a","b","b","a"],["a","a","a","a"]],), True),
    (([["c","c","c","a"],["c","d","c","c"],["c","c","e","c"],["f","c","c","c"]],), True),
    (([["a","b","b"],["b","z","b"],["b","b","a"]],), False),
])
