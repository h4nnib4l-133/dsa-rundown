import os, sys
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))
from test_runner import run_tests


# Surrounded Regions (LC #130) -- Medium
# Input:  board: List[List[str]] ('X' or 'O', modify in-place)
# Output: None (flip all 'O's COMPLETELY surrounded by 'X' to 'X')
# 'O's on the border and any 'O' connected to them stay.
# All other 'O's (fully surrounded) become 'X'.
#
# Trick: REVERSE THINKING. Start from border 'O's and mark them safe. Flip the rest.
#
# Example:
# #   X X X X         X X X X
#   X O O X   ->    X X X X   (inner O's surrounded -> flip)
#   X X O X         X X X X
#   X O X X         X O X X   (border O stays)
#
#   Key: 1. BFS/DFS from every border 'O', mark safe (e.g. to 'S').
#        2. Flip remaining 'O' -> 'X'. Flip 'S' -> 'O'.

def solve_surrounded(board):
    pass


def run(board):
    solve_surrounded(board)
    return board

run_tests(run, [
    (([["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]],),
     [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]),
    (([["X"]],),  [["X"]]),
    (([["O"]],),  [["O"]]),
])
