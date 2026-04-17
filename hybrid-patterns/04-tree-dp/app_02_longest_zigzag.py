import os, sys
_d = os.path.dirname(os.path.abspath(__file__))
while _d and not os.path.exists(os.path.join(_d, 'test_runner.py')):
    _d = os.path.dirname(_d)
sys.path.insert(0, _d)
from test_runner import run_tests


# Longest ZigZag Path in Tree (LC #1372) -- Medium
# Input:  root: TreeNode
# Output: int (length of longest zigzag path: alternating left/right moves)
# Path alternates left-right-left-... Length = edges.
#
# Example:
# #   Complex example -> longest alternating path
#
#   Pattern: TREE DP (two states: from-left / from-right)
#   Key: DFS returns (left_len, right_len) from this node.
#        left_len = 1 + child.right_len (went left from parent, so child goes right).
#        Update global max.

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


def longest_zigzag(root):
    pass


def solve(arr):
    return longest_zigzag(make_tree(arr))

run_tests(longest_zigzag, [
    (([1,None,1,1,1,None,None,1,1,None,1,None,None,None,1],),     3),
    (([1,1,1,None,1,None,None,1,1,None,1],),  4),
    (([1],),                   0),
])
