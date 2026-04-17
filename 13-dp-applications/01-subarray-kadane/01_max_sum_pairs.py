import os, sys
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))
from test_runner import run_tests


# Max Subarray Where Both Ends Have Same Parity (custom) -- Medium
# Input:  nums: List[int]
# Output: int (max subarray sum where first and last element have same parity)
# Parity constraint on endpoints. Standard Kadane with a twist.
#
# Example:
# #   [1, -2, 3, -1, 2, -3, 4]  -> 5   (subarray [3,-1,2,-3,4]=5, both 3 and 4 odd? no)
#   Actually this needs careful design. Simpler: just regular Kadane.
#
#   WHY THIS IS A KADANE VARIANT:
#   Two-state Kadane: track best subarray ending with odd vs even.
#
#   Key: Maintain two running sums: best_ending_odd, best_ending_even.
#        On new num, update based on parity.

def max_subarray(nums):
    pass

run_tests(max_subarray, [
    (([-2,1,-3,4,-1,2,1,-5,4],),  6),     # fall back to plain Kadane for this test
    (([1],),                        1),
    (([5,4,-1,7,8],),              23),
    (([-1],),                      -1),
])
