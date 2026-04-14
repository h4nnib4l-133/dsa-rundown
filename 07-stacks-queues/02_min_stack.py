import sys, os; sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from test_runner import run_tests


class MinStack:
    def __init__(self):
        pass

    def push(self, val):
        pass

    def pop(self):
        pass

    def top(self):
        pass

    def get_min(self):
        pass


def solve(ops):
    s = MinStack()
    results = []
    for op, val in ops:
        if op == 'push':
            s.push(val)
        elif op == 'pop':
            s.pop()
        elif op == 'top':
            results.append(s.top())
        elif op == 'min':
            results.append(s.get_min())
    return results


run_tests(solve, [
    (([('push',-2),('push',0),('push',-3),('min',0),('pop',0),('top',0),('min',0)],),
     [-3, 0, -2]),
])
