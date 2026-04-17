import os, sys
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))
from test_runner import run_tests


# Min Operations to Connect Network (LC #1319) -- Medium
# Input:  n: int (computers), connections: List[[a,b]]
# Output: int (min cable moves to connect all, -1 if impossible)
# Computers 0..n-1, some connected by cables. You can UNPLUG a cable and REPLUG elsewhere.
# Minimize moves to connect ALL computers.
#
# Example:
# #   n=4, connections=[[0,1],[0,2],[1,2]]     -> 1
#     (move the redundant cable between 1,2 to connect 3)
#   n=6, connections=[[0,1],[0,2],[0,3],[1,2]]  -> 2
#   n=6, connections=[[0,1],[0,2],[0,3]]         -> -1 (not enough cables)
#
#   WHY THIS IS A UNION-FIND (components):
#   Key insight: if you have C connected components, you need exactly C-1 moves.
#   But you only have extra cables (len(connections) - (n-1)) to work with.
#   Return C-1 if enough cables, else -1.
#
#   Key: 1. Need at least n-1 edges: if len(connections) < n-1, return -1.
#        2. Count components via Union-Find.
#        3. Return components - 1.

def make_connected(n, connections):
    pass

run_tests(make_connected, [
    ((4, [[0,1],[0,2],[1,2]]),              1),
    ((6, [[0,1],[0,2],[0,3],[1,2]]),        2),
    ((6, [[0,1],[0,2],[0,3]]),             -1),
    ((5, [[0,1],[0,2],[3,4],[2,3]]),        0),     # already connected
    ((1, []),                               0),
])
