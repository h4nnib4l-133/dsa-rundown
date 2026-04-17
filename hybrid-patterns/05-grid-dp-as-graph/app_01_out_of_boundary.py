import os, sys
_d = os.path.dirname(os.path.abspath(__file__))
while _d and not os.path.exists(os.path.join(_d, 'test_runner.py')):
    _d = os.path.dirname(_d)
sys.path.insert(0, _d)
from test_runner import run_tests


# Out of Boundary Paths (LC #576) -- Medium
# Input:  m: int, n: int, maxMove: int, startRow: int, startColumn: int
# Output: int (paths moving ball off grid in at most maxMove moves, mod 10^9+7)
# Ball on grid. Move 4 directions. Count paths that leave the grid.
#
# Example:
# #   m=2, n=2, maxMove=2, start=(0,0)  -> 6
#
#   Pattern: GRID DP + MOVE COUNT
#   Key: dp[k][i][j] = paths ending off-grid in <= k moves starting at (i,j).
#        Transition: sum of dp[k-1][neighbor] (1 if neighbor out of bounds).

def find_paths(m, n, max_move, start_row, start_column):
    pass

run_tests(find_paths, [
    ((2, 2, 2, 0, 0),   6),
    ((1, 3, 3, 0, 1),  12),
    ((1, 1, 0, 0, 0),   0),
])
