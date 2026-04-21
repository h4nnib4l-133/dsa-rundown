import os, sys
_d = os.path.dirname(os.path.abspath(__file__))
while _d and not os.path.exists(os.path.join(_d, 'test_runner.py')):
    _d = os.path.dirname(_d)
sys.path.insert(0, _d)
from test_runner import run_tests


# Queue Reconstruction by Height (LC #406) -- Medium
# Input:  people: List[[h, k]] (h=height, k=# taller/equal before)
# Output: List[[h, k]] (valid queue ordering)
# Each person [h, k] means there are k people ahead with height >= h.
#
# Example:
# #   [[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]
#   -> [[5,0],[7,0],[5,2],[6,1],[4,4],[7,1]]
#
#   Greedy insight: Sort desc by height, asc by k. Then insert each at position k (shorter people slide down).

def reconstruct_queue(people):
    pass

run_tests(reconstruct_queue, [
    (([[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]],),
     [[5,0],[7,0],[5,2],[6,1],[4,4],[7,1]]),
    (([[6,0],[5,0],[4,0],[3,2],[2,2],[1,4]],),
     [[4,0],[5,0],[2,2],[3,2],[1,4],[6,0]]),
    (([[1,0]],),  [[1,0]]),
])
