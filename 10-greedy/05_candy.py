import sys, os; sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from test_runner import run_tests


def candy(ratings):
    pass


run_tests(candy, [
    (([1,0,2],),    5),
    (([1,2,2],),    4),
    (([1,3,2,2,1],),7),
])
