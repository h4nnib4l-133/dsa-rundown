import sys, os; sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from test_runner import run_tests


def search_matrix(matrix, target):
    """Return True if target is in matrix"""
    pass


run_tests(search_matrix, [
    (([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 3),   True),
    (([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 13),  False),
    (([[1]], 1),   True),
    (([[1]], 2),   False),
    (([[1,3]], 3), True),
])
