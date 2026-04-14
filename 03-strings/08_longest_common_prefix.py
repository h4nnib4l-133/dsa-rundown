import sys, os; sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from test_runner import run_tests


def longest_common_prefix(strs):
    pass


run_tests(longest_common_prefix, [
    ((["flower","flow","flight"],), "fl"),
    ((["dog","racecar","car"],),    ""),
    ((["a"],),                      "a"),
    ((["","b"],),                   ""),
])
