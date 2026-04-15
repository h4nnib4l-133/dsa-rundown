import sys, os; sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from test_runner import run_tests


# Reorder List (LC #143) -- Medium
# Reorder: L0 -> Ln -> L1 -> Ln-1 -> ...
#
#   Key: Find middle, reverse second half, merge alternating

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


def reorder_list(head):
    """Reorder in-place: L0->Ln->L1->Ln-1->..."""
    pass


def solve(arr):
    head = make_list(arr)
    reorder_list(head)
    return to_array(head)


run_tests(solve, [
    (([1,2,3,4],),   [1,4,2,3]),
    (([1,2,3,4,5],), [1,5,2,4,3]),
    (([1],),         [1]),
    (([1,2],),       [1,2]),
])
