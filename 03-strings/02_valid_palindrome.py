import sys, os; sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from test_runner import run_tests


# Valid Palindrome (LC #125) -- Easy
# Check palindrome considering only alphanumeric chars, case-insensitive.
#
#   Key: Two pointers from both ends, skip non-alphanumeric

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
