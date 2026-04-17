import os, sys
_d = os.path.dirname(os.path.abspath(__file__))
while _d and not os.path.exists(os.path.join(_d, 'test_runner.py')):
    _d = os.path.dirname(_d)
sys.path.insert(0, _d)
from test_runner import run_tests


# Minimum Number of Refueling Stops (LC #871) -- Hard
# Input:  target: int, startFuel: int, stations: List[[position, fuel]]
# Output: int (min stops to reach target, -1 if impossible)
# Car can go 1 mile per unit fuel. Optionally refuel at stations.
#
# Example:
# #   target=100, startFuel=10, stations=[[10,60],[20,30],[30,30],[60,40]]
#   -> 2   (refuel at 10, then at 60)
#
#   Pattern: DP OR GREEDY+HEAP
#   Key: DP: dp[i] = farthest distance with i refuels.
#        Iterate stations, for each i from current max down to 0:
#        if dp[i] >= station.pos, dp[i+1] = max(dp[i+1], dp[i] + station.fuel).

def min_refuel_stops(target, start_fuel, stations):
    pass

run_tests(min_refuel_stops, [
    ((100, 10, [[10,60],[20,30],[30,30],[60,40]]),   2),
    ((1, 1, []),                                      0),
    ((100, 1, [[10,100]]),                           -1),
    ((1000, 83, [[25,27],[36,187],[140,186],[378,6],[492,202],[517,89],[579,234],[673,86],[808,53],[954,49]]),  4),
])
