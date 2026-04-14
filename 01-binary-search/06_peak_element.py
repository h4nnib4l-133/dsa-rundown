import sys, os; sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from test_runner import run_tests


def find_peak(nums):
    """Return index of any peak element"""
    pass


# Peak can be any valid peak, so we validate differently
def validate_peak(nums):
    idx = find_peak(nums)
    if idx is None:
        return False
    n = len(nums)
    left_ok = (idx == 0 or nums[idx] > nums[idx-1])
    right_ok = (idx == n-1 or nums[idx] > nums[idx+1])
    return left_ok and right_ok


run_tests(validate_peak, [
    (([1,2,3,1],),        True),
    (([1,2,1,3,5,6,4],),  True),
    (([1],),              True),
    (([1,2],),            True),
    (([2,1],),            True),
])
