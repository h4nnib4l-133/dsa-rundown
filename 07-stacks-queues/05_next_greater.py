import sys, os; sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from test_runner import run_tests


def next_greater_element(nums1, nums2):
    pass


run_tests(next_greater_element, [
    (([4,1,2], [1,3,4,2]),  [-1,3,-1]),
    (([2,4], [1,2,3,4]),    [3,-1]),
])
