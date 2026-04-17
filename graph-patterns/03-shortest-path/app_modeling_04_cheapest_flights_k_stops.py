import os, sys
_d = os.path.dirname(os.path.abspath(__file__))
while _d and not os.path.exists(os.path.join(_d, 'test_runner.py')):
    _d = os.path.dirname(_d)
sys.path.insert(0, _d)
from test_runner import run_tests


# Cheapest Flights Within K Stops (LC #787) -- Medium
# Input:  n: int, flights: List[[u,v,price]], src: int, dst: int, k: int
# Output: int (cheapest price using at most k STOPS between, -1 if impossible)
# Find cheapest route with a hop-count constraint.
#
# Example:
# #   n=3, flights=[[0,1,100],[1,2,100],[0,2,500]], src=0, dst=2, k=1 -> 200
#   same with k=0 -> 500 (direct only)
#
#   WHY THIS IS A WEIGHTED GRAPH + CONSTRAINT:
#   Pure Dijkstra doesn't handle 'at most k edges' easily. Bellman-Ford's
#   k+1 iterations naturally encode this constraint -- classic trick.
#
#   Key: Bellman-Ford with k+1 iterations. In each iteration, use a COPY of prev dist
#        to avoid using multi-hop updates from same round.

def find_cheapest_price(n, flights, src, dst, k):
    pass

run_tests(find_cheapest_price, [
    ((3, [[0,1,100],[1,2,100],[0,2,500]], 0, 2, 1),  200),
    ((3, [[0,1,100],[1,2,100],[0,2,500]], 0, 2, 0),  500),
    ((2, [[0,1,100]], 0, 1, 0),                      100),
    ((2, [], 0, 1, 5),                              -1),
])
