import os, sys
_d = os.path.dirname(os.path.abspath(__file__))
while _d and not os.path.exists(os.path.join(_d, 'test_runner.py')):
    _d = os.path.dirname(_d)
sys.path.insert(0, _d)
from test_runner import run_tests


# Hand of Straights (LC #846) -- Medium
# Input:  hand: List[int], groupSize: int
# Output: bool (can cards be grouped into consecutive runs of groupSize?)
# Arrange cards into groups each of consecutive integers of size groupSize.
#
# Example:
# #   [1,2,3,6,2,3,4,7,8], 3  -> True   ([1,2,3],[2,3,4],[6,7,8])
#
#   Greedy insight: Sort or use min-heap. Greedy: for each smallest remaining card, try to form a run.

def is_n_straight_hand(hand, group_size):
    pass

run_tests(is_n_straight_hand, [
    (([1,2,3,6,2,3,4,7,8], 3),  True),
    (([1,2,3,4,5], 4),          False),
    (([1,1,2,2,3,3], 3),        True),
    (([1,2,3,4,5,6], 2),        True),
    (([1], 1),                  True),
])
