import sys, os; sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from test_runner import run_tests


# Trapping Rain Water (LC #42) -- Hard
# How much water trapped between bars?
#
#   Key: Two pointers from ends. Water at position = `min(left_max, right_max) - height`
#   Alt: Stack-based approach

def trap(height):
    pass


run_tests(trap, [
    (([0,1,0,2,1,0,1,3,2,1,2,1],), 6),
    (([4,2,0,3,2,5],),              9),
    (([1,0,1],),                     1),
])
