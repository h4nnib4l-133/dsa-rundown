import sys, os; sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from test_runner import run_tests


# Longest Substring Without Repeating Characters (LC #3) -- Medium
# Find length of longest substring with all unique characters.
#
#   Key: Sliding window + hashset. Move left pointer when duplicate found.

def length_of_longest_substring(s):
    pass


run_tests(length_of_longest_substring, [
    (("abcabcbb",), 3),
    (("bbbbb",),    1),
    (("pwwkew",),   3),
    (("",),         0),
    (("au",),       2),
    (("dvdf",),     3),
])
