import sys, os; sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from test_runner import run_tests


# Palindrome Partitioning (LC #131) -- Medium
# Input:  s: str
# Output: List[List[str]] (all ways to partition so every part is palindrome)
# Partition string so every part is a palindrome.
#
#   Key: Backtrack with start index. For each end position, if substring is palindrome, recurse on remainder.

def partition(s):
    pass


def solve(s):
    return sorted(partition(s))


run_tests(solve, [
    (("aab",), [["a","a","b"],["aa","b"]]),
    (("a",),   [["a"]]),
])
