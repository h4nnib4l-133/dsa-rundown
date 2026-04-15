import sys, os; sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from test_runner import run_tests



# Minimum Number of Arrows to Burst Balloons (LC #452) -- Medium
# Input:  points: List[[start, end]] (balloon intervals on x-axis)
# Output: int (minimum arrows to burst all balloons)
# Balloons as intervals [start, end] on x-axis. Arrow shot at x bursts
# all balloons where start <= x <= end.
# Find minimum arrows to burst all balloons.
#
# Example:
#   [[10,16],[2,8],[1,6],[7,12]] -> 2
#   (arrow at x=6 bursts [2,8] and [1,6]; arrow at x=11 bursts [10,16] and [7,12])
#
#   Key: Sort by end. Shoot at each interval's end.
#        Skip all subsequent intervals that include this shot point.

def find_min_arrow_shots(points):
    pass


run_tests(find_min_arrow_shots, [
    (([[10,16],[2,8],[1,6],[7,12]],),   2),
    (([[1,2],[3,4],[5,6],[7,8]],),      4),     # no overlap at all
    (([[1,2],[2,3],[3,4],[4,5]],),      2),     # touching overlaps
    (([[1,10]],),                        1),     # single balloon
    (([[1,2],[1,2],[1,2]],),            1),     # all same
    (([[1,6],[2,8],[7,12],[10,16]],),   2),     # sorted by start
])
