import os, sys
_d = os.path.dirname(os.path.abspath(__file__))
while _d and not os.path.exists(os.path.join(_d, 'test_runner.py')):
    _d = os.path.dirname(_d)
sys.path.insert(0, _d)
from test_runner import run_tests


# Sum of Distances in Tree (LC #834) -- Hard
# Input:  n: int, edges: List[[u,v]]
# Output: List[int] (answer[i] = sum of distances from i to all other nodes)
# For each node, sum of distances to every other node.
#
# Example:
# #   n=6, edges=[[0,1],[0,2],[2,3],[2,4],[2,5]]
#   -> [8,12,6,10,10,10]
#
#   Pattern: REROOTING DP
#   Key: Two DFS:
#        1. Compute subtree size and sum of distances from root.
#        2. Reroot: move root to each neighbor, update sum using subtree size.
#        ans[v] = ans[u] - size[v] + (n - size[v]) when moving from u to v.

def sum_of_distances_in_tree(n, edges):
    pass

run_tests(sum_of_distances_in_tree, [
    ((6, [[0,1],[0,2],[2,3],[2,4],[2,5]]),  [8,12,6,10,10,10]),
    ((1, []),                                [0]),
    ((2, [[0,1]]),                           [1,1]),
])
