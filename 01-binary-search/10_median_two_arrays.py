import sys, os; sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from test_runner import run_tests


# Median of Two Sorted Arrays (LC #4) -- Hard
# Find median of two sorted arrays in O(log(min(m,n))).
#
#   Key: Binary search on partition of shorter array. Ensure left halves <= right halves.
#   Hint: Partition so that `left1 + left2 = (m+n+1)//2`

def find_median(nums1, nums2):
    pass


run_tests(find_median, [
    (([1,3], [2]),         2.0),
    (([1,2], [3,4]),       2.5),
    (([0,0], [0,0]),       0.0),
    (([], [1]),            1.0),
    (([2], []),            2.0),
])
