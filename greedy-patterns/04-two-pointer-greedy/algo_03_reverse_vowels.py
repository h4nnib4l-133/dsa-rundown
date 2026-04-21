import os, sys
_d = os.path.dirname(os.path.abspath(__file__))
while _d and not os.path.exists(os.path.join(_d, 'test_runner.py')):
    _d = os.path.dirname(_d)
sys.path.insert(0, _d)
from test_runner import run_tests


# Reverse Vowels of a String (LC #345) -- Easy
# Input:  s: str
# Output: str (vowels reversed, consonants in place)
# Reverse only the vowels. Both lowercase and uppercase count.
#
# Example:
# #   "hello" -> "holle"
#   leetcode -> leotcede
#
#   Greedy insight: Two pointers. Skip non-vowels. Swap when both point to vowels.

def reverse_vowels(s):
    pass

run_tests(reverse_vowels, [
    (("hello",),    "holle"),
    (("leetcode",), "leotcede"),
    (("a",),        "a"),
    (("",),         ""),
    (("aeiou",),    "uoiea"),
])
