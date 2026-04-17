import os, sys
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))
from test_runner import run_tests


# Dungeon Game (LC #174) -- Hard
# Input:  dungeon: List[List[int]] (negative=damage, positive=heal)
# Output: int (min initial health to reach bottom-right alive, health must stay >= 1)
# Must keep health >= 1 at ALL times. Only right/down.
#
# Trick: BACKWARDS DP. Forward DP fails because future damage affects needed init.
# dp[i][j] = min health needed ENTERING (i,j) to survive from there.
#
# Example:
# #   [[-2,-3,3],
#    [-5,-10,1],    -> 7
#    [10,30,-5]]
#
#   Key: From bottom-right backwards:
#        need = max(1, min(dp[i+1][j], dp[i][j+1]) - dungeon[i][j]).

def calculate_minimum_hp(dungeon):
    pass

run_tests(calculate_minimum_hp, [
    (([[-2,-3,3],[-5,-10,1],[10,30,-5]],),  7),
    (([[0]],),   1),
    (([[-1]],),  2),
    (([[100]],), 1),
])
