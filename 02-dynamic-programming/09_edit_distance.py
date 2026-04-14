import sys, os; sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from test_runner import run_tests


def min_distance(word1, word2):
    pass


run_tests(min_distance, [
    (("horse", "ros"),        3),
    (("intention", "execution"), 5),
    (("", "abc"),             3),
    (("abc", ""),             3),
    (("abc", "abc"),          0),
])
