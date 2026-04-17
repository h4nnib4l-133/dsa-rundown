import os, sys
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))
from test_runner import run_tests


# Longest Path in DAG (custom) -- Medium
# Input:  n: int, edges: List[[u,v,w]] (weighted DAG), start: int
# Output: int (longest path from start, 0 if no outgoing)
# Longest weighted path from start in a DAG.
#
# Example:
# #   n=4, edges=[[0,1,2],[0,2,3],[1,3,1],[2,3,5]], start=0
#   -> 8   (0->2->3: weights 3+5)
#
#   WHY THIS IS A TOPOLOGICAL SORT + DP:
#   Can't use Dijkstra directly (would want min, not max). But in DAG,
#   topological order lets you DP: process nodes in order, relax outgoing edges
#   to update max distances.
#
#   Key: Topsort nodes. Init dist[start]=0, rest=-inf.
#        For each node in topo order: for edge (u,v,w):
#        dist[v] = max(dist[v], dist[u]+w).

def longest_path_dag(n, edges, start):
    pass

run_tests(longest_path_dag, [
    ((4, [[0,1,2],[0,2,3],[1,3,1],[2,3,5]], 0),  8),
    ((2, [[0,1,5]], 0),                            5),
    ((3, [[0,1,1],[1,2,1]], 0),                    2),
    ((1, [], 0),                                   0),
])
