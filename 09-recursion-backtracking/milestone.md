# Recursion and Backtracking

## The Pattern

Backtracking = DFS through decision tree. At each step: **choose, explore, unchoose**.

**Template:**
```python
def backtrack(state, choices):
    if is_complete(state):
        result.append(state.copy())
        return
    for choice in choices:
        if is_valid(choice):
            state.add(choice)        # choose
            backtrack(state, ...)     # explore
            state.remove(choice)     # unchoose
```

**Key decisions:**
- **Subsets:** include or exclude each element (order doesn't matter)
- **Permutations:** try each unused element at current position (order matters)
- **Combinations:** like subsets but with target constraint
- **Constraint satisfaction:** N-Queens, Sudoku -- check validity before placing

**Pruning:** Skip invalid choices early to avoid unnecessary recursion.

---

## Problems

### 1. Subsets (LC #78) -- Medium
Generate all subsets of distinct integers.
- **Key:** For each element, include it or don't. Or iterative: start empty, for each num, add it to all existing subsets.
- **Files:** `01_subsets.py`, `01_subsets.c`

### 2. Permutations (LC #46) -- Medium
Generate all permutations of distinct integers.
- **Key:** Backtrack with used[] array. Or swap-based approach.
- **Files:** `02_permutations.py`, `02_permutations.c`

### 3. Combination Sum (LC #39) -- Medium
Find combinations that sum to target. Can reuse elements.
- **Key:** Backtrack with start index. Include current element (don't advance index) or skip (advance).
- **Files:** `03_combination_sum.py`, `03_combination_sum.c`

### 4. Letter Combinations of Phone Number (LC #17) -- Medium
Map digits to letters, generate all combinations.
- **Key:** Backtrack through digits. For each digit, try all mapped letters.
- **Files:** `04_phone_combos.py`, `04_phone_combos.c`

### 5. Generate Parentheses (LC #22) -- Medium
Generate all valid combinations of n pairs of parentheses.
- **Key:** Track open/close count. Can add `(` if open < n. Can add `)` if close < open.
- **Files:** `05_generate_parens.py`, `05_generate_parens.c`

### 6. Word Search (LC #79) -- Medium
Find if word exists in 2D grid following adjacent cells.
- **Key:** DFS from each cell. Mark visited (set to '#'), restore after backtrack.
- **Files:** `06_word_search.py`, `06_word_search.c`

### 7. Palindrome Partitioning (LC #131) -- Medium
Partition string so every part is a palindrome.
- **Key:** Backtrack with start index. For each end position, if substring is palindrome, recurse on remainder.
- **Files:** `07_palindrome_partition.py`, `07_palindrome_partition.c`

### 8. N-Queens (LC #51) -- Hard
Place N queens on NxN board so none attack each other.
- **Key:** Place queen row by row. Track columns, diagonals (`row-col`), anti-diagonals (`row+col`) in sets.
- **Files:** `08_n_queens.py`, `08_n_queens.c`

### 9. Sudoku Solver (LC #37) -- Hard
Fill valid Sudoku board.
- **Key:** Find empty cell, try 1-9, validate row/col/box, backtrack if stuck.
- **Files:** `09_sudoku.py`, `09_sudoku.c`

### 10. Subsets II (LC #90) -- Medium
Generate all subsets when array may contain duplicates.
- **Key:** Sort first. Skip duplicate elements at same recursion level: `if i > start and nums[i] == nums[i-1]: continue`
- **Files:** `10_subsets_ii.py`, `10_subsets_ii.c`
