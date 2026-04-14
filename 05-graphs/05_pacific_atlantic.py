import sys, os; sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from test_runner import run_tests


def pacific_atlantic(heights):
    """Return list of [r,c] that can flow to both oceans"""
    pass


def solve(heights):
    result = pacific_atlantic(heights)
    return sorted(result)


run_tests(solve, [
    (([[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]],),
     [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]),
    (([[1]],), [[0,0]]),
])
