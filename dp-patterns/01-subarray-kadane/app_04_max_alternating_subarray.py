import os, sys
_d = os.path.dirname(os.path.abspath(__file__))
while _d and not os.path.exists(os.path.join(_d, 'test_runner.py')):
    _d = os.path.dirname(_d)
sys.path.insert(0, _d)
from test_runner import run_tests


# Maximum Alternating Subarray Sum (LC #2036) -- Medium
# Input:  nums: List[int]
# Output: int (max value of nums[i] - nums[i+1] + nums[i+2] - ... for any subarray)
# Alternating sum with +/- starting positive.
#
# Example:
# #   [3,-1,1,2]  -> 5   ([3,-1,1,2]? sum=3-(-1)+1-2=3... let me reconsider)
#     Actually [3,-1,1,2]: 3-(-1)+1-2 = 5. Start subarray to maximize.
#
#   Pattern: STATE MACHINE KADANE
#   Key: Two states: odd_end (ends at + position), even_end (ends at - position).
#        odd_end = max(even_end + num, num)
#        even_end = odd_end - num

def maximum_alternating_subarray_sum(nums):
    pass

run_tests(maximum_alternating_subarray_sum, [
    (([3,-1,1,2],),    5),
    (([2,2,2,2,2],),   2),
    (([1],),           1),
])
