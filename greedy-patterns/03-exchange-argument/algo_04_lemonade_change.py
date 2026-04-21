import os, sys
_d = os.path.dirname(os.path.abspath(__file__))
while _d and not os.path.exists(os.path.join(_d, 'test_runner.py')):
    _d = os.path.dirname(_d)
sys.path.insert(0, _d)
from test_runner import run_tests


# Lemonade Change (LC #860) -- Easy
# Input:  bills: List[int] (payments of $5, $10, or $20)
# Output: bool (can you give correct change to everyone?)
# Each lemonade costs $5. Customers pay $5/$10/$20. Give exact change.
#
# Example:
# #   [5,5,5,10,20]  -> True
#   [10,10]         -> False
#
#   Greedy insight: Track counts of 5s and 10s. For $20, prefer giving 10+5 over 5+5+5 (save 5s).

def lemonade_change(bills):
    pass

run_tests(lemonade_change, [
    (([5,5,5,10,20],),  True),
    (([10,10],),         False),
    (([5,5,10,10,20],),  False),
    (([5,5,5,10,5,20,5,10,5,20],),  True),
    (([5,5],),           True),
])
