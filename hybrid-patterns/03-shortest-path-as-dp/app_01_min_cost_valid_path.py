import os, sys
_d = os.path.dirname(os.path.abspath(__file__))
while _d and not os.path.exists(os.path.join(_d, 'test_runner.py')):
    _d = os.path.dirname(_d)
sys.path.insert(0, _d)
from test_runner import run_tests


# Min Cost to Make at Least One Valid Path (LC #1368) -- Hard
# Input:  grid: List[List[int]] (1=right, 2=left, 3=down, 4=up)
# Output: int (min cells to modify to have a valid path from (0,0) to bottom-right)
# Each cell dictates a direction. Follow direction for free; cost 1 to change.
#
# Example:
# #   [[1,1,1,1],
#    [2,2,2,2],  -> 3
#    [1,1,1,1],
#    [2,2,2,2]]
#
#   Pattern: 0-1 BFS (deque)
#   Key: Weighted BFS. Following arrow = 0 cost (push front). Changing = 1 cost (push back).
#        Use deque for 0-1 BFS instead of Dijkstra.

def min_cost_valid_path(grid):
    pass

run_tests(min_cost_valid_path, [
    (([[1,1,1,1],[2,2,2,2],[1,1,1,1],[2,2,2,2]],),  3),
    (([[1,1,3],[3,2,2],[1,1,4]],),                   0),
    (([[1,2],[4,3]],),                               1),
])
