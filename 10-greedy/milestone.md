# Greedy Algorithms

## The Pattern

Greedy makes the locally optimal choice at each step, hoping for a global optimum. Works when:
1. **Greedy choice property** -- local optimum leads to global optimum
2. **Optimal substructure** -- optimal solution contains optimal sub-solutions

**Common strategies:**
- Sort by some criteria (end time, ratio, etc.) then scan
- Two pointers from both ends
- Track running max/min/sum

**How to verify greedy works:** Try to construct a counterexample. If you can't, it's likely correct.

---

## Problems

### 1. Best Time to Buy and Sell Stock II (LC #122) -- Medium
Max profit with unlimited transactions.
- **Key:** Collect every upward slope: if `prices[i] > prices[i-1]`, add the difference
- **Files:** `01_buy_sell_stock_ii.py`, `01_buy_sell_stock_ii.c`

### 2. Jump Game (LC #55) -- Medium
Can you reach the last index?
- **Key:** Track farthest reachable index. At each position, update `farthest = max(farthest, i + nums[i])`.
- **Files:** `02_jump_game.py`, `02_jump_game.c`

### 3. Jump Game II (LC #45) -- Medium
Minimum jumps to reach last index.
- **Key:** BFS-style greedy. Track current end and farthest. When i reaches current end, jump.
- **Files:** `03_jump_game_ii.py`, `03_jump_game_ii.c`

### 4. Gas Station (LC #134) -- Medium
Find starting gas station to complete circular tour.
- **Key:** If total gas >= total cost, solution exists. Start from station where running surplus first goes negative + 1.
- **Files:** `04_gas_station.py`, `04_gas_station.c`

### 5. Candy (LC #135) -- Hard
Min candies for children with ratings. Higher rating than neighbor = more candy.
- **Key:** Two passes. Left-to-right: if rating increases, increment. Right-to-left: same. Take max at each position.
- **Files:** `05_candy.py`, `05_candy.c`

### 6. Non-overlapping Intervals (LC #435) -- Medium
Min intervals to remove to make rest non-overlapping.
- **Key:** Sort by end time. Greedily keep intervals that don't overlap with last kept.
- **Equivalent to:** Total intervals - max non-overlapping intervals (activity selection)
- **Files:** `06_non_overlapping.py`, `06_non_overlapping.c`

### 7. Task Scheduler (LC #621) -- Medium
Min intervals to execute all tasks with cooldown n between same tasks.
- **Key:** Most frequent task determines frame. Answer = `max(len(tasks), (max_freq - 1) * (n + 1) + count_of_max_freq)`
- **Files:** `07_task_scheduler.py`, `07_task_scheduler.c`

### 8. Boats to Save People (LC #881) -- Medium
Min boats, each holds 2 people with weight limit.
- **Key:** Sort. Pair lightest with heaviest. If they fit, pair them. Else heaviest goes alone.
- **Files:** `08_boats.py`, `08_boats.c`

### 9. Minimum Arrows to Burst Balloons (LC #452) -- Medium
Min arrows to burst all balloons (intervals on x-axis).
- **Key:** Sort by end. Shoot at each interval's end. Skip all intervals that include this point.
- **Files:** `09_min_arrows.py`, `09_min_arrows.c`

### 10. Partition Labels (LC #763) -- Medium
Max partitions so each letter appears in at most one part.
- **Key:** Record last occurrence of each char. Extend partition end to `max(end, last[char])`. When i reaches end, cut.
- **Files:** `10_partition_labels.py`, `10_partition_labels.c`
