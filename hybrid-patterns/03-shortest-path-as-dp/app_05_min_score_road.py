import os, sys
_d = os.path.dirname(os.path.abspath(__file__))
while _d and not os.path.exists(os.path.join(_d, 'test_runner.py')):
    _d = os.path.dirname(_d)
sys.path.insert(0, _d)
from test_runner import run_tests


# Minimum Score of a Path Between Two Cities (LC #2492) -- Medium
# Input:  n: int, roads: List[[u,v,w]]
# Output: int (min edge weight in any path between city 1 and city n)
# Among all paths 1 -> n (any length, reusing edges allowed), find min edge weight.
#
# Example:
# #   n=4, roads=[[1,2,9],[2,3,6],[2,4,5],[1,4,7]]  -> 5
#
#   Pattern: GRAPH TRAVERSAL (any connected component)
#   Key: Since you can walk in circles, answer = min edge in connected component of node 1.
#        DFS/BFS/Union-Find from 1, track min edge weight seen.

def min_score(n, roads):
    pass

run_tests(min_score, [
    ((4, [[1,2,9],[2,3,6],[2,4,5],[1,4,7]]),    5),
    ((4, [[1,2,2],[1,3,4],[3,4,7]]),             2),
])
