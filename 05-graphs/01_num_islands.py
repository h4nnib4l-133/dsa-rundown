import sys, os; sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from test_runner import run_tests


def num_islands(grid):
    pass


run_tests(num_islands, [
    (([["1","1","1","1","0"],
       ["1","1","0","1","0"],
       ["1","1","0","0","0"],
       ["0","0","0","0","0"]],), 1),
    (([["1","1","0","0","0"],
       ["1","1","0","0","0"],
       ["0","0","1","0","0"],
       ["0","0","0","1","1"]],), 3),
])
