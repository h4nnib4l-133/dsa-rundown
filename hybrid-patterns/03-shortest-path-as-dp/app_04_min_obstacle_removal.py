import os, sys
_d = os.path.dirname(os.path.abspath(__file__))
while _d and not os.path.exists(os.path.join(_d, 'test_runner.py')):
    _d = os.path.dirname(_d)
sys.path.insert(0, _d)
from test_runner import run_tests


# Minimum Obstacle Removal to Reach Corner (LC #2290) -- Hard
# Input:  grid: List[List[int]] (0=open, 1=obstacle)
# Output: int (min obstacles to remove for path from (0,0) to bottom-right)
# Move any direction. Obstacle = cost 1 to pass. Open = cost 0.
#
# Example:
# #   [[0,1,1],[1,1,0],[1,1,0]]  -> 2
#
#   Pattern: 0-1 BFS
#   Key: Deque-based BFS. Push open cells to front (0 cost), obstacles to back (1 cost).
#        Distance = obstacles removed on path.

def minimum_obstacles(grid):
    pass

run_tests(minimum_obstacles, [
    (([[0,1,1],[1,1,0],[1,1,0]],),             2),
    (([[0,1,0,0,0],[0,1,0,1,0],[0,0,0,1,0]],),  0),
    (([[0]],),                                  0),
])
