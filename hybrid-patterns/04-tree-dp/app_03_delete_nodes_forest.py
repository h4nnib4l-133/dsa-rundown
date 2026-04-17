import os, sys
_d = os.path.dirname(os.path.abspath(__file__))
while _d and not os.path.exists(os.path.join(_d, 'test_runner.py')):
    _d = os.path.dirname(_d)
sys.path.insert(0, _d)
from test_runner import run_tests


# Delete Nodes and Return Forest (LC #1110) -- Medium
# Input:  root: TreeNode, to_delete: List[int]
# Output: List[TreeNode] (roots of remaining forest after deletions)
# Delete specified nodes. Resulting trees form a forest.
#
# Example:
# #   root=[1,2,3,4,5,6,7], to_delete=[3,5]
#   -> 3 trees: [1,2,None,4], [6], [7]
#
#   Pattern: TREE DP + SET LOOKUP
#   Key: DFS. If node should be deleted, its children become new forest roots (if they exist).
#        Return 'self if not deleted, else None' so parent can disconnect.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val; self.left = left; self.right = right


def make_tree(arr):
    if not arr or arr[0] is None:
        return None
    from collections import deque
    root = TreeNode(arr[0])
    q = deque([root]); i = 1
    while q and i < len(arr):
        node = q.popleft()
        if i < len(arr) and arr[i] is not None:
            node.left = TreeNode(arr[i]); q.append(node.left)
        i += 1
        if i < len(arr) and arr[i] is not None:
            node.right = TreeNode(arr[i]); q.append(node.right)
        i += 1
    return root


def del_nodes(root, to_delete):
    pass


def solve(arr, to_delete):
    roots = del_nodes(make_tree(arr), to_delete)
    # return sorted list of root values for deterministic comparison
    return sorted([r.val for r in roots] if roots else [])

run_tests(del_nodes, [
    (([1,2,3,4,5,6,7], [3,5]),  [1,6,7]),
    (([1,2,4,None,3], [3]),     [1]),
    (([1,2,3], [1,2,3]),         []),
])
