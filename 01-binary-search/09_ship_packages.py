import sys, os; sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from test_runner import run_tests


# Capacity to Ship Packages (LC #1011) -- Medium
# Find minimum ship capacity to ship all packages within d days.
#
#   Key: BS on answer. lo = max(weights), hi = sum(weights). Greedy check per capacity.

def ship_within_days(weights, days):
    pass


run_tests(ship_within_days, [
    (([1,2,3,4,5,6,7,8,9,10], 5),  15),
    (([3,2,2,4,1,4], 3),            6),
    (([1,2,3,1,1], 4),              3),
])
