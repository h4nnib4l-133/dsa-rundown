import os, sys
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))
from test_runner import run_tests


# Cheapest Flights Within K Stops (LC #787) -- Medium
# Input:  n: int, flights: List[[u,v,w]], src: int, dst: int, k: int
# Output: int (cheapest price with at most k STOPS, -1 if impossible)
# Shortest path with edge count constraint.
# 'k stops' means path length <= k+1 edges.
#
# Pattern: Modified Dijkstra or Bellman-Ford (k iterations).
#
# Example:
# #   n=3, flights=[[0,1,100],[1,2,100],[0,2,500]], src=0, dst=2, k=1 -> 200
#   same but k=0 -> 500 (direct only)
#
#   Key: Bellman-Ford: run k+1 iterations. Use copy of previous dist to avoid
#        using updates from same iteration.

def find_cheapest_price(n, flights, src, dst, k):
    pass

run_tests(find_cheapest_price, [
    ((3, [[0,1,100],[1,2,100],[0,2,500]], 0, 2, 1),  200),
    ((3, [[0,1,100],[1,2,100],[0,2,500]], 0, 2, 0),  500),
    ((2, [[0,1,100]], 0, 1, 0),                      100),
    ((2, [], 0, 1, 5),                              -1),
])
