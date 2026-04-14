import sys, os; sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from test_runner import run_tests
import heapq


def network_delay_time(times, n, k):
    """times[i] = [u, v, w]. Return min time to reach all nodes from k, or -1."""
    pass


run_tests(network_delay_time, [
    (([[2,1,1],[2,3,1],[3,4,1]], 4, 2),  2),
    (([[1,2,1]], 2, 1),                   1),
    (([[1,2,1]], 2, 2),                  -1),
])
