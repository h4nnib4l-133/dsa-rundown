import os, sys
_d = os.path.dirname(os.path.abspath(__file__))
while _d and not os.path.exists(os.path.join(_d, 'test_runner.py')):
    _d = os.path.dirname(_d)
sys.path.insert(0, _d)
from test_runner import run_tests



# Linked List Cycle (LC #141) -- Easy
# Input:  head: ListNode (or None, may contain cycle)
# Output: bool (True if cycle exists)
# Given head of linked list, return True if there is a cycle.
# A cycle exists if some node's next points to a previous node.
#
# Example:
#   3 -> 2 -> 0 -> -4 -> (back to 2)  -> True
#   1 -> 2 -> (back to 1)              -> True
#   1 -> None                          -> False
#
#   Key: Floyd's tortoise and hare.
#        Slow moves 1 step, fast moves 2.
#        If they meet, cycle exists. If fast hits None, no cycle.

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
    (([3,2,0,-4], 1),    True),     # cycle at node index 1
    (([1,2], 0),         True),     # cycle at head
    (([1], -1),          False),    # no cycle, single node
    (([1,2,3], -1),      False),    # no cycle, 3 nodes
    (([1,2,3,4,5], 2),   True),     # cycle at middle
    (([1], 0),           True),     # self-loop
])
