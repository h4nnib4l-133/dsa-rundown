import os, sys
_d = os.path.dirname(os.path.abspath(__file__))
while _d and not os.path.exists(os.path.join(_d, 'test_runner.py')):
    _d = os.path.dirname(_d)
sys.path.insert(0, _d)
from test_runner import run_tests


# Knight Probability in Chessboard (LC #688) -- Medium
# Input:  n: int (board size), k: int (moves), row: int, column: int
# Output: float (probability knight still on board after k moves)
# Knight makes k moves (8 choices uniformly at random each).
# Probability it remains on board.
#
# Example:
# #   n=3, k=2, row=0, column=0  -> 0.0625
#
#   Pattern: GRID DP + PROBABILITY
#   Key: dp[k][r][c] = probability knight is at (r,c) after k moves from start.
#        Sum probabilities at all on-board cells after k moves.

def knight_probability(n, k, row, column):
    pass


def solve(n, k, row, column):
    return round(knight_probability(n, k, row, column), 5)

run_tests(knight_probability, [
    ((3, 2, 0, 0),  0.0625),
    ((1, 0, 0, 0),  1.0),
    ((8, 30, 6, 4), 0.00019),     # approx; adjust tolerance
])
