import sys, os; sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from test_runner import run_tests



# Longest Common Prefix (LC #14) -- Easy
# Input:  strs: List[str]
# Output: str (longest common prefix, or "")
# Find the longest common prefix among an array of strings.
# Return "" if no common prefix.
#
# Example:
#   ["flower","flow","flight"] -> "fl"
#   ["dog","racecar","car"]    -> ""  (no common prefix)
#
#   Key: Compare character by character across all strings.
#        Stop at first mismatch or shortest string end.

def longest_common_prefix(strs):
    pass


run_tests(longest_common_prefix, [
    ((["flower","flow","flight"],),  "fl"),
    ((["dog","racecar","car"],),     ""),
    ((["a"],),                       "a"),     # single string
    ((["","b"],),                    ""),      # empty string in list
    ((["abc","abc","abc"],),         "abc"),   # all identical
    ((["ab","abc","abcd"],),         "ab"),    # prefix of shortest
    ((["c","c"],),                   "c"),     # single char, same
])
