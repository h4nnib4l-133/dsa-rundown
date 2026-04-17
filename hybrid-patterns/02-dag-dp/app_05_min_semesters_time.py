import os, sys
_d = os.path.dirname(os.path.abspath(__file__))
while _d and not os.path.exists(os.path.join(_d, 'test_runner.py')):
    _d = os.path.dirname(_d)
sys.path.insert(0, _d)
from test_runner import run_tests


# Minimum Time to Complete All Tasks with Prereqs (custom) -- Medium
# Input:  n: int, deps: List[[a,b]] (a must finish before b), time: List[int]
# Output: int (min time, unlimited parallelism)
# Like Parallel Courses III but here presented with different phrasing.
#
# Example:
# #   n=3, deps=[[0,2],[1,2]], time=[3,2,5]  -> 8
#
#   Pattern: DAG DP
#   Key: finish[v] = max(finish[u] for predecessors u) + time[v]. Topsort, then DP.

def min_total_time(n, deps, time):
    pass

run_tests(min_total_time, [
    ((3, [[0,2],[1,2]], [3,2,5]),                8),
    ((1, [], [10]),                               10),
    ((3, [[0,1],[1,2]], [1,1,1]),                 3),
])
