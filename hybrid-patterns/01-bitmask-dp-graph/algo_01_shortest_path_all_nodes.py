import os, sys
_d = os.path.dirname(os.path.abspath(__file__))
while _d and not os.path.exists(os.path.join(_d, 'test_runner.py')):
    _d = os.path.dirname(_d)
sys.path.insert(0, _d)
from test_runner import run_tests


# Shortest Path Visiting All Nodes (LC #847) -- Hard
# Input:  graph: List[List[int]] (adjacency list, n <= 12)
# Output: int (shortest path visiting every node, can revisit)
# Start anywhere. Visit every node. Can revisit edges and nodes.
#
# Example:
# #   graph=[[1,2,3],[0],[0],[0]]  -> 4   (e.g. 1->0->2->0->3)
#
#   Pattern: BITMASK DP + BFS
#   Key: State: (node, visited_mask). BFS from ALL start states (0, 1<<i) for each i.
#        Goal: any state with mask == (1<<n) - 1.

def shortest_path_length(graph):
    pass

run_tests(shortest_path_length, [
    (([[1,2,3],[0],[0],[0]],),  4),
    (([[1],[0,2,4],[1,3,4],[2],[1,2]],),  4),
    (([[1],[0]],),  1),
])
