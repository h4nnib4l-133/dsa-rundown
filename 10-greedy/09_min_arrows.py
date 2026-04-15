import sys, os; sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from test_runner import run_tests


# Minimum Arrows to Burst Balloons (LC #452) -- Medium
# Min arrows to burst all balloons (intervals on x-axis).
#
#   Key: Sort by end. Shoot at each interval's end. Skip all intervals that include this point.

def find_min_arrow_shots(points):
    pass


run_tests(find_min_arrow_shots, [
    (([[10,16],[2,8],[1,6],[7,12]],), 2),
    (([[1,2],[3,4],[5,6],[7,8]],),    4),
    (([[1,2],[2,3],[3,4],[4,5]],),    2),
])
