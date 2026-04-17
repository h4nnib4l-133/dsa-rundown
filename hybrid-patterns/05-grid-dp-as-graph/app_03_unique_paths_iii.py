import os, sys
_d = os.path.dirname(os.path.abspath(__file__))
while _d and not os.path.exists(os.path.join(_d, 'test_runner.py')):
    _d = os.path.dirname(_d)
sys.path.insert(0, _d)
from test_runner import run_tests


# Unique Paths III (LC #980) -- Hard
# Input:  grid: List[List[int]] (1=start, 2=end, 0=empty, -1=obstacle)
# Output: int (paths from start to end visiting every empty cell exactly once)
# Hamiltonian-path-style enumeration on small grid.
#
# Example:
# #   [[1,0,0,0],[0,0,0,0],[0,0,2,-1]]  -> 2
#
#   Pattern: BACKTRACKING DFS
#   Key: DFS with visited set. Only succeed if at end AND visited count = empty_count.
#        Mark/unmark cells for backtracking.

def unique_paths_iii(grid):
    pass

run_tests(unique_paths_iii, [
    (([[1,0,0,0],[0,0,0,0],[0,0,2,-1]],),       2),
    (([[1,0,0,0],[0,0,0,0],[0,0,0,2]],),         4),
    (([[0,1],[2,0]],),                           0),
])
