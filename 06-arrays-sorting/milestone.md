# Arrays and Sorting

## The Patterns

1. **Two pointers** -- sorted arrays, pair/triplet sum, container problems
2. **Prefix sum** -- range sum queries, subarray sum problems
3. **Hash map** -- O(1) lookup for complement, frequency counting
4. **Merge intervals** -- sort by start, merge overlapping
5. **Dutch National Flag** -- 3-way partition with lo/mid/hi pointers

---

## Problems

### 1. Two Sum (LC #1) -- Easy
Find two numbers that add up to target. Return indices.
- **Key:** Hash map: for each num, check if `target - num` exists
- **Files:** `01_two_sum.py`, `01_two_sum.c`

### 2. Best Time to Buy and Sell Stock (LC #121) -- Easy
Max profit from single buy and sell.
- **Key:** Track min price so far, compute max profit at each step
- **Files:** `02_buy_sell_stock.py`, `02_buy_sell_stock.c`

### 3. Remove Duplicates from Sorted Array (LC #26) -- Easy
Remove duplicates in-place, return new length.
- **Key:** Two pointers: read and write. Write only when value changes.
- **Files:** `03_remove_duplicates.py`, `03_remove_duplicates.c`

### 4. 3Sum (LC #15) -- Medium
Find all unique triplets that sum to zero.
- **Key:** Sort array. Fix one element, two-pointer on remainder. Skip duplicates.
- **Files:** `04_three_sum.py`, `04_three_sum.c`

### 5. Container With Most Water (LC #11) -- Medium
Find two lines forming container with most water.
- **Key:** Two pointers from both ends. Move the shorter line inward.
- **Files:** `05_container_water.py`, `05_container_water.c`

### 6. Merge Intervals (LC #56) -- Medium
Merge all overlapping intervals.
- **Key:** Sort by start. If current overlaps previous, merge. Else add new interval.
- **Files:** `06_merge_intervals.py`, `06_merge_intervals.c`

### 7. Product of Array Except Self (LC #238) -- Medium
Compute product of all elements except self, without division.
- **Key:** Two passes: prefix products left-to-right, then suffix right-to-left
- **Files:** `07_product_except_self.py`, `07_product_except_self.c`

### 8. Sort Colors / Dutch National Flag (LC #75) -- Medium
Sort array of 0s, 1s, 2s in-place, one pass.
- **Key:** Three pointers: lo (0s boundary), mid (current), hi (2s boundary)
- **Files:** `08_sort_colors.py`, `08_sort_colors.c`

### 9. Trapping Rain Water (LC #42) -- Hard
How much water trapped between bars?
- **Key:** Two pointers from ends. Water at position = `min(left_max, right_max) - height`
- **Alternative:** Stack-based approach
- **Files:** `09_trapping_rain.py`, `09_trapping_rain.c`

### 10. Subarray Sum Equals K (LC #560) -- Medium
Count subarrays with sum equal to k.
- **Key:** Prefix sum + hash map. Count how many times `prefix_sum - k` has occurred.
- **Files:** `10_subarray_sum_k.py`, `10_subarray_sum_k.c`
