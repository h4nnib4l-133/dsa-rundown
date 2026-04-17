import os, sys
_d = os.path.dirname(os.path.abspath(__file__))
while _d and not os.path.exists(os.path.join(_d, 'test_runner.py')):
    _d = os.path.dirname(_d)
sys.path.insert(0, _d)
from test_runner import run_tests


# Word Search (LC #79) -- Medium
# Input:  board: List[List[str]] (m x n grid of chars), word: str
# Output: bool (True if word exists following adjacent cells)
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
