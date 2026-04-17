import os
import sys

sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
from test_runner import run_tests

# Find Peak Element (LC #162) -- Medium
# Input:  nums: List[int] (nums[-1] = nums[n] = -inf, no adjacent equal)
# Output: int (index of ANY peak element)
# A peak element is strictly greater than its neighbors.
# nums[-1] = nums[n] = -infinity. Return index of ANY peak.
#
# Example:
#   nums = [1,2,3,1]      -> 2  (nums[2]=3 is a peak)
#   nums = [1,2,1,3,5,6,4] -> 5  (nums[5]=6 is a peak, or 1 also valid)
#
#   Key: If nums[mid] < nums[mid+1], peak must be to the right.
#        Otherwise peak is at mid or to the left. O(log n).


def find_peak(nums):
    """Return index of any peak element"""
    lo, hi = 0, len(nums) - 1
    while lo < hi:
        mid = (lo + hi) // 2
        if nums[mid] < nums[mid + 1]:
            lo = mid + 1
        else:
            hi = mid
    return lo


# Peak can be any valid peak, so we validate the result
def validate_peak(nums):
    idx = find_peak(nums)
    if idx is None:
        return False
    n = len(nums)
    left_ok = idx == 0 or nums[idx] > nums[idx - 1]
    right_ok = idx == n - 1 or nums[idx] > nums[idx + 1]
    return left_ok and right_ok


run_tests(
    validate_peak,
    [
        (([1, 2, 3, 1],), True),            # peak in middle
        (([1, 2, 1, 3, 5, 6, 4],), True),   # multiple peaks, find any
        (([1],), True),                     # single element is a peak
        (([1, 2],), True),                  # ascending, peak at end
        (([2, 1],), True),                  # descending, peak at start
        (([1, 2, 3],), True),               # ascending, peak at end
        (([3, 2, 1],), True),               # descending, peak at start
        (([1, 3, 2, 1],), True),            # peak near start
        (([1, 2, 3, 4, 5],), True),         # strictly increasing
        (([5, 4, 3, 2, 1],), True),         # strictly decreasing
        (([1, 3, 2, 4, 1],), True),         # two peaks, algorithm finds one
    ],
)
