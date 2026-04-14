import sys, os; sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from test_runner import run_tests


def generate_parenthesis(n):
    pass


def solve(n):
    return sorted(generate_parenthesis(n))


run_tests(solve, [
    ((3,), ["((()))","(()())","(())()","()(())","()()()"]),
    ((1,), ["()"]),
])
