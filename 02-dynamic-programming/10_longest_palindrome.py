import sys, os; sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from test_runner import run_tests


def longest_palindrome(s):
    """Return the longest palindromic substring"""
    pass


# Multiple valid answers possible, so check length and palindrome property
def validate(s):
    result = longest_palindrome(s)
    if result is None:
        return False
    return result == result[::-1]


run_tests(validate, [
    (("babad",), True),
    (("cbbd",),  True),
    (("a",),     True),
    (("racecar",), True),
])
