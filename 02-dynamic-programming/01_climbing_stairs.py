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
# You're climbing a staircase of n steps. Each time you can climb 1 or 2 steps.
# How many distinct ways can you reach the top?
#
# Example:
#   n=2: [1+1, 2]            -> 2 ways
#   n=3: [1+1+1, 1+2, 2+1]  -> 3 ways
#   n=4: 5 ways  (1111, 112, 121, 211, 22)
#
#   Key: dp[i] = dp[i-1] + dp[i-2]. Same as Fibonacci.
#        Optimize: only need last 2 values.

def climb_stairs(n):
    pass


run_tests(climb_stairs, [
    ((1,),    1),     # only one way
    ((2,),    2),     # 1+1 or 2
    ((3,),    3),     # 1+1+1, 1+2, 2+1
    ((4,),    5),
    ((5,),    8),
    ((10,),  89),
    ((20,), 10946),   # larger input
    ((0,),    1),     # already at top (edge case)
])
