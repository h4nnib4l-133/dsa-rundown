import os, sys
_d = os.path.dirname(os.path.abspath(__file__))
while _d and not os.path.exists(os.path.join(_d, 'test_runner.py')):
    _d = os.path.dirname(_d)
sys.path.insert(0, _d)
from test_runner import run_tests


# Longest Increasing Path (DAG topological) -- Medium
# Input:  n: int, edges: List[[u,v,w]] (DAG), start: int
# Output: int (length of longest path from start)
# Classic longest path in a DAG via topological sort + DP.
#
# Example:
# #   n=4, edges=[[0,1,2],[0,2,3],[1,3,1],[2,3,5]], start=0
#   -> 8   (0->2->3 with weights 3+5)
#
#   Key: Topological sort. Process nodes in order, relax outgoing edges:
#        dist[v] = max(dist[v], dist[u] + weight).

def longest_path_dag(n, edges, start):
    pass

run_tests(longest_path_dag, [
    ((4, [[0,1,2],[0,2,3],[1,3,1],[2,3,5]], 0),  8),
    ((2, [[0,1,5]], 0),                            5),
    ((3, [[0,1,1],[1,2,1]], 0),                    2),
    ((1, [], 0),                                   0),
])
