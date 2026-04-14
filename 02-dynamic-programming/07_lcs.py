import sys, os; sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from test_runner import run_tests


def longest_common_subseq(text1, text2):
    pass


run_tests(longest_common_subseq, [
    (("abcde", "ace"),   3),
    (("abc", "abc"),     3),
    (("abc", "def"),     0),
    (("", "abc"),        0),
    (("bsbininm", "jmjkbkjkv"), 1),
])
