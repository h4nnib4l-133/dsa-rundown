import os, sys
_d = os.path.dirname(os.path.abspath(__file__))
while _d and not os.path.exists(os.path.join(_d, 'test_runner.py')):
    _d = os.path.dirname(_d)
sys.path.insert(0, _d)
from test_runner import run_tests


# Longest Harmonious Subsequence (LC #594) -- Easy
# Input:  nums: List[int]
# Output: int (longest subsequence where max-min == 1)
# Harmonious subseq: max - min = exactly 1. Return max length.
#
# Example:
# #   [1,3,2,2,5,2,3,7]  -> 5   (subseq [3,2,2,2,3])
#
#   Greedy insight: Count frequencies. For each value v, if v+1 exists, candidate = count[v] + count[v+1].

def find_lhs(nums):
    pass

run_tests(find_lhs, [
    (([1,3,2,2,5,2,3,7],),  5),
    (([1,2,3,4],),           2),
    (([1,1,1,1],),           0),
    (([1,2],),               2),
    (([],),                  0),
])
