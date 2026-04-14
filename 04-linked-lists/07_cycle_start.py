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


def detect_cycle(head):
    """Return the node where cycle begins, or None"""
    pass


def solve(arr, pos):
    head = make_list(arr)
    if pos == -1:
        node = detect_cycle(head)
        return -1 if node is None else node.val
    nodes = []
    curr = head
    while curr:
        nodes.append(curr)
        curr = curr.next
    nodes[-1].next = nodes[pos]
    node = detect_cycle(head)
    return -1 if node is None else node.val


run_tests(solve, [
    (([3,2,0,-4], 1),  2),
    (([1,2], 0),       1),
    (([1], -1),       -1),
])
