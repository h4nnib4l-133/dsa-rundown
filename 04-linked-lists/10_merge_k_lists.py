import sys, os; sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from test_runner import run_tests



# Merge K Sorted Lists (LC #23) -- Hard
# Given array of k sorted linked lists, merge into one sorted list.
#
# Example:
#   [[1,4,5], [1,3,4], [2,6]]
#   -> [1,1,2,3,4,4,5,6]
#
#   Key (heap): Push all heads into min-heap. Pop smallest, push its next.
#   Key (divide & conquer): Merge pairs recursively, like merge sort.
#   Time: O(N log k) where N = total nodes, k = number of lists.

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
    (([[1,4,5],[1,3,4],[2,6]],),   [1,1,2,3,4,4,5,6]),
    (([],),                         []),        # no lists
    (([[]],),                       []),        # one empty list
    (([[1],[2],[3]],),              [1,2,3]),    # single element each
    (([[1,2,3]],),                  [1,2,3]),    # single list
    (([[],[1],[],[]],),             [1]),        # mostly empty
    (([[5,10],[1,3,8],[2,6,7]],),  [1,2,3,5,6,7,8,10]),
])
