import os, sys
_d = os.path.dirname(os.path.abspath(__file__))
while _d and not os.path.exists(os.path.join(_d, 'test_runner.py')):
    _d = os.path.dirname(_d)
sys.path.insert(0, _d)
from test_runner import run_tests


# Cheapest Flights Within K Stops (LC #787) -- Medium
# Input:  n: int, flights: List[[u,v,w]], src: int, dst: int, k: int
# Output: int (cheapest price with at most k stops, -1 if impossible)
# Shortest path with hop constraint = Bellman-Ford with k+1 iterations.
#
# Example:
# #   n=3, flights=[[0,1,100],[1,2,100],[0,2,500]], src=0, dst=2, k=1 -> 200
#
#   Pattern: BELLMAN-FORD = DP
#   Key: dp[i][v] = min cost to reach v using at most i edges.
#        dp[i][v] = min(dp[i-1][u] + w(u,v)) for all edges.
#        Run k+1 iterations. Bellman-Ford IS DP on edges.

def find_cheapest_price(n, flights, src, dst, k):
    pass

run_tests(find_cheapest_price, [
    ((3, [[0,1,100],[1,2,100],[0,2,500]], 0, 2, 1),  200),
    ((3, [[0,1,100],[1,2,100],[0,2,500]], 0, 2, 0),  500),
    ((2, [[0,1,100]], 0, 1, 0),                      100),
    ((2, [], 0, 1, 5),                              -1),
])
