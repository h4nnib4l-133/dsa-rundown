# ============================================================
# PATTERN: DYNAMIC PROGRAMMING
# ============================================================
# DP = recursion + memoization (or bottom-up tabulation). Identify:
# 1. **State** -- what variables define a subproblem?
# 2. **Transition** -- how does current state relate to smaller states?
# 3. **Base case** -- what are the trivial subproblems?
#
# **Common DP types:**
# - **1D DP:** `dp[i]` depends on `dp[i-1]`, `dp[i-2]`, etc.
# - **2D DP:** `dp[i][j]` for two sequences or grid problems
# - **Knapsack:** pick/skip items with weight/value constraints
# - **Interval DP:** `dp[i][j]` for subarray/substring from i to j
#
# **Always ask:** Can I reduce space? (Often 2D -> 1D, or 1D -> two variables)
#
# ---
# ============================================================

import sys, os; sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from test_runner import run_tests


# Climbing Stairs (LC #70) -- Easy
# Count ways to reach step n, taking 1 or 2 steps at a time.
#
#   State: `dp[i]` = ways to reach step i
#   Transition: `dp[i] = dp[i-1] + dp[i-2]`
#   Optimize: Only need last 2 values

def climb_stairs(n):
    pass


run_tests(climb_stairs, [
    ((2,), 2),
    ((3,), 3),
    ((1,), 1),
    ((5,), 8),
    ((10,), 89),
])
