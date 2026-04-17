import os, sys
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))
from test_runner import run_tests


# Path With Minimum Effort (LC #1631) -- Medium
# Input:  heights: List[List[int]] (grid)
# Output: int (min 'effort' for path from (0,0) to bottom-right)
# Effort of path = MAX absolute difference between adjacent cells on path.
# Find path minimizing this max difference.
#
# Pattern: DIJKSTRA ON GRID where 'distance' is max edge weight.
#
# Example:
# #   [[1,2,2],[3,8,2],[5,3,5]]  -> 2
#   [[1,2,3],[3,8,4],[5,3,5]]  -> 1
#
#   Key: Min-heap of (max_diff_so_far, r, c).
#        When relaxing: new_diff = max(current_diff, |h[nr][nc] - h[r][c]|).

def minimum_effort_path(heights):
    pass

run_tests(minimum_effort_path, [
    (([[1,2,2],[3,8,2],[5,3,5]],),    2),
    (([[1,2,3],[3,8,4],[5,3,5]],),    1),
    (([[1,2,1,1,1],[1,2,1,2,1],[1,2,1,2,1],[1,2,1,2,1],[1,1,1,2,1]],), 0),
    (([[1]],),                        0),
])
