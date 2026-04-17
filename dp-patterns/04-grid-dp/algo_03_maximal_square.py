import os, sys
_d = os.path.dirname(os.path.abspath(__file__))
while _d and not os.path.exists(os.path.join(_d, 'test_runner.py')):
    _d = os.path.dirname(_d)
sys.path.insert(0, _d)
from test_runner import run_tests


# Maximal Square (LC #221) -- Medium
# Input:  matrix: List[List[str]] ('0' or '1')
# Output: int (area of largest all-1 square)
# Find the side length of the largest square of all 1s, return area.
#
# Example:
# #   [["1","0","1","0","0"],
#    ["1","0","1","1","1"],
#    ["1","1","1","1","1"],    -> 4   (2x2 square bottom-left, area 4)
#    ["1","0","0","1","0"]]
#
#   Key: If cell is 1: dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1.
#        Return (max dp value)^2.

def maximal_square(matrix):
    pass

run_tests(maximal_square, [
    (([["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]],), 4),
    (([["0","1"],["1","0"]],),  1),
    (([["0"]],),                0),
    (([["1"]],),                1),
    (([["1","1"],["1","1"]],),  4),
])
