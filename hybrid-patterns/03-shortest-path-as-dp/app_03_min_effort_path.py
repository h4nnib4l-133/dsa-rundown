import os, sys
_d = os.path.dirname(os.path.abspath(__file__))
while _d and not os.path.exists(os.path.join(_d, 'test_runner.py')):
    _d = os.path.dirname(_d)
sys.path.insert(0, _d)
from test_runner import run_tests


# Path with Minimum Effort (LC #1631) -- Medium
# Input:  heights: List[List[int]]
# Output: int (min possible 'effort' = max adjacent absolute diff on any path)
# Path effort = max |height[i] - height[j]| between adjacent cells.
#
# Example:
# #   [[1,2,2],[3,8,2],[5,3,5]]  -> 2
#
#   Pattern: DIJKSTRA (max edge variant)
#   Key: Min-heap of (max_diff_so_far, r, c).
#        Relaxation: new_diff = max(current, |h[nr][nc] - h[r][c]|).

def minimum_effort_path(heights):
    pass

run_tests(minimum_effort_path, [
    (([[1,2,2],[3,8,2],[5,3,5]],),    2),
    (([[1,2,3],[3,8,4],[5,3,5]],),    1),
    (([[1]],),                        0),
])
