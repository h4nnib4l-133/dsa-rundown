import sys, os; sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from test_runner import run_tests



# First Bad Version (LC #278) -- Easy
# Input:  n: int (total versions 1..n), isBadVersion: callable
# Output: int (first version where isBadVersion returns True)
# You have n versions [1, 2, ..., n]. One version is bad, and all after it are bad.
# Given isBadVersion(v) API, find the first bad version.
#
# Example:
#   n = 5, bad = 4
#   isBadVersion(3) -> False
#   isBadVersion(4) -> True
#   -> 4  (first bad version)
#
#   Key: Binary search on boolean predicate. Classic boundary search.

def make_checker(bad):
    def isBadVersion(v):
        return v >= bad
    return isBadVersion


def first_bad_version(n, isBadVersion):
    pass


# Wrapper for testing
def solve(n, bad):
    return first_bad_version(n, make_checker(bad))


run_tests(solve, [
    ((5, 4),      4),     # bad in second half
    ((5, 1),      1),     # very first is bad
    ((1, 1),      1),     # only one version, it's bad
    ((10, 7),     7),     # bad in second half
    ((100, 50),  50),     # larger range
    ((10, 10),   10),     # last version is bad
    ((10, 1),     1),     # all versions are bad
    ((2, 1),      1),     # two versions, first is bad
    ((2, 2),      2),     # two versions, second is bad
])
