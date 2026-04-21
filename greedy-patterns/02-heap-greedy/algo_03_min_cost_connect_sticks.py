import os, sys
_d = os.path.dirname(os.path.abspath(__file__))
while _d and not os.path.exists(os.path.join(_d, 'test_runner.py')):
    _d = os.path.dirname(_d)
sys.path.insert(0, _d)
from test_runner import run_tests


# Minimum Cost to Connect Sticks (LC #1167) -- Medium
# Input:  sticks: List[int]
# Output: int (min total cost to combine all sticks; cost = sum of combined)
# Combine two sticks with cost = sum. Repeat until one remains. Min total cost.
#
# Example:
# #   [2,4,3]  -> 14
#     2+3=5 (cost 5), 5+4=9 (cost 9), total=14.
#     Or 4+3=7 (cost 7), 7+2=9 (cost 9), total=16. Greedy wins.
#
#   Greedy insight: Min-heap. Always pop two smallest, combine, push back. Sum all combination costs.

def connect_sticks(sticks):
    pass

run_tests(connect_sticks, [
    (([2,4,3],),           14),
    (([1,8,3,5],),         30),
    (([5],),                0),
    (([1,1],),              2),
    (([1,2,3,4,5,6],),     51),
])
