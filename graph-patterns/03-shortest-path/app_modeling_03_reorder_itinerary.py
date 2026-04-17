import os, sys
_d = os.path.dirname(os.path.abspath(__file__))
while _d and not os.path.exists(os.path.join(_d, 'test_runner.py')):
    _d = os.path.dirname(_d)
sys.path.insert(0, _d)
from test_runner import run_tests


# Reconstruct Itinerary (LC #332) -- Hard
# Input:  tickets: List[[from, to]]
# Output: List[str] (lexicographically smallest Eulerian path starting from 'JFK')
# Use all tickets exactly once, start from 'JFK', find smallest ordering.
#
# Example:
# #   [["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]
#   -> ["JFK","MUC","LHR","SFO","SJC"]
#
#   WHY THIS IS A EULERIAN PATH (Hierholzer's):
#   Airports are nodes, tickets are edges. You must use every edge once = Eulerian path.
#   Non-obvious: the clean solution is Hierholzer's algorithm.
#
#   Key: Build adjacency list with destinations sorted (use heap or sort).
#        DFS: recursively visit smallest destination, appending to result POSTORDER.
#        Reverse at end.

def find_itinerary(tickets):
    pass

run_tests(find_itinerary, [
    (([["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]],),
     ["JFK","MUC","LHR","SFO","SJC"]),
    (([["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]],),
     ["JFK","ATL","JFK","SFO","ATL","SFO"]),
    (([["JFK","A"],["A","B"]],),   ["JFK","A","B"]),
])
