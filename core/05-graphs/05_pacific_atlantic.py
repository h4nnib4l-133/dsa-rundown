import os, sys
_d = os.path.dirname(os.path.abspath(__file__))
while _d and not os.path.exists(os.path.join(_d, 'test_runner.py')):
    _d = os.path.dirname(_d)
sys.path.insert(0, _d)
from test_runner import run_tests



# Pacific Atlantic Water Flow (LC #417) -- Medium
# Input:  heights: List[List[int]] (m x n grid of elevations)
# Output: List[[row, col]] (cells that can flow to both oceans)
# m x n island. Pacific ocean touches top and left edges.
# Atlantic ocean touches bottom and right edges.
# Water flows from higher/equal cells to lower/equal cells (4-directional).
# Find all cells where water can flow to BOTH oceans.
#
# Example:
#   heights = [[1,2,2,3,5],    Pacific touches top+left
#              [3,2,3,4,4],    Atlantic touches bottom+right
#              [2,4,5,3,1],
#              [6,7,1,4,5],
#              [5,1,1,2,4]]
#   -> [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]
#
#   Key: BFS/DFS from ocean borders inward (reverse flow).
#        Two visited sets: one for Pacific, one for Atlantic.
#        Answer = intersection.

def pacific_atlantic(heights):
    """Return list of [r,c] that can flow to both oceans"""
    pass


def solve(heights):
    result = pacific_atlantic(heights)
    return sorted(result)


run_tests(solve, [
    (([[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]],),
     [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]),
    (([[1]],), [[0,0]]),     # single cell flows to both
    (([[1,1],[1,1]],), [[0,0],[0,1],[1,0],[1,1]]),   # flat grid, all flow both ways
])
