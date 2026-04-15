import sys, os; sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from test_runner import run_tests


# Largest Rectangle in Histogram (LC #84) -- Hard
# Largest rectangle that can be formed in histogram.
#
#   Key: Monotonic increasing stack. For each bar, find how far it extends left and right.

def largest_rectangle_area(heights):
    pass


run_tests(largest_rectangle_area, [
    (([2,1,5,6,2,3],), 10),
    (([2,4],),           4),
    (([1],),             1),
])
