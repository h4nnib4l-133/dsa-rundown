import sys, os; sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from test_runner import run_tests


def product_except_self(nums):
    pass


run_tests(product_except_self, [
    (([1,2,3,4],),    [24,12,8,6]),
    (([-1,1,0,-3,3],),[0,0,9,0,0]),
    (([2,3],),        [3,2]),
])
