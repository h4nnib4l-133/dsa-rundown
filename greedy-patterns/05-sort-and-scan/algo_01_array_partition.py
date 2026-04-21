import os, sys
_d = os.path.dirname(os.path.abspath(__file__))
while _d and not os.path.exists(os.path.join(_d, 'test_runner.py')):
    _d = os.path.dirname(_d)
sys.path.insert(0, _d)
from test_runner import run_tests


# Array Partition (LC #561) -- Easy
# Input:  nums: List[int] (length 2n)
# Output: int (max possible sum of min(a_i, b_i) over all pairings)
# Pair up 2n numbers to maximize sum of pair minimums.
#
# Example:
# #   [1,4,3,2] -> 4   (pair (1,2) and (3,4): min=1+3=4)
#
#   Greedy insight: Sort. Sum every second element (indices 0, 2, 4, ...).

def array_pair_sum(nums):
    pass

run_tests(array_pair_sum, [
    (([1,4,3,2],),    4),
    (([6,2,6,5,1,2],), 9),
    (([1,1],),         1),
    (([],),            0),
])
