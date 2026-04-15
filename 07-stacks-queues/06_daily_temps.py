import sys, os; sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from test_runner import run_tests



# Daily Temperatures (LC #739) -- Medium
# Input:  temperatures: List[int] (daily temperatures)
# Output: List[int] (days until warmer temp, 0 if none)
# Given array of temperatures, for each day, find how many days until warmer.
# If no warmer day ahead, put 0.
#
# Example:
#   [73,74,75,71,69,72,76,73] -> [1,1,4,2,1,1,0,0]
#   Day 0 (73): next warmer is day 1 (74), wait 1 day.
#   Day 2 (75): next warmer is day 6 (76), wait 4 days.
#   Day 6 (76): no warmer day, 0.
#
#   Key: Monotonic decreasing stack of indices.
#        For each temp, pop all smaller temps from stack -- they found their answer.

def daily_temperatures(temperatures):
    pass


run_tests(daily_temperatures, [
    (([73,74,75,71,69,72,76,73],), [1,1,4,2,1,1,0,0]),
    (([30,40,50,60],),              [1,1,1,0]),      # increasing
    (([30,60,90],),                 [1,1,0]),
    (([60,50,40,30],),              [0,0,0,0]),       # decreasing, no warmer
    (([50],),                       [0]),              # single day
    (([50,50,50],),                 [0,0,0]),          # all same
    (([89,62,70,58,47,47,46,76,100,70],), [8,1,5,4,3,2,1,1,0,0]),
])
