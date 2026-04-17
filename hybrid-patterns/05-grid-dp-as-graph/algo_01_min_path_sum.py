import os, sys
_d = os.path.dirname(os.path.abspath(__file__))
while _d and not os.path.exists(os.path.join(_d, 'test_runner.py')):
    _d = os.path.dirname(_d)
sys.path.insert(0, _d)
from test_runner import run_tests


# Minimum Path Sum (LC #64) -- Medium
# Input:  grid: List[List[int]] (m x n)
# Output: int (min sum path from top-left to bottom-right, moving right/down only)
# Classic grid DP. Can also be solved as shortest path (Dijkstra).
#
# Example:
# #   [[1,3,1],[1,5,1],[4,2,1]]  -> 7
#
#   Pattern: GRID DP OR DIJKSTRA
#   Key: DP: dp[i][j] = grid[i][j] + min(dp[i-1][j], dp[i][j-1]).
#        (Dijkstra also works but overkill for this.)

def min_path_sum(grid):
    pass

run_tests(min_path_sum, [
    (([[1,3,1],[1,5,1],[4,2,1]],),  7),
    (([[1,2,3],[4,5,6]],),          12),
    (([[1]],),                       1),
])
