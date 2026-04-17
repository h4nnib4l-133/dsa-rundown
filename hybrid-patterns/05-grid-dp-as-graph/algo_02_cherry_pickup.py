import os, sys
_d = os.path.dirname(os.path.abspath(__file__))
while _d and not os.path.exists(os.path.join(_d, 'test_runner.py')):
    _d = os.path.dirname(_d)
sys.path.insert(0, _d)
from test_runner import run_tests


# Cherry Pickup (LC #741) -- Hard
# Input:  grid: List[List[int]] (0=empty, 1=cherry, -1=block, n x n)
# Output: int (max cherries from (0,0) to (n-1,n-1) and back)
# Go to bottom-right and back. Collect cherries along the way.
# Equivalent to two people walking from (0,0) to (n-1,n-1) simultaneously.
#
# Example:
# #   [[0,1,-1],[1,0,-1],[1,1,1]]  -> 5
#
#   Pattern: 3D GRID DP (two agents)
#   Key: State: (r1, c1, r2) — c2 derived from r1+c1 == r2+c2.
#        dp[r1][c1][r2] = max cherries collected by two paths with same step count.

def cherry_pickup(grid):
    pass

run_tests(cherry_pickup, [
    (([[0,1,-1],[1,0,-1],[1,1,1]],),                     5),
    (([[1,1,-1],[1,-1,1],[-1,1,1]],),                     0),
    (([[1]],),                                            1),
])
