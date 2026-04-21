import os, sys
_d = os.path.dirname(os.path.abspath(__file__))
while _d and not os.path.exists(os.path.join(_d, 'test_runner.py')):
    _d = os.path.dirname(_d)
sys.path.insert(0, _d)
from test_runner import run_tests


# Sort Array By Parity (LC #905) -- Easy
# Input:  nums: List[int]
# Output: List[int] (evens before odds; any valid order)
# Move all even numbers before odd numbers.
#
# Example:
# #   [3,1,2,4] -> [2,4,3,1] (any valid)
#
#   Greedy insight: Two pointers from both ends. Swap when left is odd, right is even.

def sort_array_by_parity(nums):
    pass


def solve(nums):
    result = sort_array_by_parity(nums)
    # validate: first half evens, second half odds
    seen_odd = False
    for x in result:
        if x % 2 == 1:
            seen_odd = True
        elif seen_odd:
            return False
    return sorted(result) == sorted(nums)

run_tests(sort_array_by_parity, [
    (([3,1,2,4],),    True),
    (([0],),          True),
    (([1,2,3,4,5,6,7],),  True),
    (([],),           True),
])
