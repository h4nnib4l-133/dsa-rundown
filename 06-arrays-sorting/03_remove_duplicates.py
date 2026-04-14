import sys, os; sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from test_runner import run_tests


def remove_duplicates(nums):
    """Return new length. Modify nums in-place."""
    pass


run_tests(remove_duplicates, [
    (([1,1,2],),          2),
    (([0,0,1,1,1,2,2,3,3,4],), 5),
    (([1],),              1),
])
