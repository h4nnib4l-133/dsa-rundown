import sys, os; sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from test_runner import run_tests


# Implement Queue using Stacks (LC #232) -- Easy
# Input:  operations: push(x), pop(), peek(), empty()
# Output: FIFO queue behavior using only LIFO stacks
# FIFO queue using two LIFO stacks.
#
#   Key: Push to stack1. For pop, transfer stack1 -> stack2 if stack2 empty.

class MyQueue:
    def __init__(self):
        pass

    def push(self, x):
        pass

    def pop(self):
        pass

    def peek(self):
        pass

    def empty(self):
        pass


def solve(ops):
    q = MyQueue()
    results = []
    for op, val in ops:
        if op == 'push': q.push(val)
        elif op == 'pop': results.append(q.pop())
        elif op == 'peek': results.append(q.peek())
        elif op == 'empty': results.append(q.empty())
    return results


run_tests(solve, [
    (([('push',1),('push',2),('peek',0),('pop',0),('empty',0)],),
     [1, 1, False]),
])
