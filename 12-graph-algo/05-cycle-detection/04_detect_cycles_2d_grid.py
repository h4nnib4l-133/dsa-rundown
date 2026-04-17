import os, sys
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))
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
