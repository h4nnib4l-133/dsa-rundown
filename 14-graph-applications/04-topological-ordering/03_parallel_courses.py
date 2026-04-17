import os, sys
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))
from test_runner import run_tests


# Parallel Courses (LC #1136) -- Medium
# Input:  n: int, relations: List[[prereq, course]]
# Output: int (min semesters to finish all courses, -1 if impossible)
# Each semester take ALL courses whose prereqs are satisfied.
#
# Example:
# #   n=3, [[1,3],[2,3]]  -> 2  (sem 1: {1,2}; sem 2: {3})
#   n=3, cycle -> -1
#
#   WHY THIS IS A TOPOLOGICAL SORT (levels):
#   BFS topsort but count LEVELS (not positions). Each BFS level = one semester.
#
#   Key: Kahn's BFS with level counting. Initialize queue with all indegree-0 nodes.
#        Each level = semester. If processed < n, cycle exists.

def minimum_semesters(n, relations):
    pass

run_tests(minimum_semesters, [
    ((3, [[1,3],[2,3]]),            2),
    ((3, [[1,2],[2,3],[3,1]]),     -1),
    ((3, [[1,2],[2,3]]),            3),
    ((1, []),                       1),
])
