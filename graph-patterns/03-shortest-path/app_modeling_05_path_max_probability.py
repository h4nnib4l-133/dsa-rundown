import os, sys
_d = os.path.dirname(os.path.abspath(__file__))
while _d and not os.path.exists(os.path.join(_d, 'test_runner.py')):
    _d = os.path.dirname(_d)
sys.path.insert(0, _d)
from test_runner import run_tests


# Path With Maximum Probability (LC #1514) -- Medium
# Input:  n: int, edges: List[[u,v]], succProb: List[float], start: int, end: int
# Output: float (max probability of reaching end from start, 0.0 if impossible)
# Each edge has success probability. Path probability = product of edge probs.
# Find maximum probability path.
#
# Example:
# #   n=3, edges=[[0,1],[1,2],[0,2]], succProb=[0.5,0.5,0.2], start=0, end=2
#   -> 0.25   (via 0->1->2: 0.5*0.5=0.25; direct: 0.2; pick max)
#
#   WHY THIS IS A MODIFIED DIJKSTRA:
#   Non-obvious: Dijkstra for MAX instead of MIN. Use max-heap.
#   Relaxation: instead of dist[u]+w, use prob[u]*p (multiplication).
#   Initial prob = 1.0 at start.
#
#   Key: Max-heap of (-probability, node) since Python heap is min-heap.
#        For each neighbor: new_prob = curr_prob * edge_prob. If better, push.

def max_probability(n, edges, succ_prob, start, end):
    pass


def solve(n, edges, succ_prob, start, end):
    # allow small tolerance
    result = max_probability(n, edges, succ_prob, start, end)
    return round(result, 5)

run_tests(max_probability, [
    ((3, [[0,1],[1,2],[0,2]], [0.5,0.5,0.2], 0, 2),  0.25),
    ((3, [[0,1],[1,2],[0,2]], [0.5,0.5,0.3], 0, 2),  0.3),
    ((3, [[0,1]], [0.5], 0, 2),                       0.0),
    ((2, [[0,1]], [0.5], 0, 1),                       0.5),
])
