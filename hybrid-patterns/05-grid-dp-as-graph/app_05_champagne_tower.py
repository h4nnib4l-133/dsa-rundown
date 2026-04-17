import os, sys
_d = os.path.dirname(os.path.abspath(__file__))
while _d and not os.path.exists(os.path.join(_d, 'test_runner.py')):
    _d = os.path.dirname(_d)
sys.path.insert(0, _d)
from test_runner import run_tests


# Champagne Tower (LC #799) -- Medium
# Input:  poured: int, query_row: int, query_glass: int
# Output: float (fraction of glass (query_row, query_glass) that is full)
# Champagne tower. Pour overflows to two glasses below.
#
# Example:
# #   poured=2, query_row=1, query_glass=1  -> 0.5
#
#   Pattern: GRID DP (simulation)
#   Key: Simulate row by row. Each glass holds up to 1.0. Excess overflows equally
#        to the two glasses below. dp[r][c] = amount received at (r,c).

def champagne_tower(poured, query_row, query_glass):
    pass


def solve(poured, query_row, query_glass):
    return round(champagne_tower(poured, query_row, query_glass), 5)

run_tests(champagne_tower, [
    ((1, 1, 1),     0.0),
    ((2, 1, 1),     0.5),
    ((100000009, 33, 17),  1.0),
])
