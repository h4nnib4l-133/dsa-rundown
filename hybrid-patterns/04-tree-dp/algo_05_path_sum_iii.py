import os, sys
_d = os.path.dirname(os.path.abspath(__file__))
while _d and not os.path.exists(os.path.join(_d, 'test_runner.py')):
    _d = os.path.dirname(_d)
sys.path.insert(0, _d)
from test_runner import run_tests


# Path Sum III (LC #437) -- Medium
# Input:  root: TreeNode, targetSum: int
# Output: int (number of paths (root-to-leaf NOT required) with sum == target)
# Path can start/end anywhere, must go downward.
#
# Example:
# #   [10,5,-3,3,2,null,11,3,-2,null,1], target=8  -> 3
#
#   Pattern: TREE DP + PREFIX SUM HASHMAP
#   Key: DFS tracking prefix sum from root.
#        Hashmap {prefix_sum: count}. When visiting node with prefix p,
#        paths ending here = count[p - target]. Add/remove on enter/exit (backtracking).

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


def path_sum(root, target):
    pass


def solve(arr, target):
    return path_sum(make_tree(arr), target)

run_tests(path_sum, [
    (([10,5,-3,3,2,None,11,3,-2,None,1], 8),  3),
    (([5,4,8,11,None,13,4,7,2,None,None,5,1], 22),  3),
    (([],   0),       0),
])
