import os, sys
_d = os.path.dirname(os.path.abspath(__file__))
while _d and not os.path.exists(os.path.join(_d, 'test_runner.py')):
    _d = os.path.dirname(_d)
sys.path.insert(0, _d)
from test_runner import run_tests


# Minimum Path Cost in a Grid (LC #2304) -- Medium
# Input:  grid: List[List[int]], moveCost: List[List[int]]
# Output: int (min cost path from top to bottom)
# At row r, cell value grid[r][c]. moveCost[grid[r][c]][j] = cost to move to (r+1, j).
#
# Example:
# #   grid=[[5,3],[4,0],[2,1]], moveCost=[[9,8],[1,5],[10,12],[18,6],[2,4],[14,3]]
#   -> 17
#
#   Pattern: GRID DP
#   Key: dp[r][c] = min cost to reach (r,c). Transitions: dp[r][c] = grid[r][c] + min(dp[r-1][c'] + moveCost[grid[r-1][c']][c]).

def min_path_cost(grid, move_cost):
    pass

run_tests(min_path_cost, [
    (([[5,3],[4,0],[2,1]], [[9,8],[1,5],[10,12],[18,6],[2,4],[14,3]]),  17),
    (([[5,1,2],[4,0,3]], [[12,10,15],[20,23,8],[21,7,1],[8,1,13],[9,10,25],[5,3,2]]), 6),
])
