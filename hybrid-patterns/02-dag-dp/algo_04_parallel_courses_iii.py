import os, sys
_d = os.path.dirname(os.path.abspath(__file__))
while _d and not os.path.exists(os.path.join(_d, 'test_runner.py')):
    _d = os.path.dirname(_d)
sys.path.insert(0, _d)
from test_runner import run_tests


# Parallel Courses III (LC #2050) -- Hard
# Input:  n: int, relations: List[[prev, next]], time: List[int]
# Output: int (min months to finish all with unlimited parallelism)
# Courses have durations. Can take in parallel if prereqs satisfied.
#
# Example:
# #   n=3, relations=[[1,3],[2,3]], time=[3,2,5]  -> 8   (1 and 2 parallel; then 3)
#
#   Pattern: TOPSORT + DP
#   Key: completion[v] = max(completion[u] for predecessors) + time[v].
#        Process in topo order.

def minimum_time_all_courses(n, relations, time):
    pass

run_tests(minimum_time_all_courses, [
    ((3, [[1,3],[2,3]], [3,2,5]),                      8),
    ((5, [[1,5],[2,5],[3,5],[3,4],[4,5]], [1,2,3,4,5]),  12),
    ((1, [], [100]),                                   100),
])
