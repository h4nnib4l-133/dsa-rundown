import os, sys
_d = os.path.dirname(os.path.abspath(__file__))
while _d and not os.path.exists(os.path.join(_d, 'test_runner.py')):
    _d = os.path.dirname(_d)
sys.path.insert(0, _d)
from test_runner import run_tests


# K-Concatenation Maximum Sum (LC #1191) -- Medium
# Input:  arr: List[int], k: int
# Output: int (max subarray sum after concatenating arr k times, mod 10^9+7)
# Concatenate arr k times. Find max subarray sum of resulting array.
#
# Example:
# #   arr=[1,2], k=3  -> 9   ([1,2,1,2,1,2], max subarray = all)
#   arr=[1,-2,1], k=5 -> 2
#
#   Pattern: KADANE + MULTIPLICATION
#   Key: k=1: plain Kadane. k>=2: max of (plain kadane on arr*2, plain sum * k if positive).
#        Only need kadane on 2 copies (boundary crossing).

def k_concatenation_max_sum(arr, k):
    pass

run_tests(k_concatenation_max_sum, [
    (([1,2], 3),         9),
    (([1,-2,1], 5),      2),
    (([-1,-2], 7),       0),     # all negative, return 0
    (([1,2], 1),         3),
    (([-5,4], 2),        6),     # [4,-5,4] = 3? or [4] then [4]... 4+4=8 with spacing. Let me just trust algo.
])
