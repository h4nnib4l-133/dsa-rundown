import os, sys
_d = os.path.dirname(os.path.abspath(__file__))
while _d and not os.path.exists(os.path.join(_d, 'test_runner.py')):
    _d = os.path.dirname(_d)
sys.path.insert(0, _d)
from test_runner import run_tests


# Satisfiability of Equality Equations (LC #990) -- Medium
# Input:  equations: List[str] (each is 'x==y' or 'x!=y')
# Output: bool (True if all can be satisfied)
# Process == first (union vars). Then check each != (must NOT be in same set).
#
# Example:
# #   ["a==b","b!=a"]    -> False
#   ["b==a","a==b"]    -> True
#   ["a==b","b==c","a==c"]  -> True
#
#   Key: Two passes. First union all == pairs.
#        Then for each !=, check they have different roots.

def equations_possible(equations):
    pass

run_tests(equations_possible, [
    ((["a==b","b!=a"],),              False),
    ((["b==a","a==b"],),              True),
    ((["a==b","b==c","a==c"],),       True),
    ((["a==b","b!=c","c==a"],),       False),
    ((["c==c","b==d","x!=z"],),       True),
])
