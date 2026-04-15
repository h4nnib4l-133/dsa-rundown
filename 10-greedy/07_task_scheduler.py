import sys, os; sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from test_runner import run_tests


# Task Scheduler (LC #621) -- Medium
# Min intervals to execute all tasks with cooldown n between same tasks.
#
#   Key: Most frequent task determines frame. Answer = `max(len(tasks), (max_freq - 1) * (n + 1) + count_of_max_freq)`

def least_interval(tasks, n):
    pass


run_tests(least_interval, [
    ((["A","A","A","B","B","B"], 2), 8),
    ((["A","A","A","B","B","B"], 0), 6),
    ((["A","A","A","A","A","A","B","C","D","E","F","G"], 2), 16),
])
