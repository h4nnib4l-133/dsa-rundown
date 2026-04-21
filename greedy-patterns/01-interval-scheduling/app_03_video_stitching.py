import os, sys
_d = os.path.dirname(os.path.abspath(__file__))
while _d and not os.path.exists(os.path.join(_d, 'test_runner.py')):
    _d = os.path.dirname(_d)
sys.path.insert(0, _d)
from test_runner import run_tests


# Video Stitching (LC #1024) -- Medium
# Input:  clips: List[[start, end]], time: int
# Output: int (min clips to cover [0, time], -1 if impossible)
# Same as Min Taps but more explicit.
#
# Example:
# #   clips=[[0,2],[4,6],[8,10],[1,9],[1,5],[5,9]], time=10
#   -> 3   ([0,2],[1,9],[8,10] or similar)
#
#   Greedy insight: Sort by start. Greedy: from current coverage end, pick clip starting within
#        that range and reaching farthest.

def video_stitching(clips, time):
    pass

run_tests(video_stitching, [
    (([[0,2],[4,6],[8,10],[1,9],[1,5],[5,9]], 10),  3),
    (([[0,1],[1,2]], 5),                              -1),
    (([[0,1],[6,8],[0,2],[5,6],[0,4],[0,3],[6,7],[1,3],[4,7],[1,4],[2,5],[2,6],[3,4],[4,5],[5,7],[6,9]], 9), 3),
    (([[0,5],[1,5]], 5),   1),
])
