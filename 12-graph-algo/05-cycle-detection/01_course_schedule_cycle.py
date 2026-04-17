import os, sys
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))
from test_runner import run_tests


# Course Schedule (LC #207) -- Medium
# Input:  numCourses: int, prerequisites: List[[a,b]] (b before a)
# Output: bool (True if can finish all courses, i.e. no cycle in directed graph)
# Directed graph cycle detection.
#
# Example:
# #   2, [[1,0],[0,1]]  -> False  (cycle)
#   2, [[1,0]]        -> True
#
#   Key: Approach 1: Kahn's BFS. If processed count < numCourses, cycle.
#        Approach 2: DFS with 3 colors (white=unvisited, gray=in-stack, black=done).
#        Gray neighbor encountered = back edge = cycle.

def can_finish(num_courses, prerequisites):
    pass

run_tests(can_finish, [
    ((2, [[1,0]]),             True),
    ((2, [[1,0],[0,1]]),       False),
    ((1, []),                  True),
    ((4, [[1,0],[2,1],[3,2]]), True),
    ((3, [[0,1],[1,2],[2,0]]), False),
])
