import os, sys
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))
from test_runner import run_tests


# Redundant Connection II (LC #685) -- Hard
# Input:  edges: List[[u,v]] (directed, was a rooted tree + 1 extra edge)
# Output: List[int] (the redundant edge to remove)
# Directed version. Extra edge causes either:
#   (a) A node with two parents (indegree 2), or
#   (b) A cycle, or
#   (c) Both (node with two parents AND a cycle).
#
# Much harder than undirected version.
#
# Example:
# #   [[1,2],[1,3],[2,3]]         -> [2,3]   (node 3 has two parents)
#   [[1,2],[2,3],[3,4],[4,1],[1,5]]  -> [4,1]   (cycle)
#
#   Key: 1. Find node with indegree 2 (if any). Mark the two candidate edges.
#        2. Try Union-Find EXCLUDING the later candidate.
#           - If no cycle, that candidate was the bad one.
#           - If cycle, the other candidate is bad.
#        3. If no indegree-2 node, just return the cycle-forming edge via Union-Find.

def find_redundant_directed_connection(edges):
    pass

run_tests(find_redundant_directed_connection, [
    (([[1,2],[1,3],[2,3]],),               [2,3]),
    (([[1,2],[2,3],[3,4],[4,1],[1,5]],),   [4,1]),
    (([[2,1],[3,1],[4,2],[1,4]],),         [2,1]),
])
