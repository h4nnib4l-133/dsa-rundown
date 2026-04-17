import os, sys
_d = os.path.dirname(os.path.abspath(__file__))
while _d and not os.path.exists(os.path.join(_d, 'test_runner.py')):
    _d = os.path.dirname(_d)
sys.path.insert(0, _d)
from test_runner import run_tests


# Bus Routes (LC #815) -- Hard
# Input:  routes: List[List[int]] (routes[i] = stops on bus i), source: int, target: int
# Output: int (min buses to take, -1 if impossible)
# Each bus has a fixed circular route. You start at source, want target.
# Count MINIMUM BUSES (not stops) to reach target.
#
# Example:
# #   routes=[[1,2,7],[3,6,7]], source=1, target=6  -> 2
#     (bus 1 at stop 1 -> stop 7; transfer to bus 2 at stop 7 -> stop 6)
#
#   WHY THIS IS A BFS SHORTEST PATH (unusual modeling):
#   Don't model stops as nodes -- model BUSES as nodes. Two buses connect if they
#   share a stop. BFS counts buses (each level = one more bus).
#   This reframing is the clever insight.
#
#   Key: 1. For each stop, find which buses visit it (stop -> list of bus ids).
#        2. BFS from 'buses containing source'. Each level = one bus ride.
#        3. Stop when any current bus contains target.

def num_buses_to_destination(routes, source, target):
    pass

run_tests(num_buses_to_destination, [
    (([[1,2,7],[3,6,7]], 1, 6),         2),
    (([[7,12],[4,5,15],[6],[15,19],[9,12,13]], 15, 12),  -1),
    (([[1,2,3]], 1, 3),                 1),
    (([[1,2,3]], 1, 1),                 0),     # already there
])
