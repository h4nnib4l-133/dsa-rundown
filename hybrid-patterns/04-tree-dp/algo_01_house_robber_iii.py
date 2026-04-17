import os, sys
_d = os.path.dirname(os.path.abspath(__file__))
while _d and not os.path.exists(os.path.join(_d, 'test_runner.py')):
    _d = os.path.dirname(_d)
sys.path.insert(0, _d)
from test_runner import run_tests


# House Robber III (LC #337) -- Medium
# Input:  root: TreeNode (binary tree with money values)
# Output: int (max money, can't rob parent + child)
# Binary tree version of House Robber.
#
# Example:
# #     3
#    / \
#   2   3     -> 7 (rob 3 root + 1 leaf... wait, [3, [2,None,3], [3,None,1]] = robs of 3+3+1=7)
#    \   \
#     3   1
#
#   Pattern: TREE DP
#   Key: For each node, return (rob, skip):
#        rob_this = node.val + left.skip + right.skip
#        skip_this = max(left) + max(right).

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def make_tree(arr):
    if not arr or arr[0] is None:
        return None
    from collections import deque
    root = TreeNode(arr[0])
    q = deque([root])
    i = 1
    while q and i < len(arr):
        node = q.popleft()
        if i < len(arr) and arr[i] is not None:
            node.left = TreeNode(arr[i]); q.append(node.left)
        i += 1
        if i < len(arr) and arr[i] is not None:
            node.right = TreeNode(arr[i]); q.append(node.right)
        i += 1
    return root


def rob(root):
    pass


def solve(arr):
    return rob(make_tree(arr))

run_tests(rob, [
    (([3,2,3,None,3,None,1],),  7),
    (([3,4,5,1,3,None,1],),     9),
    (([],),                     0),
    (([5],),                    5),
])
