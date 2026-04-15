import sys, os; sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
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
