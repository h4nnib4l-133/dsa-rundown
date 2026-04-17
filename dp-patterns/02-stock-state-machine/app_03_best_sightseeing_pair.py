import os, sys
_d = os.path.dirname(os.path.abspath(__file__))
while _d and not os.path.exists(os.path.join(_d, 'test_runner.py')):
    _d = os.path.dirname(_d)
sys.path.insert(0, _d)
from test_runner import run_tests


# Best Sightseeing Pair (LC #1014) -- Medium
# Input:  values: List[int]
# Output: int (max score of values[i] + values[j] + i - j for i < j)
# Pick i < j maximizing values[i] + values[j] + i - j.
#
# Example:
# #   [8,1,5,2,6] -> 11   (i=0, j=2: 8+5+0-2 = 11)
#
#   Pattern: RUNNING MAX (state DP)
#   Key: Rewrite as (values[i]+i) + (values[j]-j). Maintain running max of values[i]+i.
#        For each j, update answer with max_so_far + (values[j]-j).

def max_score_sightseeing(values):
    pass

run_tests(max_score_sightseeing, [
    (([8,1,5,2,6],),    11),
    (([1,2],),           2),
    (([1,3,5],),         7),
    (([10,1,1,1,10],),  15),
])
