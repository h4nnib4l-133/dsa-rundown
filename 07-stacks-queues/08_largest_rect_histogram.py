import sys, os; sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from test_runner import run_tests



# Largest Rectangle in Histogram (LC #84) -- Hard
# Input:  heights: List[int] (bar heights >= 0)
# Output: int (area of largest rectangle formed by contiguous bars)
# Given array of bar heights, find area of largest rectangle.
# Rectangle must be formed by contiguous bars.
#
# Example:
#   [2,1,5,6,2,3] -> 10  (bars at index 2,3 of height 5: 5*2=10)
#   [2,4] -> 4  (bar of height 4, width 1. Or both bars min height 2: 2*2=4)
#
#   Key: Monotonic increasing stack. For each bar:
#        Pop taller bars -- for each, calculate width it can extend.
#        Width = current_index - stack_top_index - 1.

def largest_rectangle_area(heights):
    pass


run_tests(largest_rectangle_area, [
    (([2,1,5,6,2,3],),  10),
    (([2,4],),            4),
    (([1],),              1),     # single bar
    (([1,1],),            2),     # two equal bars
    (([5,4,3,2,1],),      9),     # decreasing: 3*3=9
    (([1,2,3,4,5],),      9),     # increasing: 3*3=9
    (([3,3,3,3],),        12),    # all same: 3*4=12
    (([0],),              0),     # zero height
])
