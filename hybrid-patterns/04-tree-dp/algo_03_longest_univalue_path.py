import os, sys
_d = os.path.dirname(os.path.abspath(__file__))
while _d and not os.path.exists(os.path.join(_d, 'test_runner.py')):
    _d = os.path.dirname(_d)
sys.path.insert(0, _d)
from test_runner import run_tests


# Longest Univalue Path (LC #687) -- Medium
# Input:  root: TreeNode
# Output: int (length of longest path where all nodes share same value)
# Longest path (edges count) where all nodes have same value.
#
# Example:
# #   [5,4,5,1,1,null,5]  -> 2   (path of 5->5->5)
#
#   Pattern: TREE DP (post-order)
#   Key: DFS returns length of univalue path UP from this node.
#        If child has same value, length = child_dfs + 1, else 0.
#        Global max updates with left + right at each node.

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


def longest_univalue_path(root):
    pass


def solve(arr):
    return longest_univalue_path(make_tree(arr))

run_tests(longest_univalue_path, [
    (([5,4,5,1,1,None,5],),  2),
    (([1,4,5,4,4,None,5],),  2),
    (([],),                  0),
    (([1],),                 0),
])
