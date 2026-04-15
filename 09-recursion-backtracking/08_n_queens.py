import sys, os; sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from test_runner import run_tests



# N-Queens (LC #51) -- Hard
# Input:  n: int (board size n x n)
# Output: int (number of valid queen placements)
# Place N queens on NxN board so no two queens attack each other.
# Return the NUMBER of distinct solutions.
# (Queens attack same row, column, or diagonal.)
#
# Example:
#   n=4 -> 2 solutions:
#     . Q . .     . . Q .
#     . . . Q     Q . . .
#     Q . . .     . . . Q
#     . . Q .     . Q . .
#
#   n=1 -> 1, n=8 -> 92
#
#   Key: Place queen row by row. Track occupied columns, diagonals (row-col),
#        and anti-diagonals (row+col) in sets. Backtrack when no valid column.

def solve_n_queens(n):
    """Return number of solutions"""
    pass


run_tests(solve_n_queens, [
    ((1,),   1),
    ((4,),   2),
    ((5,),  10),
    ((8,),  92),
    ((2,),   0),     # impossible
    ((3,),   0),     # impossible
])
