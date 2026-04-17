import os, sys
_d = os.path.dirname(os.path.abspath(__file__))
while _d and not os.path.exists(os.path.join(_d, 'test_runner.py')):
    _d = os.path.dirname(_d)
sys.path.insert(0, _d)
from test_runner import run_tests


# Diameter of Binary Tree (LC #543) -- Easy
# Input:  root: TreeNode
# Output: int (length of longest path between any two nodes)
# Path may or may not pass through root. Length = # of edges.
#
# Example:
# #   [1,2,3,4,5]  -> 3   (path 4->2->1->3 or 5->2->1->3)
#
#   Pattern: TREE DP (post-order)
#   Key: DFS returns depth of subtree.
#        At each node, update global max with left_depth + right_depth.

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


def diameter_of_binary_tree(root):
    pass


def solve(arr):
    return diameter_of_binary_tree(make_tree(arr))

run_tests(diameter_of_binary_tree, [
    (([1,2,3,4,5],),  3),
    (([1,2],),        1),
    (([1],),          0),
    (([],),           0),
])
