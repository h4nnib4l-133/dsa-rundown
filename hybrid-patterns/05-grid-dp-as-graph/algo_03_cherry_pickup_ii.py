import os, sys
_d = os.path.dirname(os.path.abspath(__file__))
while _d and not os.path.exists(os.path.join(_d, 'test_runner.py')):
    _d = os.path.dirname(_d)
sys.path.insert(0, _d)
from test_runner import run_tests


# Cherry Pickup II (LC #1463) -- Hard
# Input:  grid: List[List[int]] (rows, cols)
# Output: int (max cherries when TWO robots start at top corners, go down)
# Two robots: start at (0,0) and (0,cols-1), each moves down
# (diagonal down-left, down, or down-right). Collect cherries.
#
# Example:
# #   [[3,1,1],[2,5,1],[1,5,5],[2,1,1]]  -> 24
#
#   Pattern: 3D GRID DP
#   Key: dp[r][c1][c2] = max cherries at row r with robots at c1, c2.
#        9 transitions per state (3 moves per robot).

def cherry_pickup_ii(grid):
    pass

run_tests(cherry_pickup_ii, [
    (([[3,1,1],[2,5,1],[1,5,5],[2,1,1]],),           24),
    (([[1,0,0,0,0,0,1],[2,0,0,0,0,3,0],[2,0,9,0,0,0,0],[0,3,0,5,4,0,0],[1,0,2,3,0,0,6]],),  28),
])
