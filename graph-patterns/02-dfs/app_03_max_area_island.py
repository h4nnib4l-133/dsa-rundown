import os, sys
_d = os.path.dirname(os.path.abspath(__file__))
while _d and not os.path.exists(os.path.join(_d, 'test_runner.py')):
    _d = os.path.dirname(_d)
sys.path.insert(0, _d)
from test_runner import run_tests


# Max Area of Island (LC #695) -- Medium
# Input:  grid: List[List[int]] (0=water, 1=land)
# Output: int (area of LARGEST connected island)
# Find the biggest island's area (count of 1-cells).
#
# Example:
# #   grid with islands of sizes 4, 1, 6, 2 -> 6
#
#   WHY THIS IS A CONNECTED COMPONENTS (size):
#   Each island is a connected component in a grid graph.
#   Run DFS from each unvisited land cell, compute size, track max.
#
#   Key: DFS returns size of the component it explored.
#        max_area = max over all starting cells.

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
    (([[0,0,0,0,0]],),    0),
    (([[1]],),            1),
])
