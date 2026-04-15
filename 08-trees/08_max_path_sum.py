import sys, os; sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from test_runner import run_tests
from collections import deque


# Binary Tree Maximum Path Sum (LC #124) -- Hard
# Maximum path sum (path can start/end at any node).
#
#   Key: DFS returns max single-path through node. Update global max with `left + node + right`.
#   Hint: Return `node.val + max(left, right, 0)` to parent. Negative paths = return 0.

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


def max_path_sum(root):
    pass


def solve(arr):
    return max_path_sum(make_tree(arr))


run_tests(solve, [
    (([1,2,3],),           6),
    (([-10,9,20,None,None,15,7],), 42),
    (([-3],),             -3),
])
