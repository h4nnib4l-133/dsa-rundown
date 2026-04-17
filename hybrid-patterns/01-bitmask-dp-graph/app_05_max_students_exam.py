import os, sys
_d = os.path.dirname(os.path.abspath(__file__))
while _d and not os.path.exists(os.path.join(_d, 'test_runner.py')):
    _d = os.path.dirname(_d)
sys.path.insert(0, _d)
from test_runner import run_tests


# Maximum Students Taking Exam (LC #1349) -- Hard
# Input:  seats: List[List[str]] ('.' = good, '#' = broken)
# Output: int (max students seated with no cheating)
# Students cheat if sitting at L/R/UL/UR diagonal. Max seated.
#
# Example:
# #   [["#",".","#","#",".","#"],
#    [".","#","#","#","#","."],    -> 4
#    ["#",".","#","#",".","#"]]
#
#   Pattern: BITMASK DP (row by row)
#   Key: For each row, enumerate valid bitmasks (no LR neighbors, within good seats).
#        dp[row][mask] = max students with row set to mask, compatible with row-1.

def max_students(seats):
    pass

run_tests(max_students, [
    (([["#",".","#","#",".","#"],[".","#","#","#","#","."],["#",".","#","#",".","#"]],), 4),
    (([[".","#"],["#","."],["#","."],[".","#"]],),  3),
    (([["#",".",".",".","#"],[".","#",".","#","."],[".",".","#",".","."],[".","#",".","#","."],["#",".",".",".","#"]],), 10),
])
