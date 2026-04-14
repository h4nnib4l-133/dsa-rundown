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


# ---- WRITE YOUR SOLUTION HERE ----

def reverse_list(head):
    """head is a ListNode. Return new head."""
    pass

# ---- END SOLUTION ----


def solve(arr):
    return to_array(reverse_list(make_list(arr)))


run_tests(solve, [
    (([1,2,3,4,5],),  [5,4,3,2,1]),
    (([1,2],),        [2,1]),
    (([1],),          [1]),
    (([],),           []),
])
