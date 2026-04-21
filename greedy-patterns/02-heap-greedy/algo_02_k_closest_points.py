import os, sys
_d = os.path.dirname(os.path.abspath(__file__))
while _d and not os.path.exists(os.path.join(_d, 'test_runner.py')):
    _d = os.path.dirname(_d)
sys.path.insert(0, _d)
from test_runner import run_tests


# K Closest Points to Origin (LC #973) -- Medium
# Input:  points: List[[x,y]], k: int
# Output: List[[x,y]] (k closest points to origin, any order)
# Find k points closest to (0,0) by Euclidean distance.
#
# Example:
# #   points=[[1,3],[-2,2]], k=1  -> [[-2,2]]
#
#   Greedy insight: Max-heap of size k (keep closest k). Or min-heap and pop k times.
#        Max-heap: for each point, push and pop if size > k. O(n log k).

def k_closest(points, k):
    pass


def solve(points, k):
    result = k_closest(points, k)
    return sorted(result)

run_tests(k_closest, [
    (([[1,3],[-2,2]], 1),              [[-2,2]]),
    (([[3,3],[5,-1],[-2,4]], 2),       [[-2,4],[3,3]]),
    (([[1,1]], 1),                      [[1,1]]),
    (([[0,1],[1,0]], 2),                [[0,1],[1,0]]),
])
