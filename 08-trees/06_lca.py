import sys, os; sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from test_runner import run_tests
from collections import deque


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


def lowest_common_ancestor(root, p_val, q_val):
    """Return value of LCA node"""
    pass


def solve(arr, p, q):
    return lowest_common_ancestor(make_tree(arr), p, q)


run_tests(solve, [
    (([3,5,1,6,2,0,8,None,None,7,4], 5, 1), 3),
    (([3,5,1,6,2,0,8,None,None,7,4], 5, 4), 5),
    (([1,2], 1, 2), 1),
])
