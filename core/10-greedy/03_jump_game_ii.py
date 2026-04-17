import os, sys
_d = os.path.dirname(os.path.abspath(__file__))
while _d and not os.path.exists(os.path.join(_d, 'test_runner.py')):
    _d = os.path.dirname(_d)
sys.path.insert(0, _d)
from test_runner import run_tests


# Jump Game II (LC #45) -- Medium
# Input:  nums: List[int] (max jump length, guaranteed reachable)
# Output: int (minimum number of jumps to reach last index)
# Minimum jumps to reach last index.
#
#   Key: BFS-style greedy. Track current end and farthest. When i reaches current end, jump.

def jump(nums):
    pass


run_tests(jump, [
    (([2,3,1,1,4],), 2),
    (([2,3,0,1,4],), 2),
    (([1],),         0),
])
