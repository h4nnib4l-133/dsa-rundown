import sys, os; sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from test_runner import run_tests


# String to Integer - atoi (LC #8) -- Medium
# Implement atoi with whitespace, sign, overflow handling.
#
#   Key: State machine or step-by-step parsing. Clamp to INT_MIN/INT_MAX.

def my_atoi(s):
    """Clamp to [-2^31, 2^31 - 1]"""
    pass


run_tests(my_atoi, [
    (("42",),               42),
    (("   -42",),          -42),
    (("4193 with words",),  4193),
    (("words and 987",),    0),
    (("-91283472332",),    -2147483648),
])
