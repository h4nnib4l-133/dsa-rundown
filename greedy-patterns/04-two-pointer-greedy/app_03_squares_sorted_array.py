import os, sys
_d = os.path.dirname(os.path.abspath(__file__))
while _d and not os.path.exists(os.path.join(_d, 'test_runner.py')):
    _d = os.path.dirname(_d)
sys.path.insert(0, _d)
from test_runner import run_tests


# Squares of a Sorted Array (LC #977) -- Easy
# Input:  nums: List[int] (sorted, may contain negatives)
# Output: List[int] (squares sorted ascending)
# Return squares of nums sorted.
#
# Example:
# #   [-4,-1,0,3,10] -> [0,1,9,16,100]
#
#   Greedy insight: Two pointers from both ends. Compare absolute values. Place larger square at end of result.

def sorted_squares(nums):
    pass

run_tests(sorted_squares, [
    (([-4,-1,0,3,10],),   [0,1,9,16,100]),
    (([-7,-3,2,3,11],),   [4,9,9,49,121]),
    (([0],),              [0]),
    (([-5,-3,-2,-1],),    [1,4,9,25]),
    (([1,2,3],),          [1,4,9]),
])
