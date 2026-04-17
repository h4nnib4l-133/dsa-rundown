import os, sys
_d = os.path.dirname(os.path.abspath(__file__))
while _d and not os.path.exists(os.path.join(_d, 'test_runner.py')):
    _d = os.path.dirname(_d)
sys.path.insert(0, _d)
from test_runner import run_tests


# Sliding Puzzle (LC #773) -- Hard
# Input:  board: List[List[int]] (2x3 board, 0 is empty)
# Output: int (min moves to reach [[1,2,3],[4,5,0]], -1 if impossible)
# Classic sliding puzzle. Each move slides a tile into the empty cell.
#
# Example:
# #   [[1,2,3],[4,0,5]]    -> 1   (slide 5 left)
#   [[4,1,2],[5,0,3]]    -> 5
#   [[1,2,3],[5,4,0]]    -> -1
#
#   WHY THIS IS A BFS OVER STATE SPACE:
#   Non-obvious graph: nodes are BOARD STATES (serialized as strings).
#   Edges connect states reachable by one slide. BFS finds shortest path to goal.
#
#   Key: Serialize board to string. BFS from start state.
#        Neighbors: for each position of 0, swap with adjacent. Precompute adjacency per cell.

def sliding_puzzle(board):
    pass

run_tests(sliding_puzzle, [
    (([[1,2,3],[4,0,5]],),    1),
    (([[1,2,3],[5,4,0]],),   -1),
    (([[4,1,2],[5,0,3]],),    5),
    (([[1,2,3],[4,5,0]],),    0),     # already solved
])
