import sys, os; sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from test_runner import run_tests



# Median of Two Sorted Arrays (LC #4) -- Hard
# Input:  nums1: List[int] (sorted), nums2: List[int] (sorted)
# Output: float (median of merged array)
# Find the median of two sorted arrays. Must be O(log(min(m,n))).
#
# Example:
#   nums1 = [1,3], nums2 = [2]        -> 2.0   (merged: [1,2,3])
#   nums1 = [1,2], nums2 = [3,4]      -> 2.5   (merged: [1,2,3,4], avg of 2,3)
#
#   Key: Binary search on partition of shorter array.
#        Partition so left_count = (m+n+1)//2.
#        Ensure max(left1) <= min(right2) and max(left2) <= min(right1).

def find_median(nums1, nums2):
    pass


run_tests(find_median, [
    (([1,3], [2]),           2.0),     # odd total
    (([1,2], [3,4]),         2.5),     # even total
    (([0,0], [0,0]),         0.0),     # all zeros
    (([], [1]),              1.0),     # one empty
    (([2], []),              2.0),     # other empty
    (([1,2,3], [4,5,6]),     3.5),     # no overlap
    (([1,3], [2,4]),         2.5),     # interleaved
    (([1], [2,3,4,5,6]),     3.5),     # very uneven sizes
    (([3], [1,2]),           2.0),     # small left, needs to go right
])
