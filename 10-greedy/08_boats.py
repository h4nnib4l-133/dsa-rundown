import sys, os; sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from test_runner import run_tests


# Boats to Save People (LC #881) -- Medium
# Min boats, each holds 2 people with weight limit.
#
#   Key: Sort. Pair lightest with heaviest. If they fit, pair them. Else heaviest goes alone.

def num_rescue_boats(people, limit):
    pass


run_tests(num_rescue_boats, [
    (([1,2], 3),      1),
    (([3,2,2,1], 3),  3),
    (([3,5,3,4], 5),  4),
])
