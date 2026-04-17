import os, sys
_d = os.path.dirname(os.path.abspath(__file__))
while _d and not os.path.exists(os.path.join(_d, 'test_runner.py')):
    _d = os.path.dirname(_d)
sys.path.insert(0, _d)
from test_runner import run_tests



# Course Schedule (LC #207) -- Medium
# Input:  numCourses: int, prerequisites: List[[course, prereq]]
# Output: bool (True if all courses can be finished, i.e. no cycle)
# There are numCourses courses. prerequisites[i] = [a, b] means
# you must take course b before course a.
# Return True if you can finish all courses (no cycle in dependency graph).
#
# Example:
#   numCourses=2, prereqs=[[1,0]]       -> True  (take 0 then 1)
#   numCourses=2, prereqs=[[1,0],[0,1]] -> False (circular dependency)
#
#   Key: Cycle detection in directed graph.
#        Kahn's algo: BFS with indegree. If processed count == numCourses, no cycle.
#        Or DFS with 3 colors (white/gray/black).

def can_finish(num_courses, prerequisites):
    pass


run_tests(can_finish, [
    ((2, [[1,0]]),            True),      # simple chain
    ((2, [[1,0],[0,1]]),      False),     # cycle
    ((3, [[1,0],[2,1]]),      True),      # chain of 3
    ((1, []),                 True),      # single course, no prereqs
    ((3, []),                 True),      # no prereqs at all
    ((4, [[1,0],[2,1],[3,2],[1,3]]), False),  # longer cycle
    ((5, [[1,0],[2,0],[3,1],[4,3]]), True),   # tree-like
])
