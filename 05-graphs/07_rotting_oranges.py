import sys, os; sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from test_runner import run_tests


def oranges_rotting(grid):
    """Return minutes until all rot, or -1 if impossible"""
    pass


run_tests(oranges_rotting, [
    (([[2,1,1],[1,1,0],[0,1,1]],),  4),
    (([[2,1,1],[0,1,1],[1,0,1]],), -1),
    (([[0,2]],),                    0),
])
