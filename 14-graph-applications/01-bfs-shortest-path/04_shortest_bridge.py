import os, sys
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))
from test_runner import run_tests


# Shortest Bridge (LC #934) -- Medium
# Input:  grid: List[List[int]] (exactly 2 islands of 1s)
# Output: int (min 0s to flip to 1 to connect the two islands)
# Grid has exactly 2 islands. Find shortest bridge between them.
#
# Approach: DFS one island to find all its cells, then BFS outward until
# hitting the other island. Distance = answer.
#
# Example:
# #   [[0,1],
#    [1,0]]         -> 1
#
#   [[0,1,0],
#    [0,0,0],       -> 2
#    [0,0,1]]
#
#   WHY THIS IS A BFS + DFS HYBRID:
#   Two subproblems: (1) identify island A via DFS, (2) shortest path from
#   A to any cell of island B via BFS. Classic multi-source BFS from island A.
#
#   Key: 1. DFS to find cells of first island, add to BFS queue. Mark as 2.
#        2. BFS outward. Each level, if we step onto a 1, that's the other island. Return level-1.

def shortest_bridge(grid):
    pass

run_tests(shortest_bridge, [
    (([[0,1],[1,0]],),                  1),
    (([[0,1,0],[0,0,0],[0,0,1]],),      2),
    (([[1,1,1,1,1],[1,0,0,0,1],[1,0,1,0,1],[1,0,0,0,1],[1,1,1,1,1]],), 1),
])
