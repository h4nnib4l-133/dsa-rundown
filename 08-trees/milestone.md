# Trees (Binary Trees / BST)

## The Patterns

1. **DFS recursion** -- most tree problems. Think: what does each node return to its parent?
2. **BFS level-order** -- use queue for level-by-level traversal
3. **BST property** -- inorder traversal is sorted. Use for validation, kth element.
4. **Build tree** -- from traversal arrays using recursive partitioning

**Template for DFS:**
```python
def dfs(node):
    if not node: return base_case
    left = dfs(node.left)
    right = dfs(node.right)
    return combine(node.val, left, right)
```

**C tips:** `struct TreeNode { int val; struct TreeNode *left, *right; };`. Recursive DFS is natural. For BFS, use array-based queue.

---

## Problems

### 1. Maximum Depth of Binary Tree (LC #104) -- Easy
Find height of binary tree.
- **Key:** `return max(depth(left), depth(right)) + 1`
- **Files:** `01_max_depth.py`, `01_max_depth.c`

### 2. Invert Binary Tree (LC #226) -- Easy
Mirror a binary tree.
- **Key:** Swap left and right children recursively
- **Files:** `02_invert_tree.py`, `02_invert_tree.c`

### 3. Same Tree (LC #100) -- Easy
Check if two trees are identical.
- **Key:** Both null = true. One null = false. Same val + recurse both children.
- **Files:** `03_same_tree.py`, `03_same_tree.c`

### 4. Binary Tree Level Order Traversal (LC #102) -- Medium
Return nodes grouped by level.
- **Key:** BFS with queue. Process all nodes at current level before moving to next.
- **Files:** `04_level_order.py`, `04_level_order.c`

### 5. Validate BST (LC #98) -- Medium
Is the tree a valid BST?
- **Key:** Each node has a valid range (min, max). Or inorder traversal must be strictly increasing.
- **Files:** `05_validate_bst.py`, `05_validate_bst.c`

### 6. Lowest Common Ancestor (LC #236) -- Medium
Find LCA of two nodes in binary tree.
- **Key:** If current node is p or q, return it. If left and right both return non-null, current is LCA.
- **Files:** `06_lca.py`, `06_lca.c`

### 7. Kth Smallest Element in BST (LC #230) -- Medium
Find kth smallest value in BST.
- **Key:** Inorder traversal (left -> root -> right), count to k
- **Files:** `07_kth_smallest_bst.py`, `07_kth_smallest_bst.c`

### 8. Binary Tree Maximum Path Sum (LC #124) -- Hard
Maximum path sum (path can start/end at any node).
- **Key:** DFS returns max single-path through node. Update global max with `left + node + right`.
- **Hint:** Return `node.val + max(left, right, 0)` to parent. Negative paths = return 0.
- **Files:** `08_max_path_sum.py`, `08_max_path_sum.c`

### 9. Serialize and Deserialize Binary Tree (LC #297) -- Hard
Convert tree to string and back.
- **Key:** Preorder with null markers. Serialize: `"1,2,#,#,3,4,#,#,5,#,#"`. Deserialize with queue/index.
- **Files:** `09_serialize_tree.py`, `09_serialize_tree.c`

### 10. Construct Tree from Preorder and Inorder (LC #105) -- Medium
Build tree from preorder and inorder traversal arrays.
- **Key:** First element of preorder = root. Find root in inorder to split left/right subtrees.
- **Optimization:** Use hashmap for O(1) index lookup in inorder
- **Files:** `10_build_tree.py`, `10_build_tree.c`
