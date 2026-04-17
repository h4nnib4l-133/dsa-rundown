import os, sys
_d = os.path.dirname(os.path.abspath(__file__))
while _d and not os.path.exists(os.path.join(_d, 'test_runner.py')):
    _d = os.path.dirname(_d)
sys.path.insert(0, _d)
from test_runner import run_tests


# Travelling Salesman (small N) -- Hard
# Input:  dist: List[List[int]] (n x n distance matrix, n <= 15)
# Output: int (min tour cost starting and ending at node 0)
# Visit every city exactly once, return to start. Minimize total distance.
#
# Example:
# #   dist=[[0,10,15,20],[10,0,35,25],[15,35,0,30],[20,25,30,0]]
#   -> 80   (0->1->3->2->0)
#
#   Pattern: BITMASK DP
#   Key: dp[mask][i] = min cost ending at i having visited set mask.
#        dp[mask|1<<j][j] = min(dp[mask][i] + dist[i][j]) for j not in mask.
#        Answer = min(dp[full][i] + dist[i][0]).

def tsp(dist):
    pass

run_tests(tsp, [
    (([[0,10,15,20],[10,0,35,25],[15,35,0,30],[20,25,30,0]],),  80),
    (([[0,1],[1,0]],),  2),
    (([[0]],),          0),
])
