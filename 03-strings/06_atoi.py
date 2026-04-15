import sys, os; sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from test_runner import run_tests



# String to Integer - atoi (LC #8) -- Medium
# Parse a string to 32-bit signed integer. Rules:
#   1. Skip leading whitespace
#   2. Optional '+' or '-' sign
#   3. Read digits until non-digit or end
#   4. Clamp to [-2^31, 2^31-1] on overflow
#   5. Return 0 if no digits found
#
# Example:
#   "42"             -> 42
#   "   -42"         -> -42
#   "4193 with words" -> 4193
#   "words and 987"  -> 0  (first non-space is not digit/sign)
#   "-91283472332"   -> -2147483648  (clamped to INT_MIN)

def my_atoi(s):
    """Clamp to [-2^31, 2^31 - 1]"""
    pass


run_tests(my_atoi, [
    (("42",),                42),
    (("   -42",),           -42),
    (("4193 with words",),   4193),
    (("words and 987",),     0),
    (("-91283472332",),     -2147483648),   # clamp to INT_MIN
    (("91283472332",),       2147483647),   # clamp to INT_MAX
    (("",),                  0),            # empty string
    (("   ",),               0),            # only whitespace
    (("+-12",),              0),            # invalid sign combo
    (("+1",),                1),            # explicit positive
    (("  0000000000012345678",), 12345678), # leading zeros
    (("00000-42a1234",),     0),            # digits then sign = 0? no, 00000 then -
    (("-2147483649",),      -2147483648),   # just below INT_MIN
])
