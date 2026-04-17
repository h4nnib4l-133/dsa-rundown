import os, sys
_d = os.path.dirname(os.path.abspath(__file__))
while _d and not os.path.exists(os.path.join(_d, 'test_runner.py')):
    _d = os.path.dirname(_d)
sys.path.insert(0, _d)
from test_runner import run_tests


# Can I Win (LC #464) -- Medium
# Input:  max_choosable: int, desired_total: int
# Output: bool (True if first player can always win)
# Two players pick from {1..max_choosable} without replacement.
# First to make running total >= desired wins.
#
# Example:
# #   max=10, desired=11  -> False (any choice leads to opponent winning)
#   max=10, desired=0   -> True
#
#   Pattern: BITMASK GAME DP
#   Key: State = bitmask of used numbers. Memoize 'can current player win from this state'.
#        Player wins if any available choice makes opponent lose.

def can_i_win(max_choosable, desired_total):
    pass

run_tests(can_i_win, [
    ((10, 11),    False),
    ((10, 0),     True),
    ((10, 1),     True),
    ((5, 50),     False),     # impossible
    ((4, 6),      True),
])
