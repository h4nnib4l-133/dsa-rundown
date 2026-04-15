import sys, os; sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from test_runner import run_tests



# Reorder List (LC #143) -- Medium
# Reorder in-place: L0 -> Ln -> L1 -> Ln-1 -> L2 -> Ln-2 -> ...
#
# Example:
#   1->2->3->4       -> 1->4->2->3
#   1->2->3->4->5    -> 1->5->2->4->3
#
#   Key: Three steps:
#     1. Find middle (slow/fast)
#     2. Reverse second half
#     3. Merge first half and reversed second half alternating

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
    (([1,2,3,4],),     [1,4,2,3]),
    (([1,2,3,4,5],),   [1,5,2,4,3]),
    (([1],),           [1]),             # single node
    (([1,2],),         [1,2]),           # two nodes
    (([1,2,3],),       [1,3,2]),         # three nodes
    (([1,2,3,4,5,6],), [1,6,2,5,3,4]),  # six nodes
])
