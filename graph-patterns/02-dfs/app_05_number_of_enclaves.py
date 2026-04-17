import os, sys
_d = os.path.dirname(os.path.abspath(__file__))
while _d and not os.path.exists(os.path.join(_d, 'test_runner.py')):
    _d = os.path.dirname(_d)
sys.path.insert(0, _d)
from test_runner import run_tests


# Number of Enclaves (LC #1020) -- Medium
# Input:  grid: List[List[int]] (0=sea, 1=land)
# Output: int (count of land cells that CAN'T reach the border)
# Count land cells such that no path of land reaches any border cell.
#
# Example:
# #   [[0,0,0,0],
#    [1,0,1,0],     -> 3
#    [0,1,1,0],
#    [0,0,0,0]]
#
#   WHY THIS IS A REVERSE FLOOD FILL:
#   Reverse thinking: flood-fill from all border land cells. Anything unreached
#   is enclosed. Count remaining 1s.
#
#   Key: 1. DFS from every border '1' cell, mark as 0 (or visited).
#        2. Count remaining 1s.

def num_enclaves(grid):
    pass

run_tests(num_enclaves, [
    (([[0,0,0,0],[1,0,1,0],[0,1,1,0],[0,0,0,0]],),  3),
    (([[0,1,1,0],[0,0,1,0],[0,0,1,0],[0,0,0,0]],),  0),     # connected to border
    (([[0]],),                                      0),
    (([[1]],),                                      0),     # border itself
])
