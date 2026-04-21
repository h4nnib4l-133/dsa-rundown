import os, sys
_d = os.path.dirname(os.path.abspath(__file__))
while _d and not os.path.exists(os.path.join(_d, 'test_runner.py')):
    _d = os.path.dirname(_d)
sys.path.insert(0, _d)
from test_runner import run_tests


# Find K Pairs with Smallest Sums (LC #373) -- Medium
# Input:  nums1: List[int], nums2: List[int] (sorted), k: int
# Output: List[[a,b]] (k pairs with smallest sum)
# From sorted arrays, pick k pairs (one from each) with smallest sums.
#
# Example:
# #   nums1=[1,7,11], nums2=[2,4,6], k=3  -> [[1,2],[1,4],[1,6]]
#
#   Greedy insight: Min-heap. Start with (nums1[0]+nums2[0], 0, 0). Pop and push its right/down neighbor.
#        BFS-like expansion with visited set.

def k_smallest_pairs(nums1, nums2, k):
    pass


def solve(nums1, nums2, k):
    return sorted([sorted(p) for p in k_smallest_pairs(nums1, nums2, k)])

run_tests(k_smallest_pairs, [
    (([1,7,11], [2,4,6], 3),      [[1,2],[1,4],[1,6]]),
    (([1,1,2], [1,2,3], 2),       [[1,1],[1,1]]),
    (([1,2], [3], 3),             [[1,3],[2,3]]),
])
