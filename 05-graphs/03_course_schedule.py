import sys, os; sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from test_runner import run_tests


# Course Schedule (LC #207) -- Medium
# Can you finish all courses given prerequisites? (Cycle detection in directed graph)
#
#   Key: Topological sort with Kahn's algorithm. If sorted count != numCourses, cycle exists.
#   Alt: DFS with 3 colors (white/gray/black)

def can_finish(num_courses, prerequisites):
    pass


run_tests(can_finish, [
    ((2, [[1,0]]),         True),
    ((2, [[1,0],[0,1]]),   False),
    ((3, [[1,0],[2,1]]),   True),
    ((1, []),              True),
])
