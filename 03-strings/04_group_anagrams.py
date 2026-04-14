import sys, os; sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from test_runner import run_tests


def group_anagrams(strs):
    """Return list of groups (order doesn't matter)"""
    pass


def solve(strs):
    groups = group_anagrams(strs)
    # normalize: sort each group, sort groups by first element
    return sorted([sorted(g) for g in groups])


run_tests(solve, [
    ((["eat","tea","tan","ate","nat","bat"],),
     [["ate","eat","tea"], ["bat"], ["nat","tan"]]),
    (([""],),  [[""]]),
    ((["a"],), [["a"]]),
])
