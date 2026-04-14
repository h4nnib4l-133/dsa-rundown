import sys, os; sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from test_runner import run_tests


def sort_colors(nums):
    """Sort in-place. Return nums for testing."""
    pass
    return nums


run_tests(sort_colors, [
    (([2,0,2,1,1,0],), [0,0,1,1,2,2]),
    (([2,0,1],),        [0,1,2]),
    (([0],),            [0]),
    (([1,0],),          [0,1]),
])
