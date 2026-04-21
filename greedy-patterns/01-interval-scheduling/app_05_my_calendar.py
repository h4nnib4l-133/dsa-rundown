import os, sys
_d = os.path.dirname(os.path.abspath(__file__))
while _d and not os.path.exists(os.path.join(_d, 'test_runner.py')):
    _d = os.path.dirname(_d)
sys.path.insert(0, _d)
from test_runner import run_tests


# My Calendar I (LC #729) -- Medium
# Input:  events: List[[start, end]] (book in sequence)
# Output: List[bool] (can each new booking be made without conflict?)
# Book events one at a time. Can book iff no overlap with previously booked.
#
# Example:
# #   bookings=[[10,20],[15,25],[20,30]]
#   -> [True, False, True]   ([15,25] overlaps [10,20]; [20,30] touches [10,20] OK)
#
#   Greedy insight: Maintain sorted list of bookings. For each new [s,e], check no existing overlap.
#        Overlap: exists booking [a,b] with a < e and s < b.

def my_calendar(events):
    pass

run_tests(my_calendar, [
    (([[10,20],[15,25],[20,30]],),  [True, False, True]),
    (([[47,50],[33,41],[39,45]],),  [True, True, False]),
    (([[1,2],[2,3],[3,4]],),         [True, True, True]),
])
