import os, sys
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))
from test_runner import run_tests


# Evaluate Division (LC #399) -- Medium
# Input:  equations: List[[a,b]], values: List[float], queries: List[[c,d]]
# Output: List[float] (c/d value from equations, -1.0 if unknown)
# equations[i] + values[i] tells you a/b = value.
# For each query, compute c/d using chained ratios if possible.
#
# Example:
# #   equations=[["a","b"],["b","c"]], values=[2.0,3.0]
#   queries=[["a","c"],["b","a"],["a","e"]]
#   -> [6.0, 0.5, -1.0]
#     (a/c = a/b * b/c = 2*3=6; b/a = 1/2 = 0.5; e not in graph -> -1)
#
#   WHY THIS IS A WEIGHTED GRAPH TRAVERSAL:
#   Variables are nodes. Each equation is a weighted edge (a -> b with weight value,
#   and b -> a with weight 1/value). Query = find product of weights along path c->d.
#   DFS/BFS multiplying weights.
#
#   Key: Build graph {node: {neighbor: ratio}}.
#        For each query, DFS from c multiplying ratios until you reach d.
#        Return product, or -1 if no path.

def calc_equation(equations, values, queries):
    pass

run_tests(calc_equation, [
    (([["a","b"],["b","c"]], [2.0,3.0], [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]),
     [6.0, 0.5, -1.0, 1.0, -1.0]),
    (([["a","b"]], [2.0], [["a","b"],["b","a"]]),
     [2.0, 0.5]),
    (([["a","b"],["c","d"]], [1.0, 2.0], [["a","c"]]),
     [-1.0]),     # disconnected components
])
