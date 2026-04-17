import os, sys
_d = os.path.dirname(os.path.abspath(__file__))
while _d and not os.path.exists(os.path.join(_d, 'test_runner.py')):
    _d = os.path.dirname(_d)
sys.path.insert(0, _d)
from test_runner import run_tests

# Binary Tree Maximum Path Sum (LC #124) -- Hard
# Find the maximum SUM of any path in the tree.
# Path = sequence of nodes where each pair of adjacent nodes has an edge.
# Path does NOT need to pass through root. Can start/end at any node.
#
# Example:
#     1
#    / \
#   2   3    -> 6  (path: 2->1->3)
#
#     -10
#    /   \
#   9    20   -> 42  (path: 15->20->7)
#       /  \
#      15   7
#
#   Key: DFS returns max single-direction path through node.
#        At each node, update global max with left+node+right.
#        Return node.val + max(left, right, 0) to parent.

from collections import deque


# Binary Tree Maximum Path Sum (LC #124) -- Hard
# Input:  root: TreeNode (values can be negative)
# Output: int (max sum of any path, path can start/end at any node)
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
    (([1,2,3],),                       6),     # 2+1+3
    (([-10,9,20,None,None,15,7],),    42),     # 15+20+7
    (([-3],),                         -3),     # single negative node
    (([1,-2,-3,1,3,-2,None,-1],),      3),     # just the node 3
    (([2,-1],),                        2),     # skip negative child
])
