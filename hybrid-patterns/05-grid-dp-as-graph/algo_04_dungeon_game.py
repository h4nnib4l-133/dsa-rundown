import os, sys
_d = os.path.dirname(os.path.abspath(__file__))
while _d and not os.path.exists(os.path.join(_d, 'test_runner.py')):
    _d = os.path.dirname(_d)
sys.path.insert(0, _d)
from test_runner import run_tests


# Dungeon Game (LC #174) -- Hard
# Input:  dungeon: List[List[int]] (negative=damage, positive=heal)
# Output: int (min initial health to reach bottom-right alive, must stay >= 1)
# Bottom-up DP. Trying forward DP is tricky because of healing potions.
#
# Example:
# #   [[-2,-3,3],[-5,-10,1],[10,30,-5]]  -> 7
#
#   Pattern: BACKWARDS GRID DP
#   Key: dp[i][j] = min health entering (i,j) to survive.
#        From bottom-right backward: dp[i][j] = max(1, min(dp[i+1][j], dp[i][j+1]) - dungeon[i][j]).

def calculate_minimum_hp(dungeon):
    pass

run_tests(calculate_minimum_hp, [
    (([[-2,-3,3],[-5,-10,1],[10,30,-5]],),   7),
    (([[0]],),   1),
    (([[-1]],),  2),
    (([[100]],), 1),
])
