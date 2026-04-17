import os, sys
_d = os.path.dirname(os.path.abspath(__file__))
while _d and not os.path.exists(os.path.join(_d, 'test_runner.py')):
    _d = os.path.dirname(_d)
sys.path.insert(0, _d)
from test_runner import run_tests
from collections import deque


# Implement Stack using Queues (LC #225) -- Easy
# Input:  operations: push(x), pop(), top(), empty()
# Output: LIFO stack behavior using only FIFO queues
# LIFO stack using queues.
#
#   Key: On push, enqueue to q2, then transfer q1 -> q2, swap q1 and q2

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
