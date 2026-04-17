import os, sys
_d = os.path.dirname(os.path.abspath(__file__))
while _d and not os.path.exists(os.path.join(_d, 'test_runner.py')):
    _d = os.path.dirname(_d)
sys.path.insert(0, _d)
from test_runner import run_tests


# Swim in Rising Water (LC #778) -- Hard
# Input:  grid: List[List[int]] (n x n elevations)
# Output: int (min time t so path from (0,0) to (n-1,n-1) uses only cells <= t)
# Water rises. At time t, cells with height <= t are accessible.
#
# Example:
# #   [[0,2],[1,3]]  -> 3
#
#   Pattern: DIJKSTRA (max edge weight variant)
#   Key: Min-heap Dijkstra. 'Distance' = max height so far on path.
#        Relaxation: new_t = max(current_t, grid[nr][nc]).

def swim_in_water(grid):
    pass

run_tests(swim_in_water, [
    (([[0,2],[1,3]],),                                3),
    (([[0]],),                                         0),
    (([[0,1,2,3,4],[24,23,22,21,5],[12,13,14,15,16],[11,17,18,19,20],[10,9,8,7,6]],),  16),
])
