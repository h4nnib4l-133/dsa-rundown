import sys, os; sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from test_runner import run_tests


# ---- WRITE YOUR SOLUTION HERE ----

def search(nums, target):
    pass

# ---- END SOLUTION ----


run_tests(search, [
    (([1, 2, 3, 4, 5], 3),       2),
    (([1, 2, 3, 4, 5], 1),       0),
    (([1, 2, 3, 4, 5], 5),       4),
    (([1, 2, 3, 4, 5], 6),      -1),
    (([-1, 0, 3, 5, 9, 12], 9),  4),
    (([5], 5),                    0),
    (([5], 3),                   -1),
])
