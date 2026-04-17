import os, sys
_d = os.path.dirname(os.path.abspath(__file__))
while _d and not os.path.exists(os.path.join(_d, 'test_runner.py')):
    _d = os.path.dirname(_d)
sys.path.insert(0, _d)
from test_runner import run_tests


# Number of Restricted Paths (LC #1786) -- Medium
# Input:  n: int, edges: List[[u,v,w]]
# Output: int (paths from 1 to n with strictly decreasing distances to n, mod 10^9+7)
# Dist(x) = shortest dist from x to n. Count paths 1->n where
# dist decreases strictly along the path.
#
# Example:
# #   n=5, edges=[[1,2,3],[1,3,3],[2,3,1],[1,4,2],[5,2,2],[3,5,1],[5,4,10]]
#   -> 3
#
#   Pattern: DIJKSTRA + DAG DP
#   Key: Step 1: Dijkstra from n to get dist[].
#        Step 2: Edges where dist decreases form a DAG. DP: paths[u] = sum(paths[v])
#        for neighbors v with dist[v] < dist[u]. Process in order of dist.

def count_restricted_paths(n, edges):
    pass

run_tests(count_restricted_paths, [
    ((5, [[1,2,3],[1,3,3],[2,3,1],[1,4,2],[5,2,2],[3,5,1],[5,4,10]]),  3),
    ((7, [[1,3,1],[4,1,2],[7,3,4],[2,5,3],[5,6,1],[6,7,2],[7,5,3],[2,6,4]]), 1),
])
