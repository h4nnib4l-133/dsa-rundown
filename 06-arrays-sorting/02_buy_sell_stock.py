import sys, os; sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from test_runner import run_tests


def max_profit(prices):
    pass


run_tests(max_profit, [
    (([7,1,5,3,6,4],), 5),
    (([7,6,4,3,1],),   0),
    (([2,4,1],),        2),
    (([1],),            0),
])
