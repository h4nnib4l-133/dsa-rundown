# Dynamic Programming

## The Pattern

DP = recursion + memoization (or bottom-up tabulation). Identify:
1. **State** -- what variables define a subproblem?
2. **Transition** -- how does current state relate to smaller states?
3. **Base case** -- what are the trivial subproblems?

**Common DP types:**
- **1D DP:** `dp[i]` depends on `dp[i-1]`, `dp[i-2]`, etc.
- **2D DP:** `dp[i][j]` for two sequences or grid problems
- **Knapsack:** pick/skip items with weight/value constraints
- **Interval DP:** `dp[i][j]` for subarray/substring from i to j

**Always ask:** Can I reduce space? (Often 2D -> 1D, or 1D -> two variables)

---

## Problems

### 1. Climbing Stairs (LC #70) -- Easy
Count ways to reach step n, taking 1 or 2 steps at a time.
- **State:** `dp[i]` = ways to reach step i
- **Transition:** `dp[i] = dp[i-1] + dp[i-2]`
- **Optimize:** Only need last 2 values
- **Files:** `01_climbing_stairs.py`, `01_climbing_stairs.c`

### 2. House Robber (LC #198) -- Medium
Max money from non-adjacent houses.
- **State:** `dp[i]` = max money considering houses 0..i
- **Transition:** `dp[i] = max(dp[i-1], dp[i-2] + nums[i])`
- **Files:** `02_house_robber.py`, `02_house_robber.c`

### 3. Coin Change (LC #322) -- Medium
Fewest coins to make amount. Unlimited supply of each coin.
- **State:** `dp[amount]` = min coins for that amount
- **Transition:** `dp[a] = min(dp[a], dp[a - coin] + 1)` for each coin
- **Files:** `03_coin_change.py`, `03_coin_change.c`

### 4. Longest Increasing Subsequence (LC #300) -- Medium
Find length of longest strictly increasing subsequence.
- **O(n^2):** `dp[i]` = LIS ending at i. `dp[i] = max(dp[j]+1)` for j < i where `nums[j] < nums[i]`
- **O(n log n):** Maintain tails array + binary search
- **Files:** `04_lis.py`, `04_lis.c`

### 5. Word Break (LC #139) -- Medium
Can string s be segmented into words from dictionary?
- **State:** `dp[i]` = can s[0..i] be segmented?
- **Transition:** `dp[i] = any(dp[j] and s[j:i] in dict)` for j < i
- **Files:** `05_word_break.py`, `05_word_break.c`

### 6. Unique Paths (LC #62) -- Medium
Count paths from top-left to bottom-right (only right/down moves).
- **State:** `dp[i][j]` = paths to reach (i,j)
- **Transition:** `dp[i][j] = dp[i-1][j] + dp[i][j-1]`
- **Files:** `06_unique_paths.py`, `06_unique_paths.c`

### 7. Longest Common Subsequence (LC #1143) -- Medium
LCS of two strings.
- **State:** `dp[i][j]` = LCS of s1[0..i], s2[0..j]
- **Transition:** Match: `dp[i-1][j-1] + 1`. No match: `max(dp[i-1][j], dp[i][j-1])`
- **Files:** `07_lcs.py`, `07_lcs.c`

### 8. 0/1 Knapsack -- Medium
Max value with weight constraint, each item used at most once.
- **State:** `dp[i][w]` = max value using items 0..i with capacity w
- **Transition:** `dp[i][w] = max(dp[i-1][w], dp[i-1][w-wt[i]] + val[i])`
- **Optimize:** 1D array, iterate w backwards
- **Files:** `08_knapsack.py`, `08_knapsack.c`

### 9. Edit Distance (LC #72) -- Medium
Min operations (insert/delete/replace) to transform word1 -> word2.
- **State:** `dp[i][j]` = edit distance of word1[0..i], word2[0..j]
- **Transition:** Match: `dp[i-1][j-1]`. Else: `1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])`
- **Files:** `09_edit_distance.py`, `09_edit_distance.c`

### 10. Longest Palindromic Substring (LC #5) -- Medium
Find longest palindromic substring.
- **Approach 1:** Expand around center for each index. O(n^2) time, O(1) space.
- **Approach 2:** DP table `dp[i][j]` = is s[i..j] palindrome?
- **Files:** `10_longest_palindrome.py`, `10_longest_palindrome.c`
