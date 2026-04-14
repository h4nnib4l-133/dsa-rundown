import sys, os; sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from test_runner import run_tests


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
    (([[2,4],[1,3],[2,4],[1,3]],), True),
    (([[],],),                     True),
])
