# Linked Lists

## The Patterns

1. **Two pointers (slow/fast)** -- cycle detection, find middle, nth from end
2. **Dummy head** -- simplifies edge cases when head might change
3. **Reverse** -- iterative (prev/curr/next) or recursive
4. **Merge** -- two-pointer merge like merge sort

**C tips:** Use `struct ListNode { int val; struct ListNode* next; };`. Always `malloc` new nodes, `free` deleted nodes. Watch for dangling pointers.

---

## Problems

### 1. Reverse Linked List (LC #206) -- Easy
Reverse a singly linked list.
- **Key:** Three pointers: prev, curr, next. Or recursive.
- **Files:** `01_reverse_list.py`, `01_reverse_list.c`

### 2. Middle of Linked List (LC #876) -- Easy
Return middle node. If two middle nodes, return second.
- **Key:** Slow moves 1 step, fast moves 2. When fast reaches end, slow is at middle.
- **Files:** `02_middle_list.py`, `02_middle_list.c`

### 3. Linked List Cycle (LC #141) -- Easy
Detect if linked list has a cycle.
- **Key:** Floyd's tortoise and hare. If they meet, cycle exists.
- **Files:** `03_has_cycle.py`, `03_has_cycle.c`

### 4. Merge Two Sorted Lists (LC #21) -- Easy
Merge two sorted lists into one sorted list.
- **Key:** Dummy head + compare and link smaller node
- **Files:** `04_merge_two_lists.py`, `04_merge_two_lists.c`

### 5. Remove Nth Node From End (LC #19) -- Medium
Remove nth node from end in one pass.
- **Key:** Two pointers with gap of n. When fast reaches end, slow is at target.
- **Files:** `05_remove_nth.py`, `05_remove_nth.c`

### 6. Add Two Numbers (LC #2) -- Medium
Add two numbers represented as reversed linked lists.
- **Key:** Traverse both lists, sum digits + carry, create new nodes
- **Files:** `06_add_two_numbers.py`, `06_add_two_numbers.c`

### 7. Linked List Cycle II (LC #142) -- Medium
Find the node where cycle begins.
- **Key:** Floyd's phase 2 -- after detection, move one pointer to head, advance both by 1 until they meet.
- **Files:** `07_cycle_start.py`, `07_cycle_start.c`

### 8. Reorder List (LC #143) -- Medium
Reorder: L0 -> Ln -> L1 -> Ln-1 -> ...
- **Key:** Find middle, reverse second half, merge alternating
- **Files:** `08_reorder_list.py`, `08_reorder_list.c`

### 9. Copy List with Random Pointer (LC #138) -- Medium
Deep copy list where each node has a next and random pointer.
- **Key:** HashMap {old -> new} in first pass, link in second pass. Or interleaving trick.
- **Files:** `09_copy_random_list.py`, `09_copy_random_list.c`

### 10. Merge K Sorted Lists (LC #23) -- Hard
Merge k sorted linked lists.
- **Key:** Min-heap of size k, always pop smallest and push its next. Or divide-and-conquer merge.
- **Files:** `10_merge_k_lists.py`, `10_merge_k_lists.c`
