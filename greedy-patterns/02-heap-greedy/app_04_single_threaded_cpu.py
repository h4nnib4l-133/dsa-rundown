import os, sys
_d = os.path.dirname(os.path.abspath(__file__))
while _d and not os.path.exists(os.path.join(_d, 'test_runner.py')):
    _d = os.path.dirname(_d)
sys.path.insert(0, _d)
from test_runner import run_tests


# Single-Threaded CPU (LC #1834) -- Medium
# Input:  tasks: List[[enqueueTime, processingTime]]
# Output: List[int] (order of task indices processed by CPU)
# CPU picks available task with shortest processing time (ties -> smallest index).
#
# Example:
# #   [[1,2],[2,4],[3,2],[4,1]]  -> [0,2,3,1]
#
#   Greedy insight: Sort tasks by enqueue time. Min-heap of (processing_time, index) for available.
#        Advance time. Pop smallest. If no tasks, jump time to next enqueue.

def get_order(tasks):
    pass

run_tests(get_order, [
    (([[1,2],[2,4],[3,2],[4,1]],),     [0,2,3,1]),
    (([[7,10],[7,12],[7,5],[7,4],[7,2]],), [4,3,2,0,1]),
    (([[1,1]],),                        [0]),
])
