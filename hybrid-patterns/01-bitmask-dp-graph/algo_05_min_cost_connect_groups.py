import os, sys
_d = os.path.dirname(os.path.abspath(__file__))
while _d and not os.path.exists(os.path.join(_d, 'test_runner.py')):
    _d = os.path.dirname(_d)
sys.path.insert(0, _d)
from test_runner import run_tests


# Minimum Cost to Connect Two Groups (LC #1595) -- Hard
# Input:  cost: List[List[int]] (cost[i][j] = cost to connect group1[i] with group2[j])
# Output: int (min cost so every point in both groups has >=1 connection)
# Every point in group1 AND group2 must have at least one connection.
#
# Example:
# #   cost=[[15,96],[36,2]]  -> 17
#
#   Pattern: BITMASK DP (over group2)
#   Key: State: (i in group1, mask of group2 covered). For each i, either:
#        - Connect i to some j (costs[i][j], sets bit j).
#        - Handle remaining group2 indices by connecting them to their cheapest group1 partner.

def connect_two_groups(cost):
    pass

run_tests(connect_two_groups, [
    (([[15,96],[36,2]],),            17),
    (([[1,3,5],[4,1,1],[1,5,3]],),    4),
    (([[2,5,1],[3,4,7],[8,1,2],[6,2,4],[3,8,8]],),  10),
])
