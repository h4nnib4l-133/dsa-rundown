import os, sys
_d = os.path.dirname(os.path.abspath(__file__))
while _d and not os.path.exists(os.path.join(_d, 'test_runner.py')):
    _d = os.path.dirname(_d)
sys.path.insert(0, _d)
from test_runner import run_tests



# Capacity to Ship Packages Within D Days (LC #1011) -- Medium
# Input:  weights: List[int] (package weights in order), days: int
# Output: int (minimum ship capacity)
# Packages must be shipped in order. Find minimum ship capacity
# to ship all packages within 'days' days.
#
# Example:
#   weights = [1,2,3,4,5,6,7,8,9,10], days = 5
#   capacity=15: day1=[1,2,3,4,5] day2=[6,7] day3=[8] day4=[9] day5=[10] ✓
#   -> 15
#
#   Key: BS on answer. lo = max(weights), hi = sum(weights).
#        For each capacity, greedily check if we can ship in <= days.

def ship_within_days(weights, days):
    pass


run_tests(ship_within_days, [
    (([1,2,3,4,5,6,7,8,9,10], 5),   15),   # classic example
    (([3,2,2,4,1,4], 3),             6),    # small array
    (([1,2,3,1,1], 4),               3),    # many days
    (([1,2,3,4,5,6,7,8,9,10], 1),  55),    # 1 day = must carry everything
    (([1,2,3,4,5,6,7,8,9,10], 10), 10),    # 10 days = one package per day
    (([10], 1),                      10),   # single package
    (([1,1,1,1,1], 1),               5),    # all in one day
    (([1,1,1,1,1], 5),               1),    # one per day
])
