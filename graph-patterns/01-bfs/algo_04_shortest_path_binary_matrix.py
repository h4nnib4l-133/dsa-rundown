import os, sys
_d = os.path.dirname(os.path.abspath(__file__))
while _d and not os.path.exists(os.path.join(_d, 'test_runner.py')):
    _d = os.path.dirname(_d)
sys.path.insert(0, _d)
from test_runner import run_tests


# Shortest Path in Binary Matrix (LC #1091) -- Medium
# Input:  grid: List[List[int]] (0=open, 1=blocked, 8-directional)
# Output: int (shortest path from (0,0) to (n-1,n-1), or -1)
# 8-directional moves (including diagonals). Both start and end must be 0.
#
# Example:
# #   [[0,1],[1,0]]  -> 2   ((0,0)->diagonal->(1,1))
#   [[0,0,0],[1,1,0],[1,1,0]]  -> 4
#
#   Key: BFS from (0,0). Use 8 directions. Return distance when reaching (n-1,n-1).

def shortest_path_binary_matrix(grid):
    pass

run_tests(shortest_path_binary_matrix, [
    (([[0,1],[1,0]],),                2),
    (([[0,0,0],[1,1,0],[1,1,0]],),    4),
    (([[1,0,0],[1,1,0],[1,1,0]],),   -1),      # start blocked
    (([[0]],),                        1),      # 1x1 grid
    (([[0,0],[0,0]],),                2),
])
