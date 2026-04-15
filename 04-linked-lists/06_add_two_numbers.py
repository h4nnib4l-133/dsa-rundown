import sys, os; sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from test_runner import run_tests



# Add Two Numbers (LC #2) -- Medium
# Two non-empty linked lists represent non-negative integers in REVERSE order.
# Each node is a single digit. Add them and return sum as linked list.
#
# Example:
#   2->4->3  +  5->6->4  =  7->0->8    (342 + 465 = 807)
#   0  +  0  =  0
#   9->9->9  +  1  =  0->0->0->1        (999 + 1 = 1000)
#
#   Key: Traverse both lists simultaneously. Sum digits + carry.
#        Create new node for each digit. Don't forget final carry.

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


def add_two_numbers(l1, l2):
    pass


def solve(a1, a2):
    return to_array(add_two_numbers(make_list(a1), make_list(a2)))


run_tests(solve, [
    (([2,4,3], [5,6,4]),         [7,0,8]),       # 342+465=807
    (([0], [0]),                  [0]),            # 0+0=0
    (([9,9,9], [1]),              [0,0,0,1]),      # 999+1=1000
    (([9,9,9,9], [9,9,9]),        [8,9,9,0,1]),    # 9999+999=10998
    (([5], [5]),                  [0,1]),           # 5+5=10
    (([1,8], [0]),                [1,8]),           # 81+0=81
    (([2,4,3], [5,6,4,1]),        [7,0,8,1]),      # different lengths: 342+1465=1807
])
