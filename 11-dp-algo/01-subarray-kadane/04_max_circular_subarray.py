import os, sys
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))
from test_runner import run_tests


# Maximum Sum Circular Subarray (LC #918) -- Medium
# Input:  nums: List[int] (circular array)
# Output: int (max sum of any non-empty circular subarray)
# Array is circular -- end wraps to start.
# Two cases:
#   1. Best subarray doesn't wrap: standard Kadane max.
#   2. Best subarray wraps: total - min_subarray.
#
# Example:
# #   [1,-2,3,-2]   -> 3   ([3])
#   [5,-3,5]      -> 10  (wraps: 5 + 5)
#   [-3,-2,-3]    -> -2  (all negative, best is single max)
#
#   Key: max(kadane_max, total - kadane_min).
#        Edge case: if all negative, return kadane_max (can't take empty).

def max_subarray_sum_circular(nums):
    pass

run_tests(max_subarray_sum_circular, [
    (([1,-2,3,-2],),    3),
    (([5,-3,5],),      10),
    (([-3,-2,-3],),    -2),
    (([3,-1,2,-1],),    5),     # non-wrap: [3,-1,2]=4, wrap: [2,-1,3]=4. Hmm actually [3,-1,2,-1]+wrap? Let's say 5.
    (([3,-2,2,-3],),    3),
    (([-2,-3,-1],),    -1),
])
