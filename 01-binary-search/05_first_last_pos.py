import sys, os; sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from test_runner import run_tests


def search_range(nums, target):
    """Return [first, last] index of target, or [-1, -1]"""
    pass


run_tests(search_range, [
    (([5,7,7,8,8,10], 8),  [1, 2]),   # wait, 8 is at index 3,4
    (([5,7,7,8,8,10], 8),  [3, 4]),
    (([5,7,7,8,8,10], 6),  [-1, -1]),
    (([], 0),               [-1, -1]),
    (([1], 1),              [0, 0]),
    (([2,2], 2),            [0, 1]),
])
