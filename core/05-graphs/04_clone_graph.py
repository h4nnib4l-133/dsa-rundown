import os, sys
_d = os.path.dirname(os.path.abspath(__file__))
while _d and not os.path.exists(os.path.join(_d, 'test_runner.py')):
    _d = os.path.dirname(_d)
sys.path.insert(0, _d)
from test_runner import run_tests



# Clone Graph (LC #133) -- Medium
# Input:  node: GraphNode (.val: int, .neighbors: List[GraphNode])
# Output: GraphNode (deep copy of entire connected graph)
# Deep copy a connected undirected graph.
# Each node has val and list of neighbors.
# Must create new node objects (not reuse originals).
#
# Example:
#   Node 1 -- Node 2
#   |          |
#   Node 4 -- Node 3
#   -> New graph with same structure but all different objects.
#
#   Key: BFS/DFS with hashmap {original_node: clone_node}.
#        Visit each node, create clone, link neighbors via the map.

class GraphNode:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors else []


def clone_graph(node):
    pass


def solve(adj_list):
    if not adj_list:
        return True
    nodes = [GraphNode(i+1) for i in range(len(adj_list))]
    for i, neighbors in enumerate(adj_list):
        nodes[i].neighbors = [nodes[j-1] for j in neighbors]
    clone = clone_graph(nodes[0])
    # verify clone has same structure but different objects
    if clone is None:
        return False
    visited_orig = set()
    visited_clone = set()
    stack = [(nodes[0], clone)]
    while stack:
        o, c = stack.pop()
        if id(o) in visited_orig:
            continue
        visited_orig.add(id(o))
        visited_clone.add(id(c))
        if o.val != c.val or o is c:
            return False
        if len(o.neighbors) != len(c.neighbors):
            return False
        for on, cn in zip(o.neighbors, c.neighbors):
            stack.append((on, cn))
    return True


run_tests(solve, [
    (([[2,4],[1,3],[2,4],[1,3]],), True),   # 4-node square
    (([[],],),                     True),   # single node, no neighbors
    (([[2],[1,3],[2]],),           True),   # 3-node chain
])
