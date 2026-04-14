import sys, os; sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from test_runner import run_tests


def num_rescue_boats(people, limit):
    pass


run_tests(num_rescue_boats, [
    (([1,2], 3),      1),
    (([3,2,2,1], 3),  3),
    (([3,5,3,4], 5),  4),
])
