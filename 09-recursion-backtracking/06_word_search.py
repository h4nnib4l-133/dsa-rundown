import sys, os; sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from test_runner import run_tests


# Word Search (LC #79) -- Medium
# Find if word exists in 2D grid following adjacent cells.
#
#   Key: DFS from each cell. Mark visited (set to '#'), restore after backtrack.

def exist(board, word):
    pass


run_tests(exist, [
    (([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCCED"), True),
    (([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "SEE"),    True),
    (([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCB"),   False),
])
