import sys, os; sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from test_runner import run_tests


# Daily Temperatures (LC #739) -- Medium
# Days until warmer temperature for each day.
#
#   Key: Monotonic decreasing stack of indices. Pop when current temp > stack top.

def daily_temperatures(temperatures):
    pass


run_tests(daily_temperatures, [
    (([73,74,75,71,69,72,76,73],), [1,1,4,2,1,1,0,0]),
    (([30,40,50,60],),              [1,1,1,0]),
    (([30,60,90],),                 [1,1,0]),
])
