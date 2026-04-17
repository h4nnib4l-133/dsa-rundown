import os, sys
_d = os.path.dirname(os.path.abspath(__file__))
while _d and not os.path.exists(os.path.join(_d, 'test_runner.py')):
    _d = os.path.dirname(_d)
sys.path.insert(0, _d)
from test_runner import run_tests


# Alien Dictionary (LC #269) -- Hard
# Input:  words: List[str] (sorted in alien alphabet order)
# Output: str (valid alphabet ordering, or '' if impossible)
# Given words in sorted alien-dict order, derive the character ordering.
#
# Trick: Compare adjacent word pairs. First differing char gives an edge.
# Then topological sort on characters.
#
# Example:
# #   ["wrt","wrf","er","ett","rftt"]  -> "wertf"
#   ["z","x","z"]                     -> ""  (cycle: z<x and x<z)
#
#   Key: 1. Build graph: for adjacent words, first differing char (a,b) gives edge a->b.
#        2. Topological sort. Collect all chars seen, including those with no constraints.
#        3. If cycle, return ''.

def alien_order(words):
    pass


def solve(words, expected_possible):
    result = alien_order(words)
    if not expected_possible:
        return result == ''
    if not result:
        return False
    # verify the order respects constraints
    pos = {c: i for i, c in enumerate(result)}
    for i in range(len(words)-1):
        w1, w2 = words[i], words[i+1]
        for a, b in zip(w1, w2):
            if a != b:
                if pos.get(a, -1) >= pos.get(b, -1):
                    return False
                break
        else:
            if len(w1) > len(w2):
                return False
    return True

run_tests(alien_order, [
    ((["wrt","wrf","er","ett","rftt"], True),   True),
    ((["z","x","z"], False),                     True),     # cycle
    ((["ab","adc"], True),                       True),
    ((["abc","ab"], False),                      True),     # prefix after longer is invalid
])
