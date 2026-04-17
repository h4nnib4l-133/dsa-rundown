import os, sys
_d = os.path.dirname(os.path.abspath(__file__))
while _d and not os.path.exists(os.path.join(_d, 'test_runner.py')):
    _d = os.path.dirname(_d)
sys.path.insert(0, _d)
from test_runner import run_tests


# Minimum Falling Path Sum (LC #931) -- Medium
# Input:  matrix: List[List[int]]
# Output: int (min sum path falling top to bottom, each step to adjacent 3 cells)
# Fall down one row at a time. Move to (r+1, c-1), (r+1, c), or (r+1, c+1).
#
# Example:
# #   [[2,1,3],[6,5,4],[7,8,9]]  -> 13
#
#   Pattern: GRID DP
#   Key: dp[i][j] = matrix[i][j] + min(dp[i-1][j-1], dp[i-1][j], dp[i-1][j+1]).
#        Answer = min of last row.

def min_falling_path_sum(matrix):
    pass

run_tests(min_falling_path_sum, [
    (([[2,1,3],[6,5,4],[7,8,9]],),  13),
    (([[-19,57],[-40,-5]],),        -59),
    (([[7]],),                       7),
])
