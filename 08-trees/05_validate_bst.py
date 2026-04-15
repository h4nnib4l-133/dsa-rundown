import sys, os; sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from test_runner import run_tests
from collections import deque


# Validate BST (LC #98) -- Medium
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
    (([2,1,3],), True),
    (([5,1,4,None,None,3,6],), False),
    (([1],), True),
])
