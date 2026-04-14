import sys, os; sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from test_runner import run_tests
from collections import deque


class MyStack:
    def __init__(self):
        pass

    def push(self, x):
        pass

    def pop(self):
        pass

    def top(self):
        pass

    def empty(self):
        pass


def solve(ops):
    s = MyStack()
    results = []
    for op, val in ops:
        if op == 'push': s.push(val)
        elif op == 'pop': results.append(s.pop())
        elif op == 'top': results.append(s.top())
        elif op == 'empty': results.append(s.empty())
    return results


run_tests(solve, [
    (([('push',1),('push',2),('top',0),('pop',0),('empty',0)],),
     [2, 2, False]),
])
