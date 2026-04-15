import sys, os; sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from test_runner import run_tests



# Trapping Rain Water (LC #42) -- Hard
# Input:  height: List[int] (bar heights >= 0)
# Output: int (total water trapped between bars)
# Given array of bar heights, compute how much rain water is trapped.
#
# Example:
#   [0,1,0,2,1,0,1,3,2,1,2,1] -> 6
#   (water fills between the bars)
#
#   [4,2,0,3,2,5] -> 9
#
#   Key: Water at each position = min(max_left, max_right) - height[i].
#        Two pointers from ends. Track left_max and right_max.
#        Process from the side with smaller max.

def trap(height):
    pass


run_tests(trap, [
    (([0,1,0,2,1,0,1,3,2,1,2,1],),  6),
    (([4,2,0,3,2,5],),               9),
    (([1,0,1],),                      1),     # simple valley
    (([3,0,0,0,3],),                  9),     # flat bottom
    (([0],),                          0),     # single bar
    (([1,2,3],),                      0),     # ascending, no trap
    (([3,2,1],),                      0),     # descending, no trap
    (([5,2,1,2,1,5],),               14),     # deep valley
    (([],),                           0),     # empty
])
