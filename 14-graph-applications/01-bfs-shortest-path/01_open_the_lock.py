import os, sys
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))
from test_runner import run_tests


# Open the Lock (LC #752) -- Medium
# Input:  deadends: List[str] (forbidden codes), target: str (4-digit)
# Output: int (min turns to reach target from '0000', -1 if impossible)
# Lock has 4 wheels, each with digits 0-9. Each turn rotates one wheel by 1.
# You start at '0000'. Some codes are deadends (can't be there).
# Find min turns to reach target.
#
# Example:
# #   deadends=["0201","0101","0102","1212","2002"], target="0202" -> 6
#   deadends=["8888"], target="0009" -> 1   (rotate 4th wheel once: 0->9)
#
#   WHY THIS IS A BFS SHORTEST PATH:
#   States are 4-digit codes. Each state connects to 8 neighbors (each wheel +1 or -1).
#   Min turns = shortest path from '0000' to target. BFS because unweighted.
#
#   Key: BFS from '0000'. Generate 8 neighbors per state. Skip deadends/visited.
#        Return level when you reach target.

def open_lock(deadends, target):
    pass

run_tests(open_lock, [
    ((["0201","0101","0102","1212","2002"], "0202"),  6),
    ((["8888"], "0009"),                                1),
    ((["8887","8889","8878","8898","8788","8988","7888","9888"], "8888"), -1),
    (([], "0000"),                                      0),
    ((["0000"], "8888"),                               -1),     # start is deadend
])
