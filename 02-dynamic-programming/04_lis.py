import sys, os; sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from test_runner import run_tests



# Longest Increasing Subsequence (LC #300) -- Medium
# Input:  nums: List[int] (unsorted integers)
# Output: int (length of longest strictly increasing subsequence)
# Find the length of the longest STRICTLY increasing subsequence.
# Subsequence = not necessarily contiguous.
#
# Example:
#   [10,9,2,5,3,7,101,18] -> 4  (one LIS: [2,3,7,101])
#   [0,1,0,3,2,3]         -> 4  ([0,1,2,3])
#   [7,7,7,7,7]           -> 1  (all same, no increase)
#
#   Key (O(n^2)): dp[i] = LIS ending at i. dp[i] = max(dp[j]+1) for j<i where nums[j]<nums[i].
#   Key (O(n log n)): Maintain tails array, binary search to find insertion point.

def length_of_lis(nums):
    pass


run_tests(length_of_lis, [
    (([10,9,2,5,3,7,101,18],),  4),    # classic example
    (([0,1,0,3,2,3],),          4),    # [0,1,2,3]
    (([7,7,7,7,7],),            1),    # all same (strictly increasing!)
    (([1],),                    1),    # single element
    (([1,2,3,4,5],),            5),    # already sorted
    (([5,4,3,2,1],),            1),    # reverse sorted
    (([3,5,6,2,5,4,19,5,6,7,12],), 6), # longer example
    (([1,3,6,7,9,4,10,5,6],),  6),    # multiple possible LIS
])
