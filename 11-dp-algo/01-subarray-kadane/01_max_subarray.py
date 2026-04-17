import os, sys
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))
from test_runner import run_tests


# Maximum Subarray (LC #53) -- Medium
# Input:  nums: List[int] (may contain negatives)
# Output: int (max sum of any contiguous subarray)
# Classic Kadane's algorithm baseline.
# At each index, decide: extend previous subarray OR start fresh here.
#
# Example:
# #   [-2,1,-3,4,-1,2,1,-5,4] -> 6  (subarray [4,-1,2,1])
#   [1]                      -> 1
#   [5,4,-1,7,8]             -> 23
#
#   Key: curr = max(nums[i], curr + nums[i])
#        best = max(best, curr)

def max_subarray(nums):
    pass

run_tests(max_subarray, [
    (([-2,1,-3,4,-1,2,1,-5,4],),  6),
    (([1],),                         1),
    (([5,4,-1,7,8],),               23),
    (([-1],),                       -1),      # all negative
    (([-3,-1,-2],),                 -1),      # all negative, pick max
    (([1,2,3,4,5],),                15),      # all positive
    (([0,0,0],),                     0),
])
