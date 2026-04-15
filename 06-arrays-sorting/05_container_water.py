import sys, os; sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from test_runner import run_tests



# Container With Most Water (LC #11) -- Medium
# Input:  height: List[int] (bar heights, len >= 2)
# Output: int (max water area between two bars)
# Array of heights. Find two lines that form container holding most water.
# Width = distance between lines. Height = shorter line.
#
# Example:
#   [1,8,6,2,5,4,8,3,7] -> 49  (lines at index 1,8: min(8,7)*7=49)
#   [1,1] -> 1
#
#   Key: Two pointers from both ends. Area = min(h[l],h[r]) * (r-l).
#        Move the shorter pointer inward (it limits the area).

def max_area(height):
    pass


run_tests(max_area, [
    (([1,8,6,2,5,4,8,3,7],),  49),
    (([1,1],),                  1),
    (([4,3,2,1,4],),           16),    # 4*4
    (([1,2,1],),                2),    # min(1,1)*2
    (([2,3,4,5,18,17,6],),    17),     # 17*1? no. check: min(2,6)*5=10, min(3,17)*4=12...
    (([1,8,6,2,5,4,8,3,7],),  49),
])
