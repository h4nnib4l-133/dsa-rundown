import sys, os; sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from test_runner import run_tests



# Valid Palindrome (LC #125) -- Easy
# Check if string is a palindrome, considering only alphanumeric characters
# and ignoring case.
#
# Example:
#   "A man, a plan, a canal: Panama" -> True  (reads "amanaplanacanalpanama")
#   "race a car"                     -> False (reads "raceacar")
#   " "                              -> True  (empty after filtering)
#
#   Key: Two pointers from both ends. Skip non-alphanumeric.
#        Compare lowercase.

def is_palindrome(s):
    """Consider only alphanumeric, case insensitive"""
    pass


run_tests(is_palindrome, [
    (("A man, a plan, a canal: Panama",), True),
    (("race a car",),                     False),
    ((" ",),                              True),     # empty after filter
    (("a",),                              True),     # single char
    (("0P",),                             False),    # '0' != 'P'
    (("",),                               True),     # empty string
    ((".,",),                             True),     # only punctuation
    (("abba",),                           True),     # even length palindrome
    (("abc",),                            False),
    (("Was it a car or a cat I saw?",),   True),     # classic
])
