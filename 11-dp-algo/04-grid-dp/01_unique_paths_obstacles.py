import os, sys
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))
from test_runner import run_tests


# Unique Paths II (LC #63) -- Medium
# Input:  obstacleGrid: List[List[int]] (0=open, 1=obstacle)
# Output: int (number of paths from top-left to bottom-right)
# Only right/down moves. Obstacles block the path.
#
# Example:
# #   [[0,0,0],
#    [0,1,0],      -> 2
#    [0,0,0]]
#
#   Key: dp[i][j] = 0 if obstacle, else dp[i-1][j] + dp[i][j-1].

def unique_paths_with_obstacles(grid):
    pass

run_tests(unique_paths_with_obstacles, [
    (([[0,0,0],[0,1,0],[0,0,0]],),  2),
    (([[0,1],[0,0]],),              1),
    (([[1]],),                      0),     # start blocked
    (([[0]],),                      1),     # trivial
    (([[0,0],[1,0]],),              1),
])
