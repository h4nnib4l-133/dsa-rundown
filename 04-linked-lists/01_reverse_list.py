# ============================================================
# PATTERN: LINKED LISTS
# ============================================================
# 1. **Two pointers (slow/fast)** -- cycle detection, find middle, nth from end
# 2. **Dummy head** -- simplifies edge cases when head might change
# 3. **Reverse** -- iterative (prev/curr/next) or recursive
# 4. **Merge** -- two-pointer merge like merge sort
#
# **C tips:** Use `struct ListNode { int val; struct ListNode* next; };`. Always `malloc` new nodes, `free` deleted nodes. Watch for dangling pointers.
#
# ---
# ============================================================

import sys, os; sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from test_runner import run_tests


class ListNode:
    def __init__(self, val=0, nxt=None):
        self.val = val
        self.next = nxt


def make_list(arr):
    dummy = ListNode(0)
    curr = dummy
    for v in arr:
        curr.next = ListNode(v)
        curr = curr.next
    return dummy.next


def to_array(head):
    arr = []
    while head:
        arr.append(head.val)
        head = head.next
    return arr


# Reverse Linked List (LC #206) -- Easy
# Reverse a singly linked list.
#
#   Key: Three pointers: prev, curr, next. Or recursive.

def reverse_list(head):
    """head is a ListNode. Return new head."""
    pass


def solve(arr):
    return to_array(reverse_list(make_list(arr)))


run_tests(solve, [
    (([1,2,3,4,5],),  [5,4,3,2,1]),
    (([1,2],),        [2,1]),
    (([1],),          [1]),
    (([],),           []),
])
