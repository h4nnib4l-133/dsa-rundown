import os, sys
_d = os.path.dirname(os.path.abspath(__file__))
while _d and not os.path.exists(os.path.join(_d, 'test_runner.py')):
    _d = os.path.dirname(_d)
sys.path.insert(0, _d)
from test_runner import run_tests


# IPO (LC #502) -- Hard
# Input:  k: int, w: int (initial capital), profits: List[int], capital: List[int]
# Output: int (max capital after at most k projects)
# Pick at most k projects. Each needs capital[i] to start, gives profit[i].
# Maximize final capital.
#
# Example:
# #   k=2, w=0, profits=[1,2,3], capital=[0,1,1]  -> 4
#     Start with project 0 (need 0, get 1). w=1. Pick project 2 (need 1, get 3). w=4.
#
#   Greedy insight: Two heaps:
#        - Min-heap on capital (pending projects).
#        - Max-heap on profit (available projects).
#        Loop: move projects with capital <= w to max-heap. Pick max-profit. Update w.

def find_maximized_capital(k, w, profits, capital):
    pass

run_tests(find_maximized_capital, [
    ((2, 0, [1,2,3], [0,1,1]),    4),
    ((3, 0, [1,2,3], [0,1,2]),    6),
    ((1, 0, [1,2,3], [1,1,2]),    0),     # can't start any
    ((1, 2, [1,2,3], [1,1,2]),    5),
])
