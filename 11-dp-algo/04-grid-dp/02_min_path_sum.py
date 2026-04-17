import os, sys
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))
from test_runner import run_tests


# Minimum Path Sum (LC #64) -- Medium
# Input:  grid: List[List[int]] (non-negative)
# Output: int (min sum path from top-left to bottom-right)
# Only right/down moves. Minimize sum of values on path.
#
# Example:
# #   [[1,3,1],
#    [1,5,1],     -> 7   (1->3->1->1->1)
#    [4,2,1]]
#
#   Key: dp[i][j] = grid[i][j] + min(dp[i-1][j], dp[i][j-1]).

def min_path_sum(grid):
    pass

run_tests(min_path_sum, [
    (([[1,3,1],[1,5,1],[4,2,1]],),  7),
    (([[1,2,3],[4,5,6]],),           12),
    (([[1]],),                       1),
    (([[1,2],[1,1]],),               3),
])
