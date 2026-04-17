import os, sys
_d = os.path.dirname(os.path.abspath(__file__))
while _d and not os.path.exists(os.path.join(_d, 'test_runner.py')):
    _d = os.path.dirname(_d)
sys.path.insert(0, _d)
from test_runner import run_tests


# Minimum Height Trees (LC #310) -- Medium
# Input:  n: int, edges: List[[u,v]] (undirected tree)
# Output: List[int] (roots that give min height tree)
# Find roots that minimize tree height.
# There can be at most 2 such roots (centroids of the tree).
#
# Trick: Peel leaves iteratively (topological sort on undirected tree).
#
# Example:
# #   n=4, edges=[[1,0],[1,2],[1,3]]  -> [1]
#   n=6, edges=[[3,0],[3,1],[3,2],[3,4],[5,4]]  -> [3,4]
#
#   Key: Start with all leaves (degree 1). Remove them. Update degrees.
#        Repeat. Last 1 or 2 nodes remaining are the roots.

def find_min_height_trees(n, edges):
    pass


def solve(n, edges):
    return sorted(find_min_height_trees(n, edges))

run_tests(find_min_height_trees, [
    ((4, [[1,0],[1,2],[1,3]]),                         [1]),
    ((6, [[3,0],[3,1],[3,2],[3,4],[5,4]]),              [3,4]),
    ((1, []),                                           [0]),
    ((2, [[0,1]]),                                      [0,1]),
])
