import os, sys
_d = os.path.dirname(os.path.abspath(__file__))
while _d and not os.path.exists(os.path.join(_d, 'test_runner.py')):
    _d = os.path.dirname(_d)
sys.path.insert(0, _d)
from test_runner import run_tests


# Maximum Score After Splitting a String (LC #1422) -- Easy
# Input:  s: str ('0' or '1')
# Output: int (max of (zeros in left) + (ones in right) over all non-empty splits)
# Split into two non-empty parts. Maximize score.
#
# Example:
# #   "011101" -> 5   (split after index 1: '01' and '1101': 1 zero + 3 ones + ... wait)
#
#   Greedy insight: Precompute total ones. Sweep left accumulating zeros, right uses total_ones - ones_so_far_in_left.

def max_score_split(s):
    pass

run_tests(max_score_split, [
    (("011101",),     5),
    (("00111",),      5),
    (("1111",),       3),
    (("0000",),       3),
    (("010",),        2),
])
