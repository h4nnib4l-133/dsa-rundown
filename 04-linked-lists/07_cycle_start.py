import sys, os; sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from test_runner import run_tests



# Linked List Cycle II (LC #142) -- Medium
# Input:  head: ListNode (may have cycle)
# Output: ListNode (node where cycle starts, or None)
# If linked list has a cycle, return the NODE where cycle begins.
# Return None if no cycle.
#
# Example:
#   3 -> 2 -> 0 -> -4 -> (back to 2)  -> return node with val=2
#   1 -> 2 -> (back to 1)              -> return node with val=1
#   1 -> None                          -> return None
#
#   Key: Floyd's algorithm, phase 2.
#        1. Detect cycle with slow/fast.
#        2. Move one pointer to head, keep other at meeting point.
#        3. Both advance 1 step. They meet at cycle start.

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
    (([3,2,0,-4], 1),   2),     # cycle starts at node val=2
    (([1,2], 0),        1),     # cycle starts at head
    (([1], -1),        -1),     # no cycle
    (([1,2,3,4,5], 2),  3),     # cycle starts at node val=3
    (([1], 0),          1),     # self-loop
])
