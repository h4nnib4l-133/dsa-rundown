import sys, os; sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from test_runner import run_tests


# Search Insert Position (LC #35) -- Easy
# Find index where target would be inserted in sorted array.
#
#   Key: Lower bound -- first index where `arr[i] >= target`

def search_insert(nums, target):
    pass


run_tests(search_insert, [
    (([1,3,5,6], 5),  2),
    (([1,3,5,6], 2),  1),
    (([1,3,5,6], 7),  4),
    (([1,3,5,6], 0),  0),
    (([1], 0),        0),
    (([1], 2),        1),
])
