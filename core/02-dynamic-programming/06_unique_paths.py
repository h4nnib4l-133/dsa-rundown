import os, sys
_d = os.path.dirname(os.path.abspath(__file__))
while _d and not os.path.exists(os.path.join(_d, 'test_runner.py')):
    _d = os.path.dirname(_d)
sys.path.insert(0, _d)
from test_runner import run_tests



# Unique Paths (LC #62) -- Medium
# Input:  m: int (rows), n: int (cols), both >= 1
# Output: int (number of unique paths from top-left to bottom-right)
# Robot at top-left of m x n grid. Can only move right or down.
# Count distinct paths to bottom-right corner.
#
# Example:
#   m=3, n=7 -> 28
#   m=3, n=2 -> 3  (RD, DR, RD... paths: DDR, DRD, RDD -> wait m=rows n=cols)
#        3x2 grid:  paths = RDD, DRD, DDR -> 3
#
#   Key: dp[i][j] = dp[i-1][j] + dp[i][j-1].
#        First row and first col are all 1 (only one way to reach them).

def unique_paths(m, n):
    pass


run_tests(unique_paths, [
    ((3, 7),  28),
    ((3, 2),   3),
    ((1, 1),   1),     # already there
    ((7, 3),  28),     # same as (3,7)
    ((3, 3),   6),
    ((1, 5),   1),     # single row
    ((5, 1),   1),     # single column
    ((2, 2),   2),     # RD or DR
    ((10, 10), 48620), # larger grid
])
