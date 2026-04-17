import os, sys
_d = os.path.dirname(os.path.abspath(__file__))
while _d and not os.path.exists(os.path.join(_d, 'test_runner.py')):
    _d = os.path.dirname(_d)
sys.path.insert(0, _d)
from test_runner import run_tests


# Matchsticks to Square (LC #473) -- Medium
# Input:  matchsticks: List[int]
# Output: bool (can they form a square using all sticks?)
# Partition sticks into 4 equal-sum groups. Use all sticks.
#
# Example:
# #   [1,1,2,2,2]  -> True  (2+2 on each side? sum=8, side=2. sides: 2, 2, 1+1, 2)
#
#   Pattern: BITMASK DP / BACKTRACKING
#   Key: Bitmask DP: dp[mask] = remainder when sum of mask % side == ?
#        Or backtracking with 4 buckets.

def makesquare(matchsticks):
    pass

run_tests(makesquare, [
    (([1,1,2,2,2],),      True),
    (([3,3,3,3,4],),       False),
    (([5,5,5,5,4,4,4,4,3,3,3,3],),  True),     # two squares possible? sum=48, side=12. 5+4+3=12. yes
    (([1],),               False),
    (([1,1,1,1],),         True),
])
