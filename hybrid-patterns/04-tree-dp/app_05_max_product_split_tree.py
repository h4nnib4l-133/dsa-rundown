import os, sys
_d = os.path.dirname(os.path.abspath(__file__))
while _d and not os.path.exists(os.path.join(_d, 'test_runner.py')):
    _d = os.path.dirname(_d)
sys.path.insert(0, _d)
from test_runner import run_tests


# Maximum Product of Splitted Binary Tree (LC #1339) -- Medium
# Input:  root: TreeNode
# Output: int (max product of sums of two subtrees after removing one edge, mod 10^9+7)
# Remove one edge, get two trees. Max product of their sums.
#
# Example:
# #   [1,2,3,4,5,6]  -> 110   (total=21, split into 11 and 10: 110)
#
#   Pattern: TREE DP (two DFS passes)
#   Key: 1. Compute total sum.
#        2. DFS to compute subtree sums. At each node, product = subtree_sum * (total - subtree_sum).
#        Track max product.

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


def max_product(root):
    pass


def solve(arr):
    return max_product(make_tree(arr))

run_tests(max_product, [
    (([1,2,3,4,5,6],),     110),
    (([1,None,2,3,4,None,None,5,6],),  90),
    (([2,3,9,10,7,8,6,5,4,11,1],),     1025),
])
