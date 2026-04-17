import os, sys
_d = os.path.dirname(os.path.abspath(__file__))
while _d and not os.path.exists(os.path.join(_d, 'test_runner.py')):
    _d = os.path.dirname(_d)
sys.path.insert(0, _d)
from test_runner import run_tests



# Number of Connected Components (LC #323) -- Medium
# Input:  n: int (nodes 0..n-1), edges: List[[u,v]] (undirected)
# Output: int (number of connected components)
# Given n nodes and undirected edges, count connected components.
#
# Example:
#   n=5, edges=[[0,1],[1,2],[3,4]]
#   Components: {0,1,2} and {3,4} -> 2
#
#   Key: DFS/BFS from each unvisited node, or Union-Find.
#        Each time you start a new DFS = one more component.

def count_components(n, edges):
    pass


run_tests(count_components, [
    ((5, [[0,1],[1,2],[3,4]]),          2),
    ((5, [[0,1],[1,2],[2,3],[3,4]]),    1),     # all connected
    ((4, []),                            4),     # no edges, each node is a component
    ((1, []),                            1),     # single node
    ((6, [[0,1],[2,3],[4,5]]),          3),     # three pairs
    ((4, [[0,1],[0,2],[0,3]]),          1),     # star topology
])
