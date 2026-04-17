import os, sys
_d = os.path.dirname(os.path.abspath(__file__))
while _d and not os.path.exists(os.path.join(_d, 'test_runner.py')):
    _d = os.path.dirname(_d)
sys.path.insert(0, _d)
from test_runner import run_tests


# Count Good Nodes in Binary Tree (LC #1448) -- Medium
# Input:  root: TreeNode
# Output: int (count of 'good' nodes: no ancestor has greater value)
# A node is good if no node on path from root is strictly greater.
#
# Example:
# #   [3,1,4,3,None,1,5]  -> 4
#
#   Pattern: TREE DP (track max on path)
#   Key: DFS passing max_so_far. Node is good if node.val >= max_so_far.
#        Update max_so_far and recurse to children.

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


def good_nodes(root):
    pass


def solve(arr):
    return good_nodes(make_tree(arr))

run_tests(good_nodes, [
    (([3,1,4,3,None,1,5],),    4),
    (([3,3,None,4,2],),        3),
    (([1],),                   1),
])
