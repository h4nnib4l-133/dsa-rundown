import os, sys
_d = os.path.dirname(os.path.abspath(__file__))
while _d and not os.path.exists(os.path.join(_d, 'test_runner.py')):
    _d = os.path.dirname(_d)
sys.path.insert(0, _d)
from test_runner import run_tests


# Find Eventual Safe States (LC #802) -- Medium
# Input:  graph: List[List[int]] (adjacency list, directed)
# Output: List[int] (sorted list of 'safe' nodes)
# A node is 'safe' if every path starting from it leads to a terminal (no out-edges).
# If any path leads into a cycle, the node is unsafe.
#
# Example:
# #   [[1,2],[2,3],[5],[0],[5],[],[]]  -> [2,4,5,6]
#
#   Key: DFS with 3 colors. Node is safe iff DFS never enters a gray node.
#        Alternative: reverse graph + topological sort (Kahn's on reversed).

def eventual_safe_nodes(graph):
    pass

run_tests(eventual_safe_nodes, [
    (([[1,2],[2,3],[5],[0],[5],[],[]],),    [2,4,5,6]),
    (([[1,2,3,4],[1,2],[3,4],[0,4],[]],),   [4]),
    (([[]],),                                [0]),
    (([[0]],),                               []),     # self-loop, unsafe
])
