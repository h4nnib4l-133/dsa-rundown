import sys, os; sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from test_runner import run_tests


# Container With Most Water (LC #11) -- Medium
# Find two lines forming container with most water.
#
#   Key: Two pointers from both ends. Move the shorter line inward.

def max_area(height):
    pass


run_tests(max_area, [
    (([1,8,6,2,5,4,8,3,7],), 49),
    (([1,1],),                 1),
    (([4,3,2,1,4],),           16),
])
