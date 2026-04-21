import os, sys
_d = os.path.dirname(os.path.abspath(__file__))
while _d and not os.path.exists(os.path.join(_d, 'test_runner.py')):
    _d = os.path.dirname(_d)
sys.path.insert(0, _d)
from test_runner import run_tests


# Top K Frequent Elements (LC #347) -- Medium
# Input:  nums: List[int], k: int
# Output: List[int] (k most frequent elements)
# Return the k most frequent elements.
#
# Example:
# #   nums=[1,1,1,2,2,3], k=2  -> [1,2]
#
#   Greedy insight: Counter to get frequencies. Min-heap of (freq, num) size k.

def top_k_frequent(nums, k):
    pass


def solve(nums, k):
    return sorted(top_k_frequent(nums, k))

run_tests(top_k_frequent, [
    (([1,1,1,2,2,3], 2),  [1,2]),
    (([1], 1),             [1]),
    (([1,2], 2),           [1,2]),
    (([4,1,-1,2,-1,2,3], 2),  [-1,2]),
])
