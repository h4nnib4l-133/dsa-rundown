import sys, os; sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from test_runner import run_tests

# BFS Shortest Reach (HackerRank) -- Medium
# Given unweighted undirected graph, find shortest distance from start to all nodes.
# Return -1 for unreachable nodes.
#
# Example:
#   4 nodes, edges: 0-1, 0-2, 1-3, start=0
#   -> [0, 1, 1, 2]  (0 to itself=0, 0->1=1, 0->2=1, 0->1->3=2)
#
#   Key: Standard BFS with queue. Each level = distance + 1.

from collections import deque


# BFS Shortest Reach (HackerRank) -- Medium
# Input:  n: int (nodes 0..n-1), edges: List[[u,v]] (undirected), start: int
# Output: List[int] (shortest distance from start to each node, -1 if unreachable)
# Find shortest distances from a start node to all others in unweighted graph.
#
#   Key: Standard BFS. Distance = level * edge_weight.

def bfs_shortest(n, edges, start):
    """Return list of shortest distances from start to all nodes. -1 if unreachable."""
    pass


run_tests(bfs_shortest, [
    ((4, [[0,1],[0,2],[1,3]], 0),       [0,1,1,2]),
    ((3, [[0,1]], 0),                   [0,1,-1]),     # node 2 unreachable
    ((1, [], 0),                        [0]),           # single node
    ((5, [[0,1],[1,2],[2,3],[3,4]], 0), [0,1,2,3,4]),  # chain
    ((4, [[0,1],[2,3]], 0),             [0,1,-1,-1]),   # disconnected
    ((3, [[0,1],[1,2],[0,2]], 0),       [0,1,1]),       # triangle
])
