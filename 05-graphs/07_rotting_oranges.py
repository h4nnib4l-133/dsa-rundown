import sys, os; sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from test_runner import run_tests



# Rotting Oranges (LC #994) -- Medium
# Input:  grid: List[List[int]] (0=empty, 1=fresh, 2=rotten)
# Output: int (minutes until all rotten, or -1 if impossible)
# Grid: 0=empty, 1=fresh orange, 2=rotten orange.
# Each minute, fresh oranges adjacent (4-dir) to rotten ones become rotten.
# Return minutes until no fresh oranges remain, or -1 if impossible.
#
# Example:
#   [[2,1,1],
#    [1,1,0],    -> 4 minutes
#    [0,1,1]]
#
#   [[2,1,1],
#    [0,1,1],    -> -1  (bottom-left 1 is isolated)
#    [1,0,1]]
#
#   Key: Multi-source BFS. Start with ALL rotten oranges in queue.
#        BFS level = 1 minute. Count remaining fresh at end.

def oranges_rotting(grid):
    """Return minutes until all rot, or -1 if impossible"""
    pass


run_tests(oranges_rotting, [
    (([[2,1,1],[1,1,0],[0,1,1]],),   4),
    (([[2,1,1],[0,1,1],[1,0,1]],),  -1),     # isolated fresh
    (([[0,2]],),                     0),      # no fresh oranges
    (([[0]],),                       0),      # empty grid
    (([[1]],),                      -1),      # one fresh, no rotten
    (([[2]],),                       0),      # one rotten, no fresh
    (([[2,1],[1,1]],),               2),      # 2x2 grid
    (([[1,2,1,1,2,1,1]],),          2),      # single row, two sources
])
