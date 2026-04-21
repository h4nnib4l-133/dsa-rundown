import os, sys
_d = os.path.dirname(os.path.abspath(__file__))
while _d and not os.path.exists(os.path.join(_d, 'test_runner.py')):
    _d = os.path.dirname(_d)
sys.path.insert(0, _d)
from test_runner import run_tests


# Min Deletion Cost to Avoid Repeating Letters (LC #1578) -- Medium
# Input:  s: str, cost: List[int] (cost to delete each char)
# Output: int (min total cost so no two adjacent chars are equal)
# Delete some chars to avoid adjacent duplicates. Minimize total delete cost.
#
# Example:
# #   s="abaac", cost=[1,2,3,4,5] -> 3   (delete s[2]='a' with cost 3)
#
#   Greedy insight: For each run of same chars, keep the max-cost one, delete the rest.
#        Sum = run_total - run_max.

def min_cost_delete(s, cost):
    pass

run_tests(min_cost_delete, [
    (("abaac", [1,2,3,4,5]),   3),
    (("abc", [1,2,3]),          0),
    (("aabaa", [1,2,3,4,1]),    2),
    (("bbbaaa", [4,9,3,8,5,2]),  15),
    (("aaaa", [3,4,5,6]),       12),
])
