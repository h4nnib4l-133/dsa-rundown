import os, sys
_d = os.path.dirname(os.path.abspath(__file__))
while _d and not os.path.exists(os.path.join(_d, 'test_runner.py')):
    _d = os.path.dirname(_d)
sys.path.insert(0, _d)
from test_runner import run_tests


# Maximum Number of Events You Can Attend (LC #1353) -- Medium
# Input:  events: List[[start, end]]
# Output: int (max events attended, one per day)
# Attend events one day each. Each event [s,e] can be attended on any day s..e.
#
# Example:
# #   [[1,2],[2,3],[3,4]]  -> 3
#   [[1,2],[2,3],[3,4],[1,2]] -> 4
#
#   Greedy insight: For each day, pick the event with earliest end day among available (started but
#        not expired). Min-heap of end days, add events whose start == day.

def max_events(events):
    pass

run_tests(max_events, [
    (([[1,2],[2,3],[3,4]],),           3),
    (([[1,2],[2,3],[3,4],[1,2]],),     4),
    (([[1,4],[4,4],[2,2],[3,4],[1,1]],), 4),
    (([[1,1]],),                        1),
])
