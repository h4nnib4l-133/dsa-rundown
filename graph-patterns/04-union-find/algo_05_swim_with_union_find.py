import os, sys
_d = os.path.dirname(os.path.abspath(__file__))
while _d and not os.path.exists(os.path.join(_d, 'test_runner.py')):
    _d = os.path.dirname(_d)
sys.path.insert(0, _d)
from test_runner import run_tests


# Number of Islands II (LC #305) -- Hard
# Input:  m: int, n: int, positions: List[[r,c]] (add land incrementally)
# Output: List[int] (number of islands after each addition)
# Dynamic: add land cells one by one. After each, report # of islands.
#
# Pattern: Dynamic Union-Find on grid.
#
# Example:
# #   m=3, n=3, positions=[[0,0],[0,1],[1,2],[2,1]]
#   -> [1,1,2,3]
#
#   Key: Union-Find indexed by r*n + c. When adding (r,c):
#        increment island count. For each already-land neighbor, try to union.
#        If union succeeds (different roots), decrement count.

def num_islands_2(m, n, positions):
    pass

run_tests(num_islands_2, [
    ((3, 3, [[0,0],[0,1],[1,2],[2,1]]),              [1,1,2,3]),
    ((3, 3, [[0,0],[0,0]]),                           [1,1]),     # duplicate add
    ((1, 1, [[0,0]]),                                 [1]),
    ((2, 2, [[0,0],[1,1],[0,1]]),                     [1,2,1]),
])
