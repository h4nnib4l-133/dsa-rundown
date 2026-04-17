import os, sys
_d = os.path.dirname(os.path.abspath(__file__))
while _d and not os.path.exists(os.path.join(_d, 'test_runner.py')):
    _d = os.path.dirname(_d)
sys.path.insert(0, _d)
from test_runner import run_tests

# Find First and Last Position of Element (LC #34) -- Medium
# Input:  nums: List[int] (sorted ascending, may have duplicates), target: int
# Output: List[int] of length 2: [first_index, last_index] or [-1, -1]
# Given sorted array, find starting and ending position of target.
# Return [-1, -1] if not found. Must be O(log n).
#
# Example:
#   nums = [5,7,7,8,8,10], target = 8  -> [3, 4]
#   nums = [5,7,7,8,8,10], target = 6  -> [-1, -1]
#   nums = [], target = 0              -> [-1, -1]
#
#   Key: Two binary searches -- one for leftmost, one for rightmost.


def right(nums, target):
    lo, hi = 0, len(nums) - 1
    result = -1
    while lo <= hi:
        mid = (lo + hi) // 2
        if nums[mid] == target:
            result = mid
            lo = mid + 1
        elif nums[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return result


def left(nums, target):
    lo, hi = 0, len(nums) - 1
    result = -1
    while lo <= hi:
        mid = (lo + hi) // 2
        if nums[mid] == target:
            result = mid
            hi = mid - 1
        elif nums[mid] > target:
            hi = mid - 1
        else:
            lo = mid + 1
    return result


def search_range(nums, target):
    """Return [first, last] index of target, or [-1, -1]"""
    return [left(nums, target), right(nums, target)]


run_tests(
    search_range,
    [
        (([5, 7, 7, 8, 8, 10], 8), [3, 4]),  # target appears twice
        (([5, 7, 7, 8, 8, 10], 7), [1, 2]),  # target appears twice
        (([5, 7, 7, 8, 8, 10], 5), [0, 0]),  # target at start, once
        (([5, 7, 7, 8, 8, 10], 10), [5, 5]),  # target at end, once
        (([5, 7, 7, 8, 8, 10], 6), [-1, -1]),  # not found
        (([], 0), [-1, -1]),  # empty array
        (([1], 1), [0, 0]),  # single element found
        (([1], 2), [-1, -1]),  # single element not found
        (([2, 2], 2), [0, 1]),  # all same
        (([1, 1, 1, 1, 1], 1), [0, 4]),  # all duplicates
        (([1, 2, 3, 4, 5], 3), [2, 2]),  # unique elements
    ],
)
