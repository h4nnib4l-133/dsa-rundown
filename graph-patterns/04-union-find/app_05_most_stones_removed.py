import os, sys
_d = os.path.dirname(os.path.abspath(__file__))
while _d and not os.path.exists(os.path.join(_d, 'test_runner.py')):
    _d = os.path.dirname(_d)
sys.path.insert(0, _d)
from test_runner import run_tests


# Most Stones Removed with Same Row or Column (LC #947) -- Medium
# Input:  stones: List[[x,y]]
# Output: int (max stones removable)
# A stone can be removed if it shares a row or column with another stone.
# Find max removable.
#
# Example:
# #   stones=[[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]]  -> 5
#     (all 6 stones form one connected group; keep 1 per group)
#
#   WHY THIS IS A UNION-FIND (row/col identity):
#   Stones sharing a row or column form a connected group. You can remove all
#   but one per group. Answer = total_stones - num_groups.
#   Trick: union row_id with col_id (encode them as separate IDs).
#
#   Key: Union-Find where each row and each col is a node.
#        For each stone, union its row with its col.
#        Count unique roots among row/col nodes that appeared. Answer = len(stones) - roots.

def remove_stones(stones):
    pass

run_tests(remove_stones, [
    (([[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]],),     5),
    (([[0,0],[0,2],[1,1],[2,0],[2,2]],),            3),
    (([[0,0]],),                                    0),
    (([[0,0],[1,1]],),                              0),     # disjoint
])
