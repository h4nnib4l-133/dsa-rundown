import sys, os; sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from test_runner import run_tests


def find_min_arrow_shots(points):
    pass


run_tests(find_min_arrow_shots, [
    (([[10,16],[2,8],[1,6],[7,12]],), 2),
    (([[1,2],[3,4],[5,6],[7,8]],),    4),
    (([[1,2],[2,3],[3,4],[4,5]],),    2),
])
