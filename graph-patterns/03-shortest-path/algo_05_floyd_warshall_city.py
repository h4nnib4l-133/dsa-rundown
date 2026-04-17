import os, sys
_d = os.path.dirname(os.path.abspath(__file__))
while _d and not os.path.exists(os.path.join(_d, 'test_runner.py')):
    _d = os.path.dirname(_d)
sys.path.insert(0, _d)
from test_runner import run_tests


# Find City with Smallest # of Neighbors (LC #1334) -- Medium
# Input:  n: int, edges: List[[u,v,w]], distance_threshold: int
# Output: int (city with FEWEST reachable cities within threshold, ties -> largest index)
# All-pairs shortest path.
#
# Pattern: FLOYD-WARSHALL (O(n^3), good for dense all-pairs).
#
# Example:
# #   n=4, edges=[[0,1,3],[1,2,1],[1,3,4],[2,3,1]], threshold=4  -> 3
#
#   Key: dist[i][j] = min direct edge, else infinity.
#        For k: for i: for j: dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j]).
#        Count reachable within threshold for each node. Pick min, break ties by larger index.

def find_the_city(n, edges, distance_threshold):
    pass

run_tests(find_the_city, [
    ((4, [[0,1,3],[1,2,1],[1,3,4],[2,3,1]], 4),         3),
    ((5, [[0,1,2],[0,4,8],[1,2,3],[1,4,2],[2,3,1],[3,4,1]], 2),  0),
    ((1, [], 10),                                        0),
    ((2, [[0,1,5]], 3),                                  1),     # tie -> larger index
])
