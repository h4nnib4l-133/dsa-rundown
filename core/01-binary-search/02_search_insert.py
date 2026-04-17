import os, sys
_d = os.path.dirname(os.path.abspath(__file__))
while _d and not os.path.exists(os.path.join(_d, 'test_runner.py')):
    _d = os.path.dirname(_d)
sys.path.insert(0, _d)
from test_runner import run_tests


# Search Insert Position (LC #35) -- Easy
# Input:  nums: List[int] (sorted ascending, no duplicates), target: int
# Output: int (index of target, or index where it would be inserted)
# Given sorted array and target, return index if found.
# If not, return the index where it would be inserted to keep sorted.
#
# Example:
#   nums = [1, 3, 5, 6], target = 5  -> 2  (found at index 2)
#   nums = [1, 3, 5, 6], target = 2  -> 1  (insert between 1 and 3)
#   nums = [1, 3, 5, 6], target = 7  -> 4  (insert at end)
#   nums = [1, 3, 5, 6], target = 0  -> 0  (insert at start)
#
#   Key: Lower bound -- first index where nums[i] >= target.

def search_insert(nums, target):
    hi, lo = len(nums) - 1, 0
    if nums[lo] > target:
        return 0

    if nums[hi] <= target:
        return len(nums)

    while lo <= hi:
        mid = (lo + hi) // 2
        if nums[mid] >= target:
            return mid
        else:
            lo = mid + 1


run_tests(search_insert, [
    (([1, 3, 5, 6], 5),  2),     # target exists
    (([1, 3, 5, 6], 2),  1),     # insert in middle
    (([1, 3, 5, 6], 7),  4),     # insert at end
    (([1, 3, 5, 6], 0),  0),     # insert at start
    (([1], 0),            0),     # single, insert before
    (([1], 1),            0),     # single, exact match
    (([1], 2),            1),     # single, insert after
    (([1, 3], 2),         1),     # two elements, insert between
    (([1, 3, 5, 6], 4),  2),     # insert between 3 and 5
])
