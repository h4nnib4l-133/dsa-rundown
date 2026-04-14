import sys, os; sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from test_runner import run_tests


def search_rotated(nums, target):
    pass


run_tests(search_rotated, [
    (([4,5,6,7,0,1,2], 0),   4),
    (([4,5,6,7,0,1,2], 5),   1),
    (([4,5,6,7,0,1,2], 3),  -1),
    (([1], 0),               -1),
    (([1], 1),                0),
    (([3,1], 1),              1),
    (([5,1,2,3,4], 1),       1),
])
