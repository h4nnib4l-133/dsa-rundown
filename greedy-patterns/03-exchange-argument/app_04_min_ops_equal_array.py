import os, sys
_d = os.path.dirname(os.path.abspath(__file__))
while _d and not os.path.exists(os.path.join(_d, 'test_runner.py')):
    _d = os.path.dirname(_d)
sys.path.insert(0, _d)
from test_runner import run_tests


# Minimum Operations to Make Array Equal (LC #1551) -- Medium
# Input:  n: int (array is [1,3,5,...,2n-1])
# Output: int (min ops; one op: decrement i, increment j by 1)
# Array is [1,3,5,...,2n-1]. Each op: pick i, j; arr[i]--; arr[j]++.
# Min ops to make all equal.
#
# Example:
# #   n=3 -> 2   ([1,3,5] -> [2,3,4] -> [3,3,3])
#
#   Greedy insight: Target = n (middle value). Sum of differences on the higher-half = answer.
#        Formula: if n even: n^2/4. If n odd: (n^2-1)/4.

def min_operations(n):
    pass

run_tests(min_operations, [
    ((3,),    2),
    ((6,),    9),
    ((1,),    0),
    ((2,),    1),
    ((10,),   25),
])
