import os, sys
_d = os.path.dirname(os.path.abspath(__file__))
while _d and not os.path.exists(os.path.join(_d, 'test_runner.py')):
    _d = os.path.dirname(_d)
sys.path.insert(0, _d)
from test_runner import run_tests


# Longest Path in Weighted DAG -- Medium
# Input:  n: int, edges: List[[u,v,w]] (directed), start: int
# Output: int (longest path from start)
# DAG, find longest weighted path from a given start.
#
# Example:
# #   n=4, edges=[[0,1,2],[0,2,3],[1,3,1],[2,3,5]], start=0
#   -> 8   (0->2->3)
#
#   Pattern: TOPSORT + DP
#   Key: Topologically sort. Process in order, relax outgoing edges:
#        dist[v] = max(dist[v], dist[u] + w).

def longest_path_dag(n, edges, start):
    pass

run_tests(longest_path_dag, [
    ((4, [[0,1,2],[0,2,3],[1,3,1],[2,3,5]], 0),  8),
    ((2, [[0,1,5]], 0),                            5),
    ((1, [], 0),                                   0),
])
