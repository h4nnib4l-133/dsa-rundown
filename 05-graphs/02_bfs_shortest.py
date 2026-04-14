import sys, os; sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from test_runner import run_tests
from collections import deque


def bfs_shortest(n, edges, start):
    """Return list of shortest distances from start to all nodes. -1 if unreachable."""
    pass


run_tests(bfs_shortest, [
    ((4, [[0,1],[0,2],[1,3]], 0),  [0,1,1,2]),
    ((3, [[0,1]], 0),              [0,1,-1]),
    ((1, [], 0),                   [0]),
])
