import sys, os; sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from test_runner import run_tests


# Remove Nth Node From End (LC #19) -- Medium
# Remove nth node from end in one pass.
#
#   Key: Two pointers with gap of n. When fast reaches end, slow is at target.

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


def remove_nth_from_end(head, n):
    pass


def solve(arr, n):
    return to_array(remove_nth_from_end(make_list(arr), n))


run_tests(solve, [
    (([1,2,3,4,5], 2), [1,2,3,5]),
    (([1], 1),         []),
    (([1,2], 1),       [1]),
    (([1,2], 2),       [2]),
])
