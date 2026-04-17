import os, sys
_d = os.path.dirname(os.path.abspath(__file__))
while _d and not os.path.exists(os.path.join(_d, 'test_runner.py')):
    _d = os.path.dirname(_d)
sys.path.insert(0, _d)
from test_runner import run_tests


# Sudoku Solver (LC #37) -- Hard
# Input:  board: List[List[str]] (9x9, '.' = empty, '1'-'9' = filled)
# Output: None (modify board in-place to solve)
# Fill valid Sudoku board.
#
#   Key: Find empty cell, try 1-9, validate row/col/box, backtrack if stuck.

def solve_sudoku(board):
    """Modify board in-place"""
    pass


# Test: check the solved board is valid
def validate(board):
    solve_sudoku(board)
    for i in range(9):
        row = set()
        col = set()
        for j in range(9):
            if board[i][j] in row: return False
            row.add(board[i][j])
            if board[j][i] in col: return False
            col.add(board[j][i])
    return True


board1 = [
    ["5","3",".",".","7",".",".",".","."],
    ["6",".",".","1","9","5",".",".","."],
    [".","9","8",".",".",".",".","6","."],
    ["8",".",".",".","6",".",".",".","3"],
    ["4",".",".","8",".","3",".",".","1"],
    ["7",".",".",".","2",".",".",".","6"],
    [".","6",".",".",".",".","2","8","."],
    [".",".",".","4","1","9",".",".","5"],
    [".",".",".",".","8",".",".","7","9"]
]

run_tests(validate, [
    ((board1,), True),
])
