import os, sys
_d = os.path.dirname(os.path.abspath(__file__))
while _d and not os.path.exists(os.path.join(_d, 'test_runner.py')):
    _d = os.path.dirname(_d)
sys.path.insert(0, _d)
from test_runner import run_tests


# Paint House (LC #256) -- Medium
# Input:  costs: List[List[int]] (n x 3 matrix; cost[i][j] = cost to paint house i color j)
# Output: int (min total cost, no two adjacent houses same color)
# 3 colors. No two adjacent houses can share a color. Minimize total cost.
#
# Example:
# #   [[17,2,17],[16,16,5],[14,3,19]]  -> 10   (2+5+3)
#
#   WHY THIS IS A STATE MACHINE DP:
#   Each house has 3 states (colors). Transition depends on previous color.
#   dp[i][c] = min cost for first i houses with house i painted color c.
#
#   Key: dp[i][0] = costs[i][0] + min(dp[i-1][1], dp[i-1][2])
#        Similar for colors 1, 2. Return min(dp[n-1]).

def min_cost(costs):
    pass

run_tests(min_cost, [
    (([[17,2,17],[16,16,5],[14,3,19]],), 10),
    (([[7,6,2]],),                         2),
    (([[1,2,3],[1,2,3]],),                 3),
])
