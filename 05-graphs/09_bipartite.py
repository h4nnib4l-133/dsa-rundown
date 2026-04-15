import sys, os; sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from test_runner import run_tests


# Is Graph Bipartite? (LC #785) -- Medium
# Can graph be 2-colored?
#
#   Key: BFS/DFS coloring. If neighbor has same color, not bipartite.

def is_bipartite(graph):
    """graph[i] = list of neighbors of node i"""
    pass


run_tests(is_bipartite, [
    (([[1,2,3],[0,2],[0,1,3],[0,2]],),   False),
    (([[1,3],[0,2],[1,3],[0,2]],),       True),
    (([[],],),                            True),
])
