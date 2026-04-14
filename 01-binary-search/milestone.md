# Binary Search

## The Pattern

Binary search eliminates half the search space each step. Works on any **monotonic** condition -- not just sorted arrays.

**Template:**
```
lo, hi = min_possible, max_possible
while lo < hi:
    mid = (lo + hi) // 2
    if condition(mid):
        hi = mid       # answer is mid or left
    else:
        lo = mid + 1   # answer is right
return lo
```

**Three flavors:**
1. **Search for value** -- classic sorted array lookup
2. **Search for boundary** -- first/last occurrence, lower/upper bound
3. **Search on answer** -- minimize/maximize some value (Koko, ships, cows)

---

## Problems

### 1. Binary Search (LC #704) -- Easy
Find target in sorted array. Return index or -1.
- **Key:** Basic `lo, hi, mid` template
- **Files:** `01_search_sorted.py`, `01_search_sorted.c`

### 2. Search Insert Position (LC #35) -- Easy
Find index where target would be inserted in sorted array.
- **Key:** Lower bound -- first index where `arr[i] >= target`
- **Files:** `02_search_insert.py`, `02_search_insert.c`

### 3. First Bad Version (LC #278) -- Easy
Given n versions, find the first bad one using `isBadVersion(n)` API.
- **Key:** Binary search on boolean predicate
- **Files:** `03_first_bad_version.py`, `03_first_bad_version.c`

### 4. Search in Rotated Sorted Array (LC #33) -- Medium
Search target in a rotated sorted array in O(log n).
- **Key:** Determine which half is sorted, then decide which half to search
- **Hint:** Check if `nums[lo] <= nums[mid]` to identify sorted half
- **Files:** `04_rotated_search.py`, `04_rotated_search.c`

### 5. First and Last Position (LC #34) -- Medium
Find starting and ending index of target in sorted array.
- **Key:** Run two binary searches -- one for left bound, one for right bound
- **Files:** `05_first_last_pos.py`, `05_first_last_pos.c`

### 6. Find Peak Element (LC #162) -- Medium
Find element greater than its neighbors. Multiple peaks OK, return any.
- **Key:** If `nums[mid] < nums[mid+1]`, peak is to the right
- **Files:** `06_peak_element.py`, `06_peak_element.c`

### 7. Search a 2D Matrix (LC #74) -- Medium
Search value in m x n matrix where each row is sorted and first element > last of previous row.
- **Key:** Treat as flattened sorted array: `row = mid // cols`, `col = mid % cols`
- **Files:** `07_search_2d_matrix.py`, `07_search_2d_matrix.c`

### 8. Koko Eating Bananas (LC #875) -- Medium
Koko eats bananas at speed k. Find minimum k to finish all piles in h hours.
- **Key:** Binary search on answer. For each k, check if `sum(ceil(pile/k)) <= h`
- **Files:** `08_koko_bananas.py`, `08_koko_bananas.c`

### 9. Capacity to Ship Packages (LC #1011) -- Medium
Find minimum ship capacity to ship all packages within d days.
- **Key:** BS on answer. lo = max(weights), hi = sum(weights). Greedy check per capacity.
- **Files:** `09_ship_packages.py`, `09_ship_packages.c`

### 10. Median of Two Sorted Arrays (LC #4) -- Hard
Find median of two sorted arrays in O(log(min(m,n))).
- **Key:** Binary search on partition of shorter array. Ensure left halves <= right halves.
- **Hint:** Partition so that `left1 + left2 = (m+n+1)//2`
- **Files:** `10_median_two_arrays.py`, `10_median_two_arrays.c`
