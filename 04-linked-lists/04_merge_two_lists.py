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


def merge_two_lists(l1, l2):
    pass


def solve(a1, a2):
    return to_array(merge_two_lists(make_list(a1), make_list(a2)))


run_tests(solve, [
    (([1,2,4], [1,3,4]),  [1,1,2,3,4,4]),
    (([], []),             []),
    (([], [0]),            [0]),
    (([1], [2]),           [1,2]),
])
