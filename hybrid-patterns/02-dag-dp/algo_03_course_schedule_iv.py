import os, sys
_d = os.path.dirname(os.path.abspath(__file__))
while _d and not os.path.exists(os.path.join(_d, 'test_runner.py')):
    _d = os.path.dirname(_d)
sys.path.insert(0, _d)
from test_runner import run_tests


# Course Schedule IV (LC #1462) -- Medium
# Input:  numCourses: int, prerequisites: List[[a,b]], queries: List[[u,v]]
# Output: List[bool] (for each query: is u a prereq of v?)
# For each query, check transitive reachability.
#
# Example:
# #   n=2, prereqs=[[1,0]], queries=[[0,1],[1,0]]  -> [False, True]
#
#   Pattern: TRANSITIVE CLOSURE (Floyd-Warshall or toposort+DP)
#   Key: reach[i][j] = True if i is prereq of j (direct or transitive).
#        Toposort then propagate. Or Floyd-Warshall O(n^3).

def check_if_prerequisite(num_courses, prerequisites, queries):
    pass

run_tests(check_if_prerequisite, [
    ((2, [[1,0]], [[0,1],[1,0]]),                [False, True]),
    ((2, [], [[1,0],[0,1]]),                     [False, False]),
    ((3, [[1,2],[1,0],[2,0]], [[1,0],[1,2]]),   [True, True]),
])
