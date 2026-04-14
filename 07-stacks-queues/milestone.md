# Stacks and Queues

## The Patterns

1. **Matching/balancing** -- brackets, parentheses validation
2. **Monotonic stack** -- next greater/smaller element, histogram
3. **Stack as evaluator** -- postfix expressions, calculators
4. **Deque** -- sliding window max/min (monotonic deque)
5. **Simulate one with another** -- queue using stacks, stack using queues

**C tips:** Implement stack with array + top index. Queue with circular buffer or two stacks.

---

## Problems

### 1. Valid Parentheses (LC #20) -- Easy
Check if string of `()[]{}` is balanced.
- **Key:** Push opening brackets, pop and compare for closing brackets
- **Files:** `01_valid_parens.py`, `01_valid_parens.c`

### 2. Min Stack (LC #155) -- Medium
Stack with push, pop, top, getMin all in O(1).
- **Key:** Auxiliary stack tracking minimum at each level
- **Files:** `02_min_stack.py`, `02_min_stack.c`

### 3. Implement Queue using Stacks (LC #232) -- Easy
FIFO queue using two LIFO stacks.
- **Key:** Push to stack1. For pop, transfer stack1 -> stack2 if stack2 empty.
- **Files:** `03_queue_using_stacks.py`, `03_queue_using_stacks.c`

### 4. Implement Stack using Queues (LC #225) -- Easy
LIFO stack using queues.
- **Key:** On push, enqueue to q2, then transfer q1 -> q2, swap q1 and q2
- **Files:** `04_stack_using_queues.py`, `04_stack_using_queues.c`

### 5. Next Greater Element I (LC #496) -- Easy
For each element in nums1, find next greater element in nums2.
- **Key:** Monotonic decreasing stack. Process nums2, map each element to its next greater.
- **Files:** `05_next_greater.py`, `05_next_greater.c`

### 6. Daily Temperatures (LC #739) -- Medium
Days until warmer temperature for each day.
- **Key:** Monotonic decreasing stack of indices. Pop when current temp > stack top.
- **Files:** `06_daily_temps.py`, `06_daily_temps.c`

### 7. Evaluate Reverse Polish Notation (LC #150) -- Medium
Evaluate postfix expression.
- **Key:** Push numbers. On operator, pop two, compute, push result.
- **Files:** `07_rpn.py`, `07_rpn.c`

### 8. Largest Rectangle in Histogram (LC #84) -- Hard
Largest rectangle that can be formed in histogram.
- **Key:** Monotonic increasing stack. For each bar, find how far it extends left and right.
- **Files:** `08_largest_rect_histogram.py`, `08_largest_rect_histogram.c`

### 9. Balanced Brackets (HackerRank) -- Medium
Like valid parentheses but specifically the HackerRank version.
- **Key:** Same stack matching pattern. Handle edge cases: empty string, single bracket.
- **Files:** `09_balanced_brackets.py`, `09_balanced_brackets.c`

### 10. Sliding Window Maximum (LC #239) -- Hard
Max element in each sliding window of size k.
- **Key:** Monotonic decreasing deque. Front = current max. Remove from back if smaller.
- **Files:** `10_sliding_window_max.py`, `10_sliding_window_max.c`
