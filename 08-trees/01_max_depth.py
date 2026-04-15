# ============================================================
# PATTERN: TREES
# ============================================================
# 1. **DFS recursion** -- most tree problems. Think: what does each node return to its parent?
# 2. **BFS level-order** -- use queue for level-by-level traversal
# 3. **BST property** -- inorder traversal is sorted. Use for validation, kth element.
# 4. **Build tree** -- from traversal arrays using recursive partitioning
#
# **Template for DFS:**
# ```python
# def dfs(node):
#     if not node: return base_case
#     left = dfs(node.left)
#     right = dfs(node.right)
#     return combine(node.val, left, right)
# ```
#
# **C tips:** `struct TreeNode { int val; struct TreeNode *left, *right; };`. Recursive DFS is natural. For BFS, use array-based queue.
#
# ---
# ============================================================

import sys, os; sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from test_runner import run_tests
from collections import deque


# Maximum Depth of Binary Tree (LC #104) -- Easy
# Find height of binary tree.
#
#   Key: `return max(depth(left), depth(right)) + 1`

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


def max_depth(root):
    pass


def solve(arr):
    return max_depth(make_tree(arr))


run_tests(solve, [
    (([3,9,20,None,None,15,7],), 3),
    (([1,None,2],),               2),
    (([],),                       0),
])
