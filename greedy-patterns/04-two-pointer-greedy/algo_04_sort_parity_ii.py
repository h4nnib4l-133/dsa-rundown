import os, sys
_d = os.path.dirname(os.path.abspath(__file__))
while _d and not os.path.exists(os.path.join(_d, 'test_runner.py')):
    _d = os.path.dirname(_d)
sys.path.insert(0, _d)
from test_runner import run_tests


# Sort Array By Parity II (LC #922) -- Easy
# Input:  nums: List[int] (half even, half odd)
# Output: List[int] (even at even indices, odd at odd indices)
# nums[even_idx] must be even, nums[odd_idx] must be odd.
#
# Example:
# #   [4,2,5,7] -> [4,5,2,7] or [4,7,2,5]
#
#   Greedy insight: Two pointers: i on even indices, j on odd. Advance i while nums[i] even. Similarly j.
#        Swap when both mismatched.

def sort_array_by_parity_ii(nums):
    pass


def solve(nums):
    result = sort_array_by_parity_ii(nums)
    if sorted(result) != sorted(nums):
        return False
    for i, v in enumerate(result):
        if (i % 2) != (v % 2):
            return False
    return True

run_tests(sort_array_by_parity_ii, [
    (([4,2,5,7],),     True),
    (([2,3],),         True),
    (([1,4,5,2],),     True),
    (([],),            True),
])
