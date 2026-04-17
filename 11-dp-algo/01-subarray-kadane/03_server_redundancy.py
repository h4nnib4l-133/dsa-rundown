import os, sys
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))
from test_runner import run_tests


# Maximum Server Redundancy (custom) -- Medium
# Input:  s: str (binary string of '0' and '1')
# Output: int (number of distinct redundancy values reachable)
# Binary string. At most one [l,r] toggle operation.
# Count distinct values of sum('1's) after any (or no) operation.
#
# Pattern: TRANSFORMATION + KADANE
# Map 0->+1, 1->-1. Then toggling range [l,r] changes the '1' count by
# sum of transformed subarray. Reachable counts form a contiguous integer
# range because adjacent subarrays differ by exactly +/-1.
#
# Example:
# #   "0110" -> 4   (reachable: {0,1,2,3})
#   "1111" -> 5   (reachable: {0,1,2,3,4}, any flip decreases)
#   "0" -> 2   ({0,1})
#
#   Key: original_ones + [min_sum, max_sum] covers all reachable counts.
#        Also include original_ones (do-nothing) for edge case.
#        Answer = (max_reachable - min_reachable + 1).

def max_redundancy(s):
    pass

run_tests(max_redundancy, [
    (("0110",),  4),
    (("0011",),  4),
    (("1111",),  5),
    (("0",),     2),
    (("1",),     2),
    (("00",),    3),     # {0,1,2}
    (("01",),    3),
])
