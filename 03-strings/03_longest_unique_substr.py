import sys, os; sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from test_runner import run_tests



# Longest Substring Without Repeating Characters (LC #3) -- Medium
# Input:  s: str (may contain any characters)
# Output: int (length of longest substring with all unique characters)
# Find the length of the longest substring with all unique characters.
#
# Example:
#   "abcabcbb" -> 3  ("abc")
#   "bbbbb"    -> 1  ("b")
#   "pwwkew"   -> 3  ("wke")
#   ""         -> 0
#
#   Key: Sliding window with hashset/hashmap.
#        Expand right. When duplicate found, shrink from left until no dup.

def length_of_longest_substring(s):
    pass


run_tests(length_of_longest_substring, [
    (("abcabcbb",), 3),     # "abc"
    (("bbbbb",),    1),     # all same
    (("pwwkew",),   3),     # "wke"
    (("",),         0),     # empty
    (("au",),       2),     # all unique
    (("dvdf",),     3),     # "vdf"
    ((" ",),        1),     # single space
    (("abcdef",),   6),     # all unique, whole string
    (("aab",),      2),     # "ab"
    (("abba",),     2),     # "ab" or "ba"
    (("tmmzuxt",),  5),     # "mzuxt"
])
