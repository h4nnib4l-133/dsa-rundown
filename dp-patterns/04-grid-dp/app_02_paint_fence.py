import os, sys
_d = os.path.dirname(os.path.abspath(__file__))
while _d and not os.path.exists(os.path.join(_d, 'test_runner.py')):
    _d = os.path.dirname(_d)
sys.path.insert(0, _d)
from test_runner import run_tests


# Paint Fence (LC #276) -- Medium
# Input:  n: int (posts), k: int (colors)
# Output: int (ways to paint n posts so no 3 consecutive share color)
# Paint fence posts with k colors. At most 2 consecutive can share a color.
#
# Example:
# #   n=3, k=2 -> 6
#   n=1, k=1 -> 1
#
#   Pattern: STATE DP (same/diff as prev)
#   Key: same[i] = ways where post i matches i-1.
#        diff[i] = ways where post i differs from i-1.
#        same[i] = diff[i-1].
#        diff[i] = (same[i-1] + diff[i-1]) * (k-1).

def num_ways_paint_fence(n, k):
    pass

run_tests(num_ways_paint_fence, [
    ((3, 2),    6),
    ((1, 1),    1),
    ((2, 4),   16),
    ((7, 2),   42),
    ((0, 5),    0),
])
