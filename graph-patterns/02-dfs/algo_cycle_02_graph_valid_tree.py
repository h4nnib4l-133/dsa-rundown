import os, sys
_d = os.path.dirname(os.path.abspath(__file__))
while _d and not os.path.exists(os.path.join(_d, 'test_runner.py')):
    _d = os.path.dirname(_d)
sys.path.insert(0, _d)
from test_runner import run_tests


# Graph Valid Tree (LC #261) -- Medium
# Input:  n: int, edges: List[[u,v]] (undirected)
# Output: bool (True if graph is a valid tree: connected + no cycle)
# A tree has EXACTLY n-1 edges and is connected (i.e. 1 component).
#
# Two conditions: (1) no cycle (2) fully connected.
#
# Example:
# #   n=5, [[0,1],[0,2],[0,3],[1,4]]  -> True
#   n=5, [[0,1],[1,2],[2,3],[1,3],[1,4]]  -> False (cycle)
#
#   Key: Quick check: must have exactly n-1 edges.
#        Then Union-Find: if union finds same root, cycle.
#        At end, must have exactly 1 component.

def valid_tree(n, edges):
    pass

run_tests(valid_tree, [
    ((5, [[0,1],[0,2],[0,3],[1,4]]),              True),
    ((5, [[0,1],[1,2],[2,3],[1,3],[1,4]]),         False),
    ((4, [[0,1],[2,3]]),                            False),     # disconnected
    ((1, []),                                       True),
    ((3, [[0,1],[0,2]]),                            True),
])
