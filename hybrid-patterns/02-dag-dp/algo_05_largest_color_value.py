import os, sys
_d = os.path.dirname(os.path.abspath(__file__))
while _d and not os.path.exists(os.path.join(_d, 'test_runner.py')):
    _d = os.path.dirname(_d)
sys.path.insert(0, _d)
from test_runner import run_tests


# Largest Color Value in DAG (LC #1857) -- Hard
# Input:  colors: str, edges: List[[u,v]]
# Output: int (max count of most-frequent color on any path, -1 if cycle)
# Directed graph. Find longest path's dominant color count.
#
# Example:
# #   colors="abaca", edges=[[0,1],[0,2],[2,3],[3,4]]  -> 3   ('a' appears 3 times on path 0->2->3->4)
#
#   Pattern: TOPSORT + COLOR COUNT DP
#   Key: dp[v][c] = max count of color c along any path ending at v.
#        On processing v: dp[v][c] = max(dp[u][c] for predecessors) + (1 if color[v]==c).
#        Answer = max over all (v, c). Cycle detection via Kahn's.

def largest_path_value(colors, edges):
    pass

run_tests(largest_path_value, [
    (("abaca", [[0,1],[0,2],[2,3],[3,4]]),  3),
    (("a", [[0,0]]),                          -1),
    (("aaa", [[0,1],[1,2]]),                  3),
])
