import sys, os; sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from test_runner import run_tests



# Copy List with Random Pointer (LC #138) -- Medium
# Input:  head: Node (each node has .val, .next, .random)
# Output: Node (deep copy, new objects with same structure)
# Deep copy a linked list where each node has next AND random pointer.
# Random can point to any node in the list or None.
#
# Example:
#   Node(7,null) -> Node(13,0) -> Node(11,4) -> ...
#   (random pointers shown as indices)
#   Must create entirely new nodes, not reuse originals.
#
#   Key: HashMap approach: {original_node: copy_node}.
#        Pass 1: create all copy nodes.
#        Pass 2: link next and random pointers.
#        Alt: Interleaving trick (no extra space).

class Node:
    def __init__(self, val=0, nxt=None, random=None):
        self.val = val
        self.next = nxt
        self.random = random


def copy_random_list(head):
    """Return deep copy of list with random pointers"""
    pass


# Test: build list, copy, verify values match and nodes are different objects
def solve(vals, random_indices):
    if not vals:
        return True
    nodes = [Node(v) for v in vals]
    for i in range(len(nodes)-1):
        nodes[i].next = nodes[i+1]
    for i, ri in enumerate(random_indices):
        nodes[i].random = nodes[ri] if ri is not None else None

    copy = copy_random_list(nodes[0])
    # verify
    orig, cp = nodes[0], copy
    for i in range(len(vals)):
        if cp is None or cp.val != orig.val:
            return False
        if cp is orig:  # same object = not a deep copy
            return False
        orig = orig.next
        cp = cp.next
    return True


run_tests(solve, [
    (([7,13,11,10,1], [None,0,4,2,0]),  True),
    (([1,2], [1,1]),                     True),
    (([],    []),                         True),     # empty list
    (([3,3,3], [None,0,None]),           True),      # some randoms None
])
