import os, sys
_d = os.path.dirname(os.path.abspath(__file__))
while _d and not os.path.exists(os.path.join(_d, 'test_runner.py')):
    _d = os.path.dirname(_d)
sys.path.insert(0, _d)
from test_runner import run_tests


# Second Minimum Time to Reach Destination (LC #2045) -- Hard
# Input:  n: int, edges: List[[u,v]], time: int (per edge), change: int (traffic light period)
# Output: int (second minimum time to reach n from 1)
# Traffic lights toggle every 'change' minutes.
#
# Example:
# #   See LeetCode. Complex with traffic light constraints.
#
#   Pattern: MODIFIED BFS (TRACK TWO BEST DISTANCES)
#   Key: BFS but track BOTH shortest and second-shortest distance to each node.
#        Handle traffic light timing when adding edge weights.

def second_minimum(n, edges, time, change):
    pass

run_tests(second_minimum, [
    ((5, [[1,2],[1,3],[1,4],[3,4],[4,5]], 3, 5),    13),
    ((2, [[1,2]], 3, 2),                              11),
])
