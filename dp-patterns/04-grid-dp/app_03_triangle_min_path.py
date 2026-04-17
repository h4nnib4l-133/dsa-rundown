import os, sys
_d = os.path.dirname(os.path.abspath(__file__))
while _d and not os.path.exists(os.path.join(_d, 'test_runner.py')):
    _d = os.path.dirname(_d)
sys.path.insert(0, _d)
from test_runner import run_tests


# Triangle (LC #120) -- Medium
# Input:  triangle: List[List[int]]
# Output: int (min path sum from top to bottom; move to adjacent below)
# Each step can go to adjacent numbers in the row below.
#
# Example:
# #   [[2],[3,4],[6,5,7],[4,1,8,3]]
#   -> 11   (2 + 3 + 5 + 1 = 11)
#
#   Pattern: GRID DP (bottom-up)
#   Key: Process from bottom up. dp[i][j] = triangle[i][j] + min(dp[i+1][j], dp[i+1][j+1]).
#        Optimize to 1D array of size n.

def minimum_total(triangle):
    pass

run_tests(minimum_total, [
    (([[2],[3,4],[6,5,7],[4,1,8,3]],),  11),
    (([[-10]],),                        -10),
    (([[1],[2,3]],),                     3),
])
