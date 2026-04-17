import os, sys
_d = os.path.dirname(os.path.abspath(__file__))
while _d and not os.path.exists(os.path.join(_d, 'test_runner.py')):
    _d = os.path.dirname(_d)
sys.path.insert(0, _d)
from test_runner import run_tests



# Gas Station (LC #134) -- Medium
# Input:  gas: List[int] (fuel at each station), cost: List[int] (fuel to next)
# Output: int (starting station index, or -1 if impossible)
# Circular route with n gas stations. gas[i] = fuel gained at station i.
# cost[i] = fuel needed to travel from station i to i+1.
# Find starting station index to complete full circle, or -1 if impossible.
# Guaranteed at most one solution exists.
#
# Example:
#   gas  = [1,2,3,4,5]
#   cost = [3,4,5,1,2]
#   Start at station 3: tank = 4-1=3 -> 3+5-2=6 -> 6+1-3=4 -> 4+2-4=2 -> 2+3-5=0 ✓
#   -> 3
#
#   Key: If total gas >= total cost, solution exists.
#        Track running surplus. When it goes negative, restart from next station.

def can_complete_circuit(gas, cost):
    pass


run_tests(can_complete_circuit, [
    (([1,2,3,4,5], [3,4,5,1,2]),   3),
    (([2,3,4], [3,4,3]),           -1),     # total gas < total cost
    (([5,1,2,3,4], [4,4,1,5,1]),    4),
    (([1], [1]),                    0),     # single station, gas == cost
    (([2], [1]),                    0),     # single station, enough gas
    (([1], [2]),                   -1),     # single station, not enough
])
