import os, sys
_d = os.path.dirname(os.path.abspath(__file__))
while _d and not os.path.exists(os.path.join(_d, 'test_runner.py')):
    _d = os.path.dirname(_d)
sys.path.insert(0, _d)
from test_runner import run_tests


# Number of Provinces (LC #547) -- Medium
# Input:  isConnected: List[List[int]] (n x n symmetric matrix)
# Output: int (number of connected components)
# Cities with bidirectional connections. Province = group of directly or
# indirectly connected cities. Count provinces.
#
# Example:
# #   [[1,1,0],[1,1,0],[0,0,1]]  -> 2 (cities {0,1} and {2})
#
#   WHY THIS IS A CONNECTED COMPONENTS:
#   Graph is given as adjacency matrix. Count connected components
#   via DFS/BFS (or Union-Find).
#
#   Key: For each unvisited city, DFS marks all in its component. Increment count.

def find_circle_num(is_connected):
    pass

run_tests(find_circle_num, [
    (([[1,1,0],[1,1,0],[0,0,1]],),   2),
    (([[1,0,0],[0,1,0],[0,0,1]],),   3),
    (([[1]],),                       1),
    (([[1,1,1],[1,1,1],[1,1,1]],),  1),
])
