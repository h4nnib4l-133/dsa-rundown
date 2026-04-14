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


import heapq


def merge_k_lists(lists):
    pass


def solve(arrs):
    heads = [make_list(a) for a in arrs]
    return to_array(merge_k_lists(heads))


run_tests(solve, [
    (([[1,4,5],[1,3,4],[2,6]],),  [1,1,2,3,4,4,5,6]),
    (([],),                        []),
    (([[]],),                      []),
])
