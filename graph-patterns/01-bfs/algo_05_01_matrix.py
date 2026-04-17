import os, sys
_d = os.path.dirname(os.path.abspath(__file__))
while _d and not os.path.exists(os.path.join(_d, 'test_runner.py')):
    _d = os.path.dirname(_d)
sys.path.insert(0, _d)
from test_runner import run_tests


# 01 Matrix (LC #542) -- Medium
# Input:  mat: List[List[int]] (0s and 1s)
# Output: List[List[int]] (distance from each cell to nearest 0)
# For each cell, compute distance to nearest 0.
#
# Pattern: MULTI-SOURCE BFS from all 0s simultaneously.
#
# Example:
# #   [[0,0,0],
#    [0,1,0],     -> same
#    [0,0,0]]
#
#   [[0,0,0],           [[0,0,0],
#    [0,1,0],     ->     [0,1,0],
#    [1,1,1]]            [1,2,1]]
#
#   Key: Push all 0s into queue. BFS expands to 1s, setting distance = parent+1.

def update_matrix(mat):
    pass

run_tests(update_matrix, [
    (([[0,0,0],[0,1,0],[0,0,0]],),  [[0,0,0],[0,1,0],[0,0,0]]),
    (([[0,0,0],[0,1,0],[1,1,1]],),  [[0,0,0],[0,1,0],[1,2,1]]),
    (([[0]],),                        [[0]]),
    (([[1,0,1]],),                    [[1,0,1]]),
])
