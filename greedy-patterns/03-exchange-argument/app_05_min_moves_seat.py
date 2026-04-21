import os, sys
_d = os.path.dirname(os.path.abspath(__file__))
while _d and not os.path.exists(os.path.join(_d, 'test_runner.py')):
    _d = os.path.dirname(_d)
sys.path.insert(0, _d)
from test_runner import run_tests


# Minimum Moves to Seat Everyone (LC #2037) -- Easy
# Input:  seats: List[int], students: List[int]
# Output: int (min total moves, each move shifts a student by 1)
# Assign each student to a seat. Min total absolute differences.
#
# Example:
# #   seats=[3,1,5], students=[2,7,4]  -> 4
#     sort both -> [1,3,5] and [2,4,7], abs diffs: 1+1+2 = 4
#
#   Greedy insight: Sort both. Pair i-th seat with i-th student. Sum |differences|.

def min_moves_to_seat(seats, students):
    pass

run_tests(min_moves_to_seat, [
    (([3,1,5], [2,7,4]),        4),
    (([4,1,5,9], [1,3,2,6]),    7),
    (([2,2,6,6], [1,3,2,6]),    4),
    (([1], [1]),                 0),
])
