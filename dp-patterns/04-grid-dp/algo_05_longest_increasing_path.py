import os, sys
_d = os.path.dirname(os.path.abspath(__file__))
while _d and not os.path.exists(os.path.join(_d, 'test_runner.py')):
    _d = os.path.dirname(_d)
sys.path.insert(0, _d)
from test_runner import run_tests


# Longest Increasing Path in Matrix (LC #329) -- Hard
# Input:  matrix: List[List[int]]
# Output: int (length of longest strictly increasing path, 4-directional)
# Find longest path where each step strictly increases.
#
# Pattern: DP + DFS with memoization.
#
# Example:
# #   [[9,9,4],
#    [6,6,8],    -> 4  (1->2->6->9)
#    [2,1,1]]
#
#   Key: memo[i][j] = 1 + max(dfs(neighbor) for neighbor > matrix[i][j]).
#        Since strictly increasing, no cycles possible.

def longest_increasing_path(matrix):
    pass

run_tests(longest_increasing_path, [
    (([[9,9,4],[6,6,8],[2,1,1]],),  4),
    (([[3,4,5],[3,2,6],[2,2,1]],),   4),
    (([[1]],),                        1),
    (([[1,2]],),                      2),
])
