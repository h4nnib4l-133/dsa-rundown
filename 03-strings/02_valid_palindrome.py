import sys, os; sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from test_runner import run_tests


def is_palindrome(s):
    """Consider only alphanumeric, case insensitive"""
    pass


run_tests(is_palindrome, [
    (("A man, a plan, a canal: Panama",), True),
    (("race a car",),                     False),
    ((" ",),                              True),
    (("a",),                              True),
    (("0P",),                             False),
])
