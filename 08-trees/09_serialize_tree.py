import sys, os; sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from test_runner import run_tests
from collections import deque


# Serialize and Deserialize Binary Tree (LC #297) -- Hard
# Input:  root: TreeNode (serialize) / data: str (deserialize)
# Output: str (serialize) / TreeNode (deserialize)
# Convert tree to string and back.
#
#   Key: Preorder with null markers. Serialize: `"1,2,#,#,3,4,#,#,5,#,#"`. Deserialize with queue/index.

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


def serialize(root):
    pass


def deserialize(data):
    pass


def solve(arr):
    tree = make_tree(arr)
    data = serialize(tree)
    rebuilt = deserialize(data)
    # verify by serializing again
    return serialize(rebuilt) == data


run_tests(solve, [
    (([1,2,3,None,None,4,5],), True),
    (([],),                     True),
    (([1],),                    True),
])
