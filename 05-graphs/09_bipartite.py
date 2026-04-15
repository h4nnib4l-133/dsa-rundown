import sys, os; sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from test_runner import run_tests



# Is Graph Bipartite? (LC #785) -- Medium
# Input:  graph: List[List[int]] (adjacency list, graph[i] = neighbors of i)
# Output: bool (True if graph is 2-colorable)
# Can you color the graph with 2 colors so no adjacent nodes share a color?
# graph[i] = list of neighbors of node i.
#
# Example:
#   graph = [[1,3],[0,2],[1,3],[0,2]]  -> True  (color: 0,1,0,1)
#   graph = [[1,2,3],[0,2],[0,1,3],[0,2]] -> False (triangle subgraph)
#
#   Key: BFS/DFS coloring. Assign color 0 to start, color 1 to neighbors.
#        If a neighbor already has the same color, not bipartite.

def is_bipartite(graph):
    """graph[i] = list of neighbors of node i"""
    pass


run_tests(is_bipartite, [
    (([[1,2,3],[0,2],[0,1,3],[0,2]],),     False),    # odd cycle
    (([[1,3],[0,2],[1,3],[0,2]],),         True),     # bipartite square
    (([[],],),                              True),     # single node
    (([[1],[0]],),                          True),     # single edge
    (([[1],[0,2],[1]],),                    True),     # chain of 3
    (([[1,2],[0,2],[0,1]],),               False),    # triangle
])
