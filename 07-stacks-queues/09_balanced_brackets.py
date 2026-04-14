import sys, os; sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from test_runner import run_tests


def is_balanced(s):
    pass


run_tests(is_balanced, [
    (("{[()]}",),  True),
    (("{[(])}",),  False),
    (("{{[[(())]]}}", ), True),
    (("",),        True),
    (("{",),       False),
])
