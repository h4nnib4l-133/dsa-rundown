import os, sys
_d = os.path.dirname(os.path.abspath(__file__))
while _d and not os.path.exists(os.path.join(_d, 'test_runner.py')):
    _d = os.path.dirname(_d)
sys.path.insert(0, _d)
from test_runner import run_tests


# Delete and Earn (LC #740) -- Medium
# Input:  nums: List[int]
# Output: int (max points; picking x deletes all x-1 and x+1)
# Pick nums[i] for points, but all instances of nums[i]-1 and nums[i]+1 get deleted.
#
# Example:
# #   [3,4,2]     -> 6   (pick 3's and 2. But picking 3 deletes 2 and 4.)
#                        Actually pick 2 (+2) and 4 (+4) = 6.
#   [2,2,3,3,3,4] -> 9   (pick all 3's = 9)
#
#   Pattern: HOUSE ROBBER VARIANT
#   Key: Bucket counts: sums[v] = v * count(v).
#        Now House Robber on sums array (can't take adjacent values).

def delete_and_earn(nums):
    pass

run_tests(delete_and_earn, [
    (([3,4,2],),            6),
    (([2,2,3,3,3,4],),      9),
    (([1],),                1),
    (([1,1,1,2,4,5,5,5,6],), 18),
])
