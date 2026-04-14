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


def middle_node(head):
    pass


def solve(arr):
    node = middle_node(make_list(arr))
    return to_array(node)


run_tests(solve, [
    (([1,2,3,4,5],),   [3,4,5]),
    (([1,2,3,4,5,6],), [4,5,6]),
    (([1],),            [1]),
])
