import sys, os; sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from test_runner import run_tests


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
