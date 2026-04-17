import os, sys
_d = os.path.dirname(os.path.abspath(__file__))
while _d and not os.path.exists(os.path.join(_d, 'test_runner.py')):
    _d = os.path.dirname(_d)
sys.path.insert(0, _d)
from test_runner import run_tests


# Binary Tree Cameras (LC #968) -- Hard
# Input:  root: TreeNode
# Output: int (min cameras to cover every node; each camera covers parent, self, children)
# Place min cameras such that every node is covered.
#
# Example:
# #   [0,0,null,0,0] -> 1
#
#   Pattern: TREE DP (3 states)
#   Key: Each node returns one of 3 states: NEEDS_CAMERA, HAS_CAMERA, COVERED.
#        Greedy: place camera at node if any child NEEDS_CAMERA.

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


def min_camera_cover(root):
    pass


def solve(arr):
    return min_camera_cover(make_tree(arr))

run_tests(min_camera_cover, [
    (([0,0,None,0,0],),             1),
    (([0,0,None,0,None,0,None,None,0],),  2),
    (([0],),                        1),
])
