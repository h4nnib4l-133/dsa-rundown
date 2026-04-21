import os, sys
_d = os.path.dirname(os.path.abspath(__file__))
while _d and not os.path.exists(os.path.join(_d, 'test_runner.py')):
    _d = os.path.dirname(_d)
sys.path.insert(0, _d)
from test_runner import run_tests


# Minimum Taps to Water a Garden (LC #1326) -- Hard
# Input:  n: int (garden length 0..n), ranges: List[int] (tap i waters [i-r, i+r])
# Output: int (min taps to cover [0, n], -1 if impossible)
# Disguised jump game. Each tap covers an interval.
#
# Example:
# #   n=5, ranges=[3,4,1,1,0,0] -> 1   (tap 0 covers [-3,3]; tap 1 covers [-3,5] -> 1 tap)
#
#   Greedy insight: Convert taps to intervals. Sort by start. Greedy: at each position, pick tap
#        reaching farthest. Similar to Jump Game II.

def min_taps(n, ranges):
    pass

run_tests(min_taps, [
    ((5, [3,4,1,1,0,0]),    1),
    ((3, [0,0,0,0]),         -1),
    ((7, [1,2,1,0,2,1,0,1]),  3),
    ((1, [1,0]),              1),
    ((0, [1]),                0),
])
