import os, sys
_d = os.path.dirname(os.path.abspath(__file__))
while _d and not os.path.exists(os.path.join(_d, 'test_runner.py')):
    _d = os.path.dirname(_d)
sys.path.insert(0, _d)
from test_runner import run_tests


# Reorder Routes to Lead to City Zero (LC #1466) -- Medium
# Input:  n: int, connections: List[[a,b]] (directed edges)
# Output: int (min edges to flip so every city reaches 0)
# Directed graph on n cities. Reverse minimum edges so all reach city 0.
#
# Example:
# #   n=6, connections=[[0,1],[1,3],[2,3],[4,0],[4,5]]  -> 3
#
#   Pattern: BFS/DFS ON IMPLICIT UNDIRECTED + EDGE DIRECTION
#   Key: Treat as undirected but track original direction.
#        DFS/BFS from 0. Count edges in wrong direction (pointing away from 0).

def min_reorder(n, connections):
    pass

run_tests(min_reorder, [
    ((6, [[0,1],[1,3],[2,3],[4,0],[4,5]]),    3),
    ((5, [[1,0],[1,2],[3,2],[3,4]]),          2),
    ((3, [[1,0],[2,0]]),                       0),
])
