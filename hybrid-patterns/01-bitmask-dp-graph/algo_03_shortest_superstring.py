import os, sys
_d = os.path.dirname(os.path.abspath(__file__))
while _d and not os.path.exists(os.path.join(_d, 'test_runner.py')):
    _d = os.path.dirname(_d)
sys.path.insert(0, _d)
from test_runner import run_tests


# Find the Shortest Superstring (LC #943) -- Hard
# Input:  words: List[str] (n <= 12)
# Output: str (shortest string containing all words as substrings)
# Find shortest superstring. Similar to TSP where 'distance' is overlap.
#
# Example:
# #   ["alex","loves","leetcode"] -> "alexlovesleetcode" (17 chars)
#
#   Pattern: BITMASK DP (TSP variant)
#   Key: Compute overlap[i][j] = length of overlap if we put words[j] after words[i].
#        dp[mask][i] = shortest length ending at i having included mask.
#        Then reconstruct string.

def shortest_superstring(words):
    pass


def solve(words):
    r = shortest_superstring(words)
    # check all words are substrings
    if not all(w in r for w in words):
        return False
    return True

run_tests(shortest_superstring, [
    ((["alex","loves","leetcode"],),  True),
    ((["catg","ctaagt","gcta","ttca","atgcatc"],),  True),
    ((["a"],),                         True),
])
