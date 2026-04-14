import sys, os; sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from test_runner import run_tests


def coin_change(coins, amount):
    """Return min coins needed, or -1 if impossible"""
    pass


run_tests(coin_change, [
    (([1,5,10,25], 30),   2),    # 25+5
    (([1,2,5], 11),       3),    # 5+5+1
    (([2], 3),           -1),    # impossible
    (([1], 0),            0),    # zero amount
    (([1,2,5], 100),     20),    # 20 x 5
])
