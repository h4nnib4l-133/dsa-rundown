# ============================================================
# PATTERN: RECURSION BACKTRACKING
# ============================================================
# Backtracking = DFS through decision tree. At each step: **choose, explore, unchoose**.
#
# **Template:**
# ```python
# def backtrack(state, choices):
#     if is_complete(state):
#         result.append(state.copy())
#         return
#     for choice in choices:
#         if is_valid(choice):
#             state.add(choice)        # choose
#             backtrack(state, ...)     # explore
#             state.remove(choice)     # unchoose
# ```
#
# **Key decisions:**
# - **Subsets:** include or exclude each element (order doesn't matter)
# - **Permutations:** try each unused element at current position (order matters)
# - **Combinations:** like subsets but with target constraint
# - **Constraint satisfaction:** N-Queens, Sudoku -- check validity before placing
#
# **Pruning:** Skip invalid choices early to avoid unnecessary recursion.
#
# ---
# ============================================================

import sys, os; sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from test_runner import run_tests



# Subsets (LC #78) -- Medium
# Input:  nums: List[int] (distinct integers)
# Output: List[List[int]] (all possible subsets / power set)
# Given array of DISTINCT integers, return all possible subsets (power set).
#
# Example:
#   [1,2,3] -> [[], [1], [2], [3], [1,2], [1,3], [2,3], [1,2,3]]
#   [0]     -> [[], [0]]
#
#   Key: Backtrack -- for each element, include or exclude.
#        Or iterative: start with [[]], for each num, add it to all existing subsets.

def subsets(nums):
    pass


def solve(nums):
    return sorted([sorted(s) for s in subsets(nums)])


run_tests(solve, [
    (([1,2,3],), [[],[1],[1,2],[1,2,3],[1,3],[2],[2,3],[3]]),
    (([0],),     [[],[0]]),
    (([1,2],),   [[],[1],[1,2],[2]]),
    (([],),      [[]]),     # empty input -> just empty set
])
