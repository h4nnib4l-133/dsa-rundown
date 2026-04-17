import os, sys
_d = os.path.dirname(os.path.abspath(__file__))
while _d and not os.path.exists(os.path.join(_d, 'test_runner.py')):
    _d = os.path.dirname(_d)
sys.path.insert(0, _d)
from test_runner import run_tests


# Course Schedule II (LC #210) -- Medium
# Input:  numCourses: int, prerequisites: List[[a,b]] (b before a)
# Output: List[int] (valid course ordering, or [] if impossible)
# Return a valid ordering of courses.
#
# Example:
# #   2, [[1,0]]         -> [0,1]
#   4, [[1,0],[2,0],[3,1],[3,2]]  -> [0,2,1,3] or [0,1,2,3]
#   2, [[1,0],[0,1]]   -> [] (cycle)
#
#   Key: Kahn's algorithm: BFS with indegree array.
#        Start with all indegree-0 nodes. Add to result. Decrement neighbors.
#        If result size != numCourses, cycle exists.

def find_order(num_courses, prerequisites):
    pass


def solve(num_courses, prerequisites):
    # result order varies; just check validity
    result = find_order(num_courses, prerequisites)
    if not result:
        return len(result) == 0 and num_courses > 0 and any(True for _ in prerequisites)
    if len(result) != num_courses:
        return False
    pos = {c: i for i, c in enumerate(result)}
    for a, b in prerequisites:
        if pos[b] >= pos[a]:
            return False
    return True

run_tests(find_order, [
    ((2, [[1,0]]),                         True),
    ((4, [[1,0],[2,0],[3,1],[3,2]]),       True),
    ((2, [[1,0],[0,1]]),                   False),
    ((1, []),                              True),
])
