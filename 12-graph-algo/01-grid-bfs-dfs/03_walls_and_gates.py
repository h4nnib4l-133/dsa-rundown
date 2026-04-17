import os, sys
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))
from test_runner import run_tests


# Walls and Gates (LC #286) -- Medium
# Input:  rooms: List[List[int]] (-1=wall, 0=gate, INF=empty)
# Output: None (fill each empty room with distance to nearest gate)
# Each empty room should contain distance to NEAREST gate.
# If unreachable, leave as INF (2147483647).
#
# Pattern: MULTI-SOURCE BFS from all gates at once.
#
# Example:
# #   [[INF,-1,0,INF],         [[3,-1,0,1],
#    [INF,INF,INF,-1],   ->    [2,2,1,-1],
#    [INF,-1,INF,-1],           [1,-1,2,-1],
#    [0,-1,INF,INF]]            [0,-1,3,4]]
#
#   Key: Push ALL gates into BFS queue initially. Each BFS level = +1 distance.

INF = 2147483647

def walls_and_gates(rooms):
    pass


def run_wg(rooms):
    walls_and_gates(rooms)
    return rooms

run_tests(run_wg, [
    (([[2147483647,-1,0,2147483647],
       [2147483647,2147483647,2147483647,-1],
       [2147483647,-1,2147483647,-1],
       [0,-1,2147483647,2147483647]],),
     [[3,-1,0,1],[2,2,1,-1],[1,-1,2,-1],[0,-1,3,4]]),
])
