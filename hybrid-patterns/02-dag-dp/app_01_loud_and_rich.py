import os, sys
_d = os.path.dirname(os.path.abspath(__file__))
while _d and not os.path.exists(os.path.join(_d, 'test_runner.py')):
    _d = os.path.dirname(_d)
sys.path.insert(0, _d)
from test_runner import run_tests


# Loud and Rich (LC #851) -- Medium
# Input:  richer: List[[a,b]] (a is richer than b), quiet: List[int]
# Output: List[int] (answer[i] = person with least quiet among all at least as rich as i)
# For each person, find quietest person among those at least as rich.
#
# Example:
# #   richer=[[1,0],[2,1],[3,1],[3,7],[4,3],[5,3],[6,3]]
#   quiet=[3,2,5,4,6,1,7,0]
#   -> [5,5,2,5,4,5,6,7]
#
#   Pattern: DAG + DP
#   Key: Build DAG (richer -> poorer). For each node, answer is min quiet over all ancestors.
#        DFS with memoization.

def loud_and_rich(richer, quiet):
    pass

run_tests(loud_and_rich, [
    (([[1,0],[2,1],[3,1],[3,7],[4,3],[5,3],[6,3]], [3,2,5,4,6,1,7,0]),
     [5,5,2,5,4,5,6,7]),
    (([], [0]),                                [0]),
    (([[0,1]], [1,0]),                         [0,0]),
])
