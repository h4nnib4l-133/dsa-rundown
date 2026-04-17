import os, sys
_d = os.path.dirname(os.path.abspath(__file__))
while _d and not os.path.exists(os.path.join(_d, 'test_runner.py')):
    _d = os.path.dirname(_d)
sys.path.insert(0, _d)
from test_runner import run_tests


# Number of Ways to Arrive at Destination (LC #1976) -- Medium
# Input:  n: int, roads: List[[u,v,w]]
# Output: int (count of shortest paths from 0 to n-1, mod 10^9+7)
# Count SHORTEST paths, not just find one.
#
# Example:
# #   n=7, roads=[[0,6,7],[0,1,2],[1,2,3],[1,3,3],[6,3,3],[3,5,1],[6,5,1],[2,5,1],[0,4,5],[4,6,2]]
#   -> 4
#
#   Pattern: DIJKSTRA + DP (path counting)
#   Key: Run Dijkstra. When relaxing edge u->v:
#        if dist[u]+w < dist[v]: dist[v] = dist[u]+w, ways[v] = ways[u].
#        elif == : ways[v] += ways[u].

def count_paths(n, roads):
    pass

run_tests(count_paths, [
    ((7, [[0,6,7],[0,1,2],[1,2,3],[1,3,3],[6,3,3],[3,5,1],[6,5,1],[2,5,1],[0,4,5],[4,6,2]]), 4),
    ((2, [[1,0,10]]),                           1),
    ((1, []),                                    1),
])
