import os, sys
_d = os.path.dirname(os.path.abspath(__file__))
while _d and not os.path.exists(os.path.join(_d, 'test_runner.py')):
    _d = os.path.dirname(_d)
sys.path.insert(0, _d)
from test_runner import run_tests



# Group Anagrams (LC #49) -- Medium
# Input:  strs: List[str] (lowercase English letters)
# Output: List[List[str]] (groups of anagrams, any order)
# Given array of strings, group anagrams together.
#
# Example:
#   ["eat","tea","tan","ate","nat","bat"]
#   -> [["eat","tea","ate"], ["tan","nat"], ["bat"]]
#   (order within groups and order of groups doesn't matter)
#
#   Key: Sort each string as key -> group by key.
#        Or use frequency tuple as key (faster than sorting).

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
    ((["abc","bca","cab","xyz","zyx"],),
     [["abc","bca","cab"], ["xyz","zyx"]]),
    ((["",""],), [["",""]]),     # two empty strings are anagrams
])
