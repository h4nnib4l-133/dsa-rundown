import os, sys
_d = os.path.dirname(os.path.abspath(__file__))
while _d and not os.path.exists(os.path.join(_d, 'test_runner.py')):
    _d = os.path.dirname(_d)
sys.path.insert(0, _d)
from test_runner import run_tests


# Last Stone Weight (LC #1046) -- Easy
# Input:  stones: List[int]
# Output: int (weight of final stone after repeated smashing)
# Smash two heaviest. y-x remains. Repeat until 0 or 1 left.
#
# Example:
# #   [2,7,4,1,8,1]  -> 1
#     8,7 -> 1; stones=[2,4,1,1,1]; 4,2 -> 2; ...
#
#   Greedy insight: Max-heap. Pop two largest, push difference if non-zero.

def last_stone_weight(stones):
    pass

run_tests(last_stone_weight, [
    (([2,7,4,1,8,1],),  1),
    (([1],),            1),
    (([2,2],),          0),
    (([1,3],),          2),
    (([31,26,33,21,40],),  5),
])
