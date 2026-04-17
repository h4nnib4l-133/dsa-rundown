import os, sys
_d = os.path.dirname(os.path.abspath(__file__))
while _d and not os.path.exists(os.path.join(_d, 'test_runner.py')):
    _d = os.path.dirname(_d)
sys.path.insert(0, _d)
from test_runner import run_tests


# Stone Game (LC #877) -- Medium
# Input:  piles: List[int] (even count, pick from either end)
# Output: bool (True if first player wins assuming optimal play)
# Two players alternate picking from either end. Max total wins.
#
# Example:
# #   [5,3,4,5] -> True  (first player picks 5, then always wins)
#
#   Pattern: GAME THEORY DP (min-max)
#   Key: dp[i][j] = max score diff (current player - opponent) on piles[i..j].
#        dp[i][j] = max(piles[i] - dp[i+1][j], piles[j] - dp[i][j-1]).
#        Return dp[0][n-1] > 0.

def stone_game(piles):
    pass

run_tests(stone_game, [
    (([5,3,4,5],),      True),
    (([3,7,2,3],),       True),
    (([1,2],),           True),
    (([1,100,1,100],),  True),
])
