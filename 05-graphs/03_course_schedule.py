import sys, os; sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from test_runner import run_tests



# Course Schedule (LC #207) -- Medium
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
