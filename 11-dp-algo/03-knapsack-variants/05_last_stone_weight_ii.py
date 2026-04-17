import os, sys
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))
from test_runner import run_tests


# Last Stone Weight II (LC #1049) -- Medium
# Input:  stones: List[int] (positive)
# Output: int (min possible weight of final stone)
# Smash pairs of stones; result = |x-y|. Find min final weight.
#
# Trick: assign + or - to each stone (like Target Sum). Minimize |sum|.
# Equivalently: find subset sum closest to total/2.
#
# Example:
# #   [2,7,4,1,8,1] -> 1   (optimal partition)
#   [31,26,33,21,40] -> 5
#
#   Key: Find max subset sum <= total/2. Answer = total - 2*subset_sum.
#        Classic knapsack with target = total // 2.

def last_stone_weight_ii(stones):
    pass

run_tests(last_stone_weight_ii, [
    (([2,7,4,1,8,1],),  1),
    (([31,26,33,21,40],), 5),
    (([1,2],),          1),
    (([1],),            1),
    (([5,5],),          0),
])
