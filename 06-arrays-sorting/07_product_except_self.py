import sys, os; sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from test_runner import run_tests



# Product of Array Except Self (LC #238) -- Medium
# Input:  nums: List[int] (len >= 2, product fits in 32-bit int)
# Output: List[int] (output[i] = product of all nums except nums[i])
# Return array where output[i] = product of all nums except nums[i].
# Must be O(n) without using division.
#
# Example:
#   [1,2,3,4] -> [24,12,8,6]
#   (24=2*3*4, 12=1*3*4, 8=1*2*4, 6=1*2*3)
#
#   Key: Two passes.
#        Pass 1 (left to right): prefix[i] = product of all elements before i.
#        Pass 2 (right to left): multiply by suffix product.

def product_except_self(nums):
    pass


run_tests(product_except_self, [
    (([1,2,3,4],),       [24,12,8,6]),
    (([-1,1,0,-3,3],),   [0,0,9,0,0]),      # zero in array
    (([2,3],),            [3,2]),             # two elements
    (([0,0],),            [0,0]),             # two zeros
    (([1,1,1,1],),        [1,1,1,1]),         # all ones
    (([-1,-2,-3],),       [6,-3,-2]),         # negatives: (-2)*(-3)=6, etc. wait: [-2*-3, -1*-3, -1*-2] = [6,3,2]
])
