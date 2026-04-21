import os, sys
_d = os.path.dirname(os.path.abspath(__file__))
while _d and not os.path.exists(os.path.join(_d, 'test_runner.py')):
    _d = os.path.dirname(_d)
sys.path.insert(0, _d)
from test_runner import run_tests


# Assign Cookies (LC #455) -- Easy
# Input:  g: List[int] (greed factors), s: List[int] (cookie sizes)
# Output: int (max content children; a child is content if cookie >= greed)
# Give each child at most one cookie. Child satisfied if cookie >= greed.
#
# Example:
# #   g=[1,2,3], s=[1,1]  -> 1
#
#   Greedy insight: Sort both. Two pointers: for each cookie, give to smallest greed that fits.

def find_content_children(g, s):
    pass

run_tests(find_content_children, [
    (([1,2,3], [1,1]),    1),
    (([1,2], [1,2,3]),    2),
    (([10,9,8,7], [5,6,7,8]),  2),
    (([], [1,2,3]),       0),
])
