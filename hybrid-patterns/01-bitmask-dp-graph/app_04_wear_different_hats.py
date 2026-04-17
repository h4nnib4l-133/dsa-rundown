import os, sys
_d = os.path.dirname(os.path.abspath(__file__))
while _d and not os.path.exists(os.path.join(_d, 'test_runner.py')):
    _d = os.path.dirname(_d)
sys.path.insert(0, _d)
from test_runner import run_tests


# Number of Ways to Wear Different Hats (LC #1434) -- Hard
# Input:  hats: List[List[int]] (hats[i] = list of hat IDs person i likes)
# Output: int (ways to assign hats to people so everyone wears different, mod 10^9+7)
# n people, 40 hats. Each person wears exactly one hat they like. All different.
#
# Example:
# #   [[3,4],[4,5],[5]]  -> 1   (only one assignment works)
#
#   Pattern: BITMASK DP (over people, iterate hats)
#   Key: Key insight: iterate over HATS (40) not PEOPLE (unbounded hat count would be worse).
#        State: (hat_idx, people_mask). dp[h][mask] = ways using hats 1..h covering people in mask.

def number_ways(hats):
    pass

run_tests(number_ways, [
    (([[3,4],[4,5],[5]],),             1),
    (([[3,5,1],[3,5]],),               4),
    (([[1,2,3,4],[1,2,3,4],[1,2,3,4],[1,2,3,4]],),  24),
])
