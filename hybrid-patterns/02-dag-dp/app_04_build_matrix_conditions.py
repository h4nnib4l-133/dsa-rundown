import os, sys
_d = os.path.dirname(os.path.abspath(__file__))
while _d and not os.path.exists(os.path.join(_d, 'test_runner.py')):
    _d = os.path.dirname(_d)
sys.path.insert(0, _d)
from test_runner import run_tests


# Build a Matrix with Conditions (LC #2392) -- Hard
# Input:  k: int, rowConditions: List[[a,b]], colConditions: List[[a,b]]
# Output: List[List[int]] (k x k matrix satisfying all conditions, [] if impossible)
# Place 1..k in matrix such that row and col orderings satisfy constraints.
#
# Example:
# #   k=3, rows=[[1,2],[3,2]], cols=[[2,1],[3,2]]
#   -> [[3,0,0],[0,0,1],[0,2,0]]
#
#   Pattern: TOPSORT (two separate)
#   Key: Topsort row conditions -> row_pos[i] = position of i in some row ordering.
#        Same for columns. If either has cycle, return [].
#        Place i at (row_pos[i], col_pos[i]).

def build_matrix(k, row_conditions, col_conditions):
    pass


def solve(k, row_conditions, col_conditions, should_succeed):
    result = build_matrix(k, row_conditions, col_conditions)
    if not should_succeed:
        return result == []
    if not result:
        return False
    # verify all 1..k present and constraints hold
    found = set()
    row_of = {}
    col_of = {}
    for r, row in enumerate(result):
        for c, v in enumerate(row):
            if v != 0:
                found.add(v)
                row_of[v] = r
                col_of[v] = c
    if found != set(range(1, k+1)):
        return False
    for a, b in row_conditions:
        if row_of[a] >= row_of[b]:
            return False
    for a, b in col_conditions:
        if col_of[a] >= col_of[b]:
            return False
    return True

run_tests(build_matrix, [
    ((3, [[1,2],[3,2]], [[2,1],[3,2]], True),   True),
    ((3, [[1,2],[2,3],[3,1]], [[2,1]], False),   True),
])
