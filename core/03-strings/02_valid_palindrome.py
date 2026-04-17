import os, sys
_d = os.path.dirname(os.path.abspath(__file__))
while _d and not os.path.exists(os.path.join(_d, 'test_runner.py')):
    _d = os.path.dirname(_d)
sys.path.insert(0, _d)
from test_runner import run_tests



# Valid Palindrome (LC #125) -- Easy
# Input:  s: str (may contain any characters)
# Output: bool (True if palindrome, considering only alphanumeric, case-insensitive)
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
