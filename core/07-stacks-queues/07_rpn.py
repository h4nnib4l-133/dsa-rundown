import os, sys
_d = os.path.dirname(os.path.abspath(__file__))
while _d and not os.path.exists(os.path.join(_d, 'test_runner.py')):
    _d = os.path.dirname(_d)
sys.path.insert(0, _d)
from test_runner import run_tests


# Evaluate Reverse Polish Notation (LC #150) -- Medium
# Input:  tokens: List[str] (numbers and operators "+", "-", "*", "/")
# Output: int (result of evaluating the postfix expression)
# Evaluate postfix expression.
#
#   Key: Push numbers. On operator, pop two, compute, push result.

def eval_rpn(tokens):
    pass


run_tests(eval_rpn, [
    ((["2","1","+","3","*"],),           9),
    ((["4","13","5","/","+"],),          6),
    ((["10","6","9","3","+","-11","*","/","*","17","+","5","+"],), 22),
])
