import sys, os; sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from test_runner import run_tests


def longest_palindrome(s):
    pass


def validate(s):
    r = longest_palindrome(s)
    return r is not None and r == r[::-1] and r in s


run_tests(validate, [
    (("babad",),   True),
    (("cbbd",),    True),
    (("a",),       True),
    (("racecar",), True),
])
