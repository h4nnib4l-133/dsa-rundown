import sys, os; sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from test_runner import run_tests



# Remove Nth Node From End of List (LC #19) -- Medium
# Input:  head: ListNode, n: int (1 <= n <= list length)
# Output: ListNode (head after removing nth node from end)
# Remove the nth node from the END of the list. Return modified head.
# Guaranteed n is valid.
#
# Example:
#   1->2->3->4->5, n=2  ->  1->2->3->5  (removed 4)
#   1, n=1               ->  (empty)     (removed only node)
#   1->2, n=2            ->  2           (removed head)
#
#   Key: Two pointers with gap of n.
#        Advance fast n steps ahead. Then move both until fast hits end.
#        Slow is now just before the target. Use dummy head for edge cases.

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
    (([1,2,3,4,5], 2),  [1,2,3,5]),     # remove 4th node
    (([1], 1),           []),             # remove only node
    (([1,2], 1),         [1]),            # remove tail
    (([1,2], 2),         [2]),            # remove head
    (([1,2,3], 3),       [2,3]),          # remove head of 3
    (([1,2,3,4,5], 1),  [1,2,3,4]),      # remove last
    (([1,2,3,4,5], 5),  [2,3,4,5]),      # remove first
])
