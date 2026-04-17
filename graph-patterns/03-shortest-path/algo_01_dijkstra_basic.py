import os, sys
_d = os.path.dirname(os.path.abspath(__file__))
while _d and not os.path.exists(os.path.join(_d, 'test_runner.py')):
    _d = os.path.dirname(_d)
sys.path.insert(0, _d)
from test_runner import run_tests


# Network Delay Time (LC #743) -- Medium
# Input:  times: List[[u,v,w]] (directed), n: int, k: int (source)
# Output: int (max time to reach all nodes, -1 if unreachable)
# Standard Dijkstra. Answer = max of shortest distances from source.
#
# Example:
# #   times=[[2,1,1],[2,3,1],[3,4,1]], n=4, k=2  -> 2
#
#   Key: Min-heap of (dist, node). Pop smallest, relax neighbors.
#        Return max of final distances, -1 if any is infinity.

def network_delay_time(times, n, k):
    pass

run_tests(network_delay_time, [
    (([[2,1,1],[2,3,1],[3,4,1]], 4, 2),    2),
    (([[1,2,1]], 2, 1),                      1),
    (([[1,2,1]], 2, 2),                     -1),
])
