import os, sys
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))
from test_runner import run_tests


# Swim in Rising Water (LC #778) -- Hard
# Input:  grid: List[List[int]] (n x n, elevations)
# Output: int (min time t such that a path exists using only cells with height <= t)
# Similar to Min Effort but 'distance' = max CELL height (not edge diff).
#
# Example:
# #   [[0,2],[1,3]]  -> 3   (must wait for t=3 to cover cell with height 3)
#
#   Key: Dijkstra: min-heap of (max_height_so_far, r, c).
#        Alternative: binary search on t + BFS to check reachability.

def swim_in_water(grid):
    pass

run_tests(swim_in_water, [
    (([[0,2],[1,3]],),    3),
    (([[0,1,2,3,4],[24,23,22,21,5],[12,13,14,15,16],[11,17,18,19,20],[10,9,8,7,6]],), 16),
    (([[0]],),            0),
    (([[0,1],[2,3]],),    3),
])
