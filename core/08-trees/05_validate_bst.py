import os, sys
_d = os.path.dirname(os.path.abspath(__file__))
while _d and not os.path.exists(os.path.join(_d, 'test_runner.py')):
    _d = os.path.dirname(_d)
sys.path.insert(0, _d)
from test_runner import run_tests

# Validate Binary Search Tree (LC #98) -- Medium
# Check if binary tree is a valid BST.
# BST rule: left subtree values < node < right subtree values (all nodes, not just children).
#
# Example:
#     2
#    / \
#   1   3    -> True
#
#     5
#    / \
#   1   4    -> False (4 < 5 but 4 is right child)
#      / \
#     3   6
#
#   Key: Pass valid range (min, max) to each node.
#        Or: inorder traversal must be strictly increasing.

from collections import deque


# Validate BST (LC #98) -- Medium
# Input:  root: TreeNode
# Output: bool (True if valid BST: left < node < right for ALL descendants)
# Is the tree a valid BST?
#
#   Key: Each node has a valid range (min, max). Or inorder traversal must be strictly increasing.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def make_tree(arr):
    """Build tree from level-order array. None = no node."""
    if not arr or arr[0] is None:
        return None
    root = TreeNode(arr[0])
    queue = deque([root])
    i = 1
    while queue and i < len(arr):
        node = queue.popleft()
        if i < len(arr) and arr[i] is not None:
            node.left = TreeNode(arr[i])
            queue.append(node.left)
        i += 1
        if i < len(arr) and arr[i] is not None:
            node.right = TreeNode(arr[i])
            queue.append(node.right)
        i += 1
    return root


def is_valid_bst(root):
    pass


def solve(arr):
    return is_valid_bst(make_tree(arr))


run_tests(solve, [
    (([2,1,3],),                     True),
    (([5,1,4,None,None,3,6],),       False),    # 4 < 5 in right subtree
    (([1],),                         True),     # single node
    (([],),                          True),     # empty tree (vacuously valid)
    (([5,4,6,None,None,3,7],),       False),    # 3 in right subtree but 3 < 5
    (([2,2,2],),                     False),    # equal values not valid BST
    (([10,5,15,None,None,6,20],),    False),    # 6 < 10 but in right subtree
])
