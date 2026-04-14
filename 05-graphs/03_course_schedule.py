import sys, os; sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from test_runner import run_tests


def can_finish(num_courses, prerequisites):
    pass


run_tests(can_finish, [
    ((2, [[1,0]]),         True),
    ((2, [[1,0],[0,1]]),   False),
    ((3, [[1,0],[2,1]]),   True),
    ((1, []),              True),
])
