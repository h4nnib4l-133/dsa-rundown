import sys, os; sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from test_runner import run_tests


def length_of_lis(nums):
    pass


run_tests(length_of_lis, [
    (([10,9,2,5,3,7,101,18],),  4),    # 2,3,7,101
    (([0,1,0,3,2,3],),          4),    # 0,1,2,3
    (([7,7,7,7,7],),            1),    # all same
    (([1],),                    1),
    (([1,2,3,4,5],),            5),    # already sorted
])
