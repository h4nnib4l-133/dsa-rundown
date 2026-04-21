import os, sys
_d = os.path.dirname(os.path.abspath(__file__))
while _d and not os.path.exists(os.path.join(_d, 'test_runner.py')):
    _d = os.path.dirname(_d)
sys.path.insert(0, _d)
from test_runner import run_tests


# Interval List Intersections (LC #986) -- Medium
# Input:  first: List[[a,b]], second: List[[c,d]] (both sorted, disjoint within each)
# Output: List[[start, end]] (intersection intervals)
# Find all overlapping intervals between two sorted lists.
#
# Example:
# #   first=[[0,2],[5,10],[13,23],[24,25]]
#   second=[[1,5],[8,12],[15,24],[25,26]]
#   -> [[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]
#
#   Greedy insight: Two pointers. Intersection = [max(start1,start2), min(end1,end2)] if valid.
#        Advance pointer whose interval ends first.

def interval_intersection(first, second):
    pass

run_tests(interval_intersection, [
    (([[0,2],[5,10],[13,23],[24,25]], [[1,5],[8,12],[15,24],[25,26]]),
     [[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]),
    (([], [[1,5]]),   []),
    (([[1,3]], [[5,9]]), []),
    (([[1,7]], [[3,10]]), [[3,7]]),
])
