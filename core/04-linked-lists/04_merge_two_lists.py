import os, sys
_d = os.path.dirname(os.path.abspath(__file__))
while _d and not os.path.exists(os.path.join(_d, 'test_runner.py')):
    _d = os.path.dirname(_d)
sys.path.insert(0, _d)
from test_runner import run_tests



# Merge Two Sorted Lists (LC #21) -- Easy
# Input:  l1: ListNode (sorted), l2: ListNode (sorted)
# Output: ListNode (merged sorted list)
# Merge two sorted linked lists into one sorted list.
# Made by splicing together the nodes of the first two lists.
#
# Example:
#   1->2->4  +  1->3->4  ->  1->1->2->3->4->4
#   (empty)  +  0         ->  0
#
#   Key: Dummy head node. Compare both heads, link smaller one.
#        Advance the pointer of the list you took from.
#        Attach remaining list when one is exhausted.

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
    (([1,2,4], [1,3,4]),     [1,1,2,3,4,4]),
    (([], []),                []),              # both empty
    (([], [0]),               [0]),             # one empty
    (([0], []),               [0]),             # other empty
    (([1], [2]),              [1,2]),
    (([5,10,15], [2,8,20]),   [2,5,8,10,15,20]),  # interleaved
    (([1,1,1], [1,1,1]),      [1,1,1,1,1,1]),     # all same
])
