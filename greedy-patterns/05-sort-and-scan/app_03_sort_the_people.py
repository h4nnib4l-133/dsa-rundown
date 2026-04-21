import os, sys
_d = os.path.dirname(os.path.abspath(__file__))
while _d and not os.path.exists(os.path.join(_d, 'test_runner.py')):
    _d = os.path.dirname(_d)
sys.path.insert(0, _d)
from test_runner import run_tests


# Sort the People (LC #2418) -- Easy
# Input:  names: List[str], heights: List[int] (distinct)
# Output: List[str] (names sorted by descending height)
# Sort names by height descending.
#
# Example:
# #   names=["Mary","John","Emma"], heights=[180,165,170]
#   -> ["Mary","Emma","John"]
#
#   Greedy insight: Zip and sort. Straightforward.

def sort_people(names, heights):
    pass

run_tests(sort_people, [
    ((["Mary","John","Emma"], [180,165,170]),    ["Mary","Emma","John"]),
    ((["Alice","Bob","Bob"], [155,185,150]),     ["Bob","Alice","Bob"]),
    ((["A"], [100]),                             ["A"]),
])
