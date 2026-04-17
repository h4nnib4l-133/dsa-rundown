import os, sys
_d = os.path.dirname(os.path.abspath(__file__))
while _d and not os.path.exists(os.path.join(_d, 'test_runner.py')):
    _d = os.path.dirname(_d)
sys.path.insert(0, _d)
from test_runner import run_tests



# Task Scheduler (LC #621) -- Medium
# Input:  tasks: List[str] (e.g. ["A","A","B"]), n: int (cooldown between same tasks)
# Output: int (minimum time intervals to finish all tasks)
# Given tasks (chars) and cooldown n, find minimum time intervals.
# Same task must have at least n intervals between executions.
# Can insert idle slots if needed.
#
# Example:
#   tasks=["A","A","A","B","B","B"], n=2
#   -> 8: A B _ A B _ A B  (3 A's need gaps of 2)
#
#   tasks=same, n=0 -> 6  (no cooldown, just run all)
#
#   Key: Most frequent task determines frame.
#        Result = max(len(tasks), (max_freq-1) * (n+1) + count_of_max_freq_tasks)

def least_interval(tasks, n):
    pass


run_tests(least_interval, [
    ((["A","A","A","B","B","B"], 2),  8),
    ((["A","A","A","B","B","B"], 0),  6),
    ((["A","A","A","A","A","A","B","C","D","E","F","G"], 2), 16),
    ((["A"], 2),                       1),     # single task
    ((["A","B","C","D","E","F"], 2),   6),     # all different, no idle
    ((["A","A","B","B"], 1),           4),     # ABAB, no idle needed
])
