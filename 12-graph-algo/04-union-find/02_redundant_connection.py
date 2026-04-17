import os, sys
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))
from test_runner import run_tests


# Redundant Connection (LC #684) -- Medium
# Input:  edges: List[[u,v]] (undirected, n nodes, n edges)
# Output: List[int] (the extra edge that forms a cycle, LAST such edge)
# Graph was a tree, one extra edge was added. Find that edge.
# If multiple, return the one that appears LAST in input.
#
# Example:
# #   [[1,2],[1,3],[2,3]]  -> [2,3]
#
#   Key: Union-Find. For each edge, if both already in same set, this edge creates a cycle.
#        Return the first such edge we find when iterating.

def find_redundant_connection(edges):
    pass

run_tests(find_redundant_connection, [
    (([[1,2],[1,3],[2,3]],),               [2,3]),
    (([[1,2],[2,3],[3,4],[1,4],[1,5]],),   [1,4]),
    (([[1,2],[1,3],[1,4],[3,4]],),         [3,4]),
])
