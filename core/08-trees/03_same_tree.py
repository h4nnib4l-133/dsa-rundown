import os, sys
_d = os.path.dirname(os.path.abspath(__file__))
while _d and not os.path.exists(os.path.join(_d, 'test_runner.py')):
    _d = os.path.dirname(_d)
sys.path.insert(0, _d)
from test_runner import run_tests
from collections import deque


# Same Tree (LC #100) -- Easy
# Input:  root1: TreeNode, root2: TreeNode
# Output: bool (True if structurally identical with same values)
# Check if two trees are identical.
#
#   Key: Both null = true. One null = false. Same val + recurse both children.

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


def is_same_tree(root1, root2):
    pass


def solve(arr1, arr2):
    return is_same_tree(make_tree(arr1), make_tree(arr2))


run_tests(solve, [
    (([1,2,3], [1,2,3]), True),
    (([1,2], [1,None,2]), False),
    (([], []), True),
])
