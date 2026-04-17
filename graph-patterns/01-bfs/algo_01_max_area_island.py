import os, sys
_d = os.path.dirname(os.path.abspath(__file__))
while _d and not os.path.exists(os.path.join(_d, 'test_runner.py')):
    _d = os.path.dirname(_d)
sys.path.insert(0, _d)
from test_runner import run_tests


# Max Area of Island (LC #695) -- Medium
# Input:  grid: List[List[int]] (0=water, 1=land)
# Output: int (max area of any connected island, 0 if none)
# Like Num Islands but return the LARGEST island's area.
#
# Example:
# #   Large grid with multiple islands of various sizes -> area of biggest.
#
#   Key: DFS/BFS flood fill. Each DFS returns count of cells visited.
#        Track max across all starting cells.

def max_area_of_island(grid):
    pass

run_tests(max_area_of_island, [
    (([[0,0,1,0,0,0,0,1,0,0,0,0,0],
       [0,0,0,0,0,0,0,1,1,1,0,0,0],
       [0,1,1,0,1,0,0,0,0,0,0,0,0],
       [0,1,0,0,1,1,0,0,1,0,1,0,0],
       [0,1,0,0,1,1,0,0,1,1,1,0,0],
       [0,0,0,0,0,0,0,0,0,0,1,0,0],
       [0,0,0,0,0,0,0,1,1,1,0,0,0],
       [0,0,0,0,0,0,0,1,1,0,0,0,0]],),  6),
    (([[0,0,0,0,0]],),  0),
    (([[1]],),          1),
    (([[1,1],[1,1]],),  4),
])
