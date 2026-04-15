import sys, os; sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from test_runner import run_tests



# Remove Duplicates from Sorted Array (LC #26) -- Easy
# Remove duplicates in-place from sorted array.
# Return new length k. First k elements should have unique values in order.
#
# Example:
#   [1,1,2] -> k=2, array becomes [1,2,...]
#   [0,0,1,1,1,2,2,3,3,4] -> k=5, array becomes [0,1,2,3,4,...]
#
#   Key: Two pointers. 'write' pointer tracks where to place next unique.
#        'read' pointer scans through. Write only when value changes.

def remove_duplicates(nums):
    """Return new length. Modify nums in-place."""
    pass


run_tests(remove_duplicates, [
    (([1,1,2],),                    2),
    (([0,0,1,1,1,2,2,3,3,4],),     5),
    (([1],),                        1),     # single element
    (([1,2,3],),                    3),     # no duplicates
    (([1,1,1,1],),                  1),     # all same
    (([1,2],),                      2),     # two unique
])
