import sys, os; sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from test_runner import run_tests
from collections import deque


# Binary Tree Level Order Traversal (LC #102) -- Medium
# Return nodes grouped by level.
#
#   Key: BFS with queue. Process all nodes at current level before moving to next.

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


def level_order(root):
    pass


def solve(arr):
    return level_order(make_tree(arr))


run_tests(solve, [
    (([3,9,20,None,None,15,7],), [[3],[9,20],[15,7]]),
    (([1],), [[1]]),
    (([],), []),
])
