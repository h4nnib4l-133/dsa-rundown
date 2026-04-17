import os, sys
_d = os.path.dirname(os.path.abspath(__file__))
while _d and not os.path.exists(os.path.join(_d, 'test_runner.py')):
    _d = os.path.dirname(_d)
sys.path.insert(0, _d)
from test_runner import run_tests


# Path with Max Probability (LC #1514) -- Medium
# Input:  n: int, edges: List[[u,v]], succProb: List[float], start: int, end: int
# Output: float (max product of edge probabilities, 0.0 if unreachable)
# Edges have probabilities. Path probability = product.
#
# Example:
# #   edges=[[0,1],[1,2],[0,2]], p=[0.5,0.5,0.2], start=0, end=2 -> 0.25
#
#   Pattern: DIJKSTRA (MAX variant)
#   Key: Max-heap of (-prob, node). Relaxation multiplies instead of adding.
#        Start prob = 1.0. max-Dijkstra IS DP on expanding frontier.

def max_probability(n, edges, succ_prob, start, end):
    pass


def solve(n, edges, succ_prob, start, end):
    return round(max_probability(n, edges, succ_prob, start, end), 5)

run_tests(max_probability, [
    ((3, [[0,1],[1,2],[0,2]], [0.5,0.5,0.2], 0, 2),   0.25),
    ((3, [[0,1],[1,2],[0,2]], [0.5,0.5,0.3], 0, 2),   0.3),
    ((3, [[0,1]], [0.5], 0, 2),                        0.0),
])
