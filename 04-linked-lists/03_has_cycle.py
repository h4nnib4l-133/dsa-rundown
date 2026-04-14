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


def has_cycle(head):
    pass


# Build cycled list for testing
def solve_cycle(arr, pos):
    head = make_list(arr)
    if pos == -1:
        return has_cycle(head)
    nodes = []
    curr = head
    while curr:
        nodes.append(curr)
        curr = curr.next
    nodes[-1].next = nodes[pos]
    return has_cycle(head)


run_tests(solve_cycle, [
    (([3,2,0,-4], 1),  True),
    (([1,2], 0),       True),
    (([1], -1),        False),
    (([1,2,3], -1),    False),
])
