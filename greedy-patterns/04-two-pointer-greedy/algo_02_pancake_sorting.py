import os, sys
_d = os.path.dirname(os.path.abspath(__file__))
while _d and not os.path.exists(os.path.join(_d, 'test_runner.py')):
    _d = os.path.dirname(_d)
sys.path.insert(0, _d)
from test_runner import run_tests


# Pancake Sorting (LC #969) -- Medium
# Input:  arr: List[int] (permutation of 1..n)
# Output: List[int] (sequence of k values such that flipping prefix of length k sorts arr)
# Sort array by repeatedly flipping prefixes. Return sequence of flip lengths.
#
# Example:
# #   [3,2,4,1]  -> e.g. [4,2,4,3]
#
#   Greedy insight: Work from largest down. For each value v (n, n-1, ...), find it, flip to front, flip to position.

def pancake_sort(arr):
    pass


def solve(arr):
    original = arr[:]
    ops = pancake_sort(arr)
    # simulate and verify
    a = original[:]
    for k in ops:
        a[:k] = a[:k][::-1]
    return a == sorted(original)

run_tests(pancake_sort, [
    (([3,2,4,1],),    True),
    (([1,2,3],),       True),
    (([5,4,3,2,1],),   True),
    (([1],),           True),
])
