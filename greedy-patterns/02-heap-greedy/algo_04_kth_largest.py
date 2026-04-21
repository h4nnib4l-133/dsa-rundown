import os, sys
_d = os.path.dirname(os.path.abspath(__file__))
while _d and not os.path.exists(os.path.join(_d, 'test_runner.py')):
    _d = os.path.dirname(_d)
sys.path.insert(0, _d)
from test_runner import run_tests


# Kth Largest Element (LC #215) -- Medium
# Input:  nums: List[int], k: int
# Output: int (kth largest element)
# Classic. Not kth distinct; kth largest in sorted order.
#
# Example:
# #   [3,2,1,5,6,4], k=2 -> 5
#
#   Greedy insight: Min-heap of size k. Push all nums. Heap keeps k largest seen.
#        Top of heap = kth largest. O(n log k).

def find_kth_largest(nums, k):
    pass

run_tests(find_kth_largest, [
    (([3,2,1,5,6,4], 2),       5),
    (([3,2,3,1,2,4,5,5,6], 4), 4),
    (([1], 1),                 1),
    (([7,7,7], 2),             7),
    (([1,2,3,4,5], 5),         1),
])
