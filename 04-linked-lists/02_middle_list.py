import sys, os; sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from test_runner import run_tests



# Middle of the Linked List (LC #876) -- Easy
# Input:  head: ListNode (non-empty)
# Output: ListNode (middle node; if two middles, return second)
# Return the middle node. If two middle nodes, return the second one.
#
# Example:
#   1->2->3->4->5       -> node 3  (middle of 5)
#   1->2->3->4->5->6    -> node 4  (second of two middles)
#   1                    -> node 1
#
#   Key: Slow/fast pointers. Slow moves 1 step, fast moves 2.
#        When fast reaches end, slow is at middle.

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
    (([1,2,3,4,5],),     [3,4,5]),     # odd, return middle onward
    (([1,2,3,4,5,6],),   [4,5,6]),     # even, return second middle onward
    (([1],),              [1]),         # single node
    (([1,2],),            [2]),         # two nodes, return second
    (([1,2,3],),          [2,3]),       # three nodes
])
