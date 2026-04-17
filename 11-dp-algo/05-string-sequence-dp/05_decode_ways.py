import os, sys
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))
from test_runner import run_tests


# Decode Ways (LC #91) -- Medium
# Input:  s: str (digits only)
# Output: int (number of ways to decode: 1->'A', ..., 26->'Z')
# Each digit maps to a letter. Two-digit numbers 10-26 also map to letters.
# Count distinct decodings.
#
# Example:
# #   "12"   -> 2   ("AB" = 1,2 or "L" = 12)
#   "226"  -> 3   ("BZ", "VF", "BBF")
#   "06"   -> 0   (invalid, no leading zero)
#
#   Key: dp[i] = dp[i-1] if s[i-1] != '0'
#              + dp[i-2] if 10 <= int(s[i-2:i]) <= 26.

def num_decodings(s):
    pass

run_tests(num_decodings, [
    (("12",),    2),
    (("226",),   3),
    (("06",),    0),
    (("10",),    1),
    (("27",),    1),     # only "BG"
    (("2101",),  1),
    (("0",),     0),
])
