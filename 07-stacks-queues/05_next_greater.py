import sys, os; sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from test_runner import run_tests


# Next Greater Element I (LC #496) -- Easy
# For each element in nums1, find next greater element in nums2.
#
#   Key: Monotonic decreasing stack. Process nums2, map each element to its next greater.

def next_greater_element(nums1, nums2):
    pass


run_tests(next_greater_element, [
    (([4,1,2], [1,3,4,2]),  [-1,3,-1]),
    (([2,4], [1,2,3,4]),    [3,-1]),
])
