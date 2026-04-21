import os, sys
_d = os.path.dirname(os.path.abspath(__file__))
while _d and not os.path.exists(os.path.join(_d, 'test_runner.py')):
    _d = os.path.dirname(_d)
sys.path.insert(0, _d)
from test_runner import run_tests


# Maximum Units on a Truck (LC #1710) -- Easy
# Input:  boxTypes: List[[numBoxes, unitsPerBox]], truckSize: int
# Output: int (max units carryable within truck box limit)
# Pick boxes to max units. Truck can hold truckSize boxes total.
#
# Example:
# #   [[1,3],[2,2],[3,1]], 4  -> 8   (1*3 + 2*2 + 1*1 = 8)
#
#   Greedy insight: Sort by unitsPerBox desc. Take boxes greedily until truckSize filled.

def maximum_units(box_types, truck_size):
    pass

run_tests(maximum_units, [
    (([[1,3],[2,2],[3,1]], 4),     8),
    (([[5,10],[2,5],[4,7],[3,9]], 10),  91),
    (([[1,1]], 1),                  1),
    (([[5,10]], 3),                 30),
])
