import sys, os; sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from test_runner import run_tests

# Network Delay Time (LC #743) -- Medium
# n nodes, weighted directed edges. Signal sent from node k.
# Return min time for ALL nodes to receive signal, or -1 if impossible.
#
# Example:
#   times=[[2,1,1],[2,3,1],[3,4,1]], n=4, k=2
#   Node 2 -> 1 (time 1), 2 -> 3 (time 1), 3 -> 4 (time 2)
#   All reached by time 2. -> 2
#
#   Key: Dijkstra's algorithm. Min-heap of (distance, node).
#        Answer = max of all shortest distances. -1 if any unreachable.

import heapq


# Network Delay Time (LC #743) -- Medium
# Min time for signal to reach all nodes from source.
#
#   Key: Dijkstra's algorithm. Answer = max of all shortest distances.

def network_delay_time(times, n, k):
    """times[i] = [u, v, w]. Return min time to reach all nodes from k, or -1."""
    pass


run_tests(network_delay_time, [
    (([[2,1,1],[2,3,1],[3,4,1]], 4, 2),   2),
    (([[1,2,1]], 2, 1),                    1),     # direct edge
    (([[1,2,1]], 2, 2),                   -1),     # can't reach node 1 from 2
    (([[1,2,1],[2,3,2],[1,3,4]], 3, 1),    3),     # shorter path: 1->2->3 = 3 < 1->3 = 4
    (([[1,2,1],[2,1,1]], 2, 1),            1),     # bidirectional
])
