import sys, os; sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from test_runner import run_tests



# Search in Rotated Sorted Array (LC #33) -- Medium
# Input:  nums: List[int] (sorted then rotated, no duplicates), target: int
# Output: int (index of target, or -1)
# Array was sorted, then rotated at unknown pivot.
# Search for target in O(log n). No duplicates.
#
# Example:
#   nums = [4,5,6,7,0,1,2], target = 0  -> 4
#   (was [0,1,2,4,5,6,7], rotated at index 4)
#
#   nums = [4,5,6,7,0,1,2], target = 3  -> -1  (not found)
#
#   Key: Check which half is sorted (nums[lo] <= nums[mid]).
#        If target is in the sorted half's range, search there.
#        Otherwise search the other half.

def search_rotated(nums, target):
    pass


run_tests(search_rotated, [
    (([4,5,6,7,0,1,2], 0),    4),     # target in right (unsorted) half
    (([4,5,6,7,0,1,2], 5),    1),     # target in left (sorted) half
    (([4,5,6,7,0,1,2], 3),   -1),     # not in array
    (([4,5,6,7,0,1,2], 4),    0),     # first element
    (([4,5,6,7,0,1,2], 2),    6),     # last element
    (([1], 0),                -1),     # single element, miss
    (([1], 1),                 0),     # single element, hit
    (([3,1], 1),               1),     # two elements, rotated
    (([3,1], 3),               0),     # two elements, first
    (([5,1,2,3,4], 1),        1),     # rotated by 1
    (([1,2,3,4,5], 3),        2),     # not rotated at all
    (([2,1], 1),               1),     # minimum rotation
])
