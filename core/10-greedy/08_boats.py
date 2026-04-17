import os, sys
_d = os.path.dirname(os.path.abspath(__file__))
while _d and not os.path.exists(os.path.join(_d, 'test_runner.py')):
    _d = os.path.dirname(_d)
sys.path.insert(0, _d)
from test_runner import run_tests



# Boats to Save People (LC #881) -- Medium
# Input:  people: List[int] (weights), limit: int (boat weight limit, max 2 people)
# Output: int (minimum number of boats)
# Each boat carries at most 2 people with weight limit.
# Find minimum number of boats.
#
# Example:
#   people=[1,2], limit=3      -> 1  (both fit in one boat)
#   people=[3,2,2,1], limit=3  -> 3  (1+2, 2, 3)
#   people=[3,5,3,4], limit=5  -> 4  (everyone alone)
#
#   Key: Sort. Two pointers from lightest and heaviest.
#        If lightest+heaviest <= limit, pair them (move both pointers).
#        Otherwise heaviest goes alone (move right pointer only).

def num_rescue_boats(people, limit):
    pass


run_tests(num_rescue_boats, [
    (([1,2], 3),        1),
    (([3,2,2,1], 3),    3),
    (([3,5,3,4], 5),    4),     # nobody can pair
    (([1,1], 2),        1),     # both fit
    (([2,2,2,2], 3),    4),     # no pairs possible (2+2=4>3)
    (([1,2,3,4,5], 5),  3),     # 1+4, 2+3, 5
    (([5], 5),          1),     # single person
])
