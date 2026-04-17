import os, sys
_d = os.path.dirname(os.path.abspath(__file__))
while _d and not os.path.exists(os.path.join(_d, 'test_runner.py')):
    _d = os.path.dirname(_d)
sys.path.insert(0, _d)
from test_runner import run_tests


# Parallel Courses (LC #1136) -- Medium
# Input:  n: int, relations: List[[prev, next]] (prev before next)
# Output: int (min semesters to finish all, -1 if impossible)
# Each semester, take ALL courses whose prereqs are met.
# Return min semesters.
#
# Example:
# #   n=3, [[1,3],[2,3]]  -> 2   (sem 1: {1,2}, sem 2: {3})
#   n=3, [[1,2],[2,3],[3,1]]  -> -1 (cycle)
#
#   Key: Kahn's BFS. Each BFS level = 1 semester. Track semester count.
#        If processed < n, cycle exists.

def minimum_semesters(n, relations):
    pass

run_tests(minimum_semesters, [
    ((3, [[1,3],[2,3]]),                2),
    ((3, [[1,2],[2,3],[3,1]]),         -1),
    ((3, [[1,2],[2,3]]),                3),
    ((1, []),                           1),
])
