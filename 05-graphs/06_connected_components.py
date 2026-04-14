import sys, os; sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from test_runner import run_tests


def count_components(n, edges):
    pass


run_tests(count_components, [
    ((5, [[0,1],[1,2],[3,4]]),        2),
    ((5, [[0,1],[1,2],[2,3],[3,4]]),  1),
    ((4, []),                          4),
    ((1, []),                          1),
])
