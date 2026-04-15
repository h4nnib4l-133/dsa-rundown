import sys, os; sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from test_runner import run_tests



# Search a 2D Matrix (LC #74) -- Medium
# Input:  matrix: List[List[int]] (rows sorted, row[0] > prev row[-1]), target: int
# Output: bool (True if target found)
# m x n matrix where:
#   - each row is sorted left to right
#   - first element of each row > last element of previous row
# Return True if target is in the matrix.
#
# Example:
#   matrix = [[1,3,5,7],     target = 3  -> True
#              [10,11,16,20],
#              [23,30,34,60]]
#
#   matrix = same,            target = 13 -> False
#
#   Key: Treat as one flattened sorted array of size m*n.
#        row = mid // cols, col = mid % cols.

def search_matrix(matrix, target):
    """Return True if target is in matrix"""
    pass


run_tests(search_matrix, [
    (([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 3),   True),    # found in first row
    (([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 11),  True),    # found in middle row
    (([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 60),  True),    # last element
    (([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 1),   True),    # first element
    (([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 13),  False),   # not found
    (([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 0),   False),   # less than all
    (([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 100), False),   # greater than all
    (([[1]], 1),   True),      # 1x1 matrix, found
    (([[1]], 2),   False),     # 1x1 matrix, not found
    (([[1,3]], 3), True),      # 1x2 matrix
])
