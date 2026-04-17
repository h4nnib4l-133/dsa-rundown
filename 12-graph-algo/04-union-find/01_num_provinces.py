import os, sys
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))
from test_runner import run_tests


# Number of Provinces (LC #547) -- Medium
# Input:  isConnected: List[List[int]] (symmetric adjacency matrix)
# Output: int (number of provinces = connected components)
# Connected components via Union-Find.
#
# Example:
# #   [[1,1,0],[1,1,0],[0,0,1]]  -> 2
#   [[1,0,0],[0,1,0],[0,0,1]]  -> 3
#
#   Key: Union-Find. Union i,j when isConnected[i][j] == 1.
#        Count unique roots at end.

def find_circle_num(is_connected):
    pass

run_tests(find_circle_num, [
    (([[1,1,0],[1,1,0],[0,0,1]],),   2),
    (([[1,0,0],[0,1,0],[0,0,1]],),   3),
    (([[1]],),                       1),
    (([[1,1,1],[1,1,1],[1,1,1]],),  1),
])
