import sys, os; sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from test_runner import run_tests


def find_median(nums1, nums2):
    pass


run_tests(find_median, [
    (([1,3], [2]),         2.0),
    (([1,2], [3,4]),       2.5),
    (([0,0], [0,0]),       0.0),
    (([], [1]),            1.0),
    (([2], []),            2.0),
])
